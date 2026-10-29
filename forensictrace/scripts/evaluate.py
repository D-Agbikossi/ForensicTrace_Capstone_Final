#!/usr/bin/env python3
"""Evaluate one ForensicTrace experiment against a scenario ground truth.

Implements the reconstruction-quality metrics of the proposal (Table 5/6):

  event coverage   matched ground-truth steps / ground-truth steps
  accuracy         (matched steps + reconstructed relationships)
                   / (expected steps + expected relationships)
  ordering         relationships whose endpoints were both captured AND are in
                   the correct time order / all expected relationships
  explainability   5-dimension rubric, 0-3 each (max 15), scored automatically
                   from the evidence (see explain_scores)

A relationship of type "causal" counts as reconstructed only if the later event
can be explained from the earlier one by walking parent_event / resource_event
links backwards (i.e. the correlator really linked them); type "order" only
needs correct time order.

Usage:  evaluate.py run.json scenarios/ground_truth/scenario04.json [--json]
"""
import argparse
import json
import re
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _hit(event, step):
    if event.get("syscall") not in step["syscall"]:
        return False
    if not re.search(step["target"], event.get("target", "")):
        return False
    detail = step.get("detail")
    if detail and not re.search(detail, event.get("detail", "")):
        return False
    return True


def match_steps(events, steps):
    """Map step id -> index of the event that evidences it (steps are in order)."""
    matched = {}
    for step in steps:
        start = 0
        after = step.get("after")
        if after is not None:
            if after in matched:
                start = matched[after] + 1
            else:
                # the 'after' step was not captured: fall back to the latest
                # earlier step that was, so a missing step never lets a step
                # match unrelated older events
                prior = [matched[s["id"]] for s in steps
                         if s["id"] < step["id"] and s["id"] in matched]
                start = (max(prior) + 1) if prior else 0
        nth = step.get("nth", 1)
        seen = 0
        for idx in range(start, len(events)):
            if _hit(events[idx], step):
                seen += 1
                if seen == nth:
                    matched[step["id"]] = idx
                    break
    return matched


def reachable(events, src, dst):
    """True if src can be reached from dst following links backwards in time."""
    if src > dst:
        return False
    seen = set()
    stack = [dst]
    while stack:
        i = stack.pop()
        if i == src:
            return True
        if i in seen:
            continue
        seen.add(i)
        for key in ("parent_event", "resource_event"):
            j = events[i].get(key, -1)
            if j is not None and 0 <= j < i and j not in seen:
                stack.append(j)
    return False


def explain_scores(events, steps, edges, matched, edge_ok, causal_total, causal_ok):
    """Automatic scoring of the Table 6 rubric (0-3 per dimension)."""
    by_id = {s["id"]: s for s in steps}
    m_idx = [matched[s["id"]] for s in steps if s["id"] in matched]
    dims = {}

    # --- actor identification -------------------------------------------------
    if not m_idx:
        dims["actor"] = 0
    else:
        all_exe = all(events[i].get("exe") for i in m_idx)
        all_uid = all(events[i].get("uid", -1) >= 0 for i in m_idx)
        first_of = {}
        for i, e in enumerate(events):
            first_of.setdefault(e["pid"], i)
        root = events[0]["pid"] if events else None
        roles = all(
            events[i]["pid"] == root or events[first_of[events[i]["pid"]]].get("parent_event", -1) >= 0
            for i in m_idx
        )
        if all_exe and all_uid and roles:
            dims["actor"] = 3
        elif all_exe and all_uid:
            dims["actor"] = 2
        else:
            dims["actor"] = 1          # PID only

    # --- action description ---------------------------------------------------
    n_steps = len(steps)
    if not m_idx:
        dims["action"] = 0
    elif len(m_idx) < n_steps:
        dims["action"] = 1
    else:
        needs_detail = {"openat", "open", "write", "fchmodat", "chmod"}
        intent = all(
            (events[i]["syscall"] not in needs_detail or events[i].get("detail"))
            and events[i].get("target")
            for i in m_idx
        )
        dims["action"] = 3 if intent else 2

    # --- resource identification ---------------------------------------------
    res_ids = [s["id"] for s in steps if s["kind"] in ("file", "network")]
    res_matched = [i for i in res_ids if i in matched]
    if not res_matched:
        dims["resource"] = 0
    elif len(res_matched) < len(res_ids):
        dims["resource"] = 1
    else:
        rr = [k for k, e in enumerate(edges)
              if e["from"] in res_ids and e["to"] in res_ids and e["type"] == "causal"]
        dims["resource"] = 3 if rr and all(edge_ok[k] for k in rr) else 2

    # --- temporal ordering ----------------------------------------------------
    total = len(edges)
    ordered = sum(
        1 for e in edges
        if e["from"] in matched and e["to"] in matched and matched[e["from"]] < matched[e["to"]]
    )
    ordering = ordered / total if total else 0.0
    if ordered == 0:
        dims["temporal"] = 0
    elif ordering < 0.7:
        dims["temporal"] = 1
    elif ordering < 1.0 or causal_ok < causal_total:
        dims["temporal"] = 2
    else:
        dims["temporal"] = 3

    # --- causal relationships ---------------------------------------------------
    if causal_ok == 0:
        dims["causal"] = 0
    elif causal_ok < causal_total:
        dims["causal"] = 1
    else:
        first, last = min(by_id), max(by_id)
        chain = (first in matched and last in matched and
                 reachable(events, matched[first], matched[last]))
        dims["causal"] = 3 if chain else 2

    dims["total"] = sum(dims[k] for k in ("actor", "action", "resource", "temporal", "causal"))
    return dims, ordering


def evaluate(trace, gt):
    events = trace.get("events", [])
    steps = gt["steps"]
    edges = gt["relationships"]
    matched = match_steps(events, steps)

    edge_ok = []
    order_ok = 0
    causal_total = causal_ok = 0
    for e in edges:
        both = e["from"] in matched and e["to"] in matched
        ordered = both and matched[e["from"]] < matched[e["to"]]
        if ordered:
            order_ok += 1
        if e["type"] == "causal":
            causal_total += 1
            ok = ordered and reachable(events, matched[e["from"]], matched[e["to"]])
            causal_ok += 1 if ok else 0
        else:
            ok = ordered
        edge_ok.append(bool(ok))

    n_steps, n_edges = len(steps), len(edges)
    coverage = 100.0 * len(matched) / n_steps if n_steps else 0.0
    accuracy = 100.0 * (len(matched) + sum(edge_ok)) / (n_steps + n_edges) if (n_steps + n_edges) else 0.0
    ordering = 100.0 * order_ok / n_edges if n_edges else 0.0
    dims, _ = explain_scores(events, steps, edges, matched, edge_ok, causal_total, causal_ok)

    return {
        "scenario": gt.get("scenario"),
        "config": trace.get("config"),
        "coverage_pct": round(coverage, 2),
        "accuracy_pct": round(accuracy, 2),
        "ordering_pct": round(ordering, 2),
        "explainability": dims["total"],
        "explain_dims": {k: dims[k] for k in ("actor", "action", "resource", "temporal", "causal")},
        "matched_steps": sorted(matched),
        "missing_steps": [s["id"] for s in steps if s["id"] not in matched],
        "edges_reconstructed": sum(edge_ok),
        "edges_expected": n_edges,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("trace_json")
    ap.add_argument("ground_truth_json")
    ap.add_argument("--json", action="store_true", help="print machine-readable result")
    args = ap.parse_args()

    res = evaluate(load(args.trace_json), load(args.ground_truth_json))
    if args.json:
        print(json.dumps(res, indent=2))
        return 0

    print(f"Scenario {res['scenario']} | config {res['config']}")
    print(f"  event coverage        : {res['coverage_pct']:6.2f} %   (threshold >= 80)")
    print(f"  reconstruction acc.   : {res['accuracy_pct']:6.2f} %   (threshold >= 80)")
    print(f"  ordering correctness  : {res['ordering_pct']:6.2f} %   (threshold >= 70)")
    print(f"  explainability        : {res['explainability']:6d} / 15 (threshold >= 10)")
    print(f"     dimensions         : {res['explain_dims']}")
    print(f"  relationships         : {res['edges_reconstructed']} / {res['edges_expected']}")
    print(f"  missing steps         : {res['missing_steps'] or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Statistical analysis of the ForensicTrace experiment.

Reads results/results.csv (written by run_experiments.py) and produces
results/summary.md plus results/descriptive_stats.csv and results/statistical_tests.csv.

Methods (as in the proposal)
  * descriptive statistics per configuration and per scenario: mean, median, SD,
    min, max, IQR and 95 % confidence interval of the mean (t distribution);
  * Kruskal-Wallis test across the four configurations for every metric
    (pooled over scenarios, and per scenario);
  * Dunn's post-hoc test with Bonferroni correction when KW is significant (p<0.05);
  * eta-squared effect size  eta2 = (H - k + 1) / (n - k)  (0.01 small, 0.06 medium,
    0.14 large);
  * sufficiency threshold (section 3.2.4): a configuration is sufficient only if
    EVERY run, in all four scenarios, meets coverage >= 80, accuracy >= 80,
    ordering >= 70 and explainability >= 10/15.

Requires: pandas, numpy, scipy  (chart results/tradeoff.svg uses only the standard library)
"""
import argparse
import itertools
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

import svgchart

ROOT = Path(__file__).resolve().parent.parent

CONFIGS = ["A", "B", "C", "D"]
CONFIG_NAMES = {"A": "Minimal (process)", "B": "Standard (+file)",
                "C": "Extended (+network)", "D": "Full (all syscalls)"}
QUALITY = ["coverage_pct", "accuracy_pct", "ordering_pct", "explainability"]
COST = ["cpu_overhead_ms", "memory_overhead_kb", "storage_kb", "processing_ms"]
EXTRA = ["wall_overhead_ms", "events"]
THRESH = {"coverage_pct": 80.0, "accuracy_pct": 80.0, "ordering_pct": 70.0, "explainability": 10.0}
LABEL = {
    "coverage_pct": "Event coverage (%)", "accuracy_pct": "Reconstruction accuracy (%)",
    "ordering_pct": "Ordering correctness (%)", "explainability": "Explainability (0-15)",
    "cpu_overhead_ms": "CPU overhead (ms)", "memory_overhead_kb": "Memory overhead (KiB)",
    "storage_kb": "Storage volume (KiB)", "processing_ms": "Processing time (ms)",
    "wall_overhead_ms": "Wall-time overhead (ms)", "events": "Events stored",
}
SCENARIO_LABEL = {"scenario01": "S1 download+execute", "scenario02": "S2 privilege-related",
                  "scenario03": "S3 network payload", "scenario04": "S4 file corruption"}


# ----------------------------------------------------------------- helpers
def fmt(x, nd=2):
    if x is None:
        return "n/a"
    if isinstance(x, (bool, np.bool_)):
        return "yes" if x else "no"
    if isinstance(x, (int, np.integer)):
        return str(int(x))
    if isinstance(x, (float, np.floating)):
        return "n/a" if math.isnan(x) else f"{x:.{nd}f}"
    return str(x)


def fmt_p(p):
    if p is None or (isinstance(p, float) and math.isnan(p)):
        return "n/a"
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def describe(values):
    v = np.asarray(values, dtype=float)
    n = len(v)
    mean = float(v.mean()) if n else math.nan
    sd = float(v.std(ddof=1)) if n > 1 else math.nan
    if n > 1:
        half = stats.t.ppf(0.975, n - 1) * sd / math.sqrt(n)
        lo, hi = mean - half, mean + half
    else:
        lo = hi = math.nan
    q1, q3 = (np.percentile(v, [25, 75]) if n else (math.nan, math.nan))
    return {"n": n, "mean": mean, "median": float(np.median(v)) if n else math.nan,
            "sd": sd, "min": float(v.min()) if n else math.nan,
            "max": float(v.max()) if n else math.nan, "iqr": float(q3 - q1),
            "ci_lo": lo, "ci_hi": hi}


def kruskal(groups):
    """Return (H, p, eta2); NaNs when all values are identical (test undefined)."""
    allv = np.concatenate([np.asarray(g, dtype=float) for g in groups])
    if len(np.unique(allv)) < 2:
        return math.nan, math.nan, math.nan
    h, p = stats.kruskal(*groups)
    n, k = len(allv), len(groups)
    eta2 = max(0.0, (h - k + 1) / (n - k)) if n > k else math.nan
    return float(h), float(p), float(eta2)


def eta_label(e):
    if e is None or math.isnan(e):
        return "n/a"
    if e >= 0.14:
        return "large"
    if e >= 0.06:
        return "medium"
    if e >= 0.01:
        return "small"
    return "negligible"


def dunn(groups, labels):
    """Dunn's test with tie correction and Bonferroni adjustment."""
    data = np.concatenate([np.asarray(g, dtype=float) for g in groups])
    N = len(data)
    ranks = stats.rankdata(data)
    pos, mean_rank, ns = 0, [], []
    for g in groups:
        mean_rank.append(float(ranks[pos:pos + len(g)].mean()))
        ns.append(len(g))
        pos += len(g)
    _, counts = np.unique(data, return_counts=True)
    ties = float((counts ** 3 - counts).sum())
    sigma2 = N * (N + 1) / 12.0 - ties / (12.0 * (N - 1))
    k = len(groups)
    m = k * (k - 1) / 2
    out = []
    for i, j in itertools.combinations(range(k), 2):
        if sigma2 <= 0:
            z = p = padj = math.nan
        else:
            z = (mean_rank[i] - mean_rank[j]) / math.sqrt(sigma2 * (1 / ns[i] + 1 / ns[j]))
            p = 2 * stats.norm.sf(abs(z))
            padj = min(1.0, p * m)
        out.append((labels[i], labels[j], z, p, padj))
    return out


def groups_by_config(df, metric):
    return [df.loc[df.config == c, metric].to_numpy(dtype=float) for c in CONFIGS if (df.config == c).any()], \
           [c for c in CONFIGS if (df.config == c).any()]


# ----------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", default=str(ROOT / "results" / "results.csv"))
    ap.add_argument("--out-dir", default=str(ROOT / "results"))
    ap.add_argument("--manual", default=None,
                    help="optional CSV of researcher-assigned rubric scores "
                         "(run_id,actor,action,resource,temporal,causal) for agreement statistics")
    ap.add_argument("--make-manual-template", action="store_true",
                    help="write results/manual_explainability_template.csv and exit")
    args = ap.parse_args()

    df = pd.read_csv(args.results)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.make_manual_template:
        t = df[["run_id", "scenario", "config", "exp_actor", "exp_action", "exp_resource",
                "exp_temporal", "exp_causal"]].copy()
        for c in ["actor", "action", "resource", "temporal", "causal"]:
            t[c] = ""
        t.to_csv(out_dir / "manual_explainability_template.csv", index=False)
        print(f"wrote {out_dir / 'manual_explainability_template.csv'} "
              "(fill the last five columns with 0-3 scores, save as manual_explainability.csv)")
        return 0

    configs = [c for c in CONFIGS if (df.config == c).any()]
    scenarios = sorted(df.scenario.unique())
    stat_rows, test_rows = [], []
    md = []

    # ---------------------------------------------------------- overview
    md.append("# ForensicTrace experiment: results summary\n")
    reps = df.groupby(["scenario", "config"]).size()
    md.append(f"**Runs analysed:** {len(df)} "
              f"({len(scenarios)} scenarios x {len(configs)} configurations, "
              f"{int(reps.min())}-{int(reps.max())} repetitions per condition). "
              f"Truncated traces: {int(df.truncated.sum())}.\n")
    md.append("> With n = 4 repetitions per condition the study is adequate for descriptive comparison "
              "but not for confirmatory hypothesis testing; results are indicative, not conclusive "
              "(proposal 3.2.7).\n")

    # ---------------------------------------------------------- sufficiency
    md.append("## 1. Evidence sufficiency (RQ1, RQ4)\n")
    md.append("Sufficient = **every** run in **all** scenarios meets all four thresholds "
              "(coverage >= 80 %, accuracy >= 80 %, ordering >= 70 %, explainability >= 10/15).\n")
    suff = {}
    rows = []
    for c in configs:
        d = df[df.config == c]
        met = {m: bool(d[m].min() >= THRESH[m]) for m in QUALITY}
        comp = float(np.mean([min(d[m].mean() / THRESH[m], 1.0) for m in QUALITY]))
        suff[c] = {"met": met, "n_met": sum(met.values()), "sufficient": all(met.values()), "composite": comp}
        rows.append([f"{c} {CONFIG_NAMES[c]}"] + [
            f"{fmt(d[m].min())} / {fmt(d[m].mean())} {'OK' if met[m] else 'FAIL'}" for m in QUALITY
        ] + [suff[c]["n_met"], "**SUFFICIENT**" if suff[c]["sufficient"] else "insufficient"])
    md.append(md_table(["Configuration", "Coverage min/mean", "Accuracy min/mean",
                        "Ordering min/mean", "Explainability min/mean", "Criteria met (of 4)", "Verdict"], rows))

    rows = []
    min_cfg_by_scn = {}
    for s in scenarios:
        first = None
        cells = []
        for c in configs:
            d = df[(df.scenario == s) & (df.config == c)]
            ok = all(d[m].min() >= THRESH[m] for m in QUALITY)
            cells.append("yes" if ok else "no")
            if ok and first is None:
                first = c
        min_cfg_by_scn[s] = first
        rows.append([SCENARIO_LABEL.get(s, s)] + cells + [first or "none"])
    md.append("Per-scenario sufficiency (all repetitions meet all thresholds):\n")
    md.append(md_table(["Scenario"] + [f"Config {c}" for c in configs] + ["Smallest sufficient"], rows))

    sufficient = [c for c in configs if suff[c]["sufficient"]]
    cats = {"A": "process (execve/clone/fork/exit)", "B": "process + file", "C": "process + file + network",
            "D": "process + file + network + all other syscalls"}
    if sufficient:
        m = sufficient[0]
        md.append(f"**Answer to RQ4:** the smallest sufficient configuration across all tested scenarios is "
                  f"**{m} ({CONFIG_NAMES[m]})**: {cats[m]}. ")
        needs = {s: v for s, v in min_cfg_by_scn.items()}
        md.append("Per scenario the smallest sufficient configuration is: " +
                  ", ".join(f"{SCENARIO_LABEL.get(s, s)} -> {v or 'none'}" for s, v in needs.items()) + ".\n")
        if "D" in configs and m != "D":
            dm, dd = df[df.config == m], df[df.config == "D"]
            md.append(f"Config D adds no measured quality over {m} but stores "
                      f"{dd.events.mean() / max(dm.events.mean(), 1):.1f}x more events and "
                      f"{dd.storage_kb.mean() / max(dm.storage_kb.mean(), 1e-9):.1f}x more storage.\n")
    else:
        best = max(configs, key=lambda c: (suff[c]["n_met"], suff[c]["composite"]))
        short = [f"{LABEL[m]} (worst run {df[df.config == best][m].min():.1f} vs threshold {THRESH[m]:.0f})"
                 for m in QUALITY if not suff[best]["met"][m]]
        md.append(f"**No tested configuration met all thresholds.** Highest-performing: **{best}**. Shortfall: "
                  + "; ".join(short) + ".\n")

    # ---------------------------------------------------------- descriptives
    def desc_section(title, metrics, intro):
        md.append(f"## {title}\n")
        md.append(intro + "\n")
        for m in metrics:
            rows = []
            for c in configs:
                d = describe(df.loc[df.config == c, m])
                rows.append([f"{c}", d["n"], fmt(d["mean"]), fmt(d["sd"]), fmt(d["median"]), fmt(d["min"]),
                             fmt(d["max"]), fmt(d["iqr"]), f"[{fmt(d['ci_lo'])}, {fmt(d['ci_hi'])}]"])
                stat_rows.append({"metric": m, "scenario": "ALL", "config": c, **d})
                for s in scenarios:
                    ds = describe(df.loc[(df.config == c) & (df.scenario == s), m])
                    stat_rows.append({"metric": m, "scenario": s, "config": c, **ds})
            md.append(f"**{LABEL[m]}**, pooled over scenarios\n")
            md.append(md_table(["Config", "n", "Mean", "SD", "Median", "Min", "Max", "IQR", "95% CI of mean"], rows))
        # per-scenario mean matrix
        md.append("Per-scenario means (rows: scenario, columns: configuration)\n")
        for m in metrics:
            rows = []
            for s in scenarios:
                rows.append([SCENARIO_LABEL.get(s, s)] +
                            [fmt(df.loc[(df.scenario == s) & (df.config == c), m].mean()) for c in configs])
            md.append(f"{LABEL[m]}\n")
            md.append(md_table(["Scenario"] + [f"Config {c}" for c in configs], rows))

    desc_section("2. Reconstruction quality by configuration (RQ2)", QUALITY,
                 "Descriptive statistics per configuration (n = scenarios x repetitions).")
    desc_section("3. Resource cost by configuration (RQ3)", COST + EXTRA,
                 "Overheads are measured against an unmonitored baseline run of the same scenario "
                 "in the same repetition (CPU time of the traced tree plus the tracer's own CPU; "
                 "memory = tracer peak RSS + change in workload peak RSS).")

    # ---------------------------------------------------------- tests
    md.append("## 4. Between-configuration tests\n")
    md.append("Kruskal-Wallis across configurations (pooled over scenarios). eta-squared = (H - k + 1)/(n - k). "
              "'n/a' means every observation was identical so the test is undefined.\n")
    rows, dunn_blocks = [], []
    for m in QUALITY + COST + EXTRA:
        groups, labels = groups_by_config(df, m)
        h, p, eta = kruskal(groups)
        sig = (not math.isnan(p)) and p < 0.05
        rows.append([LABEL[m], fmt(h), fmt_p(p), fmt(eta, 3), eta_label(eta), "yes" if sig else "no"])
        test_rows.append({"metric": m, "scenario": "ALL", "test": "kruskal", "H": h, "p": p, "eta2": eta})
        if sig:
            pr = []
            for a, b, z, pp, pa in dunn(groups, labels):
                pr.append([f"{a} vs {b}", fmt(z), fmt_p(pp), fmt_p(pa), "yes" if pa < 0.05 else "no"])
                test_rows.append({"metric": m, "scenario": "ALL", "test": f"dunn {a}-{b}",
                                  "H": z, "p": pp, "eta2": pa})
            dunn_blocks.append((m, pr))
    md.append(md_table(["Metric", "H", "p", "eta2", "Effect", "p < 0.05"], rows))
    if dunn_blocks:
        md.append("Dunn's post-hoc (Bonferroni-adjusted p) for the significant metrics:\n")
        for m, pr in dunn_blocks:
            md.append(f"**{LABEL[m]}**\n")
            md.append(md_table(["Pair", "z", "p (raw)", "p (Bonferroni)", "Significant"], pr))

    md.append("Per-scenario Kruskal-Wallis p-values (n = repetitions per group):\n")
    rows = []
    for m in QUALITY + COST:
        cells = []
        for s in scenarios:
            groups, _ = groups_by_config(df[df.scenario == s], m)
            h, p, eta = kruskal(groups)
            cells.append(fmt_p(p))
            test_rows.append({"metric": m, "scenario": s, "test": "kruskal", "H": h, "p": p, "eta2": eta})
        rows.append([LABEL[m]] + cells)
    md.append(md_table(["Metric"] + [SCENARIO_LABEL.get(s, s) for s in scenarios], rows))

    # ---------------------------------------------------------- references
    md.append("## 5. Comparison against the reference configurations\n")
    md.append("Mean difference of each configuration versus the baseline A (effect of adding evidence) "
              "and versus the full configuration D (effect of removing evidence).\n")
    rows = []
    for m in QUALITY + COST:
        mean = {c: df.loc[df.config == c, m].mean() for c in configs}
        row = [LABEL[m]]
        for c in configs:
            va = mean[c] - mean["A"] if "A" in mean else math.nan
            vd = mean[c] - mean["D"] if "D" in mean else math.nan
            row.append(f"{va:+.2f} / {vd:+.2f}")
        rows.append(row)
    md.append(md_table(["Metric (vs A / vs D)"] + [f"Config {c}" for c in configs], rows))

    # ---------------------------------------------------------- trade-off
    md.append("## 6. Evidence-versus-cost trade-off\n")
    rows = []
    for c in configs:
        d = df[df.config == c]
        rows.append([f"{c} {CONFIG_NAMES[c]}", fmt(d.explainability.mean()), fmt(d.coverage_pct.mean()),
                     fmt(d.events.mean(), 0), fmt(d.storage_kb.mean()), fmt(d.cpu_overhead_ms.mean()),
                     fmt(d.memory_overhead_kb.mean(), 0), fmt(d.processing_ms.mean()),
                     "yes" if suff[c]["sufficient"] else "no"])
    md.append(md_table(["Configuration", "Explainability", "Coverage %", "Events", "Storage KiB",
                        "CPU overhead ms", "Memory overhead KiB", "Processing ms", "Sufficient"], rows))

    # ---------------------------------------------------------- integrity
    md.append("## 7. Evidence integrity\n")
    rows = []
    for c in configs:
        d = df[df.config == c]
        rows.append([c, len(d), f"{int(d.integrity_verified.sum())}/{len(d)}",
                     f"{int(d.tamper_detected.sum())}/{len(d)}"])
    rows.append(["all", len(df), f"{int(df.integrity_verified.sum())}/{len(df)}",
                 f"{int(df.tamper_detected.sum())}/{len(df)}"])
    md.append("Each run: the SHA-256 sidecar must verify, and three controlled modifications "
              "(bit flip, appended byte, truncated tail) must all be detected.\n")
    md.append(md_table(["Config", "Runs", "Sidecar verified", "Tamper detected"], rows))

    # ---------------------------------------------------------- manual rubric
    manual_path = Path(args.manual) if args.manual else (out_dir / "manual_explainability.csv")
    if manual_path.exists():
        man = pd.read_csv(manual_path)
        dims = ["actor", "action", "resource", "temporal", "causal"]
        man = man.dropna(subset=dims)
        merged = df.merge(man[["run_id"] + dims], on="run_id", how="inner")
        if len(merged):
            md.append("## 8. Researcher-assigned vs automated explainability\n")
            rows = []
            for dname in dims:
                auto, hand = merged[f"exp_{dname}"], merged[dname]
                rows.append([dname, f"{100 * (auto == hand).mean():.1f}%",
                             f"{100 * ((auto - hand).abs() <= 1).mean():.1f}%"])
            tot_hand = merged[dims].sum(axis=1)
            rows.append(["total (0-15)", f"{100 * (merged.explainability == tot_hand).mean():.1f}%",
                         f"{100 * ((merged.explainability - tot_hand).abs() <= 1).mean():.1f}%"])
            md.append(f"{len(merged)} runs scored by hand.\n")
            md.append(md_table(["Dimension", "Exact agreement", "Within +/-1"], rows))

    # ---------------------------------------------------------- notes
    md.append("## Notes on measurement\n")
    md.append("- **Ground truth** is the per-scenario action list in `scenarios/ground_truth/*.json`; a step is "
              "covered when a recorded event matches its syscall/target pattern.\n"
              "- **Accuracy** = (covered steps + reconstructed relationships) / (expected steps + expected "
              "relationships); a causal relationship counts only if the correlator's `parent_event` / "
              "`resource_event` links connect the two events.\n"
              "- **Explainability** is scored automatically from the evidence with the Table 6 rubric "
              "(see `scripts/evaluate.py`); it is a proxy for, not a replacement of, expert judgement. "
              "Use `--make-manual-template` to record researcher scores and obtain agreement statistics.\n"
              "- Event timestamps come from one monotonic clock, so ordering is exact whenever both events "
              "are captured; ordering loss therefore reflects missing evidence, not clock error.\n"
              "- Overheads use `getrusage`; CPU of very short runs has ~10 ms granularity.\n")

    (out_dir / "summary.md").write_text("\n".join(md), encoding="utf-8")
    pd.DataFrame(stat_rows).to_csv(out_dir / "descriptive_stats.csv", index=False)
    pd.DataFrame(test_rows).to_csv(out_dir / "statistical_tests.csv", index=False)
    print(f"wrote {out_dir / 'summary.md'}, descriptive_stats.csv, statistical_tests.csv")

    # ---------------------------------------------------------- chart (SVG, stdlib only)
    panels = []
    for m in ["coverage_pct", "explainability", "storage_kb", "cpu_overhead_ms"]:
        panels.append({
            "title": LABEL[m], "labels": configs, "xlabel": "Evidence configuration",
            "values": [df.loc[df.config == c, m].mean() for c in configs],
            "errors": [float(np.nan_to_num(df.loc[df.config == c, m].std(ddof=1))) for c in configs],
            "threshold": THRESH.get(m),
            "ymax": {"coverage_pct": 100, "explainability": 15}.get(m),
        })
    svg = svgchart.bar_panels(panels, out_dir / "tradeoff.svg",
                              title="ForensicTrace: evidence sufficiency vs resource cost (mean, error bar = SD)")
    print(f"wrote {svg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

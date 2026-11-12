#!/usr/bin/env python3
"""Investigation reports for one evidence file, in two versions.

  technical  for investigators and assessors: case details, findings, the
             reconstructed chain with its evidence and confidence, processes,
             network, files and chain of custody
  general    for readers without a technical background: what happened, how
             serious it is, what was affected and whether the record can be trusted

Both are HTML, printable to PDF with Chromium. Everything comes from the evidence
file, scripts/reconstruct.py and, when the engine is built, `forensictrace verify`.
Evidence is untrusted (a traced program chooses its own file names), so every
value is HTML-escaped and the pages contain no script.

Usage:  case_report.py run.json [--kind technical|general] [--html out.html | --pdf out.pdf]
"""
import argparse
import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import reconstruct  # noqa: E402

KINDS = ("technical", "general")
CONFIG_NAMES = {"A": "process events only", "B": "process and file events",
                "C": "process, file and network events", "D": "every system call"}
SEVERITY_PLAIN = {"critical": "Very serious", "high": "Serious", "medium": "Worth checking", "low": "For information"}
RULE_PLAIN = {
    "FT-DOWNLOAD-EXEC": "A file was downloaded and then run as a program. This is how many attacks install harmful software.",
    "FT-DROP-EXEC": "A file created during the recording was then run as a program.",
    "FT-PAYLOAD-OUTBOUND": "A program started by that file contacted another computer, which can mean it was sending "
                           "information out or receiving instructions.",
    "FT-SENSITIVE-FILE": "A program tried to read or change a file that holds passwords or permissions.",
    "FT-EXEC-TEMP": "A program was run from a temporary folder, where normal software is rarely kept.",
    "FT-OVERWRITE": "A file was emptied and written again, replacing what it held.",
    "FT-CREATE-DELETE": "A file was created and then deleted, which can be a way of hiding traces.",
    "FT-OUTBOUND": "The computer contacted an address on the internet. This is common and is listed only for review.",
    "FT-EVIDENCE-TRUNCATED": "The recording stopped early because it reached its size limit, so later activity is missing.",
    "FT-EVIDENCE-UNTRACED": "Some programs could not be recorded, so part of the activity is missing.",
}
SCOPE_PLAIN = {"loopback": "an address on this same computer, so nothing left the machine",
               "private": "a computer on a local network", "public": "a computer on the internet",
               "link-local": "a device on the same local network link", "unknown": "an address of unknown type"}
OP_PLAIN = {"created": "created", "overwritten": "emptied and rewritten", "wrote": "changed", "deleted": "deleted",
            "chmod": "given new permissions", "read_denied": "refused when a program tried to read it",
            "write_denied": "refused when a program tried to change it", "opened_for_write": "opened for changing",
            "executed": "run as a program", "read": "read", "opened": "opened"}
STATUS_PLAIN = {
    "verified_signed_pinned": ("good", "The record is intact and its seal is genuine.",
                               "Nothing in this record has been changed since it was made, and it carries the "
                               "investigator's digital signature, checked against their trusted key."),
    "verified_signed_unpinned": ("warn", "The record is intact, but who sealed it is not confirmed.",
                                 "Nothing has been changed, and the record is signed, but the signature was not "
                                 "checked against a key known to belong to the investigator."),
    "verified_unsigned": ("warn", "The record appears intact, but it was not sealed.",
                          "No change was found, but without a signature someone who rewrote every file could go "
                          "unnoticed."),
    "legacy_sidecar_ok": ("warn", "Only a basic check was possible.",
                          "This older recording has a single fingerprint of the whole file, which matches. It has "
                          "no record-by-record protection or signature."),
    "failed": ("bad", "The record has been changed since it was made.",
               "Treat everything in this report as unreliable until the change is explained."),
}

CSS = """
@page { size: A4; margin: 15mm 16mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10pt; line-height: 1.42; color: #0f1f3d; max-width: 860px; margin: 24px auto; padding: 0 16px; background: #fff; }
h1 { font-size: 17pt; margin: 0 0 4px; color: #12284a; border-bottom: 3px solid #c8102e; padding-bottom: 4px; }
h2 { font-size: 12pt; margin: 16px 0 6px; color: #12284a; border-bottom: 1px solid #1f5fbf; padding-bottom: 2px; }
h3 { font-size: 10.5pt; margin: 10px 0 4px; color: #1f5fbf; }
p { margin: 5px 0; }
.sub { color: #3d4b66; margin-bottom: 10px; }
.box { border: 1px solid #c3cbd8; border-left: 4px solid #1f5fbf; padding: 8px 12px; margin: 10px 0; background: #f3f6fb; }
.box.bad { border-left-color: #c8102e; background: #fdf1f2; }
.box.warn { border-left-color: #b58a2e; background: #fdf8ec; }
.box.good { border-left-color: #0c7a0c; background: #f1f9f1; }
.box b.lead { display: block; margin-bottom: 2px; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 8.8pt; }
thead { display: table-header-group; }
th, td { border: 1px solid #c3cbd8; padding: 3px 5px; text-align: left; vertical-align: top; overflow-wrap: anywhere; }
th { background: #e6edf7; color: #12284a; white-space: nowrap; }
tr { page-break-inside: avoid; }
td.num, th.num { text-align: right; white-space: nowrap; }
code, .mono { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.4pt; overflow-wrap: anywhere; word-break: break-all; }
.sev { font-weight: bold; white-space: nowrap; }
.sev.critical, .sev.high { color: #b02525; } .sev.medium { color: #7a5200; } .sev.low { color: #3d4b66; }
.kv td:first-child { width: 28%; color: #3d4b66; }
ul { margin: 4px 0 8px 18px; padding: 0; } li { margin: 2px 0; }
.foot { margin-top: 18px; color: #5f6b80; font-size: 8.4pt; border-top: 1px solid #c3cbd8; padding-top: 6px; }
"""


def esc(value):
    return html.escape("" if value is None else str(value))


def base(path):
    return reconstruct.base(path or "")


def fmt_ms(ms):
    if ms is None:
        return ""
    return f"{ms / 1000:.2f} s" if ms >= 1000 else f"{ms:.1f} ms"


def fmt_bytes(n):
    n = n or 0
    if n < 1024:
        return f"{n} B"
    return f"{n / 1024:.1f} KB" if n < 1048576 else f"{n / 1048576:.1f} MB"


def plain_list(items):
    items = [i for i in items if i]
    if len(items) < 2:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


def verify(evidence, pubkey=None):
    """`forensictrace verify --json`, without writing to the audit log; None if the engine is not built."""
    binary = ROOT / "forensictrace"
    if not binary.is_file():
        return None
    cmd = [str(binary), "verify", str(evidence), "--json", "--no-audit"]
    if pubkey:
        cmd += ["--pubkey", str(pubkey)]
    p = subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=120)
    return json.loads(p.stdout) if p.returncode in (0, 1) and p.stdout.strip() else None


class Report:
    def __init__(self, doc, analysis, verification=None, manifest=None, audit=None, source=""):
        self.doc, self.a, self.v = doc, analysis, verification
        self.manifest, self.audit = manifest, audit or []
        self.source = source
        self.cust = doc.get("custody") or {}
        self.edges = {e["id"]: e for e in analysis["graph"]["edges"]}
        self.chain = [self.edges[i] for i in analysis["answers"]["chain"] if i in self.edges]
        self.procs = {p["pid"]: p for p in analysis["processes"]}
        self.events = {e["id"]: e for e in doc.get("events", [])}

    # ---- shared pieces ---------------------------------------------------------

    def title_block(self, title, subtitle):
        case = self.cust.get("case_id")
        name = case if case and case != "UNASSIGNED" else (self.doc.get("scenario") or Path(self.source).stem)
        return f"<h1>{esc(title)}: {esc(name)}</h1><p class='sub'>{esc(subtitle)}</p>"

    def status(self):
        return self.v["status"] if self.v else None

    def page(self, title, body):
        return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' "
                f"content='width=device-width, initial-scale=1'><title>{esc(title)}</title><style>{CSS}</style>"
                f"</head><body>{body}<p class='foot'>Generated by ForensicTrace from <code>{esc(Path(self.source).name)}</code>. "
                f"Confidence values are rule-based scores, not measured probabilities.</p></body></html>")

    def case_rows(self):
        d, c = self.doc, self.cust
        rows = [("Case", c.get("case_id")), ("Investigator", c.get("investigator")), ("Scenario", d.get("scenario")),
                ("Command traced", d.get("command")),
                ("Evidence configuration", f"{d.get('config')}: {CONFIG_NAMES.get(d.get('config'), '')}"),
                ("Collection mode", d.get("collection_mode")), ("Started (UTC)", c.get("started_utc")),
                ("Finished (UTC)", c.get("finished_utc")), ("Host", c.get("hostname")), ("Session ID", c.get("session_id")),
                ("Evidence file", Path(self.source).name),
                ("File SHA-256", self.v.get("evidence_sha256") if self.v else None)]
        return [(k, v) for k, v in rows if v not in (None, "", "UNASSIGNED")]

    def not_collected(self):
        missing = [k for k in ("file", "network") if not self.a["collected"][k]]
        return missing

    # ---- technical version ------------------------------------------------------

    def technical(self):
        a, s = self.a, self.a["summary"]
        out = [self.title_block("Investigation report", "Technical version, for investigators and assessors")]
        mono = ("Command traced", "File SHA-256", "Session ID")
        rows = []
        for k, v in self.case_rows():
            value = "<code>" + esc(v) + "</code>" if k in mono else esc(v)
            rows.append("<tr><td>" + esc(k) + "</td><td>" + value + "</td></tr>")
        out.append("<h2>1. Case</h2><table class='kv'>" + "".join(rows) + "</table>")
        if self.v:
            st = self.status()
            tone = STATUS_PLAIN.get(st, ("warn",))[0]
            out.append(f"<div class='box {tone}'><b class='lead'>Verification: {esc(st.replace('_', ' '))}</b>"
                       f"{esc(self.v.get('records_checked'))} records recomputed.</div>")
        missing = self.not_collected()
        if missing:
            out.append(f"<div class='box warn'><b class='lead'>Evidence not collected</b>Configuration "
                       f"{esc(self.doc.get('config'))} records no {esc(' or '.join(missing))} events. Answers about them are "
                       f"unknown, not absent.</div>")

        out.append("<h2>2. Summary</h2><table><thead><tr><th>Processes</th><th>System calls</th><th>Files accessed</th>"
                   "<th>Network connections</th><th>Suspicious activities</th><th>Duration</th></tr></thead><tbody><tr>"
                   f"<td class='num'>{s['processes']}</td><td class='num'>{s['syscalls']:,}</td>"
                   f"<td class='num'>{s['files_accessed'] if a['collected']['file'] else 'not collected'}</td>"
                   f"<td class='num'>{s['connections'] if a['collected']['network'] else 'not collected'}</td>"
                   f"<td class='num'>{s['suspicious']}</td><td class='num'>{fmt_ms(s['duration_ms'])}</td></tr></tbody></table>")

        out.append("<h2>3. Findings</h2>")
        if a["findings"]:
            out.append("<table><thead><tr><th>Severity</th><th>Rule</th><th>Finding</th><th>Events</th></tr></thead><tbody>" + "".join(
                f"<tr><td class='sev {esc(f['severity'])}'>{esc(f['severity'])}</td><td><code>{esc(f['rule'])}</code></td>"
                f"<td><b>{esc(f['title'])}</b><br>{esc(f['why'])}</td><td class='mono'>{esc(', '.join(map(str, f['events'][:12])))}</td></tr>"
                for f in a["findings"]) + "</tbody></table>")
        else:
            out.append("<p>No detection rule fired. The rules only cover known patterns.</p>")

        out.append("<h2>4. Reconstructed sequence</h2>")
        if self.chain:
            weakest = min(self.chain, key=lambda e: e["confidence"])
            out.append(f"<p>{len(self.chain)} linked steps. Weakest link: {weakest['confidence']:.0%} "
                       f"({esc(weakest['summary'])}).</p>")
            out.append("<table><thead><tr><th class='num'>Time</th><th>Relation</th><th>Basis</th><th class='num'>Confidence</th>"
                       "<th>Events</th></tr></thead><tbody>" + "".join(
                f"<tr><td class='num'>+{fmt_ms(e['ms'])}</td><td>{esc(e['summary'])}</td><td>{esc(e['tier'])}: {esc(e['rule'])}</td>"
                f"<td class='num'>{e['confidence']:.0%}</td><td class='mono'>{esc(', '.join(map(str, e['evidence'][:8])))}</td></tr>"
                for e in self.chain) + "</tbody></table>")
            inferred = [e for e in self.chain if e["tier"] == "inferred"]
            if inferred:
                out.append("<h3>How the inferred steps were scored</h3><ul>" + "".join(
                    f"<li>{esc(e['summary'])}: " + esc("; ".join(
                        f"{f['label']} ({'+' + str(round(f['value'] * 100)) if f['value'] else 'note'})" for f in e["factors"])) + "</li>"
                    for e in inferred) + "</ul>")
        else:
            out.append("<p>No download or payload-execution chain was found in this evidence.</p>")

        out.append("<h2>5. Processes</h2><table><thead><tr><th>PID</th><th>Program</th><th>Parent</th><th class='num'>Ran</th>"
                   "<th class='num'>Exit</th><th class='num'>Events</th></tr></thead><tbody>")
        for p in sorted(a["processes"], key=lambda x: x["first_ms"])[:80]:
            parent = self.procs.get(p["parent"])
            parent_label = esc("%s (%s)" % (base(parent["exe"]), parent["pid"])) if parent else "outside the trace"
            out.append(f"<tr><td class='num'>{p['pid']}</td><td><code>{esc(p['exe'] or 'unknown')}</code></td>"
                       f"<td>{parent_label}</td>"
                       f"<td class='num'>+{fmt_ms(p['first_ms'])} to +{fmt_ms(p['last_ms'])}</td>"
                       f"<td class='num'>{esc(p['exit_code']) if p['exit_code'] is not None else ''}</td><td class='num'>{p['event_count']}</td></tr>")
        out.append("</tbody></table>")
        if len(a["processes"]) > 80:
            out.append(f"<p>First 80 of {len(a['processes'])} processes shown.</p>")

        out.append("<h2>6. Network</h2>")
        conns = [c for c in a["connections"] if not c.get("probe")]
        if not a["collected"]["network"]:
            out.append("<p>Not collected under this configuration.</p>")
        elif not conns:
            out.append("<p>No connections were recorded.</p>")
        else:
            def end(host, port):
                return "%s:%s" % (host, port) if host else "not recorded"
            out.append("<table><thead><tr><th class='num'>Time</th><th>Process</th><th>Direction</th><th>Source</th>"
                       "<th>Destination</th><th>Protocol</th><th>State</th><th class='num'>Sent</th><th class='num'>Received</th>"
                       "</tr></thead><tbody>" + "".join(
                f"<tr><td class='num'>+{fmt_ms(c['ms'])}</td><td>{esc(base(c['exe']))} ({c['pid']})</td><td>{esc(c['direction'])}</td>"
                f"<td class='mono'>{esc(end(c['src_host'], c['src_port']))}</td><td class='mono'>{esc(end(c['dst_host'], c['dst_port']) if c['dst_host'] else c['endpoint'])}</td>"
                f"<td>{esc(c['proto'].upper() if c['proto'] != 'unknown' else 'not recorded')}</td><td>{esc(c['state'])}</td>"
                f"<td class='num'>{fmt_bytes(c['bytes_sent'])}</td><td class='num'>{fmt_bytes(c['bytes_received'])}</td></tr>"
                for c in conns) + "</tbody></table>")

        out.append("<h2>7. Files affected</h2>")
        files = a["answers"]["affected_files"]
        if not a["collected"]["file"]:
            out.append("<p>Not collected under this configuration.</p>")
        elif not files:
            out.append("<p>No file changes were recorded.</p>")
        else:
            out.append("<table><thead><tr><th>File</th><th>Kind</th><th>What happened</th><th>Processes</th>"
                       "<th class='num'>Written</th></tr></thead><tbody>" + "".join(
                f"<tr><td><code>{esc(f['path'])}</code></td><td>{esc(f['category'])}</td>"
                f"<td>{esc(', '.join(k + ' x' + str(n) if n > 1 else k for k, n in f['ops'].items()))}</td>"
                f"<td>{esc(', '.join('%s (%s)' % (base(p['exe']), p['pid']) for p in f['processes'][:4]))}</td>"
                f"<td class='num'>{fmt_bytes(f['bytes_written'])}</td></tr>" for f in files) + "</tbody></table>")

        out.append("<h2>8. Chain of custody</h2>")
        if self.v:
            out.append("<table><thead><tr><th>Check</th><th>Result</th><th>Detail</th></tr></thead><tbody>" + "".join(
                f"<tr><td>{esc(k['name'].replace('_', ' '))}</td><td>{esc(k['state'])}</td><td>{esc(k['text'])}</td></tr>"
                for k in self.v["checks"]) + "</tbody></table>")
            if self.v.get("issues"):
                out.append("<h3>Problems found</h3><ul>" + "".join(
                    f"<li><code>{esc(i['kind'])}</code>: {esc(i['text'])}</li>" for i in self.v["issues"][:50]) + "</ul>")
        else:
            out.append("<p>Verification was not run, because the engine is not built on this machine.</p>")
        if self.cust:
            out.append(f"<p>Chain head <code>{esc(self.cust.get('chain_head'))}</code>.")
            if self.manifest and self.manifest.get("signature"):
                out.append(f" Manifest signed with Ed25519, key fingerprint <code>{esc(self.manifest['signature'].get('key_fingerprint'))}</code>.")
            out.append("</p>")
        if self.audit:
            out.append("<h3>Audit log</h3><table><thead><tr><th class='num'>#</th><th>When (UTC)</th><th>Action</th><th>By</th>"
                       "<th>Outcome</th></tr></thead><tbody>" + "".join(
                f"<tr><td class='num'>{esc(e.get('seq'))}</td><td>{esc(e.get('ts_utc'))}</td><td>{esc(e.get('action'))}</td>"
                f"<td>{esc(e.get('investigator'))}</td><td>{esc(e.get('outcome'))}</td></tr>" for e in self.audit) + "</tbody></table>")

        out.append("<h2>9. Limits of this report</h2><ul>"
                   "<li>Inferred steps connect observations the system never linked itself. File contents and inodes are not "
                   "recorded, so a download or a payload link is likely, not proven.</li>"
                   "<li>Only the traced command and its child processes were recorded, not the whole computer.</li>"
                   "<li>Findings come from a fixed rule set. An empty list does not prove the system is clean.</li>"
                   "<li>A privileged attacker can detect or defeat a user-space tracer.</li></ul>")
        return self.page("Investigation report (technical)", "".join(out))

    # ---- general version ----------------------------------------------------------

    def story(self):
        """What happened, as plain sentences built from the reconstructed chain."""
        a = self.a
        sentences = []
        init = a["answers"]["initiator"]
        if init:
            cmd = init["command"].split()
            script = next((base(x) for x in cmd if x.endswith((".sh", ".py", ".pl"))), None)
            what = f"the script <b>{esc(script)}</b>" if script else f"the program <b>{esc(base(init['exe']) or cmd[0])}</b>"
            sentences.append(f"The recording starts when {what} was run.")
        for d in a["answers"]["downloads"]:
            ends = [n for n in a["answers"]["endpoints"] if n["endpoint"] == d["endpoint"]]
            scope = SCOPE_PLAIN.get(ends[0]["scope"], "") if ends else ""
            sentences.append(f"The program <b>{esc(base(d['exe']))}</b> downloaded a file named <b>{esc(base(d['file']))}</b> "
                             f"from <code>{esc(d['endpoint'])}</code>{f' ({esc(scope)})' if scope else ''}.")
        downloaded = {d["file"] for d in a["answers"]["downloads"]}
        for x in a["answers"]["executions"]:
            if x["file"] in downloaded:
                sentences.append("That file was then run as a program.")
            else:
                sentences.append(f"A file created during the recording, <b>{esc(base(x['file']))}</b>, was then run as a program.")
        if a["answers"]["executions"]:
            first_exec = min(e["ms"] for e in self.chain if e["kind"] == "executed") if any(
                e["kind"] == "executed" for e in self.chain) else None
            if first_exec is not None:
                after = [e for e in self.chain if e["ms"] > first_exec]
                changed = []
                for e in after:
                    if e["kind"] in ("created", "wrote", "overwritten", "deleted") and e["dst"].startswith("f:"):
                        name = base(e["dst"][2:])
                        if name not in changed:
                            changed.append(name)
                contacted = [e["dst"][2:] for e in after if e["kind"] == "connected"]
                if changed:
                    sentences.append(f"Once running, it changed {len(changed)} file{'s' if len(changed) > 1 else ''}: "
                                     + plain_list(["<b>" + esc(n) + "</b>" for n in changed]) + ".")
                if contacted:
                    sentences.append("It then contacted " + plain_list(["<code>" + esc(c) + "</code>" for c in dict.fromkeys(contacted)]) + ".")
        sensitive = [f for f in a["answers"]["affected_files"] if f["category"] == "sensitive"]
        for f in sensitive:
            refused = "read_denied" in f["ops"] or "write_denied" in f["ops"]
            sentences.append(f"A program tried to use the protected file <b>{esc(f['path'])}</b>"
                             f"{', and the computer refused' if refused else ''}.")
        if not a["answers"]["downloads"] and not a["answers"]["executions"]:
            changed = [f for f in a["answers"]["affected_files"] if f["category"] != "sensitive"]
            if changed:
                sentences.append(f"No file was downloaded and run. {len(changed)} file{'s were' if len(changed) > 1 else ' was'} "
                                 f"created, changed or deleted.")
            elif a["collected"]["file"]:
                sentences.append("No file was downloaded, run or changed.")
        return sentences

    def general(self):
        a = self.a
        out = [self.title_block("What happened", "Plain-language version of the investigation report")]
        when = self.cust.get("started_utc")
        who = self.cust.get("investigator")
        made = ("The recording was made on %s at %s UTC" % (esc(when[:10]), esc(when[11:16]))) if when \
            else "The recording date is not stored in this older file"
        if who:
            made += " by " + esc(who)
        out.append("<p>This report explains, in everyday words, what a recording of computer activity shows. " + made + ".</p>")

        out.append("<h2>In short</h2><div class='box'>" + " ".join(self.story()) + "</div>")
        missing = self.not_collected()
        if missing:
            words = {"file": "which files were used", "network": "which other computers were contacted"}
            out.append(f"<div class='box warn'><b class='lead'>Part of the activity was not recorded</b>This recording "
                       f"used a lower level of detail, so it cannot show {esc(' or '.join(words[m] for m in missing))}. "
                       f"That means it is unknown, not that it did not happen.</div>")

        out.append("<h2>How serious is it?</h2>")
        if a["findings"]:
            out.append("<ul>" + "".join(
                f"<li><span class='sev {esc(f['severity'])}'>{esc(SEVERITY_PLAIN[f['severity']])}:</span> "
                f"{esc(RULE_PLAIN.get(f['rule'], f['why']))}</li>" for f in a["findings"]) + "</ul>")
        else:
            out.append("<p>None of the warning signs the tool looks for were found. The tool only knows certain patterns, "
                       "so this does not prove that nothing harmful happened.</p>")

        out.append("<h2>What was affected</h2>")
        files = a["answers"]["affected_files"]
        if not a["collected"]["file"]:
            out.append("<p>Files: not recorded at this level of detail.</p>")
        elif files:
            # Files that were only deleted are usually leftovers being cleared; they are summarised in one line.
            changed = [f for f in files if set(f["ops"]) != {"deleted"}]
            only_deleted = [f for f in files if set(f["ops"]) == {"deleted"}]
            items = []
            for f in changed[:10]:
                folder = f["path"][:-len(base(f["path"]))] or "/"
                ops = [OP_PLAIN.get(k, k) for k in f["ops"]]
                how = "was " + ops[0] if len(ops) == 1 else "was, in this order, " + plain_list(ops)
                items.append("<li><b>" + esc(base(f["path"])) + "</b> (in <code>" + esc(folder) + "</code>) " + esc(how) + ".</li>")
            if only_deleted:
                names = plain_list(["<b>" + esc(base(f["path"])) + "</b>" for f in only_deleted[:5]])
                more = f" and {len(only_deleted) - 5} more" if len(only_deleted) > 5 else ""
                items.append(f"<li>{len(only_deleted)} other item{'s were' if len(only_deleted) > 1 else ' was'} only deleted: {names}{more}.</li>")
            out.append("<p>Files:</p><ul>" + "".join(items) + "</ul>")
            if len(changed) > 10:
                out.append(f"<p>And {len(changed) - 10} more, listed in the technical version.</p>")
        else:
            out.append("<p>Files: none were changed.</p>")
        ends = a["answers"]["endpoints"]
        if not a["collected"]["network"]:
            out.append("<p>Other computers: not recorded at this level of detail.</p>")
        elif ends:
            out.append("<p>Other computers contacted:</p><ul>" + "".join(
                f"<li><code>{esc(n['endpoint'])}</code>, {esc(SCOPE_PLAIN.get(n['scope'], n['scope']))}"
                f"{'' if n['state'] != 'failed' else ', but the connection failed'}.</li>" for n in ends) + "</ul>")
        else:
            out.append("<p>Other computers: none were contacted.</p>")

        out.append("<h2>Can this record be trusted?</h2>")
        if self.v:
            tone, lead, text = STATUS_PLAIN.get(self.status(), ("warn", "Unknown result.", ""))
            out.append(f"<div class='box {tone}'><b class='lead'>{esc(lead)}</b>{esc(text)}</div>")
        else:
            out.append("<p>The record was not checked on this computer.</p>")

        out.append("<h2>What this report cannot tell you</h2><ul>"
                   "<li>Some links are worked out from the order of events, for example that a file came from a "
                   "download. The percentages in the technical version show how much evidence supports each link. "
                   "They are not the chance of being right.</li>"
                   "<li>Only the program that was being watched, and the programs it started, were recorded. Not the whole "
                   "computer.</li>"
                   "<li>The tool records what happened. It does not stop an attack, and a skilled attacker could hide from it.</li>"
                   "</ul>")
        out.append("<h2>Words used</h2><table><tbody>"
                   "<tr><td><b>Program</b></td><td>Software that is running, such as a web browser.</td></tr>"
                   "<tr><td><b>Script</b></td><td>A file of instructions that a program follows.</td></tr>"
                   "<tr><td><b>Download</b></td><td>Copying a file from another computer.</td></tr>"
                   "<tr><td><b>Address</b></td><td>Where another computer can be reached, written like 1.2.3.4:80.</td></tr>"
                   "<tr><td><b>Digital signature</b></td><td>A seal made with the investigator's secret key, which shows "
                   "whether the record was changed.</td></tr></tbody></table>")
        return self.page("What happened (plain-language report)", "".join(out))

    def render(self, kind):
        return self.technical() if kind == "technical" else self.general()


def load_custody_files(evidence):
    manifest, audit = None, []
    mp = Path(f"{evidence}.manifest.json")
    if mp.is_file():
        try:
            manifest = json.loads(mp.read_text(encoding="utf-8", errors="replace"))
        except ValueError:
            manifest = None
    ap = Path(f"{evidence}.audit.jsonl")
    if ap.is_file():
        for line in ap.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                audit.append(json.loads(line))
            except ValueError:
                pass
    return manifest, audit


def html_to_pdf(html_text, out):
    """Print HTML to PDF with headless Chromium. Raises RuntimeError if no browser is installed."""
    browser = next((b for b in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable") if shutil.which(b)), None)
    if browser is None:
        raise RuntimeError("PDF needs Chromium or Google Chrome on this machine")
    out = Path(out).resolve()
    # Snap Chromium can only read and write under the home folder, so the page sits next to the PDF.
    page = out.with_suffix(".html")
    page.write_text(html_text, encoding="utf-8")
    try:
        subprocess.run([browser, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                        f"--print-to-pdf={out}", f"file://{page}"], check=True, timeout=90,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        page.unlink(missing_ok=True)
    if not out.is_file() or out.stat().st_size == 0:
        raise RuntimeError("Chromium did not produce a PDF")
    return out


def build(evidence, kind, pubkey=None, verification=None):
    doc = reconstruct.load_evidence(evidence)
    analysis = reconstruct.reconstruct(doc)
    if verification is None:
        verification = verify(evidence, pubkey)
    manifest, audit = load_custody_files(evidence)
    return Report(doc, analysis, verification, manifest, audit, str(evidence)).render(kind)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("evidence")
    ap.add_argument("--kind", choices=KINDS, default="technical")
    ap.add_argument("--pubkey", help="trusted public key for verification")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--html", help="write the HTML report here")
    group.add_argument("--pdf", help="write a PDF here (needs Chromium)")
    args = ap.parse_args()
    page = build(args.evidence, args.kind, args.pubkey)
    if args.pdf:
        print(f"wrote {html_to_pdf(page, args.pdf)}")
    elif args.html:
        Path(args.html).write_text(page, encoding="utf-8")
        print(f"wrote {args.html}")
    else:
        sys.stdout.write(page)


if __name__ == "__main__":
    main()

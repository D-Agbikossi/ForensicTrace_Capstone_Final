/* ForensicTrace dashboard front end. No dependencies.
 * Evidence is untrusted (a trace can contain any file name), so all text reaches
 * the page through text nodes: h() and s() never parse markup. */
"use strict";

const SVG_NS = "http://www.w3.org/2000/svg";

function fill(el, attrs, kids) {
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
    else el.setAttribute(k === "cls" ? "class" : k, v === true ? "" : v);
  }
  for (const kid of kids.flat(Infinity)) {
    if (kid === null || kid === undefined || kid === false) continue;
    el.append(kid instanceof Node ? kid : document.createTextNode(String(kid)));
  }
  return el;
}
const h = (tag, attrs, ...kids) => fill(document.createElement(tag), attrs, kids);
const s = (tag, attrs, ...kids) => fill(document.createElementNS(SVG_NS, tag), attrs, kids);
const $ = (id) => document.getElementById(id);
const base = (p) => { const t = String(p || "").replace(/\/+$/, ""); return t.slice(t.lastIndexOf("/") + 1) || p || ""; };
const pct = (v) => `${Math.round(v * 100)}%`;
const fmtNum = (v) => Number(v).toLocaleString("en-US");
const css = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();

function fmtMs(ms) {
  if (ms === null || ms === undefined) return "";
  if (ms >= 1000) return `${(ms / 1000).toFixed(2)} s`;
  return `${ms.toFixed(ms < 10 ? 2 : 1)} ms`;
}
function fmtBytes(b) {
  if (!b) return "0 B";
  if (b < 1024) return `${b} B`;
  if (b < 1048576) return `${(b / 1024).toFixed(1)} KB`;
  return `${(b / 1048576).toFixed(1)} MB`;
}
function fmtUtc(text) {
  if (!text) return "";
  return `${text.slice(0, 19).replace("T", " ")} UTC`;
}

const api = {
  token: null,
  async get(url) {
    const r = await fetch(url);
    const body = await r.json().catch(() => ({}));
    if (!r.ok) throw Object.assign(new Error(body.error || `HTTP ${r.status}`), { status: r.status });
    return body;
  },
  async post(url, payload) {
    const r = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-FT-Token": api.token },
      body: JSON.stringify(payload),
    });
    const body = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(body.error || `HTTP ${r.status}`);
    return body;
  },
};

const TABS = [
  ["overview", "Overview"], ["graph", "Reconstruction"], ["timeline", "Timeline"], ["processes", "Process tree"],
  ["network", "Network"], ["files", "Files"], ["compare", "Configurations"], ["custody", "Chain of custody"],
  ["reports", "Reports"],
];

const state = {
  session: null, cases: [], caseId: null, data: null, loadError: null, tab: "overview", custody: null,
  compare: { mode: "ptrace", scenario: "ALL" }, inspector: null,
  timeline: { types: { process: true, file: true, network: true, other: true }, signal: true, pid: "", q: "", failed: false, page: 0, view: null },
  graph: { scope: "chain", selected: null },
  files: { filter: "changed", q: "" },
  network: { probes: false },
  processes: { all: false },
};

const STATUS_TEXT = {
  verified_signed_pinned: ["good", "✓", "Verified, signed by trusted key"],
  verified_signed_unpinned: ["warn", "!", "Intact, signer not pinned"],
  verified_unsigned: ["warn", "!", "Intact, not signed"],
  legacy_sidecar_ok: ["none", "i", "Sidecar hash only (schema 2)"],
  failed: ["bad", "✕", "Verification failed"],
};
function statusPill(status) {
  const [cls, icon, text] = STATUS_TEXT[status] || ["none", "?", "Not verified yet"];
  return h("span", { cls: `status ${cls}` }, h("i", { "aria-hidden": "true" }, icon), text);
}
const SEVERITY = { critical: ["bad", "✕", "Critical"], high: ["serious", "!", "High"], medium: ["warn", "!", "Medium"], low: ["none", "i", "Low"] };
function severityPill(sev) {
  const [cls, icon, text] = SEVERITY[sev];
  return h("span", { cls: `status ${cls}` }, h("i", { "aria-hidden": "true" }, icon), text);
}
function meter(v, tier) {
  return h("span", { cls: "meter", title: tier ? `${tier}; rule-based score, not a probability` : "rule-based score, not a probability" },
    h("span", { cls: "track" }, h("span", { cls: "fill", style: `width:${Math.round(v * 100)}%` })), pct(v));
}

/* ---------- routing ---------- */

function writeHash() {
  const parts = [state.tab, encodeURIComponent(state.caseId || "")];
  const want = `#${parts.join("/")}`;
  if (location.hash !== want) history.replaceState(null, "", want);
}
function readHash() {
  const [tab, id] = location.hash.slice(1).split("/");
  if (TABS.some(([k]) => k === tab)) state.tab = tab;
  return id ? decodeURIComponent(id) : null;
}

function setTab(tab) {
  state.tab = tab;
  closeInspector();
  writeHash();
  renderNav();
  renderHeader();
  renderView();
  $("main").focus({ preventScroll: true });
  window.scrollTo(0, 0);
}

/* ---------- case loading ---------- */

async function loadCases() {
  state.cases = (await api.get("/api/cases")).cases;
  const sel = $("case-select");
  sel.replaceChildren();
  const groups = new Map();
  for (const c of state.cases) {
    if (!groups.has(c.group)) groups.set(c.group, h("optgroup", { label: c.group }));
    const bits = [c.name];
    if (c.case_id && !c.name.startsWith(c.case_id)) bits.push(c.case_id);
    groups.get(c.group).append(h("option", { value: c.id }, bits.join(" · ")));
  }
  sel.append(...groups.values());
  if (state.caseId) sel.value = state.caseId;
}

async function openCase(id) {
  state.caseId = id;
  state.data = null;
  state.loadError = null;
  state.custody = null;
  state.timeline.view = null;
  state.timeline.page = 0;
  state.timeline.pid = "";
  state.graph.selected = null;
  closeInspector();
  writeHash();
  $("case-select").value = id || "";
  renderHeader();
  renderNav();
  $("view").replaceChildren(h("p", { cls: "hint" }, h("span", { cls: "spinner" }), "Reading evidence and reconstructing the incident"));
  try {
    const data = await api.get(`/api/case?id=${encodeURIComponent(id)}`);
    if (state.caseId !== id) return;
    data.eventById = new Map(data.doc.events.map((e) => [e.id, e]));
    data.signal = new Set(data.analysis.signal_events);
    data.edgeById = new Map(data.analysis.graph.edges.map((e) => [e.id, e]));
    data.nodeById = new Map(data.analysis.graph.nodes.map((n) => [n.id, n]));
    data.procByPid = new Map(data.analysis.processes.map((p) => [p.pid, p]));
    state.data = data;
  } catch (err) {
    if (state.caseId !== id) return;
    state.loadError = err.message;
    if (state.tab !== "custody") state.tab = "custody";
  }
  renderHeader();
  renderNav();
  renderView();
  loadCustody(id);
}

async function loadCustody(id) {
  try {
    const c = await api.get(`/api/custody?id=${encodeURIComponent(id)}`);
    if (state.caseId !== id) return;
    state.custody = c;
  } catch (err) {
    if (state.caseId !== id) return;
    state.custody = { error: err.message };
  }
  renderHeader();
  if (state.tab === "custody" || state.tab === "overview") renderView();
}

/* ---------- chrome ---------- */

function renderNav() {
  $("nav").replaceChildren(...TABS.map(([key, label]) => h("button", {
    "aria-current": state.tab === key ? "page" : null, onclick: () => setTab(key),
  }, label)));
}

function renderHeader() {
  const el = $("case-header");
  const c = state.cases.find((x) => x.id === state.caseId);
  const title = Object.fromEntries(TABS)[state.tab];
  if (!c) { el.replaceChildren(h("div", { cls: "case-head" }, h("h1", null, title))); return; }
  const status = state.custody && state.custody.verification ? state.custody.verification.status : null;
  el.replaceChildren(h("div", { cls: "case-head" }, h("h1", null, title),
    h("div", { cls: "case-meta" },
      c.scenario ? h("span", null, c.scenario) : h("span", null, c.name),
      c.config ? h("span", null, `Config ${c.config}: ${state.session.config_names[c.config]}`) : null,
      h("button", { cls: "link", style: "text-decoration:none", onclick: () => setTab("custody"), "aria-label": "Open chain of custody" },
        status ? statusPill(status) : h("span", { cls: "status none" }, h("span", { cls: "spinner" }), "Verifying")))));
}

/* ---------- shared bits ---------- */

function eventLink(id, label) {
  return h("button", { cls: "link", onclick: () => inspectEvent(id) }, label || `#${id}`);
}
function evidenceLinks(ids, max = 8) {
  const list = ids.slice(0, max).map((i) => eventLink(i));
  return h("span", { cls: "evlinks" }, "Events", list, ids.length > max ? `+${ids.length - max} more` : null);
}
function card(title, sub, ...kids) {
  return h("section", { cls: "card" }, title ? h("h2", null, title) : null, sub ? h("p", { cls: "card-sub" }, sub) : null, kids);
}
function notice(kind, title, text) {
  const icons = { warn: "!", bad: "✕", good: "✓", info: "i" };
  return h("div", { cls: `notice ${kind}`, role: kind === "bad" ? "alert" : null },
    h("span", { cls: "notice-icon", "aria-hidden": "true" }, icons[kind]),
    h("div", null, h("b", null, title), text));
}
function collectionNotice(a, config) {
  const missing = [];
  if (!a.collected.file) missing.push("file");
  if (!a.collected.network) missing.push("network");
  if (!missing.length) return null;
  return notice("warn", `Configuration ${config} did not collect ${missing.join(" or ")} events`,
    `Anything shown as "not collected" is unknown, not absent. Re-run under configuration C to see it.`);
}
function openInspector(title, ...kids) {
  const el = $("inspector");
  el.hidden = false;
  el.replaceChildren();
  fill(el, null, [h("div", { cls: "inspector-head" }, h("h2", null, title),
    h("button", { onclick: closeInspector, "aria-label": "Close details" }, "Close")), kids]);
  el.scrollTop = 0;
}
function closeInspector() {
  const el = $("inspector");
  el.hidden = true;
  el.replaceChildren();
}
document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !$("investigate-dialog").open) closeInspector(); });

function inspectEvent(id) {
  const d = state.data;
  const e = d.eventById.get(id);
  if (!e) return;
  const events = d.doc.events;
  const parent = e.parent_event >= 0 ? events[e.parent_event] : null;
  const res = e.resource_event >= 0 ? events[e.resource_event] : null;
  const cited = d.analysis.graph.edges.filter((r) => r.evidence.includes(id));
  const failed = e.ret !== null && e.ret < 0 && e.ret > -4096;
  const rows = [
    ["Time", `+${fmtMs((e.ts_ns - events[0].ts_ns) / 1e6)}`], e.ts_wall ? ["UTC", e.ts_wall] : null,
    ["Type", e.type], ["System call", e.syscall],
    ["Process", `${base(e.exe) || "(starting)"} (pid ${e.pid})`], ["Parent PID", e.ppid], ["UID", e.uid],
    ["Target", e.target || "—"], ["Detail", e.detail || "—"], ["Return", e.ret === null ? "none (did not return)" : e.ret],
    e.event_uid ? ["Event ID", e.event_uid] : null,
  ].filter(Boolean);
  openInspector(`Event #${id}`,
    h("dl", { cls: "kv" }, rows.map(([k, v]) => [h("dt", null, k), h("dd", { cls: k === "Return" && failed ? "failed" : null }, String(v))])),
    e.event_hash ? [h("p", { cls: "section-title" }, "Event hash"), h("p", { cls: "hash" }, e.event_hash),
      h("p", { cls: "section-title" }, "Links to previous hash"), h("p", { cls: "hash" }, e.prev_hash)] : null,
    h("p", { cls: "section-title" }, "How it connects"),
    parent ? h("p", null, "Caused by ", eventLink(parent.id, `#${parent.id} ${parent.syscall}`), parent.pid !== e.pid ? ` in pid ${parent.pid}` : "") : h("p", { cls: "hint" }, "No process predecessor"),
    res ? h("p", null, "Same resource as ", eventLink(res.id, `#${res.id} ${res.syscall}`)) : null,
    cited.length ? [h("p", { cls: "section-title" }, "Supports these relations"),
      cited.map((r) => h("p", null, h("button", { cls: "link", onclick: () => inspectRelations([r], r.summary) }, r.summary)))] : null);
}

function inspectRelations(rels, title) {
  openInspector(title, rels.map((r) => {
    const events = r.evidence.map((i) => state.data.eventById.get(i)).filter(Boolean);
    return h("div", { cls: "rel" },
      rels.length > 1 ? h("p", { cls: "rel-head" }, r.summary) : null,
      h("div", { cls: "rel-meta" }, meter(r.confidence, r.tier),
        h("span", null, r.tier === "inferred" ? "Inferred" : "Directly observed"), h("span", null, r.rule),
        r.count > 1 ? h("span", null, `${r.count} times`) : null, r.bytes ? h("span", null, fmtBytes(r.bytes)) : null),
      h("p", { cls: "section-title" }, "Why this confidence"),
      h("ul", { cls: "factors" }, r.factors.map((f) => h("li", null,
        h("span", { cls: "v" }, f.value ? `+${Math.round(f.value * 100)}` : "note"), h("span", null, f.label)))),
      h("p", { cls: "section-title" }, `Supporting evidence (${r.evidence.length})`),
      h("div", { cls: "table-wrap" }, h("table", null, h("tbody", null, events.slice(0, 40).map((e) => h("tr", { cls: "clickable", onclick: () => inspectEvent(e.id) },
        h("td", { cls: "num" }, `#${e.id}`), h("td", null, e.syscall), h("td", { cls: "path" }, e.target || e.detail)))))),
      events.length > 40 ? h("p", { cls: "hint" }, `${events.length - 40} more not shown`) : null);
  }), h("p", { cls: "hint", style: "margin-top:12px" }, "Confidence is a rule-based score from the listed factors. It is not a measured probability."));
}

/* ---------- overview ---------- */

function renderOverview(view) {
  const { doc, analysis: a } = state.data;
  const sm = a.summary;
  const tile = (label, value, tab) => h(tab ? "button" : "div", { cls: "tile", onclick: tab ? () => setTab(tab) : null },
    h("div", { cls: "tile-label" }, label),
    value === null ? h("div", { cls: "tile-value small" }, "Not collected") : h("div", { cls: "tile-value" }, fmtNum(value)));
  view.append(h("div", { cls: "tiles" },
    tile("Processes monitored", sm.processes, "processes"),
    tile("System calls captured", sm.syscalls, "timeline"),
    tile("Files accessed", a.collected.file ? sm.files_accessed : null, "files"),
    tile("Network connections", a.collected.network ? sm.connections : null, "network"),
    tile("Suspicious activities", sm.suspicious)));
  const limit = collectionNotice(a, doc.config);
  if (limit) view.append(limit);
  if (state.custody && state.custody.verification && state.custody.verification.status === "failed") {
    view.append(notice("bad", "This evidence failed verification", "Do not rely on these results until the problem is explained. See Chain of custody."));
  }
  view.append(h("div", { cls: "grid-2" }, renderAnswers(a),
    h("div", { cls: "stack" }, renderFindings(a), renderChainSummary(a))));
}

function renderAnswers(a) {
  const q = a.answers;
  const unknown = (t) => h("p", { cls: "unknown" }, t);
  const proc = (p) => `${base(p.exe) || "process"} (pid ${p.pid})`;
  const rows = [];
  rows.push(["Who started it?", q.initiator ? h("div", { cls: "answer" },
    h("div", null, h("code", null, q.initiator.command)),
    h("div", { cls: "answer-meta" }, `pid ${q.initiator.pid}, uid ${q.initiator.uid}`, meter(q.initiator.confidence), evidenceLinks(q.initiator.evidence))) : unknown("No events recorded")]);
  rows.push(["Who downloaded the payload?", q.downloads.length ? q.downloads.map((d) => h("div", { cls: "answer" },
    h("div", null, h("b", null, proc(d)), " fetched ", h("code", null, d.file), " from ", h("code", null, d.endpoint)),
    h("div", { cls: "answer-meta" }, meter(d.confidence, "inferred"), `started via ${d.lineage.map((l) => base(l.exe) || l.pid).join(" → ")}`, evidenceLinks(d.evidence, 4)))) : unknown(q.downloads_note)]);
  rows.push(["Was anything executed?", q.executions.length ? q.executions.map((d) => h("div", { cls: "answer" },
    h("div", null, h("code", null, d.file), " ran as ", h("b", null, `pid ${d.pid}`)),
    h("div", { cls: "answer-meta" }, meter(d.confidence, "inferred"), evidenceLinks(d.evidence, 4)))) : unknown(a.collected.file ? "No file written during this trace was executed" : `not collected: configuration ${state.data.doc.config} records no file events`)]);
  const opWords = { created: "created", overwritten: "overwritten", wrote: "written", deleted: "deleted", chmod: "mode changed", read_denied: "read denied", write_denied: "write denied", opened_for_write: "opened for write" };
  rows.push(["Which files were affected?", q.affected_files.length ? h("div", null, q.affected_files.slice(0, 5).map((f) => h("div", { cls: "answer" },
    h("div", null, h("code", null, f.path)),
    h("div", { cls: "answer-meta" }, Object.keys(f.ops).map((k) => opWords[k] || k).join(", "), meter(f.confidence), f.processes.slice(0, 3).map((p) => proc(p)).join(", ")))),
    q.affected_files.length > 5 ? h("button", { cls: "link", onclick: () => setTab("files") }, `All ${q.affected_files.length} files`) : null) : unknown(q.affected_files_note || "No file changes were recorded")]);
  rows.push(["Which endpoints were contacted?", q.endpoints.length ? q.endpoints.map((n) => h("div", { cls: "answer" },
    h("div", null, h("code", null, n.endpoint), n.proto !== "unknown" ? ` ${n.proto.toUpperCase()}` : "", " ", h("span", { cls: "chip" }, n.scope), " ", n.state === "failed" ? h("span", { cls: "chip warn" }, "failed") : null),
    h("div", { cls: "answer-meta" }, n.processes.map(proc).join(", "), meter(n.confidence), `${fmtBytes(n.bytes_sent)} out, ${fmtBytes(n.bytes_received)} in`, evidenceLinks(n.evidence, 4)))) : unknown(q.endpoints_note || "No outbound connections were recorded")]);
  return card("What happened", null, h("dl", { cls: "qa" }, rows.map(([k, v], i) => [
    h("dt", { cls: i === 0 ? "first" : null }, k), h("dd", { cls: i === 0 ? null : "sep" }, v)])));
}

function renderChainSummary(a) {
  const edges = a.answers.chain.map((i) => state.data.edgeById.get(i));
  if (!edges.length) {
    return card("Attack chain", null, h("p", { cls: "unknown" }, a.collected.file ? "No download or payload-execution chain was found." : `Cannot be assessed: configuration ${state.data.doc.config} records no file events.`));
  }
  const weakest = edges.reduce((x, y) => (y.confidence < x.confidence ? y : x));
  return card("Attack chain", `${edges.length} linked steps, weakest link ${pct(weakest.confidence)} (rule-based score, not a measured probability)`,
    h("div", { cls: "actions", style: "margin-top:0" },
      h("button", { onclick: () => setTab("graph") }, "Open the reconstruction"),
      h("button", { onclick: () => setTab("reports") }, "Get the case reports")));
}

function inspectFinding(f) {
  openInspector(f.title, severityPill(f.severity), h("p", { style: "margin:8px 0" }, f.why), h("p", { cls: "hint" }, `Rule ${f.rule}`),
    f.events.length ? [h("p", { cls: "section-title" }, `Supporting events (${f.events.length})`), evidenceLinks(f.events, 30)] : null);
}

function renderFindings(a) {
  if (!a.findings.length) {
    return card("Suspicious activity", null, h("p", { cls: "unknown" }, "No detection rule fired. Rules only cover known patterns, so this is not proof of a clean system."));
  }
  return card("Suspicious activity", null, h("ul", { cls: "incident-list" }, a.findings.map((f) => h("li", null, h("button", { cls: "incident", onclick: () => inspectFinding(f) },
    h("span", { cls: "body" }, h("span", { cls: "title" }, f.title)), severityPill(f.severity))))));
}

/* ---------- reconstruction graph ---------- */

const EDGE_PRIORITY = ["downloaded", "executed", "interpreted", "connected", "connect_failed", "created", "overwritten", "deleted", "chmod", "read_denied", "write_denied", "wrote", "accepted", "spawned", "opened_for_write", "read"];
const EDGE_LABEL = { downloaded: "downloaded", executed: "executed as", interpreted: "ran script", connected: "connected", connect_failed: "failed connect", created: "created", overwritten: "overwrote", deleted: "deleted", chmod: "chmod", read_denied: "denied", write_denied: "denied", wrote: "wrote", accepted: "accepted by", spawned: "started", opened_for_write: "opened", read: "read" };

function graphSubset(a) {
  const scope = state.graph.scope;
  const chain = new Set(a.answers.chain);
  let edges = a.graph.edges;
  if (scope === "chain" && chain.size) edges = edges.filter((e) => chain.has(e.id));
  else if (scope !== "all") {
    const hide = new Set(a.graph.nodes.filter((n) => n.noise).map((n) => n.id));
    edges = edges.filter((e) => !hide.has(e.src) && !hide.has(e.dst) && e.kind !== "read");
  }
  const used = new Set(edges.flatMap((e) => [e.src, e.dst]));
  return { nodes: a.graph.nodes.filter((n) => used.has(n.id)), edges, chain };
}

/* Layered layout, top to bottom: row = longest path from a source, order = barycentre sweeps. */
function layoutGraph(nodes, edges) {
  const W = 176, H = 48, GX = 64, GY = 62, PAD = 20, SIDE = 130;
  const out = new Map(nodes.map((n) => [n.id, []]));
  const inc = new Map(nodes.map((n) => [n.id, []]));
  for (const e of edges) { out.get(e.src).push(e.dst); inc.get(e.dst).push(e.src); }
  const depth = new Map();
  const visiting = new Set();
  const walk = (id) => {
    if (depth.has(id)) return depth.get(id);
    if (visiting.has(id)) return 0;
    visiting.add(id);
    let d = 0;
    for (const p of inc.get(id)) if (!visiting.has(p)) d = Math.max(d, walk(p) + 1);
    visiting.delete(id);
    depth.set(id, d);
    return d;
  };
  nodes.forEach((n) => walk(n.id));
  const rows = [];
  for (const n of [...nodes].sort((a, b) => a.first_ms - b.first_ms)) {
    const d = depth.get(n.id);
    (rows[d] = rows[d] || []).push(n.id);
  }
  const slot = new Map();
  const assign = () => rows.forEach((row) => row && row.forEach((id, i) => slot.set(id, i - (row.length - 1) / 2)));
  assign();
  for (let sweep = 0; sweep < 4; sweep++) {
    for (const row of rows) {
      if (!row) continue;
      const score = (id) => {
        const ns = (sweep % 2 ? out : inc).get(id).filter((x) => slot.has(x));
        return ns.length ? ns.reduce((t, x) => t + slot.get(x), 0) / ns.length : slot.get(id);
      };
      const scored = row.map((id) => [score(id), id]);
      scored.sort((x, y) => x[0] - y[0]);
      row.splice(0, row.length, ...scored.map((x) => x[1]));
    }
    assign();
  }
  const cols = Math.max(1, ...rows.map((r) => (r ? r.length : 0)));
  const width = SIDE * 2 + cols * (W + GX) - GX;   // SIDE leaves room for links routed around a box
  const pos = new Map();
  rows.forEach((row, y) => {
    if (!row) return;
    const offset = (cols - row.length) * (W + GX) / 2;
    row.forEach((id, x) => pos.set(id, { x: SIDE + offset + x * (W + GX), y: PAD + y * (H + GY) }));
  });
  return { pos, W, H, width, height: PAD * 2 + rows.length * (H + GY) - GY };
}

function renderGraph(view) {
  const { doc, analysis: a } = state.data;
  const hasChain = a.answers.chain.length > 0;
  if (!hasChain && state.graph.scope === "chain") state.graph.scope = "relevant";
  const seg = (key, label) => h("button", { "aria-pressed": String(state.graph.scope === key), disabled: key === "chain" && !hasChain,
    onclick: () => { state.graph.scope = key; state.graph.selected = null; closeInspector(); renderView(); } }, label);
  const filters = h("div", { cls: "filters" },
    h("div", { cls: "seg", role: "group", "aria-label": "Graph scope" }, seg("chain", "Attack chain"), seg("relevant", "Incident"), seg("all", "Everything")),
    h("div", { cls: "legend" },
      h("span", null, h("i", { cls: "key process" }), "Process"), h("span", null, h("i", { cls: "key file" }), "File"),
      h("span", null, h("i", { cls: "key network" }), "Endpoint"),
      h("span", null, h("i", { cls: "edge-key" }), "Observed"), h("span", null, h("i", { cls: "edge-key dashed" }), "Inferred"),
      h("span", null, h("i", { cls: "edge-key hot" }), "On the chain")));

  const { nodes, edges, chain } = graphSubset(a);
  const limit = collectionNotice(a, doc.config);
  if (limit) view.append(limit);
  view.append(filters);
  if (!nodes.length) {
    view.append(card(null, null, h("p", { cls: "unknown" }, "No relations to show at this scope.")));
    return;
  }

  const pairs = new Map();
  for (const e of edges) {
    const key = `${e.src}\u0000${e.dst}`;
    if (!pairs.has(key)) pairs.set(key, []);
    pairs.get(key).push(e);
  }
  const layout = layoutGraph(nodes, edges);
  const svg = s("svg", { width: layout.width, height: layout.height, viewBox: `0 0 ${layout.width} ${layout.height}`, role: "group", "aria-label": "Incident reconstruction graph" });
  const defs = s("defs");
  for (const [id, color] of [["arrow", "--axis"], ["arrow-key", "--accent"], ["arrow-sel", "--ink"]]) {
    defs.append(s("marker", { id, viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse" },
      s("path", { d: "M0 0 L10 5 L0 10 z", fill: css(color) })));
  }
  svg.append(defs);

  // Labels slide along their line until they clear the labels already placed.
  const placed = [];
  const placeLabel = (text, curve) => {
    const w = text.length * 6.3 + 4;
    const at = (t) => {
      const u = 1 - t;
      const [a, b, c, e] = curve;
      return [u * u * u * a[0] + 3 * u * u * t * b[0] + 3 * u * t * t * c[0] + t * t * t * e[0],
        u * u * u * a[1] + 3 * u * u * t * b[1] + 3 * u * t * t * c[1] + t * t * t * e[1]];
    };
    let best = null;
    for (const t of [0.5, 0.36, 0.64, 0.24, 0.76, 0.14, 0.86]) {
      const [x, y] = at(t);
      for (const side of [1, -1]) {
        const rect = { x: side > 0 ? x + 6 : x - 6 - w, y: y - 9, w, h: 15 };
        const clash = placed.some((o) => rect.x < o.x + o.w && o.x < rect.x + rect.w && rect.y < o.y + o.h && o.y < rect.y + rect.h);
        if (!clash) { best = rect; break; }
      }
      if (best) break;
    }
    if (!best) { const [x, y] = at(0.5); best = { x: x + 6, y: y - 9, w, h: 15 }; }
    placed.push(best);
    return best;
  };
  const edgeLayer = s("g");
  const ordered = [...pairs].sort(([, x], [, y]) => Number(y.some((e) => chain.has(e.id))) - Number(x.some((e) => chain.has(e.id))));
  for (const [key, group] of ordered) {
    const sorted = [...group].sort((x, y) => EDGE_PRIORITY.indexOf(x.kind) - EDGE_PRIORITY.indexOf(y.kind));
    const lead = sorted[0];
    const p1 = layout.pos.get(lead.src), p2 = layout.pos.get(lead.dst);
    if (!p1 || !p2) continue;
    const onChain = group.some((e) => chain.has(e.id));
    const down = p2.y > p1.y;
    const x1 = p1.x + (down ? layout.W / 2 : layout.W), y1 = down ? p1.y + layout.H : p1.y + layout.H / 2;
    const x2 = p2.x + (down ? layout.W / 2 : layout.W), y2 = down ? p2.y : p2.y + layout.H / 2;
    // Links against the flow leave and enter by the right side, so they stay readable.
    // A link skipping rows must not run behind a box, or it reads as passing through that node.
    const blocked = down && nodes.some((n) => {
      const q = layout.pos.get(n.id);
      if (!q || n.id === lead.src || n.id === lead.dst || q.y + layout.H <= y1 || q.y >= y2) return false;
      const lineX = x1 + (x2 - x1) * ((q.y + layout.H / 2 - y1) / (y2 - y1));
      return Math.abs(q.x + layout.W / 2 - lineX) < layout.W / 2 + 14;
    });
    const curve = !down
      ? [[x1, y1], [x1 + 60, y1], [x2 + 60, y2], [x2, y2]]
      : blocked
        ? [[x1, y1], [x1 + layout.W, y1 + 40], [x2 + layout.W, y2 - 40], [x2, y2]]
        : [[x1, y1], [x1, y1 + 30], [x2, y2 - 30], [x2, y2]];
    const d = `M${x1} ${y1} C${curve[1].join(" ")} ${curve[2].join(" ")} ${x2} ${y2}`;
    const selected = state.graph.selected === `e:${key}`;
    const inferred = group.some((e) => e.tier === "inferred");
    const marker = selected ? "arrow-sel" : onChain ? "arrow-key" : "arrow";
    const label = `${EDGE_LABEL[lead.kind] || lead.kind}${group.length > 1 ? ` +${group.length - 1}` : ""} ${pct(lead.confidence)}`;
    const open = () => {
      state.graph.selected = `e:${key}`;
      renderView();
      inspectRelations(sorted, `${nodeName(lead.src)} → ${nodeName(lead.dst)}`);
    };
    const showLabel = onChain || inferred || selected || group.some((e) => e.kind !== "spawned");
    const spot = showLabel ? placeLabel(label, curve) : null;
    edgeLayer.append(s("g", { cls: `g-edge${onChain ? " key" : ""}${inferred ? " inferred" : ""}${selected ? " selected" : ""}`,
      tabindex: 0, role: "button", "aria-label": sorted.map((e) => `${e.summary}, ${pct(e.confidence)} ${e.tier}`).join("; "),
      onclick: open, onkeydown: (ev) => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); open(); } } },
    s("path", { cls: "line", d, "marker-end": `url(#${marker})` }), s("path", { cls: "hit", d }),
    spot ? s("text", { x: spot.x, y: spot.y + 11 }, label) : null));
  }
  svg.append(edgeLayer);

  for (const n of nodes) {
    const p = layout.pos.get(n.id);
    if (!p) continue;
    const key = `n:${n.id}`;
    const open = () => { state.graph.selected = key; renderView(); inspectNode(n); };
    const g = s("g", { cls: `g-node ${n.type}${state.graph.selected === key ? " selected" : ""}`, transform: `translate(${p.x} ${p.y})`,
      tabindex: 0, role: "button", "aria-label": `${n.type} ${n.path || n.exe || n.label}`, onclick: open,
      onkeydown: (ev) => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); open(); } },
      onpointermove: (ev) => showTip(ev, n.path || n.exe || n.label, n.type), onpointerleave: hideTip });
    if (n.type === "file") {
      const w = layout.W, ht = layout.H, c = 12;
      g.append(s("path", { cls: "shape", d: `M0 0 H${w - c} L${w} ${c} V${ht} H0 Z M${w - c} 0 V${c} H${w}` }));
    } else {
      g.append(s("rect", { width: layout.W, height: layout.H, rx: n.type === "endpoint" ? layout.H / 2 : 8 }));
    }
    const sub = n.type === "process" ? `pid ${n.pid}` : n.type === "file" ? shorten(n.path.slice(0, n.path.length - base(n.path).length), 25) || "/" : `${n.proto !== "unknown" ? n.proto.toUpperCase() + ", " : ""}${n.scope}`;
    g.append(s("text", { x: 12, y: 21 }, shorten(n.label, 21)), s("text", { cls: "sub", x: 12, y: 37 }, sub));
    svg.append(g);
  }

  const wrap = h("div", { cls: "graph-wrap" }, svg);
  view.append(card(null, null, wrap,
    h("p", { cls: "hint", style: "margin-top:8px" }, "Select a line for the events behind it and how its confidence was reached, or a box for everything that touched it.")));
  wrap.scrollLeft = (wrap.scrollWidth - wrap.clientWidth) / 2;   // the chain runs down the middle

  const sortedEdges = [...edges].sort((x, y) => x.ms - y.ms);
  view.append(card("All relations in this view", `${sortedEdges.length} relations, in time order`,
    h("div", { cls: "table-wrap" }, h("table", null,
      h("thead", null, h("tr", null, h("th", { cls: "num" }, "Time"), h("th", null, "Relation"), h("th", null, "Basis"), h("th", null, "Confidence"), h("th", { cls: "num" }, "Events"))),
      h("tbody", null, sortedEdges.map((e) => h("tr", { cls: "clickable", onclick: () => inspectRelations([e], e.summary) },
        h("td", { cls: "num" }, `+${fmtMs(e.ms)}`), h("td", { cls: "path" }, e.summary), h("td", null, e.tier), h("td", null, meter(e.confidence, e.tier)), h("td", { cls: "num" }, e.evidence.length))))))));
}

function shorten(text, n) {
  text = String(text);
  return text.length <= n ? text : `${text.slice(0, n - 1)}…`;
}
function nodeName(id) {
  const n = state.data.nodeById.get(id);
  if (!n) return id;
  return n.type === "process" ? `${n.label} (${n.pid})` : n.label;
}
function inspectNode(n) {
  const rels = state.data.analysis.graph.edges.filter((e) => e.src === n.id || e.dst === n.id).sort((x, y) => x.ms - y.ms);
  openInspector(n.path || n.exe || n.label,
    h("div", { cls: "rel-meta" }, h("span", { cls: "chip" }, n.type), n.pid ? `pid ${n.pid}` : null, n.category ? h("span", { cls: "chip" }, n.category) : null, n.scope ? h("span", { cls: "chip" }, n.scope) : null),
    n.pid ? h("div", { cls: "actions" }, h("button", { onclick: () => { state.timeline.pid = String(n.pid); state.timeline.signal = false; setTab("timeline"); } }, "Show this process in the timeline")) : null,
    h("p", { cls: "section-title" }, `Relations (${rels.length})`),
    rels.map((r) => h("div", { cls: "rel" }, h("button", { cls: "link", onclick: () => inspectRelations([r], r.summary) }, r.summary),
      h("div", { cls: "rel-meta" }, meter(r.confidence, r.tier), `+${fmtMs(r.ms)}`))));
}

function showTip(ev, title, text) {
  const t = $("tooltip");
  t.hidden = false;
  t.replaceChildren(h("b", null, title), text ? String(text) : "");
  const x = Math.min(ev.clientX + 14, innerWidth - t.offsetWidth - 8);
  const y = ev.clientY + t.offsetHeight + 24 > innerHeight ? ev.clientY - t.offsetHeight - 10 : ev.clientY + 14;
  t.style.left = `${Math.max(8, x)}px`;
  t.style.top = `${y}px`;
}
function hideTip() { $("tooltip").hidden = true; }

/* ---------- timeline ---------- */

function timelineEvents() {
  const t = state.timeline;
  const d = state.data;
  const q = t.q.trim().toLowerCase();
  return d.doc.events.filter((e) => {
    if (!t.types[e.type]) return false;
    if (t.signal && !d.signal.has(e.id)) return false;
    if (t.pid && String(e.pid) !== t.pid) return false;
    if (t.failed && !(e.ret !== null && e.ret < 0 && e.ret > -4096)) return false;
    if (q && !`${e.syscall} ${e.target} ${e.detail} ${e.exe} ${e.pid}`.toLowerCase().includes(q)) return false;
    return true;
  });
}

function renderTimeline(view) {
  const t = state.timeline;
  const { doc, analysis: a } = state.data;
  const typeBox = (type) => h("label", null, h("input", { type: "checkbox", checked: t.types[type], onchange: (e) => { t.types[type] = e.target.checked; t.page = 0; renderView(); } }), h("i", { cls: `key ${type}` }), type);
  const present = ["process", "file", "network", "other"].filter((k) => a.summary.events_by_type[k]);
  const procs = [...a.processes].sort((x, y) => x.first_ms - y.first_ms);
  const filters = h("div", { cls: "filters" },
    present.map(typeBox),
    h("label", null, h("input", { type: "checkbox", checked: t.signal, onchange: (e) => { t.signal = e.target.checked; t.page = 0; renderView(); } }), "Hide start-up noise"),
    h("label", null, h("input", { type: "checkbox", checked: t.failed, onchange: (e) => { t.failed = e.target.checked; t.page = 0; renderView(); } }), "Failed only"),
    h("select", { "aria-label": "Process", onchange: (e) => { t.pid = e.target.value; t.page = 0; renderView(); } },
      h("option", { value: "" }, "All processes"),
      procs.map((p) => h("option", { value: p.pid, selected: String(p.pid) === t.pid }, `${base(p.exe) || "process"} (${p.pid})`))),
    h("input", { type: "search", placeholder: "Search target, syscall, PID", value: t.q, "aria-label": "Search events",
      oninput: (e) => { t.q = e.target.value; t.page = 0; clearTimeout(t.timer); t.timer = setTimeout(renderTimelineBody, 180); } }));
  const body = h("div", { id: "timeline-body" });
  const limit = collectionNotice(a, doc.config);
  if (limit) view.append(limit);
  view.append(filters, body);
  renderTimelineBody();
}

function renderTimelineBody() {
  const body = $("timeline-body");
  if (!body) return;
  const t = state.timeline;
  const events = timelineEvents();
  const base0 = state.data.doc.events.length ? state.data.doc.events[0].ts_ns : 0;
  const PAGE = 100;
  const inView = t.view ? events.filter((e) => { const m = (e.ts_ns - base0) / 1e6; return m >= t.view[0] && m <= t.view[1]; }) : events;
  const pages = Math.max(1, Math.ceil(inView.length / PAGE));
  t.page = Math.min(t.page, pages - 1);
  const rows = inView.slice(t.page * PAGE, (t.page + 1) * PAGE);
  const canvas = h("canvas", { role: "img", "aria-label": `Timeline of ${events.length} events by process; the table below lists the same events` });
  const wrap = h("div", { cls: "lanes-wrap" }, canvas);
  const legend = h("div", { cls: "filters", style: "margin:8px 0 0;justify-content:space-between" },
    h("span", { cls: "hint" }, "Each row is a process. Drag across the chart to zoom, double-click to reset, select a mark for its details."),
    t.view ? h("button", { onclick: () => { t.view = null; t.page = 0; renderTimelineBody(); } }, "Reset zoom") : null);
  body.replaceChildren(
    card(null, null, wrap, legend),
    card(`${fmtNum(inView.length)} events`, null,
      h("div", { cls: "table-wrap" }, h("table", null,
        h("thead", null, h("tr", null, h("th", { cls: "num" }, "#"), h("th", { cls: "num" }, "Time"), h("th", null, "Type"), h("th", null, "Process"), h("th", null, "Call"), h("th", null, "Target"))),
        h("tbody", null, rows.map((e) => {
          const failed = e.ret !== null && e.ret < 0 && e.ret > -4096 && e.ret !== -115;
          return h("tr", { cls: "clickable", tabindex: 0, onclick: () => inspectEvent(e.id), onkeydown: (ev) => { if (ev.key === "Enter") inspectEvent(e.id); } },
            h("td", { cls: "num" }, e.id), h("td", { cls: "num" }, `+${fmtMs((e.ts_ns - base0) / 1e6)}`),
            h("td", null, h("i", { cls: `key ${e.type}`, title: e.type })), h("td", null, `${base(e.exe) || "(start)"} ${e.pid}`),
            h("td", { cls: failed ? "failed" : null }, e.syscall, failed ? " failed" : ""), h("td", { cls: "path" }, e.target || e.detail));
        })))),
      pages > 1 ? h("div", { cls: "pager" },
        h("button", { disabled: t.page === 0, onclick: () => { t.page--; renderTimelineBody(); } }, "Previous"), `Page ${t.page + 1} of ${pages}`,
        h("button", { disabled: t.page >= pages - 1, onclick: () => { t.page++; renderTimelineBody(); } }, "Next")) : null));
  drawLanes(canvas, events, base0);
}

function drawLanes(canvas, events, base0) {
  const t = state.timeline;
  const lanes = [];
  const seen = new Map();
  for (const e of events) {
    if (!seen.has(e.pid)) { seen.set(e.pid, lanes.length); lanes.push(e.pid); }
  }
  const LABEL = 150, ROW = 24, TOP = 26, RIGHT = 14;
  const cssW = Math.max(480, canvas.parentElement.clientWidth);
  const cssH = Math.max(80, TOP + lanes.length * ROW + 6);
  const dpr = window.devicePixelRatio || 1;
  canvas.width = cssW * dpr;
  canvas.height = cssH * dpr;
  canvas.style.height = `${cssH}px`;
  const g = canvas.getContext("2d");
  g.scale(dpr, dpr);
  const total = state.data.doc.events.length ? (state.data.doc.events.at(-1).ts_ns - base0) / 1e6 : 1;
  const [v0, v1] = t.view || [0, Math.max(total, 0.001)];
  const X = (ms) => LABEL + (ms - v0) / (v1 - v0) * (cssW - LABEL - RIGHT);
  const fontBody = getComputedStyle(document.body).fontFamily;
  const colors = { process: css("--process"), file: css("--file"), network: css("--network"), other: css("--other") };

  g.clearRect(0, 0, cssW, cssH);
  g.font = `11px ${fontBody}`;
  g.textBaseline = "middle";
  const ticks = 6;
  for (let i = 0; i <= ticks; i++) {
    const ms = v0 + (v1 - v0) * i / ticks;
    const x = X(ms);
    g.strokeStyle = css("--grid");
    g.beginPath(); g.moveTo(x + .5, TOP - 4); g.lineTo(x + .5, cssH); g.stroke();
    g.fillStyle = css("--muted");
    g.textAlign = i === ticks ? "right" : i === 0 ? "left" : "center";
    g.fillText(fmtMs(ms), x, 12);
  }
  g.textAlign = "left";
  lanes.forEach((pid, i) => {
    const y = TOP + i * ROW;
    if (i) { g.strokeStyle = css("--grid"); g.beginPath(); g.moveTo(0, y + .5); g.lineTo(cssW, y + .5); g.stroke(); }
    const p = state.data.procByPid.get(pid);
    g.fillStyle = css("--ink");
    g.font = `12px ${fontBody}`;
    const label = shorten(base(p && p.exe) || "process", 15);
    g.fillText(label, 8, y + ROW / 2);
    const w = g.measureText(label).width;
    g.fillStyle = css("--muted");
    g.font = `11px ${fontBody}`;
    g.fillText(String(pid), 8 + w + 6, y + ROW / 2);
  });

  // Group by pixel: dense bursts become one mark, and every mark stays hoverable.
  const marks = new Map();
  for (const e of events) {
    const ms = (e.ts_ns - base0) / 1e6;
    if (ms < v0 || ms > v1) continue;
    const key = `${seen.get(e.pid)}:${Math.round(X(ms) / 3)}`;
    if (!marks.has(key)) marks.set(key, { x: X(ms), lane: seen.get(e.pid), events: [] });
    marks.get(key).events.push(e);
  }
  const rank = { network: 3, process: 2, file: 1, other: 0 };
  const list = [...marks.values()];
  for (const m of list) {
    m.lead = m.events.reduce((a, b) => (rank[b.type] > rank[a.type] ? b : a));
    const y = TOP + m.lane * ROW + ROW / 2;
    g.fillStyle = colors[m.lead.type];
    if (m.lead.type === "network") { // diamond, so type is not carried by colour alone
      g.beginPath(); g.moveTo(m.x, y - 6); g.lineTo(m.x + 6, y); g.lineTo(m.x, y + 6); g.lineTo(m.x - 6, y); g.closePath(); g.fill();
    } else if (m.lead.type === "process") {
      g.beginPath(); g.arc(m.x, y, 5, 0, 7); g.fill();
    } else {
      g.fillRect(m.x - 1.5, y - 7, 3, 14);
    }
  }

  const nearest = (ev) => {
    const r = canvas.getBoundingClientRect();
    const px = ev.clientX - r.left, py = ev.clientY - r.top;
    const lane = Math.floor((py - TOP) / ROW);
    let best = null, dist = 12;
    for (const m of list) {
      if (m.lane !== lane) continue;
      const d = Math.abs(m.x - px);
      if (d < dist) { dist = d; best = m; }
    }
    return { best, px };
  };
  let drag = null;
  canvas.onpointerdown = (ev) => {
    const px = ev.clientX - canvas.getBoundingClientRect().left;
    if (px > LABEL) { drag = { start: px, moved: false }; canvas.setPointerCapture(ev.pointerId); }
  };
  canvas.onpointermove = (ev) => {
    if (drag) {
      const px = ev.clientX - canvas.getBoundingClientRect().left;
      if (Math.abs(px - drag.start) > 4) drag.moved = true;
      if (drag.moved) { g.save(); drawOverlay(g, Math.min(drag.start, px), Math.abs(px - drag.start), cssH, canvas, drag); g.restore(); }
      hideTip();
      return;
    }
    const { best } = nearest(ev);
    canvas.style.cursor = best ? "pointer" : "crosshair";
    if (!best) { hideTip(); return; }
    const e = best.lead;
    showTip(ev, `${e.syscall} ${shorten(e.target || e.detail, 70)}`,
      `+${fmtMs((e.ts_ns - base0) / 1e6)} · pid ${e.pid} · ${e.type}${best.events.length > 1 ? ` · ${best.events.length} events here` : ""}`);
  };
  canvas.onpointerleave = hideTip;
  canvas.onpointerup = (ev) => {
    if (!drag) return;
    const px = ev.clientX - canvas.getBoundingClientRect().left;
    if (drag.moved && Math.abs(px - drag.start) > 8) {
      const toMs = (x) => v0 + (Math.max(LABEL, Math.min(x, cssW - RIGHT)) - LABEL) / (cssW - LABEL - RIGHT) * (v1 - v0);
      t.view = [toMs(Math.min(drag.start, px)), toMs(Math.max(drag.start, px))];
      t.page = 0;
      drag = null;
      renderTimelineBody();
      return;
    }
    drag = null;
    const { best } = nearest(ev);
    if (best) inspectEvent(best.lead.id);
  };
  canvas.ondblclick = () => { t.view = null; t.page = 0; renderTimelineBody(); };
}
function drawOverlay(g, x, w, height, canvas, drag) {
  if (!drag.snapshot) drag.snapshot = g.getImageData(0, 0, canvas.width, canvas.height);
  g.putImageData(drag.snapshot, 0, 0);
  g.fillStyle = css("--wash");
  g.fillRect(x, 0, w, height);
}

/* ---------- process tree ---------- */

function renderProcesses(view) {
  const { analysis: a } = state.data;
  const noise = new Set(a.graph.nodes.filter((n) => n.type === "process" && n.noise).map((n) => n.pid));
  const procs = new Map(a.processes.map((p) => [p.pid, p]));
  const roots = a.processes.filter((p) => p.parent === null);
  const total = Math.max(a.summary.duration_ms, ...a.processes.map((p) => p.last_ms), 0.001);
  const rows = [];
  const walk = (p, depth) => {
    rows.push([p, depth]);
    p.children.map((c) => procs.get(c)).filter(Boolean).sort((x, y) => x.first_ms - y.first_ms).forEach((c) => walk(c, depth + 1));
  };
  roots.sort((x, y) => x.first_ms - y.first_ms).forEach((r) => walk(r, 0));

  const list = h("ul", { cls: "tree" }, rows.map(([p, depth]) => {
    const quiet = noise.has(p.pid);
    const left = p.first_ms / total * 100;
    const width = Math.max((p.last_ms - p.first_ms) / total * 100, .3);
    const failedExit = p.exit_code !== null && p.exit_code !== 0;
    return h("li", null, h("button", { cls: `tree-row${quiet ? " quiet" : ""}`, onclick: () => inspectProcess(p) },
      h("span", { cls: "tree-name" },
        Array.from({ length: depth }, () => h("span", { cls: "tree-indent", style: "width:16px" })),
        h("span", { cls: "exe" }, base(p.exe) || "process"), h("span", { cls: "pid" }, p.pid),
        failedExit ? h("span", { cls: "chip warn" }, `exit ${p.exit_code}`) : null),
      h("span", { cls: "tree-span", title: `${fmtMs(p.first_ms)} to ${fmtMs(p.last_ms)}` }, h("i", { style: `left:${left}%;width:${width}%` })),
      h("span", { cls: "tree-counts" },
        ["process", "file", "network"].filter((k) => p.counts[k]).map((k) => h("span", { title: `${p.counts[k]} ${k} events` }, h("i", { cls: `key ${k}` }), fmtNum(p.counts[k]))))));
  }));
  const quietCount = rows.filter(([p]) => noise.has(p.pid)).length;
  view.append(card("Execution chain", `${a.processes.length} processes. Bars show when each ran over the ${fmtMs(total)} trace.${quietCount ? ` ${quietCount} in lighter text had no effect on files or the network.` : ""}`,
    h("div", { cls: "table-wrap" }, list)));
}

function inspectProcess(p) {
  const d = state.data;
  const parent = p.parent !== null ? d.procByPid.get(p.parent) : null;
  const key = `p:${p.pid}`;
  const rels = d.analysis.graph.edges.filter((e) => e.src === key && e.kind !== "spawned").sort((x, y) => x.ms - y.ms);
  openInspector(`${base(p.exe) || "process"} (pid ${p.pid})`,
    h("dl", { cls: "kv" },
      h("dt", null, "Program"), h("dd", null, p.exe || "unknown"),
      h("dt", null, "Parent"), h("dd", null, parent ? `${base(parent.exe)} (pid ${parent.pid})` : `outside the trace (pid ${p.ppid})`),
      p.spawn_event ? [h("dt", null, "Started by"), h("dd", null, eventLink(p.spawn_event))] : null,
      parent ? [h("dt", null, "Link confidence"), h("dd", null, meter(p.parent_confidence))] : null,
      h("dt", null, "UID"), h("dd", null, p.uid),
      h("dt", null, "Ran"), h("dd", null, `+${fmtMs(p.first_ms)} to +${fmtMs(p.last_ms)}`),
      h("dt", null, "Exit code"), h("dd", null, p.exit_code === null ? "not recorded" : p.exit_code),
      h("dt", null, "Events"), h("dd", null, fmtNum(p.event_count))),
    p.exec_chain.length ? [h("p", { cls: "section-title" }, "Programs executed"), p.exec_chain.map((x) => h("p", null, eventLink(x.event, x.path)))] : null,
    h("div", { cls: "actions" }, h("button", { onclick: () => { state.timeline.pid = String(p.pid); state.timeline.signal = false; setTab("timeline"); } }, "Show in timeline")),
    rels.length ? [h("p", { cls: "section-title" }, `What it did (${rels.length})`), rels.map((r) => h("div", { cls: "rel" },
      h("button", { cls: "link", onclick: () => inspectRelations([r], r.summary) }, r.summary), h("div", { cls: "rel-meta" }, meter(r.confidence, r.tier))))] : null);
}

/* ---------- network ---------- */

function renderNetwork(view) {
  const { analysis: a, doc } = state.data;
  if (!a.collected.network) {
    view.append(notice("warn", `Configuration ${doc.config} did not collect network events`, "Network activity is unknown for this run, not absent. Re-run under configuration C."));
    return;
  }
  const all = a.connections;
  const shown = state.network.probes ? all : all.filter((c) => !c.probe);
  const distinct = shown.filter((c) => !(c.direction === "inbound" && c.peer_pid));
  const probes = all.filter((c) => c.probe).length;
  const out = shown.filter((c) => c.direction === "outbound");
  const endpoints = new Set(out.map((c) => c.endpoint));
  const bytes = distinct.reduce((t, c) => t + c.bytes_sent + c.bytes_received, 0);
  const noSource = doc.schema_version < 3;
  view.append(h("div", { cls: "tiles" },
    h("div", { cls: "tile" }, h("div", { cls: "tile-label" }, "Connections"), h("div", { cls: "tile-value" }, distinct.length)),
    h("div", { cls: "tile" }, h("div", { cls: "tile-label" }, "Endpoints contacted"), h("div", { cls: "tile-value" }, endpoints.size)),
    h("div", { cls: "tile" }, h("div", { cls: "tile-label" }, "Data moved"), h("div", { cls: "tile-value" }, fmtBytes(bytes)))));
  if (noSource) view.append(notice("info", "Source address and protocol were not recorded", "This is schema 2 evidence, written before the engine resolved sockets. Destination, process and bytes are still known."));
  if (!shown.length) {
    view.append(card(null, null, h("p", { cls: "unknown" }, "No connections were recorded in this run.")));
  } else {
    if (out.length) view.append(card("Who talked to whom", "Line weight follows bytes moved", renderFlow(out)));
  }
  const fmtEnd = (host, port) => (host ? `${host}:${port}` : "not recorded");
  const paired = shown.length - distinct.length;
  const eventsNote = [paired ? `${paired} connection${paired > 1 ? "s were" : " was"} seen from both ends, so appear${paired > 1 ? "" : "s"} twice` : null,
    probes ? `${probes} resolver and route probes are set aside: they moved no data` : null].filter(Boolean).join(". ");
  view.append(card("Connection events", eventsNote || null,
    probes ? h("div", { cls: "filters" }, h("label", null, h("input", { type: "checkbox", checked: state.network.probes, onchange: (e) => { state.network.probes = e.target.checked; renderView(); } }), "Show probes")) : null,
    h("div", { cls: "table-wrap" }, h("table", null,
      h("thead", null, h("tr", null, h("th", { cls: "num" }, "Time"), h("th", null, "Process"), h("th", null, "Direction"), h("th", null, "Source"), h("th", null, "Destination"), h("th", null, "Protocol"), h("th", null, "State"), h("th", { cls: "num" }, "Sent"), h("th", { cls: "num" }, "Received"), h("th", { cls: "num" }, "Event"))),
      h("tbody", null, shown.map((c) => h("tr", { cls: "clickable", onclick: () => inspectEvent(c.event) },
        h("td", { cls: "num" }, `+${fmtMs(c.ms)}`), h("td", null, `${base(c.exe)} ${c.pid}`), h("td", null, c.direction),
        h("td", { cls: "mono" }, fmtEnd(c.src_host, c.src_port)), h("td", { cls: "mono" }, c.dst_host ? fmtEnd(c.dst_host, c.dst_port) : c.endpoint),
        h("td", null, c.proto === "unknown" ? "not recorded" : c.proto.toUpperCase()), h("td", { cls: c.state === "failed" ? "failed" : null }, c.state, c.probe ? " (probe)" : ""),
        h("td", { cls: "num" }, fmtBytes(c.bytes_sent)), h("td", { cls: "num" }, fmtBytes(c.bytes_received)), h("td", { cls: "num" }, `#${c.event}`))))))));
  if (a.unix_connections.length) {
    const distinct = [...new Set(a.unix_connections.map((u) => u.target))];
    view.append(card("Local socket attempts", "Inter-process connections on this machine, not network traffic",
      h("p", { cls: "mono", style: "overflow-wrap:anywhere" }, distinct.join(", "))));
  }
}

function renderFlow(conns) {
  const pids = [...new Set(conns.map((c) => c.pid))];
  const ends = [...new Set(conns.map((c) => c.endpoint))];
  const ROW = 50, W = 640, BOX = 186;
  const height = Math.max(pids.length, ends.length) * ROW + 12;
  const yP = (i) => 6 + (height - 12 - pids.length * ROW) / 2 + i * ROW + ROW / 2;
  const yE = (i) => 6 + (height - 12 - ends.length * ROW) / 2 + i * ROW + ROW / 2;
  const max = Math.max(1, ...conns.map((c) => c.bytes_sent + c.bytes_received));
  const svg = s("svg", { width: W, height, viewBox: `0 0 ${W} ${height}`, role: "img", "aria-label": "Processes and the endpoints they connected to; the table below has the same data" });
  for (const c of conns) {
    const y1 = yP(pids.indexOf(c.pid)), y2 = yE(ends.indexOf(c.endpoint));
    const bytes = c.bytes_sent + c.bytes_received;
    const failed = c.state === "failed";
    svg.append(s("path", { d: `M${BOX} ${y1} C${BOX + 90} ${y1} ${W - BOX - 90} ${y2} ${W - BOX} ${y2}`, fill: "none",
      stroke: failed ? css("--critical") : css("--network"), "stroke-width": 1.5 + 4 * Math.sqrt(bytes / max),
      "stroke-dasharray": failed ? "5 4" : null, opacity: .85 }));
  }
  pids.forEach((pid, i) => {
    const y = yP(i);
    const p = state.data.procByPid.get(pid);
    svg.append(s("rect", { x: 1, y: y - 19, width: BOX - 2, height: 38, rx: 7, fill: css("--surface"), stroke: css("--process"), "stroke-width": 1.5 }),
      s("text", { x: 11, y: y - 2 }, shorten(base(p && p.exe), 22)), s("text", { cls: "sub", x: 11, y: y + 12 }, `pid ${pid}`));
  });
  ends.forEach((end, i) => {
    const y = yE(i);
    const c = conns.find((x) => x.endpoint === end);
    svg.append(s("rect", { x: W - BOX + 1, y: y - 19, width: BOX - 2, height: 38, rx: 19, fill: css("--surface"), stroke: css("--network"), "stroke-width": 1.5 }),
      s("text", { x: W - BOX + 15, y: y - 2 }, shorten(end, 22)), s("text", { cls: "sub", x: W - BOX + 15, y: y + 12 }, `${c.proto !== "unknown" ? `${c.proto.toUpperCase()}, ` : ""}${c.scope}`));
  });
  return h("div", { cls: "flow-wrap" }, svg);
}

/* ---------- files ---------- */

const FILE_FILTERS = {
  changed: ["Changed", (f) => f.relevant && ["created", "overwritten", "wrote", "deleted", "chmod", "opened_for_write"].some((k) => f.ops[k])],
  created: ["Created", (f) => f.ops.created],
  modified: ["Modified", (f) => f.ops.wrote || f.ops.overwritten || f.ops.chmod],
  deleted: ["Deleted", (f) => f.ops.deleted],
  denied: ["Denied", (f) => f.ops.read_denied || f.ops.write_denied],
  read: ["Read", (f) => f.relevant && (f.ops.read || f.ops.opened)],
  all: ["Everything", () => true],
};
const OP_LABEL = { created: "created", overwritten: "overwritten", wrote: "written", read: "read", opened: "opened", opened_for_write: "opened for write", deleted: "deleted", chmod: "mode changed", executed: "executed", read_denied: "read denied", write_denied: "write denied" };

function renderFiles(view) {
  const { analysis: a, doc } = state.data;
  if (!a.collected.file) {
    view.append(notice("warn", `Configuration ${doc.config} did not collect file events`, "File activity is unknown for this run, not absent. Re-run under configuration B or C."));
    return;
  }
  const st = state.files;
  const q = st.q.trim().toLowerCase();
  const pass = FILE_FILTERS[st.filter][1];
  const rows = a.files.filter((f) => pass(f) && (!q || f.path.toLowerCase().includes(q)));
  const counts = Object.fromEntries(Object.entries(FILE_FILTERS).map(([k, [, fn]]) => [k, a.files.filter(fn).length]));
  view.append(h("div", { cls: "filters" },
    h("div", { cls: "seg", role: "group", "aria-label": "File activity" }, Object.entries(FILE_FILTERS).map(([k, [label]]) => h("button", { "aria-pressed": String(st.filter === k), onclick: () => { st.filter = k; renderView(); } }, `${label} ${counts[k]}`))),
    h("input", { type: "search", placeholder: "Search paths", value: st.q, "aria-label": "Search paths", oninput: (e) => { st.q = e.target.value; clearTimeout(st.timer); st.timer = setTimeout(() => { renderView(); const i = document.querySelector('input[aria-label="Search paths"]'); if (i) { i.focus(); i.setSelectionRange(i.value.length, i.value.length); } }, 220); } })));
  view.append(card(`${rows.length} files`, null, rows.length ? h("div", { cls: "table-wrap" }, h("table", null,
    h("thead", null, h("tr", null, h("th", null, "File"), h("th", null, "Kind"), h("th", null, "What happened"), h("th", null, "Processes"), h("th", { cls: "num" }, "Written"), h("th", { cls: "num" }, "First seen"))),
    h("tbody", null, rows.slice(0, 500).map((f) => h("tr", { cls: "clickable", tabindex: 0, onclick: () => inspectFile(f), onkeydown: (ev) => { if (ev.key === "Enter") inspectFile(f); } },
      h("td", { cls: "path" }, f.path), h("td", null, h("span", { cls: "chip" }, f.category)),
      h("td", null, Object.entries(f.ops).map(([k, n]) => [h("span", { cls: `chip${k.endsWith("denied") ? " warn" : ""}` }, OP_LABEL[k] || k, n > 1 ? h("b", null, n) : null), " "])),
      h("td", null, f.processes.slice(0, 3).map((p) => base((state.data.procByPid.get(p) || {}).exe) || p).join(", "), f.processes.length > 3 ? ` +${f.processes.length - 3}` : ""),
      h("td", { cls: "num" }, f.bytes_written ? fmtBytes(f.bytes_written) : ""), h("td", { cls: "num" }, `+${fmtMs(f.first_ms)}`)))))) : h("p", { cls: "unknown" }, "No files match this filter."),
  rows.length > 500 ? h("p", { cls: "hint" }, `First 500 of ${rows.length} shown. Search to narrow the list.`) : null));
}

function inspectFile(f) {
  openInspector(f.path, h("div", { cls: "rel-meta" }, h("span", { cls: "chip" }, f.category), f.temp ? h("span", { cls: "chip" }, "temporary directory") : null),
    h("dl", { cls: "kv" }, h("dt", null, "Bytes written"), h("dd", null, fmtBytes(f.bytes_written)), h("dt", null, "Bytes read"), h("dd", null, fmtBytes(f.bytes_read))),
    h("p", { cls: "section-title" }, "History"),
    h("div", { cls: "table-wrap" }, h("table", null, h("tbody", null, f.timeline.map((t) => h("tr", { cls: "clickable", onclick: () => inspectEvent(t.event) },
      h("td", { cls: "num" }, `+${fmtMs(t.ms)}`), h("td", null, OP_LABEL[t.op] || t.op, t.bytes ? ` ${fmtBytes(t.bytes)}` : ""), h("td", null, `${base(t.exe) || "process"} ${t.pid}`), h("td", { cls: "num" }, `#${t.event}`)))))));
}

/* ---------- configuration comparison ---------- */

async function renderCompare(view) {
  const st = state.compare;
  const holder = h("div");
  const selects = h("div", { cls: "filters" },
    h("div", { cls: "seg", role: "group", "aria-label": "Collection mode" }, ["ptrace", "seccomp"].map((m) => h("button", { "aria-pressed": String(st.mode === m), onclick: () => { st.mode = m; renderView(); } }, m))),
    h("select", { "aria-label": "Scenario", onchange: (e) => { st.scenario = e.target.value; renderView(); } },
      h("option", { value: "ALL", selected: st.scenario === "ALL" }, "All four study scenarios"),
      ["scenario01", "scenario02", "scenario03", "scenario04"].map((k) => h("option", { value: k, selected: st.scenario === k }, `${k}: ${state.session.scenarios[k] || ""}`))));
  view.append(selects, holder);
  let data;
  try {
    data = await api.get(`/api/compare?mode=${st.mode}&scenario=${st.scenario}`);
  } catch (err) {
    holder.append(notice("bad", "Experiment results could not be read", err.message));
    return;
  }
  const smallest = data.configs.find((c) => c.sufficient);
  const current = state.data && state.data.doc.config;
  holder.append(card(null, null,
    h("p", { cls: "verdict" }, smallest ? `Configuration ${smallest.config} (${smallest.label.toLowerCase()}) is the smallest that meets every quality threshold here.` : "No configuration meets every quality threshold here."),
    h("p", { cls: "hint" }, `A configuration passes only if its worst run meets every threshold. Figures are means of ${data.configs[0].runs} stored study runs per configuration, in the baseline format without the custody chain.`)));
  const fmtVal = (v) => (v >= 100 ? fmtNum(Math.round(v)) : v >= 10 ? v.toFixed(1) : v.toFixed(2));
  const mini = (metric, thr) => {
    const W = 230, H = 138, B = 22, T = 18;
    const vals = data.configs.map((c) => c.metrics[metric.key].mean);
    const max = Math.max(...vals, thr || 0) || 1;
    const Y = (v) => H - B - (v / max) * (H - B - T);
    const bw = 34, gap = (W - 4 * bw) / 5;
    const svg = s("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": `${metric.label}: ${data.configs.map((c) => `${c.config} ${fmtVal(c.metrics[metric.key].mean)}${metric.unit}`).join(", ")}` });
    if (thr) svg.append(s("line", { cls: "thr", x1: 0, x2: W, y1: Y(thr), y2: Y(thr) }));
    data.configs.forEach((c, i) => {
      const v = c.metrics[metric.key].mean;
      const x = gap + i * (bw + gap);
      const y = Y(Math.max(v, 0));
      const barH = Math.max(H - B - y, 1);
      const m = c.metrics[metric.key];
      svg.append(s("rect", { cls: "bar", x, y, width: bw, height: barH, rx: 3, tabindex: 0,
        onpointermove: (ev) => showTip(ev, `${fmtVal(v)}${metric.unit ? ` ${metric.unit}` : ""}`, `Config ${c.config}: ${c.label}. Range ${fmtVal(m.min)} to ${fmtVal(m.max)}${thr ? `. Threshold ${thr}` : ""}`), onpointerleave: hideTip }),
      thr ? s("line", { cls: "worst", x1: x - 3, x2: x + bw + 3, y1: Y(m.min), y2: Y(m.min) }) : null,
      s("text", { cls: "val", x: x + bw / 2, y: y - 5, "text-anchor": "middle" }, fmtVal(v)),
      s("text", { cls: c.config === current ? "current" : null, x: x + bw / 2, y: H - 6, "text-anchor": "middle" }, c.config));
    });
    svg.append(s("line", { cls: "base", x1: 0, x2: W, y1: H - B, y2: H - B }));
    return h("div", { cls: "mini" }, h("h3", null, metric.label, metric.unit ? ` (${metric.unit})` : ""), thr ? h("p", { cls: "hint" }, `Threshold ${thr}`) : h("p", { cls: "hint" }, "Lower is cheaper"), svg);
  };
  holder.append(card("Evidence quality", "Bar is the mean, the short line across it is the worst run, the dashed line is the threshold", h("div", { cls: "small-multiples" }, data.quality.map((m) => mini(m, m.threshold)))));
  holder.append(card("Cost", null, h("div", { cls: "small-multiples" }, data.cost.map((m) => mini(m)))));
  const metrics = [...data.quality, ...data.cost];
  holder.append(card("The same figures as a table", current ? `This case used configuration ${current}.` : null,
    h("div", { cls: "table-wrap" }, h("table", null,
      h("thead", null, h("tr", null, h("th", null, "Measure"), data.configs.map((c) => h("th", { cls: "num" }, `${c.config}${c.config === current ? " (this case)" : ""}`)))),
      h("tbody", null, metrics.map((m) => h("tr", null, h("td", null, m.label, m.unit ? ` (${m.unit})` : ""), data.configs.map((c) => h("td", { cls: "num" }, fmtVal(c.metrics[m.key].mean), m.threshold ? ` (worst ${fmtVal(c.metrics[m.key].min)})` : "")))),
        h("tr", null, h("td", null, h("b", null, "Meets all thresholds")), data.configs.map((c) => h("td", { cls: "num" }, h("span", { cls: `status ${c.sufficient ? "good" : "none"}` }, h("i", { "aria-hidden": "true" }, c.sufficient ? "✓" : "–"), c.sufficient ? "Yes" : "No")))))))));
}

/* ---------- chain of custody ---------- */

function renderCustody(view) {
  const c = state.custody;
  if (state.loadError) view.append(notice("bad", "The evidence file could not be read", state.loadError));
  if (!c) { view.append(h("p", { cls: "hint" }, h("span", { cls: "spinner" }), "Running verification")); return; }
  if (c.error) { view.append(notice("bad", "Verification could not run", c.error)); return; }
  const v = c.verification;
  const id = state.caseId;
  const banners = {
    verified_signed_pinned: ["good", "Evidence is intact and signed by the trusted key", "Every record, the chain, the manifest, the signature and the audit log all check out."],
    verified_signed_unpinned: ["warn", "Evidence is intact, but the signer is not proven", "The signature matches the key stored in the manifest. Anyone can re-sign with their own key, so pin a trusted public key with --pubkey to prove who signed."],
    verified_unsigned: ["warn", "Evidence is consistent, but not signed", "Accidental change and partial tampering would show. Someone able to rewrite every file could still go unnoticed. Create a key with make keys."],
    legacy_sidecar_ok: ["info", "Schema 2 evidence: sidecar hash only", "This file was written in the baseline format used by the study, so it has no hash chain, session, signature or audit log."],
    failed: ["bad", "Evidence failed verification", `${v.issue_total} problem(s) found. Treat this evidence as modified until the cause is explained.`],
  };
  const [kind, title, text] = banners[v.status];
  view.append(notice(kind, title, text));

  const stateIcon = { ok: ["good", "✓", "Pass"], fail: ["bad", "✕", "Fail"], warn: ["warn", "!", "Warn"], skip: ["none", "–", "Skip"] };
  const checks = card("Verification", `${fmtNum(v.records_checked)} records recomputed by the engine`,
    h("ul", { cls: "checks" }, v.checks.map((k) => {
      const [cls, icon, label] = stateIcon[k.state];
      return h("li", null, h("span", { cls: `status ${cls}` }, h("i", { "aria-hidden": "true" }, icon), label), h("span", { cls: "name" }, k.name.replace(/_/g, " ")), h("span", { cls: "text" }, k.text));
    })));

  const issues = v.issues.length ? card("Problems found", `${v.issue_total} in total${v.issue_total > v.issues.length ? `, first ${v.issues.length} listed` : ""}`,
    h("div", { cls: "table-wrap" }, h("table", null,
      h("thead", null, h("tr", null, h("th", null, "Kind"), h("th", null, "Record"), h("th", null, "What was found"))),
      h("tbody", null, v.issues.map((i) => h("tr", null,
        h("td", null, h("span", { cls: "chip warn" }, i.kind.replace(/_/g, " "))),
        h("td", null, i.first_event ? (i.first_event === i.last_event ? (state.data && state.data.eventById.has(i.first_event) ? eventLink(i.first_event) : `#${i.first_event}`) : `#${i.first_event} to #${i.last_event}`) : "file level"),
        h("td", { cls: "path" }, i.text))))))) : null;

  const d = state.data && state.data.doc;
  const cust = d && d.custody;
  const man = c.manifest;
  const session = (cust || man) ? card("Session", null, h("dl", { cls: "kv" },
    [["Case", (cust || man).case_id], ["Investigator", (cust || man).investigator], ["OS user", (cust || man).os_user], ["Host", (cust || man).hostname], ["Kernel", (cust || man).kernel],
      ["Session ID", (cust || man).session_id], ["Started", fmtUtc((cust || man).started_utc)], ["Finished", fmtUtc((cust || man).finished_utc)]]
      .map(([k, val]) => [h("dt", null, k), h("dd", null, val)]),
    man ? [h("dt", null, "Manifest"), h("dd", null, man.signature ? `Ed25519, key ${man.signature.key_fingerprint.slice(0, 16)}...` : "unsigned")] : null,
    v.pinned_key ? [h("dt", null, "Pinned key"), h("dd", null, h("code", null, base(v.pinned_key)))] : null),
  h("p", { cls: "section-title" }, "File SHA-256"), h("p", { cls: "hash" }, v.evidence_sha256),
  cust ? [h("p", { cls: "section-title" }, "Chain head"), h("p", { cls: "hash" }, cust.chain_head)] : null) : null;

  const who = () => state.session.user || "";
  const result = h("p", { cls: "hint", style: "margin-top:8px" });
  const actions = c.writable ? h("div", { cls: "actions" },
    h("button", { cls: "primary", onclick: async (e) => {
      e.target.disabled = true;
      try { await api.post("/api/verify", { id, investigator: who() }); result.textContent = "Verified, and the check was added to the audit log."; await loadCustody(id); } catch (err) { result.textContent = err.message; }
      e.target.disabled = false;
    } }, "Verify and log"),
    v.status !== "legacy_sidecar_ok" ? h("button", { onclick: async (e) => {
      e.target.disabled = true;
      try { const r = await api.post("/api/export", { id, investigator: who() }); result.textContent = `Exported ${r.files.length} files to ${r.directory}${r.verified ? "" : " (the failed verification is recorded in the bundle)"}.`; await loadCustody(id); } catch (err) { result.textContent = err.message; }
      e.target.disabled = false;
    } }, "Export evidence bundle") : null,
    state.data && state.data.has_report ? h("a", { href: `/api/report?id=${encodeURIComponent(id)}`, download: "" }, h("button", null, "Engine report (Markdown)")) : null)
    : h("p", { cls: "hint", style: "margin-top:8px" }, "This is read-only reference data, so verifying here adds nothing to its audit log.");

  const auditCard = c.audit.length ? card("Audit log", "Hash-chained record of who did what to this evidence",
    h("div", { cls: "table-wrap" }, h("table", null,
      h("thead", null, h("tr", null, h("th", { cls: "num" }, "#"), h("th", null, "When"), h("th", null, "Action"), h("th", null, "By"), h("th", null, "Outcome"), h("th", null, "Detail"))),
      h("tbody", null, c.audit.map((a) => h("tr", null, h("td", { cls: "num" }, a.seq), h("td", null, fmtUtc(a.ts_utc)), h("td", null, a.action), h("td", null, a.investigator), h("td", { cls: a.outcome === "failed" ? "failed" : null }, (a.outcome || "").replace(/_/g, " ")), h("td", { cls: "path" }, a.detail))))))) : null;

  view.append(h("div", { cls: "grid-2" },
    h("div", { cls: "stack" }, checks, issues, auditCard),
    h("div", { cls: "stack" }, session, card("Actions", null, actions, result),
      card("Check it yourself", "No need to trust this dashboard: the signature checks with stock OpenSSL",
        h("pre", { cls: "cmd" }, `forensictrace verify <evidence.json> --pubkey <key.pub>\n\nopenssl pkeyutl -verify -pubin -inkey <key.pub> -rawin \\\n  -in <evidence.json>.manifest.json \\\n  -sigfile <evidence.json>.manifest.sig`)))));
}

/* ---------- new investigation ---------- */

function openInvestigate() {
  const dlg = $("investigate-dialog");
  const scenarios = state.session.scenarios;
  const err = h("p", { cls: "form-error", role: "alert", hidden: true });
  const scenario = h("select", null, Object.entries(scenarios).reverse().map(([k, v]) => h("option", { value: k }, `${k}: ${v}`)));
  const config = h("select", null, Object.entries(state.session.config_names).map(([k, v]) => h("option", { value: k, selected: k === "C" }, `${k}: ${v}`)));
  const mode = h("select", null, h("option", { value: "ptrace" }, "ptrace"), h("option", { value: "seccomp" }, "seccomp (lower overhead)"));
  const caseId = h("input", { type: "text", value: `CASE-${new Date().toISOString().slice(0, 10).replace(/-/g, "")}`, required: true });
  const who = h("input", { type: "text", value: state.session.user || "", required: true });
  const run = h("button", { cls: "primary" }, "Run investigation");
  const status = h("span", { cls: "hint" });
  run.addEventListener("click", async () => {
    err.hidden = true;
    run.disabled = true;
    status.replaceChildren(h("span", { cls: "spinner" }), "Tracing the scenario");
    try {
      const r = await api.post("/api/investigate", { scenario: scenario.value, config: config.value, mode: mode.value, case_id: caseId.value.trim(), investigator: who.value.trim() });
      await loadCases();
      dlg.close();
      state.tab = "overview";
      openCase(r.id);
    } catch (e) {
      err.textContent = e.message;
      err.hidden = false;
      status.replaceChildren();
    }
    run.disabled = false;
  });
  dlg.replaceChildren();
  fill(dlg, null, [
    h("h2", { style: "margin-bottom:12px" }, "New investigation"),
    h("label", { cls: "form-row" }, h("span", null, "Incident scenario"), scenario),
    h("div", { cls: "form-pair" },
      h("label", { cls: "form-row" }, h("span", null, "Evidence configuration"), config),
      h("label", { cls: "form-row" }, h("span", null, "Collection mode"), mode)),
    h("div", { cls: "form-pair" },
      h("label", { cls: "form-row" }, h("span", null, "Case ID"), caseId),
      h("label", { cls: "form-row" }, h("span", null, "Investigator"), who)),
    state.session.signing ? null : notice("warn", "This evidence will not be signed", `Create a key first: run make keys, then restart the dashboard.`),
    err,
    h("p", { cls: "hint", style: "margin-bottom:12px" }, "To trace your own command, run the engine with --output cases/name.json. It appears in the case list."),
    h("div", { cls: "actions", style: "justify-content:flex-end;align-items:center" }, status,
      h("button", { onclick: () => dlg.close() }, "Cancel"), run)]);
  dlg.showModal();
}

/* ---------- render ---------- */

async function downloadCaseReport(kind, button, message) {
  button.disabled = true;
  message.replaceChildren(h("span", { cls: "spinner" }), "Preparing the PDF, this takes a few seconds");
  try {
    const r = await fetch(`/api/case-report?id=${encodeURIComponent(state.caseId)}&kind=${kind}&format=pdf`);
    if (!r.ok) {
      const body = await r.json().catch(() => ({}));
      throw new Error(body.error || `HTTP ${r.status}`);
    }
    const disposition = r.headers.get("Content-Disposition") || "";
    const name = (disposition.match(/filename="([^"]+)"/) || [])[1] || `${kind}_report.pdf`;
    const url = URL.createObjectURL(await r.blob());
    const link = h("a", { href: url, download: name });
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 10000);
    message.replaceChildren(`Downloaded ${name}`);
  } catch (err) {
    message.replaceChildren(err.message);
  }
  button.disabled = false;
}

async function renderReports(view) {
  if (state.caseId) {
    const reportCard = (kind, title, audience, summary) => {
      const message = h("p", { cls: "hint", style: "margin-top:8px", role: "status" });
      const button = h("button", { cls: "primary" }, "Download PDF");
      button.addEventListener("click", () => downloadCaseReport(kind, button, message));
      return h("section", { cls: `card ${kind}` }, h("h2", null, title), h("p", { cls: "card-sub" }, audience), h("p", null, summary),
        h("div", { cls: "actions" }, button,
          h("a", { href: `/api/case-report?id=${encodeURIComponent(state.caseId)}&kind=${kind}&format=html`, target: "_blank", rel: "noopener" },
            h("button", { tabindex: -1 }, "Open in browser"))),
        message);
    };
    view.append(h("p", { cls: "card-sub", style: "margin:0 0 14px" }, "Reports for the case selected above, built from its evidence."),
      h("div", { cls: "report-cards" },
        reportCard("technical", "Technical report", "For investigators and assessors",
          "Case details, findings, the reconstructed sequence with its evidence and confidence, processes, network, files and chain of custody."),
        reportCard("general", "Plain-language report", "For anyone, no technical background needed",
          "What happened in everyday words, how serious it is, what was affected and whether the record can be trusted.")));
  } else {
    view.append(card("No case selected", null, h("p", null, "Open or run an investigation to get its reports.")));
  }

}

function renderView() {
  const view = $("view");
  view.replaceChildren();
  if (state.tab === "reports") { renderReports(view); return; }
  if (!state.caseId) {
    view.append(card("No evidence yet", null, h("p", null, "Select New investigation to trace a scenario, or run the engine with --output cases/name.json.")));
    return;
  }
  if (state.tab === "compare") { renderCompare(view); return; }
  if (state.tab === "custody") { renderCustody(view); return; }
  if (!state.data) {
    if (state.loadError) { state.tab = "custody"; renderNav(); renderCustody(view); }
    return;
  }
  ({ overview: renderOverview, graph: renderGraph, timeline: renderTimeline, processes: renderProcesses, network: renderNetwork, files: renderFiles })[state.tab](view);
}

async function main() {
  $("new-investigation").addEventListener("click", openInvestigate);
  $("case-select").addEventListener("change", (e) => openCase(e.target.value));
  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { if (state.tab === "timeline" && state.data) renderTimelineBody(); }, 200);
  });
  try {
    state.session = await api.get("/api/session");
    api.token = state.session.token;
    if (state.session.read_only) {
      $("new-investigation").hidden = true;
      $("main").insertBefore(notice("info", "Read-only demo",
        "This online copy shows recorded evidence only. To run new investigations, run ForensicTrace on a Linux machine."), $("case-header"));
    }
    const wanted = readHash();
    await loadCases();
    renderNav();
    renderHeader();
    const first = state.cases.find((c) => c.id === wanted) || state.cases.find((c) => c.group === "Investigations") || state.cases.find((c) => c.group === "Examples" && c.schema === "3") || state.cases[0];
    if (first) await openCase(first.id);
    else renderView();
  } catch (err) {
    $("view").replaceChildren(notice("bad", "The dashboard could not start", err.message));
  }
}
main();

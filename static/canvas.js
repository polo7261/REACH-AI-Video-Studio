// 無限畫布：節點（卡片）＋ 連線（流水線），類 n8n 工作流
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const W = 320, H = 200, GAP = 120;
  const svg = (body, size = 16, fill = "none") => `<svg class="ico" width="${size}" height="${size}" viewBox="0 0 24 24" fill="${fill}" stroke="${fill === "none" ? "currentColor" : "none"}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
  const IC = {
    text: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    image: '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="m21 16-5-5-9 8"/>',
    video: '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/>',
    audio: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    plus: '<path d="M12 5v14M5 12h14"/>', x: '<path d="M6 6l12 12M18 6 6 18"/>',
    play: '<path d="M8 5.5v13l11-6.5z"/>', layers: '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    spark: '<path d="M12 3.5 13.8 9l5.7 1.5-5.7 1.6L12 17.5l-1.8-5.4-5.7-1.6L10.2 9z"/>',
    sliders: '<path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/>',
    chev: '<path d="m6 9 6 6 6-6"/>', ratio: '<rect x="3" y="7" width="18" height="10" rx="2"/>',
  };
  const KIND = {
    text: { name: "文字", step: "script", modelKind: "text" },
    image: { name: "圖片", step: "keyframe", modelKind: "image" },
    video: { name: "影片", step: "video", modelKind: "video" },
    audio: { name: "配音", step: "tts", modelKind: "tts" },
  };
  const MODES = {
    video: [["t2v", "文生影片"], ["i2v", "首幀生成影片"], ["flf", "首尾幀生成影片", true]],
    image: [["t2i", "文生圖"], ["i2i", "參考圖生圖"]],
  };
  const RATIOS = ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"];
  const VOICES = ["male-qn-qingse", "female-shaonv", "female-yujie", "male-qn-jingying"];
  const DEFAULT_PARAMS = { video: { ratio: "16:9", duration: 5, resolution: "768P" }, image: { ratio: "16:9" }, audio: { voice: "male-qn-qingse" }, text: {} };

  const state = { pid: null, cfg: null, canvas: null, sel: null, selEdge: null, polls: new Set(), saveTimer: null };
  const cv = $("#cv"), world = $("#cv-world"), nodesEl = $("#cv-nodes"), edgesEl = $("#cv-edges");
  const panel = $("#cv-panel"), pop = $("#cv-pop");

  function toast(msg, isErr = false) {
    const el = document.createElement("div");
    el.className = "toast" + (isErr ? " err" : ""); el.textContent = msg;
    document.body.appendChild(el); setTimeout(() => el.remove(), isErr ? 7000 : 3000);
  }
  async function api(path, opt = {}) {
    const res = await fetch(path, { headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, ...opt });
    let body = null; try { body = await res.json(); } catch { body = null; }
    if (!res.ok) { const e = new Error((body && body.error) || `HTTP ${res.status}`); e.body = body; throw e; }
    return body;
  }
  const node = (id) => state.canvas.nodes.find((n) => n.id === id);
  const vp = () => state.canvas.viewport;

  // ---------------------------------------------------------------- 儲存
  function setSave(t) { $("#cv-save").textContent = t; }
  function save(now = false) {
    clearTimeout(state.saveTimer);
    setSave("未儲存…");
    const run = async () => {
      try {
        const res = await api(`/api/projects/${state.pid}/canvas`, { method: "PUT", body: JSON.stringify(state.canvas) });
        mergeServer(res.canvas); setSave("已儲存");
      } catch (err) { setSave("儲存失敗"); toast(err.message, true); }
    };
    if (now) return run();
    state.saveTimer = setTimeout(run, 600);
    return null;
  }
  // 伺服器回來的 output/status 為準，版面保留本地
  function mergeServer(serverCanvas) {
    const map = Object.fromEntries(serverCanvas.nodes.map((n) => [n.id, n]));
    state.canvas.nodes.forEach((n) => {
      const s = map[n.id]; if (!s) return;
      const changed = JSON.stringify([n.output, n.status, n.message]) !== JSON.stringify([s.output, s.status, s.message]);
      Object.assign(n, { output: s.output, status: s.status, message: s.message, job_id: s.job_id });
      if (changed) renderNode(n);
    });
  }

  // ---------------------------------------------------------------- 視圖
  function applyView() {
    const v = vp();
    world.style.transform = `translate(${v.x}px, ${v.y}px) scale(${v.k})`;
    cv.style.backgroundPosition = `${v.x}px ${v.y}px`;
    cv.style.backgroundSize = `${20 * v.k}px ${20 * v.k}px`;
    $("#cv-zoom").textContent = `${Math.round(v.k * 100)}%`;
  }
  function toWorld(cx, cy) {
    const r = cv.getBoundingClientRect(), v = vp();
    return { x: (cx - r.left - v.x) / v.k, y: (cy - r.top - v.y) / v.k };
  }
  function fit() {
    const ns = state.canvas.nodes; if (!ns.length) return;
    const r = cv.getBoundingClientRect();
    const minX = Math.min(...ns.map((n) => n.x)), maxX = Math.max(...ns.map((n) => n.x + W));
    const minY = Math.min(...ns.map((n) => n.y)), maxY = Math.max(...ns.map((n) => n.y + H));
    const k = Math.max(0.3, Math.min(1.2, Math.min((r.width - 160) / (maxX - minX), (r.height - 340) / (maxY - minY))));
    Object.assign(vp(), { k, x: r.width / 2 - ((minX + maxX) / 2) * k, y: (r.height - 200) / 2 - ((minY + maxY) / 2) * k });
    applyView(); save();
  }

  // ---------------------------------------------------------------- 渲染
  function preview(n) {
    const o = n.output;
    if (n.status === "running") return `<div class="cv-empty"><span class="cv-spin"></span><span class="muted">生成中…</span></div>`;
    if (o && o.type === "video") return `<video src="${esc(o.url)}" controls muted loop preload="metadata"></video>`;
    if (o && o.type === "image") return `<img src="${esc(o.url)}" alt="">`;
    if (o && o.type === "audio") return `<div class="cv-empty">${svg(IC.audio, 34)}<audio src="${esc(o.url)}" controls preload="none"></audio></div>`;
    if (o && o.type === "text") return `<div class="cv-text">${esc(o.text)}</div>`;
    const tries = {
      video: [["i2v", IC.layers, "首幀生成影片"], ["text", IC.spark, "文字生成影片"]],
      image: [["text", IC.spark, "由文字生成圖片"]],
      text: [], audio: [["text", IC.spark, "由文字生成配音"]],
    }[n.kind];
    return `<div class="cv-empty">
      <span class="cv-big">${svg(n.kind === "video" ? IC.play : IC[n.kind], 40, n.kind === "video" ? "currentColor" : "none")}</span>
      ${tries.length ? `<div class="cv-try"><span class="muted">嘗試：</span>${tries.map(([k, ic, label]) => `<button type="button" data-try="${k}">${svg(ic, 14)} ${label}</button>`).join("")}</div>`
        : '<span class="muted cv-tip">點選卡片，在下方輸入提示詞</span>'}
    </div>`;
  }
  function renderNode(n) {
    let el = nodesEl.querySelector(`[data-id="${n.id}"]`);
    if (!el) {
      el = document.createElement("div");
      el.className = "cv-node"; el.dataset.id = n.id;
      nodesEl.appendChild(el);
    }
    el.style.transform = `translate(${n.x}px, ${n.y}px)`;
    el.classList.toggle("sel", state.sel === n.id);
    el.classList.toggle("err", n.status === "error");
    el.innerHTML = `
      <div class="cv-label">${svg(IC[n.kind], 13)}<span>${esc(n.title)}</span>
        ${n.status === "done" ? '<span class="chip ok">完成</span>' : n.status === "error" ? '<span class="chip err">失敗</span>' : ""}
        <button class="cv-del" type="button" data-del title="刪除節點">${svg(IC.x, 13)}</button></div>
      <div class="cv-card">${preview(n)}${n.status === "error" && n.message ? `<div class="cv-msg">${esc(n.message)}</div>` : ""}</div>
      <button class="cv-port in" type="button" data-port="in" title="新增上游節點">${svg(IC.plus, 15)}</button>
      <button class="cv-port out" type="button" data-port="out" title="新增下游節點／拖曳連線">${svg(IC.plus, 15)}</button>`;
  }
  function edgePath(a, b) {
    const x1 = a.x + W, y1 = a.y + H / 2 + 22, x2 = b.x, y2 = b.y + H / 2 + 22;
    const dx = Math.max(60, Math.abs(x2 - x1) / 2);
    return `M${x1},${y1} C${x1 + dx},${y1} ${x2 - dx},${y2} ${x2},${y2}`;
  }
  function renderEdges(temp) {
    edgesEl.innerHTML = state.canvas.edges.map((e, i) => {
      const a = node(e.from), b = node(e.to); if (!a || !b) return "";
      const live = a.status === "running" || b.status === "running";
      return `<path class="cv-edge-hit" data-edge="${i}" d="${edgePath(a, b)}"/>
        <path class="cv-edge ${live ? "live" : ""} ${state.selEdge === i ? "sel" : ""}" d="${edgePath(a, b)}"/>`;
    }).join("") + (temp ? `<path class="cv-edge temp" d="${temp}"/>` : "");
  }
  function renderAll() {
    nodesEl.innerHTML = "";
    state.canvas.nodes.forEach(renderNode);
    renderEdges(); applyView(); renderPanel();
  }

  // ---------------------------------------------------------------- 節點操作
  function nextId() { return "N" + (Math.max(0, ...state.canvas.nodes.map((n) => +n.id.slice(1))) + 1); }
  function addNode(kind, x, y) {
    const id = nextId();
    const count = state.canvas.nodes.filter((n) => n.kind === kind).length + 1;
    const n = { id, kind, title: `${KIND[kind].name}節點 ${count}`, x, y, prompt: "", model: "",
      mode: (MODES[kind] || [[""]])[0][0], params: { ...DEFAULT_PARAMS[kind] }, output: null, status: "idle" };
    state.canvas.nodes.push(n); renderNode(n); return n;
  }
  function connect(from, to) {
    if (from === to || state.canvas.edges.some((e) => e.from === from && e.to === to)) return;
    state.canvas.edges.push({ from, to }); renderEdges();
  }
  function freeY(x, y) { // 避免疊在一起
    while (state.canvas.nodes.some((n) => Math.abs(n.x - x) < W && Math.abs(n.y - y) < H + 40)) y += H + 70;
    return y;
  }
  function addBeside(baseId, side, kind) {
    const b = node(baseId);
    const x = side === "out" ? b.x + W + GAP : b.x - W - GAP;
    const n = addNode(kind, x, freeY(x, b.y));
    side === "out" ? connect(b.id, n.id) : connect(n.id, b.id);
    select(n.id); save(); return n;
  }
  function removeNode(id) {
    state.canvas.nodes = state.canvas.nodes.filter((n) => n.id !== id);
    state.canvas.edges = state.canvas.edges.filter((e) => e.from !== id && e.to !== id);
    nodesEl.querySelector(`[data-id="${id}"]`)?.remove();
    if (state.sel === id) state.sel = null;
    renderEdges(); renderPanel(); save();
  }
  function select(id) {
    state.sel = id; state.selEdge = null;
    nodesEl.querySelectorAll(".cv-node").forEach((el) => el.classList.toggle("sel", el.dataset.id === id));
    renderEdges(); renderPanel();
  }

  // ---------------------------------------------------------------- 彈出選單
  function openPop(anchor, html, onClick) {
    pop.innerHTML = html; pop.hidden = false;
    const r = anchor.getBoundingClientRect(), c = cv.getBoundingClientRect();
    const pw = pop.offsetWidth, ph = pop.offsetHeight;
    let left = r.left - c.left, top = r.bottom - c.top + 6;
    if (top + ph > c.height - 8) top = r.top - c.top - ph - 6;
    left = Math.max(8, Math.min(left, c.width - pw - 8));
    pop.style.left = `${left}px`; pop.style.top = `${Math.max(8, top)}px`;
    pop.onclick = (e) => { const b = e.target.closest("[data-v]"); if (b && !b.disabled) onClick(b.dataset.v, b); };
  }
  const closePop = () => { pop.hidden = true; pop.onclick = null; };
  const kindMenu = (title) => `<div class="pop-title">${title}</div>` + Object.entries(KIND).map(([k, v]) =>
    `<button type="button" data-v="${k}">${svg(IC[k], 16)}<span>${v.name}節點</span></button>`).join("");

  // ---------------------------------------------------------------- 底部面板
  function modelsFor(kind) {
    const mk = KIND[kind].modelKind;
    return state.cfg.providers.flatMap((p) => p.models.filter((m) => m.kind === mk && m.status !== "license")
      .map((m) => ({ v: `${p.id}|${m.id}`, id: m.id, p, m })));
  }
  function currentModel(n) {
    if (n.model) return n.model;
    const r = state.cfg.routing[KIND[n.kind].step]; return `${r.provider}|${r.model}`;
  }
  function upstream(n) { return state.canvas.edges.filter((e) => e.to === n.id).map((e) => node(e.from)).filter(Boolean); }
  function paramSummary(n) {
    const p = n.params || {};
    if (n.kind === "video") return `${p.ratio || "16:9"} · ${p.resolution || "768P"} · ${p.duration || 5}s`;
    if (n.kind === "image") return p.ratio || "16:9";
    if (n.kind === "audio") return p.voice || VOICES[0];
    return "";
  }
  function renderPanel() {
    const n = state.sel && node(state.sel);
    if (!n || !state.cfg) { panel.hidden = true; return; }
    panel.hidden = false;
    const mv = currentModel(n), mi = modelsFor(n.kind).find((x) => x.v === mv);
    const modes = MODES[n.kind];
    const ups = upstream(n);
    panel.innerHTML = `
      <div class="cvp-top">
        <span class="muted">${svg(IC[n.kind], 14)} ${esc(n.title)}</span>
        ${ups.length ? `<span class="cvp-ups">上游：${ups.map((u) => `<span class="chip">${esc(u.title)}${u.output ? " ✓" : ""}</span>`).join(" ")}</span>` : '<span class="muted" style="font-size:11.5px">未連接上游</span>'}
      </div>
      <textarea id="cvp-prompt" rows="3" placeholder="${n.kind === "text" ? "描述要產生的劇本、分鏡或提示詞…" : "描述你想要生成的畫面；上游文字節點的內容會自動帶入"}">${esc(n.prompt)}</textarea>
      <div class="cvp-bar">
        <button type="button" class="cvp-btn" id="cvp-model">${svg(IC[n.kind], 14)}<span>${esc(mi ? mi.id : mv.split("|")[1])}</span>${svg(IC.chev, 12)}</button>
        ${modes ? `<button type="button" class="cvp-btn" id="cvp-mode">${esc((modes.find((m) => m[0] === n.mode) || modes[0])[1])}${svg(IC.chev, 12)}</button>` : ""}
        ${n.kind !== "text" ? `<button type="button" class="cvp-btn" id="cvp-params">${svg(n.kind === "audio" ? IC.audio : IC.ratio, 14)}<span>${esc(paramSummary(n))}</span>${svg(IC.chev, 12)}</button>` : ""}
        <span style="flex:1"></span>
        <button type="button" class="cvp-go" id="cvp-run" ${n.status === "running" ? "disabled" : ""}>${svg(IC.play, 13, "currentColor")} ${n.status === "running" ? "生成中…" : "生成"}</button>
      </div>`;
    $("#cvp-prompt").addEventListener("input", (e) => { n.prompt = e.target.value; save(); });
    $("#cvp-run").addEventListener("click", () => runNode(n.id).catch(() => {}));
    $("#cvp-model").addEventListener("click", (e) => {
      e.stopPropagation();
      const list = modelsFor(n.kind);
      const html = `<div class="pop-title">${KIND[n.kind].name}模型</div>` + ["cloud", "local"].map((scope) => {
        const items = list.filter((x) => x.p.scope === scope); if (!items.length) return "";
        return `<div class="pop-group">${scope === "cloud" ? "雲端" : "地端"}</div>` + items.map((x) => `
          <button type="button" data-v="${esc(x.v)}" class="${x.v === mv ? "on" : ""}">${svg(IC[n.kind], 15)}
            <span class="pm-name">${esc(x.id)}<small>${esc(x.p.name)}</small></span>
            <em class="chip ${x.m.status === "ok" ? "ok" : x.m.status === "quota" ? "warn" : ""}">${x.m.status === "ok" ? "已實測" : x.m.status === "quota" ? "額度" : "未實測"}</em></button>`).join("");
      }).join("");
      openPop(e.currentTarget, html, (v) => { n.model = v; closePop(); renderPanel(); save(); });
    });
    $("#cvp-mode")?.addEventListener("click", (e) => {
      e.stopPropagation();
      const html = `<div class="pop-title">${n.kind === "video" ? "影片生成模式" : "圖片生成模式"}</div>` + modes.map(([v, label, off]) =>
        `<button type="button" data-v="${v}" class="${v === n.mode ? "on" : ""}" ${off ? "disabled" : ""}>${label}${off ? '<em class="muted">即將支援</em>' : ""}</button>`).join("");
      openPop(e.currentTarget, html, (v) => { n.mode = v; closePop(); renderPanel(); save(); });
    });
    $("#cvp-params")?.addEventListener("click", (e) => { e.stopPropagation(); openParams(e.currentTarget, n); });
  }
  function openParams(anchor, n) {
    const p = n.params || (n.params = {});
    let html = "";
    if (n.kind === "video" || n.kind === "image") {
      html += `<div class="pop-title">比例</div><div class="ratio-grid">${RATIOS.map((r) => {
        const [a, b] = r.split(":").map(Number), w = a >= b ? 18 : Math.round(18 * a / b), h = a >= b ? Math.round(18 * b / a) : 18;
        return `<button type="button" data-v="ratio:${r}" class="${(p.ratio || "16:9") === r ? "on" : ""}"><i style="width:${w}px;height:${h}px"></i>${r}</button>`;
      }).join("")}</div>`;
    }
    if (n.kind === "video") {
      html += `<div class="pop-title">時長 <span class="muted" id="dur-v">${p.duration || 5}s</span></div>
        <input type="range" min="4" max="10" step="1" value="${p.duration || 5}" id="dur-r" class="range">
        <div class="pop-title">解析度</div><div class="seg">${["768P", "1080P"].map((r) => `<button type="button" data-v="res:${r}" class="${(p.resolution || "768P") === r ? "on" : ""}">${r}</button>`).join("")}</div>`;
    }
    if (n.kind === "audio") {
      html += `<div class="pop-title">聲音</div>` + VOICES.map((v) => `<button type="button" data-v="voice:${v}" class="${(p.voice || VOICES[0]) === v ? "on" : ""}">${v}</button>`).join("");
    }
    openPop(anchor, `<div class="pop-params">${html}</div>`, (v) => {
      const [k, val] = v.split(/:(.+)/);
      if (k === "ratio") p.ratio = val; if (k === "res") p.resolution = val; if (k === "voice") p.voice = val;
      save(); openParams(anchor, n); renderPanelBarOnly(n);
    });
    $("#dur-r")?.addEventListener("input", (e) => { p.duration = +e.target.value; $("#dur-v").textContent = `${p.duration}s`; renderPanelBarOnly(n); save(); });
  }
  function renderPanelBarOnly(n) { const s = $("#cvp-params span"); if (s) s.textContent = paramSummary(n); }

  // ---------------------------------------------------------------- 執行
  async function runNode(id) {
    const n = node(id);
    await save(true);
    n.status = "running"; n.message = null; renderNode(n); renderEdges(); if (state.sel === id) renderPanel();
    try {
      const res = await api(`/api/projects/${state.pid}/canvas/run`, { method: "POST", body: JSON.stringify({ node_id: id }) });
      Object.assign(n, res.node); renderNode(n); renderEdges(); if (state.sel === id) renderPanel();
      if (res.job) { toast(`影片任務已送出（${res.job.model}）`); await pollJob(res.job.id, id); }
      else toast(`${n.title} 完成`);
    } catch (err) {
      Object.assign(n, err.body && err.body.node ? err.body.node : { status: "error", message: err.message });
      renderNode(n); renderEdges(); if (state.sel === id) renderPanel();
      toast(err.message, true); throw err;
    }
  }
  async function pollJob(jid, nid) {
    if (state.polls.has(jid)) return; state.polls.add(jid);
    try {
      for (let i = 0; i < 180; i++) {
        await new Promise((r) => setTimeout(r, 5000));
        let job; try { ({ job } = await api(`/api/jobs/${jid}`)); } catch { continue; }
        if (job.state === "succeeded" || job.state === "error" || job.state === "failed") {
          const { canvas } = await api(`/api/projects/${state.pid}/canvas`);
          mergeServer(canvas); renderEdges(); if (state.sel === nid) renderPanel();
          if (job.state !== "succeeded") throw new Error(job.message || "影片生成失敗");
          toast(`${node(nid)?.title || nid} 影片完成`); return;
        }
      }
      throw new Error("影片生成逾時");
    } finally { state.polls.delete(jid); }
  }
  async function runAll() {
    const ns = state.canvas.nodes, indeg = Object.fromEntries(ns.map((n) => [n.id, 0]));
    state.canvas.edges.forEach((e) => { indeg[e.to]++; });
    const queue = ns.filter((n) => !indeg[n.id]).map((n) => n.id), order = [];
    while (queue.length) {
      const id = queue.shift(); order.push(id);
      state.canvas.edges.filter((e) => e.from === id).forEach((e) => { if (--indeg[e.to] === 0) queue.push(e.to); });
    }
    if (order.length !== ns.length) { toast("流程有循環連線，無法依序執行", true); return; }
    const btn = $("#cv-run-all"); btn.disabled = true;
    try {
      for (const id of order) {
        const n = node(id);
        if (!n.prompt.trim() && !upstream(n).length) continue; // 空節點略過
        await runNode(id);
      }
      toast("流程執行完成");
    } catch { toast("流程中斷：請查看標示失敗的節點", true); }
    finally { btn.disabled = false; }
  }

  // ---------------------------------------------------------------- 互動
  let drag = null;
  cv.addEventListener("pointerdown", (e) => {
    if (e.button !== 0 || e.target.closest(".cv-panel, .cv-pop, .cv-bar, .cv-dock, .cv-foot-left, video, audio, textarea")) return;
    closePop();
    const el = e.target.closest(".cv-node");
    const port = e.target.closest("[data-port]");
    if (el && e.target.closest("[data-del], [data-try]")) return;
    if (el && port) {
      drag = { type: "port", id: el.dataset.id, side: port.dataset.port, sx: e.clientX, sy: e.clientY, moved: false, anchor: port };
    } else if (el) {
      const n = node(el.dataset.id);
      drag = { type: "node", id: n.id, sx: e.clientX, sy: e.clientY, ox: n.x, oy: n.y, moved: false };
      if (state.sel !== n.id) select(n.id);
    } else {
      const edgeHit = e.target.closest("[data-edge]");
      if (edgeHit) { state.selEdge = +edgeHit.dataset.edge; state.sel = null; renderEdges(); renderPanel();
        nodesEl.querySelectorAll(".cv-node.sel").forEach((x) => x.classList.remove("sel")); return; }
      drag = { type: "pan", sx: e.clientX, sy: e.clientY, ox: vp().x, oy: vp().y, moved: false };
      cv.classList.add("panning");
    }
    cv.setPointerCapture(e.pointerId);
  });
  cv.addEventListener("pointermove", (e) => {
    if (!drag) return;
    const dx = e.clientX - drag.sx, dy = e.clientY - drag.sy;
    if (Math.abs(dx) + Math.abs(dy) > 3) drag.moved = true;
    if (!drag.moved) return;
    if (drag.type === "pan") { vp().x = drag.ox + dx; vp().y = drag.oy + dy; applyView(); }
    else if (drag.type === "node") {
      const n = node(drag.id); n.x = drag.ox + dx / vp().k; n.y = drag.oy + dy / vp().k;
      nodesEl.querySelector(`[data-id="${n.id}"]`).style.transform = `translate(${n.x}px, ${n.y}px)`; renderEdges();
    } else if (drag.type === "port") {
      const n = node(drag.id), p = toWorld(e.clientX, e.clientY);
      const sx = drag.side === "out" ? n.x + W : n.x, sy = n.y + H / 2 + 22;
      renderEdges(drag.side === "out" ? `M${sx},${sy} C${sx + 80},${sy} ${p.x - 80},${p.y} ${p.x},${p.y}` : `M${p.x},${p.y} C${p.x + 80},${p.y} ${sx - 80},${sy} ${sx},${sy}`);
    }
  });
  cv.addEventListener("pointerup", (e) => {
    if (!drag) return;
    const d = drag; drag = null; cv.classList.remove("panning");
    if (d.type === "pan" && !d.moved) { state.sel = null; state.selEdge = null; nodesEl.querySelectorAll(".cv-node.sel").forEach((x) => x.classList.remove("sel")); renderEdges(); renderPanel(); }
    if (d.type === "pan" && d.moved) save();
    if (d.type === "node" && d.moved) save();
    if (d.type === "port") {
      if (d.moved) {
        const target = document.elementsFromPoint(e.clientX, e.clientY).map((x) => x.closest && x.closest(".cv-node")).find(Boolean);
        if (target && target.dataset.id !== d.id) { d.side === "out" ? connect(d.id, target.dataset.id) : connect(target.dataset.id, d.id); save(); }
        renderEdges();
      } else {
        openPop(d.anchor, kindMenu(d.side === "out" ? "新增下游節點" : "新增上游節點"), (k) => { closePop(); addBeside(d.id, d.side, k); });
      }
    }
  });
  nodesEl.addEventListener("click", (e) => {
    const el = e.target.closest(".cv-node"); if (!el) return;
    if (e.target.closest("[data-del]")) { removeNode(el.dataset.id); return; }
    const t = e.target.closest("[data-try]");
    if (t) {
      const n = node(el.dataset.id);
      if (t.dataset.try === "i2v") { n.mode = "i2v"; addBeside(n.id, "in", "image"); }
      else addBeside(n.id, "in", "text");
    }
  });
  cv.addEventListener("wheel", (e) => {
    if (e.target.closest(".cv-panel, .cv-pop, .cv-text")) return;
    e.preventDefault();
    const v = vp();
    if (e.ctrlKey || e.metaKey) {
      const r = cv.getBoundingClientRect(), mx = e.clientX - r.left, my = e.clientY - r.top;
      const k = Math.max(0.2, Math.min(2.5, v.k * Math.exp(-e.deltaY * 0.01)));
      v.x = mx - (mx - v.x) * (k / v.k); v.y = my - (my - v.y) * (k / v.k); v.k = k;
    } else { v.x -= e.deltaX; v.y -= e.deltaY; }
    applyView(); save();
  }, { passive: false });
  document.addEventListener("keydown", (e) => {
    if (e.target.closest("textarea, input, select")) return;
    if (e.key === "Delete" || e.key === "Backspace") {
      if (state.sel) { removeNode(state.sel); e.preventDefault(); }
      else if (state.selEdge !== null) { state.canvas.edges.splice(state.selEdge, 1); state.selEdge = null; renderEdges(); save(); e.preventDefault(); }
    }
    if (e.key === "Escape") closePop();
  });
  document.addEventListener("pointerdown", (e) => { if (!pop.hidden && !e.target.closest(".cv-pop, .cvp-btn, [data-port]")) closePop(); });
  $("#cv-fit").addEventListener("click", fit);
  $("#cv-run-all").addEventListener("click", runAll);
  $("#cv-add").addEventListener("click", (e) => {
    e.stopPropagation();
    openPop(e.currentTarget, kindMenu("新增節點"), (k) => {
      closePop();
      const r = cv.getBoundingClientRect(), c = toWorld(r.left + r.width / 2, r.top + r.height / 2 - 100);
      const x = c.x - W / 2; const n = addNode(k, x, freeY(x, c.y - H / 2)); select(n.id); save();
    });
  });
  $("#cv-project").addEventListener("change", (e) => { location.href = `/canvas?pid=${encodeURIComponent(e.target.value)}`; });

  // ---------------------------------------------------------------- 啟動
  async function boot() {
    const [cfg, list] = await Promise.all([api("/api/config"), api("/api/projects")]);
    state.cfg = cfg;
    let projects = list.projects || [];
    let pid = new URLSearchParams(location.search).get("pid");
    if (!projects.length) {
      const res = await api("/api/projects", { method: "POST", body: JSON.stringify({ idea: "未命名畫布", title: "未命名畫布" }) });
      projects = [{ id: res.plan.id, title: res.plan.title }];
    }
    if (!pid || !projects.some((p) => p.id === pid)) pid = projects[0].id;
    state.pid = pid;
    history.replaceState(null, "", `/canvas?pid=${pid}`);
    $("#cv-project").innerHTML = projects.map((p) => `<option value="${esc(p.id)}" ${p.id === pid ? "selected" : ""}>${esc(p.title)}</option>`).join("");
    const { canvas } = await api(`/api/projects/${pid}/canvas`);
    state.canvas = canvas;
    const fresh = canvas.viewport.x === 0 && canvas.viewport.y === 0;
    renderAll(); setSave("已載入");
    if (fresh) fit();
    canvas.nodes.filter((n) => n.status === "running" && n.job_id).forEach((n) => pollJob(n.job_id, n.id).catch(() => {}));
  }
  boot().catch((err) => toast(err.message, true));
})();

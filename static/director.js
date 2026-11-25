// AI 導演：對話式創作（原創／改編／執導），結果可一鍵送到畫布
(() => {
  const $ = (s) => document.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const svg = (b, s = 16) => `<svg class="ico" width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">${b}</svg>`;
  const IC = {
    text: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    image: '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="m21 16-5-5-9 8"/>',
    video: '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/>',
    audio: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    mountain: '<path d="m3 19 6-9 4 5 3-4 5 8z"/><circle cx="17" cy="6" r="2"/>', edit: '<path d="M4 20h4L19 9l-4-4L4 16z"/>',
    sword: '<path d="M14.5 4H20v5.5L9 20.5 3.5 15z"/><path d="m6 13 5 5"/>', city: '<path d="M4 20V9l5-3v14M9 20V4h6v16M15 20v-9l5 2v7"/>',
    fan: '<path d="M12 20 4 9a11 11 0 0 1 16 0z"/><path d="M12 20 9 7M12 20l3-13"/>', eye: '<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    rocket: '<path d="M5 15c-1 2-1 4-1 4s2 0 4-1M9 15l-3-3c2-6 7-9 12-9 0 5-3 10-9 12z"/><circle cx="14" cy="10" r="1.6"/>',
    smile: '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5a4.5 4.5 0 0 0 7 0M9 9.5h.01M15 9.5h.01"/>',
    users: '<circle cx="9" cy="8" r="3"/><path d="M3 20c.6-3 3-5 6-5s5.4 2 6 5M16 5a3 3 0 0 1 0 6M18 15c1.6.6 2.7 2.4 3 5"/>',
    face: '<circle cx="12" cy="12" r="9"/><path d="M9 10h.01M15 10h.01M9.5 15h5"/>', clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    hook: '<path d="M12 3v11a4 4 0 1 1-8 0"/><circle cx="12" cy="3" r="1"/>', film: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 4v16M17 4v16M3 9h4M3 15h4M17 9h4M17 15h4"/>',
  };
  const GENRES = [
    ["文旅非遺", "mountain", ["#b77b4a", "#e2b07a"]], ["玄幻修仙", "sword", ["#4a6ab7", "#9ab4ea"]],
    ["都市現實", "city", ["#4a5563", "#a3adb9"]], ["古裝言情", "fan", ["#b74a6a", "#eaa3b7"]],
    ["懸疑驚悚", "eye", ["#3d3f55", "#8c8fb3"]], ["科幻未來", "rocket", ["#2f8a96", "#8fd8e0"]],
    ["喜劇日常", "smile", ["#c49a2a", "#f0d48a"]], ["其他（自訂）", "edit", ["#666", "#aaa"]],
  ];
  const HOT = [
    ["玄幻修仙逆襲", "玄幻修仙", "逆襲"], ["職場成長現實", "都市現實", "熱血成長"], ["末日生存基建", "科幻未來", "求生基建"],
    ["國潮非遺奇幻", "文旅非遺", "視覺奇觀"], ["古風甜寵", "古裝言情", "甜寵"], ["規則怪談懸疑", "懸疑驚悚", "懸疑反轉"],
    ["重生復仇爽劇", "都市現實", "復仇爽點"], ["家庭溫情喜劇", "喜劇日常", "療癒"],
  ];
  const OPTS = [
    ["audience", "目標受眾", "users", ["自動", "全年齡", "女性向", "男性向", "青少年"]],
    ["character", "角色設定", "face", ["自動", "單一主角", "雙主角", "群像"]],
    ["era", "時代背景", "clock", ["自動", "古代", "民國", "現代", "近未來", "架空"]],
    ["hook", "核心看點", "hook", ["自動", "逆襲", "甜寵", "懸疑反轉", "熱血成長", "療癒", "復仇爽點", "求生基建", "視覺奇觀"]],
    ["style", "畫風", "image", ["自動", "電影寫實", "日系動畫", "國風水墨", "3D 動畫", "賽博龐克"]],
    ["episodes", "劇本結構", "film", ["1 集短片", "10 集", "20 集", "40 集", "60 集"]],
  ];
  const MODE_NAME = { original: "劇本原創", adapt: "劇本改編", direct: "導演執導" };

  const st = { pid: null, cfg: null, mode: "original", model: "", attach: null, settings: { skill: "", skill_name: "", models: {}, gen_mode: "manual" }, messages: [], canvas: null, busy: false,
    preset: { genre: "玄幻修仙", fuse: null, custom: "", audience: "自動", character: "自動", era: "自動", hook: "自動", style: "自動", episodes: "20 集" } };

  function toast(msg, isErr = false) {
    const el = document.createElement("div"); el.className = "toast" + (isErr ? " err" : ""); el.textContent = msg;
    document.body.appendChild(el); setTimeout(() => el.remove(), isErr ? 7000 : 3000);
  }
  async function api(path, opt = {}) {
    const res = await fetch(path, { headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, ...opt });
    let body = null; try { body = await res.json(); } catch { body = null; }
    if (!res.ok) throw new Error((body && body.error) || `HTTP ${res.status}`);
    return body;
  }

  // ---------------------------------------------------------------- 簡易 Markdown
  function md(src) {
    const blocks = String(src).split(/```/);
    return blocks.map((b, i) => {
      if (i % 2) { const body = b.replace(/^[a-z]*\n/i, ""); return `<pre><code>${esc(body)}</code></pre>`; }
      const lines = esc(b).split("\n"); let html = "", list = null;
      const inline = (s) => s.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/`([^`]+)`/g, "<code>$1</code>");
      for (const ln of lines) {
        const m = ln.match(/^(#{1,4})\s+(.*)/), li = ln.match(/^\s*(?:[-*]|\d+[.)])\s+(.*)/);
        if (li) { if (!list) { html += "<ul>"; list = true; } html += `<li>${inline(li[1])}</li>`; continue; }
        if (list) { html += "</ul>"; list = null; }
        if (m) html += `<h${Math.min(4, m[1].length + 2)}>${inline(m[2])}</h${Math.min(4, m[1].length + 2)}>`;
        else if (/^\s*\|.*\|\s*$/.test(ln)) html += `<div class="mono md-row">${inline(ln)}</div>`;
        else if (ln.trim()) html += `<p>${inline(ln)}</p>`;
      }
      if (list) html += "</ul>";
      return html;
    }).join("");
  }
  function extractShots(text) {
    const m = String(text).match(/```json\s*([\s\S]*?)```/i);
    if (m) { try { const d = JSON.parse(m[1]); if (Array.isArray(d.shots) && d.shots.length) return d.shots.slice(0, 12); } catch { /* 改用 Markdown 解析 */ } }
    return extractMdShots(text);
  }
  // 解析「分鏡 N：標題 (00s - 10s)」＋ 畫面描述／運鏡與光線／圖片 Prompt／Negative Prompt
  function extractMdShots(text) {
    const clean = String(text).replace(/\r/g, "");
    const re = /^[#>\s*-]*\**\s*分鏡\s*(\d+)\s*[：:]\s*(.*)$/gm;
    const heads = [...clean.matchAll(re)];
    if (heads.length < 2) return null;
    const field = (sec, label) => {
      const r = new RegExp(`${label}[^：:\\n]*[：:]\\**\\s*([\\s\\S]*?)(?=\\n\\s*[*-]?\\s*\\**\\s*(?:畫面描述|運鏡與光線|運鏡|配樂情緒|配樂|圖片\\s*Prompt|Negative\\s*Prompt|負面)|$)`, "i");
      const x = sec.match(r);
      return x ? x[1].replace(/^\s*>\s?/gm, "").replace(/\*\*/g, "").replace(/\s+/g, " ").trim() : "";
    };
    const shots = heads.map((h, i) => {
      const sec = clean.slice(h.index + h[0].length, i + 1 < heads.length ? heads[i + 1].index : undefined);
      const rawTitle = h[2].replace(/\*\*/g, "").trim();
      const t = rawTitle.match(/\((\d+)\s*s?\s*[-–~]\s*(\d+)\s*s\)/i);
      const img = field(sec, "圖片\\s*Prompt"), desc = field(sec, "畫面描述");
      return {
        title: rawTitle.replace(/\s*\(.*?\)\s*$/, "") || `分鏡 ${h[1]}`,
        prompt: img || desc, hasImg: !!img,
        negative: field(sec, "(?:Negative\\s*Prompt|負面)"),
        motion: field(sec, "運鏡"),
        seconds: t ? Math.max(1, +t[2] - +t[1]) : 5,
      };
    }).filter((x) => x.prompt);
    const full = shots.some((x) => x.hasImg) ? shots.filter((x) => x.hasImg) : shots;  // 有圖片 Prompt 時略過被截斷的分鏡
    return full.length ? full.slice(0, 12) : null;
  }

  // ---------------------------------------------------------------- 渲染
  function renderMessages() {
    $("#dr-welcome").hidden = st.messages.length > 0;
    $("#dr-msgs").innerHTML = st.messages.map((m, i) => m.role === "user"
      ? `<div class="dr-msg user"><div class="dr-bubble">${esc(m.display || m.content).replace(/\n/g, "<br>")}</div>
          <span class="dr-meta">${esc(MODE_NAME[m.mode] || "")}</span></div>`
      : `<div class="dr-msg ai"><div class="dr-ai-dot"></div><div class="dr-body">
          <div class="md">${md(m.content)}</div>
          <div class="dr-actions">
            <span class="dr-meta">${esc(MODE_NAME[m.mode] || "")} · ${esc(m.model || "")}</span>
            <button class="ghost small" data-copy="${i}">複製</button>
            <button class="ghost small" data-tonode="${i}">送到畫布（文字節點）</button>
            ${extractShots(m.content) ? `<button class="small" data-shots="${i}">建立 ${extractShots(m.content).length} 鏡分鏡到畫布</button>` : ""}
          </div></div></div>`).join("") + (st.busy ? '<div class="dr-msg ai"><div class="dr-ai-dot"></div><div class="dr-body"><span class="cv-spin"></span> <span class="muted">導演思考中…</span></div></div>' : "");
    const sc = $("#dr-scroll"); sc.scrollTop = sc.scrollHeight;
  }
  function renderAssets() {
    const nodes = (st.canvas && st.canvas.nodes) || [];
    $("#dr-asset-count").textContent = nodes.length ? `${nodes.length}` : "";
    $("#dr-assets").innerHTML = nodes.length ? nodes.map((n) => {
      const o = n.output || {};
      const thumb = o.type === "image" ? `<img src="${esc(o.url)}" alt="">` : o.type === "video" ? `<video src="${esc(o.url)}" muted preload="metadata"></video>` : svg(IC[n.kind] || IC.text, 22);
      return `<a class="dr-asset" href="/canvas?pid=${encodeURIComponent(st.pid)}" title="在畫布開啟"><span class="dr-thumb">${thumb}</span><span>${esc(n.title)}</span></a>`;
    }).join("") : '<div class="muted" style="font-size:12px">畫布還沒有節點。</div>';
  }
  function renderModel() {
    const list = modelList();
    const cur = st.model || (st.cfg ? `${st.cfg.routing.script.provider}|${st.cfg.routing.script.model}` : "");
    const hit = list.find((x) => x.v === cur);
    $("#dr-model").innerHTML = `${svg(IC.text, 14)}<span>${esc(hit ? hit.id : cur.split("|")[1] || "模型")}</span>`;
  }
  function renderMode() { document.querySelectorAll("#dr-modes button").forEach((b) => b.classList.toggle("on", b.dataset.mode === st.mode)); }
  function renderSets() {
    const s = st.settings, el = $("#dr-sets"), chips = [];
    if (s.skill) chips.push(["skill", "Skill", s.skill_name || s.skill]);
    if (s.models.image) chips.push(["image", "圖片", s.models.image.split("|")[1]]);
    if (s.models.video) chips.push(["video", "影片", s.models.video.split("|")[1]]);
    if (s.skill || s.models.image || s.models.video || s.gen_mode === "auto") chips.push(["mode", "模式", s.gen_mode === "auto" ? "自動生成" : "手動生成"]);
    el.hidden = !chips.length;
    el.innerHTML = chips.map(([k, l, v]) => `<span class="dr-set"><i>${l}</i>${esc(v)}<button type="button" data-k="${k}" title="${k === "mode" ? "切換" : "移除"}">${k === "mode" ? "⇄" : "✕"}</button></span>`).join("");
    el.querySelectorAll("button").forEach((b) => b.onclick = () => {
      const k = b.dataset.k;
      if (k === "skill") { s.skill = ""; s.skill_name = ""; }
      else if (k === "mode") s.gen_mode = s.gen_mode === "auto" ? "manual" : "auto";
      else delete s.models[k];
      renderSets();
    });
  }
  function renderAttach() {
    const a = $("#dr-attach");
    if (!st.attach) { a.hidden = true; return; }
    a.hidden = false;
    a.innerHTML = `${svg(IC.text, 14)} <span>${esc(st.attach.name)}（${st.attach.text.length} 字）</span><button type="button" class="cv-del" style="opacity:1" id="dr-attach-x">✕</button>`;
    $("#dr-attach-x").onclick = () => { st.attach = null; renderAttach(); };
  }
  const modelList = () => !st.cfg ? [] : st.cfg.providers.flatMap((p) => p.models.filter((m) => m.kind === "text" && m.status !== "license").map((m) => ({ v: `${p.id}|${m.id}`, id: m.id, p, m })));

  // ---------------------------------------------------------------- 彈出選單
  const pop = $("#dr-pop");
  function openPop(anchor, html, onPick) {
    pop.innerHTML = html; pop.hidden = false;
    const r = anchor.getBoundingClientRect(), host = pop.offsetParent.getBoundingClientRect();
    pop.style.left = `${Math.max(8, r.left - host.left)}px`;
    pop.style.top = `${Math.max(8, r.top - host.top - pop.offsetHeight - 6)}px`;
    pop.onclick = (e) => { const b = e.target.closest("[data-v]"); if (b) onPick(b.dataset.v); };
  }
  const closePop = () => { pop.hidden = true; };
  document.addEventListener("pointerdown", (e) => { if (!pop.hidden && !e.target.closest("#dr-pop, #dr-model")) closePop(); });

  // ---------------------------------------------------------------- 送出
  async function send(text, opts = {}) {
    if (st.busy) return;
    text = (text ?? $("#dr-input").value).trim();
    if (!text && !st.attach) { $("#dr-input").focus(); return; }
    const mode = opts.mode || st.mode;
    const payload = { text, mode, model: st.model, use_canvas: opts.useCanvas ?? $("#dr-use-canvas").checked,
      skill: st.settings.skill, models: st.settings.models, gen_mode: st.settings.gen_mode };
    if (st.attach) { payload.attachment = st.attach.text; payload.attachment_name = st.attach.name; }
    st.busy = true;
    st.messages.push({ role: "user", display: text || `（上傳：${st.attach.name}）`, mode });
    $("#dr-input").value = ""; renderMessages();
    try {
      const res = await api(`/api/projects/${st.pid}/director/chat`, { method: "POST", body: JSON.stringify(payload) });
      st.messages.pop(); st.messages.push(res.user, res.reply);
      st.attach = null; renderAttach();
    } catch (err) { st.messages.pop(); $("#dr-input").value = text; toast(err.message, true); }
    finally { st.busy = false; renderMessages(); }
  }

  // ---------------------------------------------------------------- 送到畫布
  async function pushToCanvas(build) {
    const { canvas } = await api(`/api/projects/${st.pid}/canvas`);
    const maxId = Math.max(0, ...canvas.nodes.map((n) => +n.id.slice(1)));
    const baseY = canvas.nodes.length ? Math.max(...canvas.nodes.map((n) => n.y)) + 320 : 0;
    let next = maxId;
    const mk = (kind, title, prompt, x, y, extra = {}) => {
      const n = { id: `N${++next}`, kind, title, x, y, prompt, model: (kind === "image" || kind === "video") ? (st.settings.models[kind] || "") : "", mode: kind === "video" ? "t2v" : kind === "image" ? "t2i" : "",
        params: kind === "video" ? { ratio: "16:9", duration: 5, resolution: "768P" } : kind === "image" ? { ratio: "16:9" } : {}, ...extra };
      canvas.nodes.push(n); return n;
    };
    const before = next;
    build(canvas, mk, baseY);
    const res = await api(`/api/projects/${st.pid}/canvas`, { method: "PUT", body: JSON.stringify(canvas) });
    st.canvas = res.canvas; renderAssets();
    return canvas.nodes.filter((n) => +n.id.slice(1) > before);
  }
  // 自動生成：先跑全部圖片節點，再跑影片節點（影片以上游圖片為首影格）
  async function autoRun(nodes) {
    const run = async (n) => {
      try {
        const r = await api(`/api/projects/${st.pid}/canvas/run`, { method: "POST", body: JSON.stringify({ node_id: n.id }) });
        if (r.job) toast(`${n.title}：影片任務已送出（${r.job.model}）`); else toast(`${n.title} 完成`);
        return true;
      } catch (err) { toast(`${n.title}：${err.message}`, true); return false; }
    };
    const imgs = nodes.filter((n) => n.kind === "image"), vids = nodes.filter((n) => n.kind === "video");
    toast(`自動生成開始：${imgs.length} 張圖片 → ${vids.length} 支影片`);
    const ok = new Set();
    for (const n of imgs) if (await run(n)) ok.add(n.id);
    const edges = (st.canvas && st.canvas.edges) || [];
    for (const v of vids) {
      const up = edges.filter((e) => e.to === v.id).map((e) => e.from);
      if (up.length && !up.some((id) => ok.has(id))) { toast(`${v.title}：上游圖片失敗，略過`, true); continue; }
      await run(v);
    }
    const cv = await api(`/api/projects/${st.pid}/canvas`); st.canvas = cv.canvas; renderAssets();
    toast("自動生成已送出，影片進度請到畫布查看");
  }
  async function shotsToCanvas(shots) {
    const created = await pushToCanvas((canvas, mk, y0) => {
      shots.forEach((s, i) => {
        const y = y0 + i * 300;
        const img = mk("image", `分鏡 ${i + 1}・畫面`, String(s.prompt || ""), 0, y, s.negative ? { negative: String(s.negative) } : {});
        const vprompt = s.motion ? `${s.motion}\n${s.prompt || ""}` : String(s.prompt || "");
        const vid = mk("video", `分鏡 ${i + 1}・${String(s.title || "影片").slice(0, 20)}`, vprompt, 460, y,
          { mode: /\|MiniMax-H3/.test(st.settings.models.video || "") ? "i2v" : "t2v", params: { ratio: "16:9", duration: Math.max(4, Math.min(10, +s.seconds || 5)), resolution: "768P" } });
        canvas.edges.push({ from: img.id, to: vid.id });
      });
    });
    toast(`已建立 ${shots.length} 組「圖片 → 影片」節點`);
    if (st.settings.gen_mode === "auto") autoRun(created);
  }

  // ---------------------------------------------------------------- 劇本設定器
  function renderSetter() {
    const p = st.preset;
    $("#dr-hot-list").innerHTML = HOT.map(([name], i) => `<button type="button" data-hot="${i}" class="dr-hot-item"><span class="n">${i + 1}</span>${name}</button>`).join("");
    $("#dr-genres").innerHTML = GENRES.map(([g, ic, col]) => `<button type="button" data-genre="${esc(g)}" class="${g === p.genre ? "on" : ""} ${g === p.fuse ? "fused" : ""}">
      <span class="g-dot" style="background:linear-gradient(135deg,${col[0]},${col[1]})">${svg(IC[ic], 16)}</span>${g}${g === p.genre ? " ◂" : g === p.fuse ? " ＋" : ""}</button>`).join("")
      + (p.genre === "其他（自訂）" ? `<input type="text" id="dr-custom" placeholder="輸入自訂題材" value="${esc(p.custom)}">` : "");
    const g = GENRES.find((x) => x[0] === p.genre) || GENRES[0];
    $("#dr-orb-main").style.background = `radial-gradient(circle at 30% 30%, ${g[2][1]}, ${g[2][0]})`;
    $("#dr-orb-main").innerHTML = `${svg(IC[g[1]], 64)}<b>${esc(p.genre === "其他（自訂）" ? (p.custom || "自訂題材") : p.genre)}</b>`;
    const f = p.fuse && GENRES.find((x) => x[0] === p.fuse);
    $("#dr-orb-fuse").innerHTML = f ? `${svg(IC[f[1]], 26)}<span>${esc(f[0])}</span><small>點擊移除</small>` : `${svg('<path d="M12 5v14M5 12h14"/>', 30)}<span>融合題材</span>`;
    $("#dr-orb-fuse").classList.toggle("on", !!f);
    $("#dr-opts").innerHTML = OPTS.map(([k, label, ic]) => `<button type="button" data-opt="${k}" class="${p[k] !== "自動" ? "set" : ""}">
      <span class="o-ico">${svg(IC[ic], 20)}</span><span><small>${label}</small><b>${esc(p[k])}</b></span></button>`).join("");
    const cu = $("#dr-custom"); if (cu) cu.oninput = (e) => { p.custom = e.target.value; $("#dr-orb-main b").textContent = p.custom || "自訂題材"; };
  }
  let fusing = false;
  function openSetter() { $("#dr-modal").hidden = false; fusing = false; renderSetter(); }
  function closeSetter() { $("#dr-modal").hidden = true; }
  $("#dr-modal").addEventListener("click", (e) => {
    const p = st.preset;
    if (e.target === $("#dr-modal") || e.target.closest("[data-close]")) { closeSetter(); return; }
    const hot = e.target.closest("[data-hot]");
    if (hot) { const [, genre, hook] = HOT[+hot.dataset.hot]; Object.assign(p, { genre, hook, fuse: null }); renderSetter(); return; }
    const g = e.target.closest("[data-genre]");
    if (g) {
      const v = g.dataset.genre;
      if (fusing && v !== p.genre) { p.fuse = v; fusing = false; }
      else { p.genre = v; if (p.fuse === v) p.fuse = null; }
      renderSetter(); return;
    }
    if (e.target.closest("#dr-orb-fuse")) {
      if (p.fuse) { p.fuse = null; fusing = false; toast("已移除融合題材"); }
      else { fusing = true; toast("請在左側選擇要融合的第二個題材"); }
      renderSetter(); return;
    }
    const o = e.target.closest("[data-opt]");
    if (o) {
      const [k, label, , values] = OPTS.find((x) => x[0] === o.dataset.opt);
      const menu = document.createElement("div"); menu.className = "dr-optmenu";
      menu.innerHTML = `<div class="pop-title">${label}</div>` + values.map((v) => `<button type="button" data-pick="${esc(v)}" class="${p[k] === v ? "on" : ""}">${esc(v)}</button>`).join("");
      document.querySelectorAll(".dr-optmenu").forEach((x) => x.remove());
      o.appendChild(menu);
      menu.onclick = (ev) => { ev.stopPropagation(); const b = ev.target.closest("[data-pick]"); if (b) { p[k] = b.dataset.pick; renderSetter(); } };
      return;
    }
    document.querySelectorAll(".dr-optmenu").forEach((x) => x.remove());
  });
  $("#dr-show-hot").addEventListener("change", (e) => { $("#dr-hot").hidden = !e.target.checked; });
  $("#dr-confirm").addEventListener("click", () => {
    const p = st.preset;
    const genre = p.genre === "其他（自訂）" ? (p.custom || "自訂題材") : p.genre;
    const text = [`請原創一部劇本。`, `題材：${genre}${p.fuse ? ` × ${p.fuse}（融合）` : ""}`,
      ...OPTS.map(([k, label]) => `${label}：${p[k]}${p[k] === "自動" ? "（由你決定最合適的）" : ""}`)].join("\n");
    closeSetter(); st.mode = "original"; renderMode(); send(text, { mode: "original" });
  });

  // ---------------------------------------------------------------- 事件
  $("#dr-send").addEventListener("click", () => send());
  $("#dr-input").addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) { e.preventDefault(); send(); }
  });
  $("#dr-input").addEventListener("input", (e) => {
    const ta = e.target, before = ta.value.slice(0, ta.selectionStart);
    if (!before.endsWith("@")) return;
    const nodes = (st.canvas && st.canvas.nodes) || [];
    const html = `<div class="pop-title">節點</div>` + (nodes.length ? nodes.map((n) => `<button type="button" data-v="node:${esc(n.title)}">${svg(IC[n.kind] || IC.text, 15)}<span>${esc(n.title)}</span></button>`).join("") : '<div class="muted" style="padding:4px 10px;font-size:12px">畫布沒有節點</div>')
      + `<div class="pop-title">模型</div>` + modelList().map((x) => `<button type="button" data-v="model:${esc(x.v)}">${svg(IC.text, 15)}<span class="pm-name">${esc(x.id)}<small>${esc(x.p.name)}</small></span></button>`).join("");
    openPop(ta, html, (v) => {
      const [kind, val] = v.split(/:(.+)/);
      const pos = ta.selectionStart;
      if (kind === "node") { ta.value = ta.value.slice(0, pos - 1) + `@${val} ` + ta.value.slice(pos); $("#dr-use-canvas").checked = true; }
      else { ta.value = ta.value.slice(0, pos - 1) + ta.value.slice(pos); st.model = val; renderModel(); toast(`已切換模型：${val.split("|")[1]}`); }
      closePop(); ta.focus();
    });
  });
  $("#dr-modes").addEventListener("click", (e) => { const b = e.target.closest("[data-mode]"); if (b) { st.mode = b.dataset.mode; renderMode(); } });
  $("#dr-model").addEventListener("click", (e) => {
    const cur = st.model || `${st.cfg.routing.script.provider}|${st.cfg.routing.script.model}`;
    openPop(e.currentTarget, `<div class="pop-title">對話模型</div>` + modelList().map((x) => `<button type="button" data-v="${esc(x.v)}" class="${x.v === cur ? "on" : ""}">${svg(IC.text, 15)}<span class="pm-name">${esc(x.id)}<small>${esc(x.p.name)}</small></span><em class="chip ${x.m.status === "ok" ? "ok" : ""}">${x.m.status === "ok" ? "已實測" : "未實測"}</em></button>`).join(""),
      (v) => { st.model = v; renderModel(); closePop(); });
  });
  $("#dr-upload").addEventListener("click", () => $("#dr-file").click());
  $("#dr-preset").addEventListener("click", openSetter);
  $("#dr-file").addEventListener("change", async (e) => {
    const f = e.target.files[0]; e.target.value = "";
    if (!f) return;
    if (f.size > 2 * 1024 * 1024) { toast("檔案太大（上限 2 MB）", true); return; }
    const text = (await f.text()).slice(0, 60000);
    st.attach = { name: f.name, text }; st.mode = "adapt"; renderMode(); renderAttach();
    toast(text.length >= 60000 ? "已載入前 60,000 字" : `已載入 ${f.name}`);
    $("#dr-input").focus();
  });
  $("#dr-welcome").addEventListener("click", (e) => {
    const b = e.target.closest("[data-start]"); if (!b) return;
    const k = b.dataset.start;
    if (k === "preset") openSetter();
    else if (k === "upload") $("#dr-file").click();
    else if (k === "canvas") { $("#dr-use-canvas").checked = true; st.mode = "direct"; renderMode(); send("請根據目前畫布上的節點，分析現況，並建議下一步該補哪些鏡頭與節點。", { mode: "direct", useCanvas: true }); }
    else if (k === "optimize") { $("#dr-use-canvas").checked = true; st.mode = "direct"; renderMode(); send("請逐一優化畫布上各節點的提示詞，讓畫面更具體、運鏡與光線更清楚，最後輸出 JSON shots。", { mode: "direct", useCanvas: true }); }
    else { st.mode = "direct"; renderMode(); const ta = $("#dr-input"); ta.placeholder = "輸入一句話故事，例如：一名少女在雨夜的霓虹街道上追逐一枚飄走的紙鶴"; ta.focus(); }
  });
  $("#dr-msgs").addEventListener("click", async (e) => {
    const b = e.target.closest("button"); if (!b) return;
    if (b.dataset.copy) { const m = st.messages[+b.dataset.copy]; try { await navigator.clipboard.writeText(m.content); toast("已複製"); } catch { toast("無法存取剪貼簿", true); } }
    if (b.dataset.tonode) {
      const m = st.messages[+b.dataset.tonode];
      b.disabled = true;
      try {
        await pushToCanvas((canvas, mk, y) => { const n = mk("text", `${MODE_NAME[m.mode] || "AI 導演"}・文字`, "", 0, y); n.prompt = m.content.slice(0, 4000); });
        toast("已送到畫布（內容放在提示詞）");
      } catch (err) { toast(err.message, true); } finally { b.disabled = false; }
    }
    if (b.dataset.shots) {
      b.disabled = true;
      try { await shotsToCanvas(extractShots(st.messages[+b.dataset.shots].content)); } catch (err) { toast(err.message, true); } finally { b.disabled = false; }
    }
  });
  $("#dr-new").addEventListener("click", async () => {
    if (!st.messages.length) return;
    try { await api(`/api/projects/${st.pid}/director`, { method: "DELETE" }); st.messages = []; renderMessages(); } catch (err) { toast(err.message, true); }
  });
  $("#dr-project").addEventListener("change", (e) => { location.href = `/director?pid=${encodeURIComponent(e.target.value)}`; });

  async function boot() {
    const [cfg, list] = await Promise.all([api("/api/config"), api("/api/projects")]);
    st.cfg = cfg;
    let projects = list.projects || [];
    if (!projects.length) {
      const res = await api("/api/projects", { method: "POST", body: JSON.stringify({ idea: "AI 導演新專案", title: "未命名專案" }) });
      projects = [{ id: res.plan.id, title: res.plan.title }];
    }
    let pid = new URLSearchParams(location.search).get("pid");
    if (!pid || !projects.some((p) => p.id === pid)) pid = projects[0].id;
    st.pid = pid; history.replaceState(null, "", `/director?pid=${pid}`);
    $("#dr-project").innerHTML = projects.map((p) => `<option value="${esc(p.id)}" ${p.id === pid ? "selected" : ""}>${esc(p.title)}</option>`).join("");
    $("#dr-open-canvas").href = `/canvas?pid=${pid}`;
    const [hist, cv] = await Promise.all([api(`/api/projects/${pid}/director`), api(`/api/projects/${pid}/canvas`)]);
    st.messages = hist.messages || []; st.canvas = cv.canvas;
    const hs = hist.settings || {};
    st.settings = { skill: hs.skill || "", skill_name: "", models: hs.models || {}, gen_mode: hs.gen_mode === "auto" ? "auto" : "manual" };
    try {
      const inc = JSON.parse(sessionStorage.getItem("reach.director.settings") || "null");
      if (inc) { sessionStorage.removeItem("reach.director.settings"); st.settings = { skill: inc.skill || "", skill_name: inc.skill_name || "", models: inc.models || {}, gen_mode: inc.gen_mode === "auto" ? "auto" : "manual" }; }
    } catch (_) {}
    if (st.settings.skill && !st.settings.skill_name) {
      api("/api/skills").then((d) => { const k = (d.skills || []).find((x) => x.slug === st.settings.skill); if (k) { st.settings.skill_name = k.cn; renderSets(); } }).catch(() => {});
    }
    renderSets();
    renderMessages(); renderAssets(); renderModel(); renderMode();
    try {
      const pre = sessionStorage.getItem("reach.director.prefill");
      if (pre) { sessionStorage.removeItem("reach.director.prefill"); const el = $("#dr-input"); el.value = pre; el.focus(); el.dispatchEvent(new Event("input")); }
    } catch (_) {}
  }
  boot().catch((err) => toast(err.message, true));
})();

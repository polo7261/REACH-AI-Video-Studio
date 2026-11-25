// Skill 工作台：左對話（含 AI 提問卡）、右劇本／分鏡表
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const st = { pid: null, sid: null, ss: null, cfg: null, tab: "script", edit: false, busy: false, ask: null, saveT: null };
  const store = { get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} } };

  function toast(msg, isErr = false) {
    const el = document.createElement("div"); el.className = "toast" + (isErr ? " err" : ""); el.textContent = msg;
    document.body.appendChild(el); setTimeout(() => el.remove(), isErr ? 7000 : 3200);
  }
  async function api(path, opt = {}) {
    const res = await fetch(path, { headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, ...opt });
    let body = null; try { body = await res.json(); } catch { body = null; }
    if (!res.ok) throw new Error((body && body.error) || `HTTP ${res.status}`);
    return body;
  }
  function md(src) {
    const blocks = String(src || "").split(/```/);
    return blocks.map((b, i) => {
      if (i % 2) return `<pre><code>${esc(b.replace(/^[a-z]*\n/i, ""))}</code></pre>`;
      const lines = esc(b).split("\n"); let html = "", list = false;
      const inline = (s) => s.replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/`([^`]+)`/g, "<code>$1</code>");
      for (const ln of lines) {
        const h = ln.match(/^(#{1,4})\s+(.*)/), li = ln.match(/^\s*(?:[-*•]|\d+[.)])\s+(.*)/);
        if (li) { if (!list) { html += "<ul>"; list = true; } html += `<li>${inline(li[1])}</li>`; continue; }
        if (list) { html += "</ul>"; list = false; }
        if (h) { const lv = Math.min(4, h[1].length + 2); html += `<h${lv}>${inline(h[2])}</h${lv}>`; }
        else if (/^\s*>\s?/.test(ln)) html += `<p class="muted">${inline(ln.replace(/^\s*&gt;\s?/, ""))}</p>`;
        else if (ln.trim()) html += `<p>${inline(ln)}</p>`;
      }
      if (list) html += "</ul>";
      return html;
    }).join("");
  }
  const modelName = (v) => (v || "").split("|")[1] || "";

  // ---------------------------------------------------------------- 左：設定列
  function renderSets() {
    const s = st.ss, el = $("#wb-sets");
    if (!s) { el.innerHTML = ""; return; }
    const chips = [];
    chips.push(`<span class="wb-set skill"><i>Skill</i>${esc(s.skill_name || "自由創作")}</span>`);
    if (s.models && s.models.image) chips.push(`<span class="wb-set"><i>圖片</i>${esc(modelName(s.models.image))}</span>`);
    if (s.models && s.models.video) chips.push(`<span class="wb-set"><i>影片</i>${esc(modelName(s.models.video))}</span>`);
    chips.push(`<span class="wb-set btn" id="wb-mode" title="切換生成模式"><i>模式</i>${s.gen_mode === "auto" ? "自動（少提問）" : "手動（先提問）"} ⇄</span>`);
    el.innerHTML = chips.join("");
    $("#wb-mode").onclick = async () => {
      try { const r = await api(`/api/projects/${st.pid}/workbench/${st.sid}`, { method: "PUT", body: JSON.stringify({ gen_mode: s.gen_mode === "auto" ? "manual" : "auto" }) }); st.ss = r.session; renderSets(); }
      catch (e) { toast(e.message, true); }
    };
  }

  // ---------------------------------------------------------------- 左：訊息
  function renderMsgs() {
    const box = $("#wb-msgs"), s = st.ss;
    if (!s) { box.innerHTML = ""; return; }
    const ms = s.messages || [];
    if (!ms.length && !st.busy) {
      box.innerHTML = `<div class="wb-empty"><b>${esc(s.skill_name || "自由創作")}</b>說說你想拍什麼：題材、片長、風格、主角…<br>資訊不夠時，AI 會先用選項問你；確定後劇本與分鏡表會出現在右邊。</div>`;
    } else {
      box.innerHTML = ms.map((m, i) => {
        if (m.role === "user") return `<div class="wb-m user">${esc(m.content)}</div>`;
        const notes = (m.updated || []).map((k) => `<button type="button" data-goto="${k}">✓ 已更新${k === "script" ? "劇本" : "分鏡表"}</button>`).join("");
        const answered = m.questions && m.questions.length && i < ms.length - 1;
        return `<div class="wb-m ai"><div class="md">${md(m.text || (m.updated && m.updated.length ? "" : m.content))}</div>
          ${m.questions && m.questions.length ? `<div class="wb-asked">❓ 已詢問 ${m.questions.length} 題${answered ? "" : "（請在下方作答）"}：${m.questions.map((q) => `<b>${esc(q.q)}</b>`).join("、")}</div>` : ""}
          ${notes ? `<div class="wb-note">${notes}</div>` : ""}</div>`;
      }).join("") + (st.busy ? `<div class="wb-think"><i></i>AI 正在依 Skill 思考…（長劇本可能需要 1–2 分鐘）</div>` : "");
    }
    box.querySelectorAll("[data-goto]").forEach((b) => b.onclick = () => setTab(b.dataset.goto === "script" ? "script" : "shots"));
    box.scrollTop = box.scrollHeight;
    renderAsk();
  }

  // ---------------------------------------------------------------- 左：提問卡
  function renderAsk() {
    const el = $("#wb-ask"), ms = (st.ss && st.ss.messages) || [];
    const last = ms[ms.length - 1];
    const qs = !st.busy && last && last.role === "assistant" && last.questions && last.questions.length ? last.questions : null;
    if (!qs) { el.hidden = true; st.ask = null; return; }
    if (!st.ask || st.ask.key !== last.at + qs.length) st.ask = { key: last.at + qs.length, page: 0, ans: qs.map(() => ({ pick: null, other: "" })) };
    const a = st.ask, q = qs[a.page], ans = a.ans[a.page];
    el.hidden = false;
    el.innerHTML = `<div class="wb-ask-h"><span>${esc(q.q)}</span>
        ${qs.length > 1 ? `<small><button type="button" data-pg="-1" ${a.page ? "" : "disabled"}>‹</button>${a.page + 1}/${qs.length}<button type="button" data-pg="1" ${a.page < qs.length - 1 ? "" : "disabled"}>›</button></small>` : ""}</div>
      ${q.options.map((o, i) => `<button type="button" class="wb-opt ${ans.pick === i ? "on" : ""}" data-o="${i}"><em>${i + 1}</em>${esc(o)}</button>`).join("")}
      <div class="wb-opt ${ans.pick === -1 ? "on" : ""}" data-o="-1"><em>${q.options.length + 1}</em><input type="text" placeholder="其它，請直接輸入" value="${esc(ans.other)}"></div>
      <div class="wb-ask-f"><button type="button" class="ghost small" id="wb-skip">忽略</button>
        <button type="button" class="small" id="wb-go">${a.page < qs.length - 1 ? "下一題" : "繼續"}</button></div>`;
    el.querySelectorAll("button.wb-opt").forEach((b) => b.onclick = () => { ans.pick = +b.dataset.o; next(); });
    const inp = el.querySelector("input");
    inp.onfocus = () => { ans.pick = -1; el.querySelectorAll(".wb-opt").forEach((x) => x.classList.toggle("on", x.dataset.o === "-1")); };
    inp.oninput = () => { ans.other = inp.value; };
    inp.onkeydown = (e) => { if (e.key === "Enter") { e.preventDefault(); next(); } };
    el.querySelectorAll("[data-pg]").forEach((b) => b.onclick = () => { a.page += +b.dataset.pg; renderAsk(); });
    $("#wb-skip").onclick = () => send("先略過這些問題，請用合理的假設直接產出劇本與分鏡表，並標註你做了哪些假設。");
    $("#wb-go").onclick = next;
    function next() {
      if (a.page < qs.length - 1) { a.page++; renderAsk(); return; }
      const lines = qs.map((qq, i) => {
        const x = a.ans[i];
        const v = x.pick === -1 ? x.other.trim() : x.pick != null ? qq.options[x.pick] : "";
        return `${qq.q}\n→ ${v || "（由你決定）"}`;
      });
      send(lines.join("\n\n"));
    }
  }

  // ---------------------------------------------------------------- 送出
  async function send(text) {
    text = (text ?? $("#wb-text").value).trim();
    if (!text || st.busy || !st.sid) return;
    st.busy = true; $("#wb-send").disabled = true;
    st.ss.messages = [...(st.ss.messages || []), { role: "user", content: text }];
    if (text === $("#wb-text").value.trim()) $("#wb-text").value = "";
    renderMsgs();
    try {
      const r = await api(`/api/projects/${st.pid}/workbench/${st.sid}/chat`, { method: "POST", body: JSON.stringify({ text }) });
      const before = { script: st.ss.script, shots: (st.ss.shots || []).length };
      st.ss = r.session;
      const last = st.ss.messages[st.ss.messages.length - 1];
      if (last.updated && last.updated.includes("shots") && !last.updated.includes("script")) setTab("shots");
      else if (last.updated && last.updated.length) setTab(st.tab === "shots" && last.updated.includes("shots") ? "shots" : "script");
      else renderDoc();
      void before;
      refreshSessions();
    } catch (e) {
      st.ss.messages.pop(); $("#wb-text").value = text; toast(e.message, true);
    } finally { st.busy = false; $("#wb-send").disabled = false; renderMsgs(); }
  }

  // ---------------------------------------------------------------- 右：劇本／分鏡
  function setTab(t) { st.tab = t; st.edit = false; document.querySelectorAll("#wb-tabs button").forEach((b) => b.classList.toggle("on", b.dataset.tab === t)); renderDoc(); }
  function save(patch, quiet = true) {
    clearTimeout(st.saveT);
    st.saveT = setTimeout(async () => {
      try { const r = await api(`/api/projects/${st.pid}/workbench/${st.sid}`, { method: "PUT", body: JSON.stringify(patch) }); st.ss.script = r.session.script; if (!quiet) toast("已儲存"); }
      catch (e) { toast(e.message, true); }
    }, 500);
  }
  function renderDoc() {
    const s = st.ss, body = $("#wb-doc");
    $("#wb-shot-n").textContent = s ? (s.shots || []).length : 0;
    $("#wb-edit").textContent = st.edit ? "完成" : "編輯";
    $("#wb-edit").hidden = !s;
    if (!s) { body.innerHTML = ""; return; }
    if (st.tab === "script") {
      if (!s.script) { body.innerHTML = `<div class="wb-blank"><b>劇本還沒產生</b>在左邊跟 AI 聊聊你的想法，<br>回答完它的提問後，劇本會出現在這裡。</div>`; return; }
      if (st.edit) {
        body.innerHTML = `<div class="wb-script"><textarea id="wb-script-ta">${esc(s.script)}</textarea></div>`;
        $("#wb-script-ta").oninput = (e) => { s.script = e.target.value; save({ script: s.script }); };
      } else body.innerHTML = `<div class="wb-script md">${md(s.script)}</div>`;
      return;
    }
    const shots = s.shots || [];
    if (!shots.length) { body.innerHTML = `<div class="wb-blank"><b>分鏡表還沒產生</b>劇本確定後，請 AI「依劇本拆成分鏡表」。<br>每一鏡都會附圖片提示詞與運鏡，可一鍵建立到畫布。</div>`; return; }
    const total = shots.reduce((t, x) => t + (+x.seconds || 0), 0);
    const F = (label, k, x, i, mono) => st.edit
      ? `<label class="wb-f"><span>${label}</span><textarea data-i="${i}" data-k="${k}" rows="${mono ? 3 : 2}">${esc(x[k])}</textarea></label>`
      : x[k] ? `<div class="wb-f"><span>${label}</span><div class="${mono ? "mono" : ""}">${esc(x[k])}</div></div>` : "";
    body.innerHTML = `<div class="wb-shots"><div class="muted" style="font-size:12.5px">共 ${shots.length} 鏡 · 約 ${total} 秒</div>` + shots.map((x, i) => `
      <div class="wb-shot">
        <div class="wb-shot-no">${String(i + 1).padStart(2, "0")}<small>${st.edit ? `<input class="wb-sec" type="number" min="4" max="10" data-i="${i}" data-k="seconds" value="${x.seconds}">` : `${x.seconds} 秒`}</small></div>
        <div>
          <div class="wb-shot-h">${st.edit ? `<input data-i="${i}" data-k="title" value="${esc(x.title)}">
              <button type="button" data-mv="${i}:-1" title="上移" ${i ? "" : "disabled"}>↑</button><button type="button" data-mv="${i}:1" title="下移" ${i < shots.length - 1 ? "" : "disabled"}>↓</button><button type="button" data-del="${i}" title="刪除">✕</button>`
            : `<b>${esc(x.title || `分鏡 ${i + 1}`)}</b>`}</div>
          ${F("畫面", "desc", x, i)}${F("運鏡光線", "camera", x, i)}${F("圖片提示詞", "prompt", x, i, true)}${F("負面提示詞", "negative", x, i, true)}${F("影片運動", "motion", x, i, true)}
        </div>
      </div>`).join("") + (st.edit ? `<button type="button" class="ghost" id="wb-add-shot">＋ 新增一鏡</button>` : "") + "</div>";
    if (st.edit) {
      const put = () => { clearTimeout(st.saveT); st.saveT = setTimeout(() => api(`/api/projects/${st.pid}/workbench/${st.sid}`, { method: "PUT", body: JSON.stringify({ shots: s.shots }) }).catch((e) => toast(e.message, true)), 600); };
      body.querySelectorAll("[data-k]").forEach((el) => el.oninput = () => { const x = s.shots[+el.dataset.i]; x[el.dataset.k] = el.dataset.k === "seconds" ? Math.max(4, Math.min(10, +el.value || 5)) : el.value; put(); });
      body.querySelectorAll("[data-mv]").forEach((b) => b.onclick = () => { const [i, d] = b.dataset.mv.split(":").map(Number); [s.shots[i], s.shots[i + d]] = [s.shots[i + d], s.shots[i]]; put(); renderDoc(); });
      body.querySelectorAll("[data-del]").forEach((b) => b.onclick = () => { s.shots.splice(+b.dataset.del, 1); put(); renderDoc(); });
      $("#wb-add-shot").onclick = () => { s.shots.push({ title: `分鏡 ${s.shots.length + 1}`, seconds: 5, desc: "", camera: "", prompt: "", negative: "", motion: "" }); put(); renderDoc(); };
    }
  }

  // ---------------------------------------------------------------- 匯出／送到畫布
  $("#wb-export").onclick = () => {
    const s = st.ss; if (!s) return;
    const shots = (s.shots || []).map((x, i) => `## 分鏡 ${i + 1}：${x.title}（${x.seconds} 秒）\n- 畫面：${x.desc}\n- 運鏡光線：${x.camera}\n- 圖片提示詞：${x.prompt}\n- 負面提示詞：${x.negative}\n- 影片運動：${x.motion}`).join("\n\n");
    const blob = new Blob([`${s.script || ""}\n\n---\n\n# 分鏡表\n\n${shots}\n`], { type: "text/markdown" });
    const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = `${s.title || "skill"}-劇本分鏡.md`; a.click(); URL.revokeObjectURL(a.href);
  };
  $("#wb-canvas").onclick = async () => {
    const s = st.ss, shots = (s && s.shots) || [];
    if (!shots.length) { toast("還沒有分鏡表", true); return; }
    try {
      const { canvas } = await api(`/api/projects/${st.pid}/canvas`);
      let next = Math.max(0, ...canvas.nodes.map((n) => +n.id.slice(1)));
      const y0 = canvas.nodes.length ? Math.max(...canvas.nodes.map((n) => n.y)) + 360 : 0;
      const vm = (s.models && s.models.video) || "", im = (s.models && s.models.image) || "";
      shots.forEach((x, i) => {
        const y = y0 + i * 300, t = `分鏡 ${i + 1}`;
        const img = { id: `N${++next}`, kind: "image", title: `${t}・畫面`, x: 0, y, prompt: x.prompt || x.desc, model: im, mode: "t2i", params: { ratio: "16:9" }, output: null, status: "idle" };
        const vid = { id: `N${++next}`, kind: "video", title: `${t}・${(x.title || "影片").slice(0, 20)}`, x: 460, y,
          prompt: [x.motion, x.prompt || x.desc].filter(Boolean).join("\n"), model: vm, mode: /\|MiniMax-H3/.test(vm) ? "i2v" : "t2v",
          params: { ratio: "16:9", duration: Math.max(4, Math.min(10, +x.seconds || 5)), resolution: "768P" }, output: null, status: "idle" };
        canvas.nodes.push(img, vid); canvas.edges.push({ from: img.id, to: vid.id });
      });
      await api(`/api/projects/${st.pid}/canvas`, { method: "PUT", body: JSON.stringify(canvas) });
      const t = document.createElement("div"); t.className = "toast";
      t.innerHTML = `已建立 ${shots.length} 組「圖片 → 影片」節點　<a href="/canvas?pid=${encodeURIComponent(st.pid)}" style="color:inherit;text-decoration:underline">開啟畫布 →</a>`;
      document.body.appendChild(t); setTimeout(() => t.remove(), 7000);
    } catch (e) { toast(e.message, true); }
  };
  $("#wb-edit").onclick = () => { st.edit = !st.edit; renderDoc(); };
  document.querySelectorAll("#wb-tabs button").forEach((b) => b.onclick = () => setTab(b.dataset.tab));

  // ---------------------------------------------------------------- 工作階段
  async function refreshSessions() {
    const { sessions } = await api(`/api/projects/${st.pid}/workbench`);
    $("#wb-session").innerHTML = sessions.length ? sessions.map((x) => `<option value="${x.id}" ${x.id === st.sid ? "selected" : ""}>${esc(x.title)}${x.shots ? ` · ${x.shots} 鏡` : ""}</option>`).join("") : `<option value="">（尚無工作階段）</option>`;
    return sessions;
  }
  async function openSession(sid) {
    const { session } = await api(`/api/projects/${st.pid}/workbench/${sid}`);
    st.sid = sid; st.ss = session; st.ask = null;
    history.replaceState(null, "", `/workbench?pid=${st.pid}&sid=${sid}`);
    store.set("reach.wb.last", { pid: st.pid, sid });
    renderSets(); renderMsgs(); setTab(session.script ? "script" : (session.shots || []).length ? "shots" : "script");
    $("#wb-text").focus();
  }
  async function createSession(opts = {}) {
    const { session } = await api(`/api/projects/${st.pid}/workbench`, { method: "POST", body: JSON.stringify(opts) });
    await refreshSessions(); await openSession(session.id); await refreshSessions();
    return session;
  }
  $("#wb-session").onchange = (e) => e.target.value && openSession(e.target.value);
  $("#wb-project").onchange = (e) => { location.href = `/workbench?pid=${encodeURIComponent(e.target.value)}`; };
  $("#wb-new").onclick = () => { location.href = "/skills/"; };
  $("#wb-send").onclick = () => send();
  $("#wb-text").onkeydown = (e) => { if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) { e.preventDefault(); send(); } };

  async function boot() {
    const [cfg, list] = await Promise.all([api("/api/config"), api("/api/projects")]);
    st.cfg = cfg;
    let projects = list.projects || [];
    if (!projects.length) {
      const res = await api("/api/projects", { method: "POST", body: JSON.stringify({ idea: "Skill 工作台", title: "未命名專案" }) });
      projects = [{ id: res.plan.id, title: res.plan.title }];
    }
    const q = new URLSearchParams(location.search), last = store.get("reach.wb.last", {});
    let pid = q.get("pid") || last.pid;
    if (!pid || !projects.some((p) => p.id === pid)) pid = projects[0].id;
    st.pid = pid;
    $("#wb-project").innerHTML = projects.map((p) => `<option value="${esc(p.id)}" ${p.id === pid ? "selected" : ""}>${esc(p.title)}</option>`).join("");
    $("#wb-model").textContent = `對話模型：${cfg.routing.script.model}`;
    let incoming = null;
    try { incoming = JSON.parse(sessionStorage.getItem("reach.workbench.new") || "null"); sessionStorage.removeItem("reach.workbench.new"); } catch {}
    const sessions = await refreshSessions();
    if (incoming) {
      await createSession({ skill: incoming.skill || "", models: incoming.models || {}, gen_mode: incoming.gen_mode || "manual" });
      if (incoming.text) send(incoming.text);
      return;
    }
    const sid = q.get("sid") || (last.pid === pid ? last.sid : null);
    if (sid && sessions.some((x) => x.id === sid)) await openSession(sid);
    else if (sessions.length) await openSession(sessions[0].id);
    else await createSession({});
  }
  boot().catch((e) => toast(e.message, true));
})();

(() => {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const STATUS = { ok: ["ok", "已實測"], quota: ["warn", "額度上限"], untested: ["", "未實測"], builtin: ["use", "內建"], license: ["err", "條款限制"] };
  const KIND = { text: "文字", image: "圖片", video: "影片", tts: "語音", music: "音樂" };
  const SCOPE = { cloud: "雲端", local: "地端" };
  const NUM = ["①", "②", "③", "④", "⑤", "⑥", "⑦"];
  const badge = (st) => { const [cls, label] = STATUS[st] || ["", st]; return `<span class="chip ${cls}">${label}</span>`; };
  // 線條 SVG 圖示（stroke 跟隨文字色）
  const svg = (body, size = 22) => `<svg class="ico" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${body}</svg>`;
  const ICON = {
    script: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
    character: '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5"/>',
    keyframe: '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="m21 16-5-5-9 8"/>',
    video: '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/>',
    tts: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    cloud: '<path d="M7 18h10a4 4 0 0 0 .6-7.96A6 6 0 0 0 6.2 9.6 4.2 4.2 0 0 0 7 18z"/>',
    local: '<rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01M11 7.5h6M11 16.5h6"/>',
    text: '<path d="M4 6h16M4 12h16M4 18h10"/>',
    image: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m21 16-5-5-9 8"/>',
    tts_k: '<path d="M4 12h2M8 8v8M12 5v14M16 8v8M20 12h0"/>',
    music: '<path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/>',
  };
  const kindIcon = (k) => svg(ICON[k === "tts" ? "tts_k" : k] || ICON.text, 14);
  let cfg = null;
  let tab = location.hash === "#local" ? "local" : "cloud";

  // 大廠穩定供應商目錄（static/vendors.json：CC Switch 模板＋影音專用分類）
  const CAT_LABEL = { official: "帳號登入", cn_official: "模型廠商", third_party: "第三方平台",
                      aggregator: "第三方平台", cloud_provider: "雲端服務商", local: "跨應用", av: "影音模型",
                      "模型廠商": "模型廠商", "第三方平台": "第三方平台", "雲端服務商": "雲端服務商" };
  const catOf = (v) => CAT_LABEL[v.category] || v.category || "其他";
  let VENDORS = null;
  fetch("/static/vendors.json").then((r) => r.json()).then((d) => { VENDORS = d; });

  function toast(msg, isErr = false) {
    const el = document.createElement("div");
    el.className = "toast" + (isErr ? " err" : "");
    el.textContent = msg; document.body.appendChild(el);
    setTimeout(() => el.remove(), isErr ? 7000 : 3000);
  }

  // 依步驟需要的類型，列出可選模型（雲端／地端分組）
  function options(kind, current) {
    return ["cloud", "local"].map((scope) => {
      const opts = cfg.providers.filter((p) => p.scope === scope).flatMap((p) =>
        p.models.filter((m) => m.kind === kind && m.status !== "license").map((m) => {
          const v = `${p.id}|${m.id}`;
          const mark = m.status === "ok" ? "✓ " : m.status === "quota" ? "⚠ " : "· ";
          return `<option value="${esc(v)}" ${v === current ? "selected" : ""}>${mark}${esc(m.id)}（${esc(p.name.replace(/（.*?）/g, ""))}）</option>`;
        }));
      return opts.length ? `<optgroup label="${SCOPE[scope]}">${opts.join("")}</optgroup>` : "";
    }).join("");
  }

  function renderFlow() {
    document.getElementById("flow").innerHTML = cfg.steps.map((s, i) => {
      const r = cfg.routing[s.id];
      const p = cfg.providers.find((x) => x.id === r.provider) || {};
      return `${i ? '<span class="arrow">→</span>' : ""}
        <div class="step">
          <div class="step-head"><span class="step-ico">${svg(ICON[s.id] || ICON.text)}</span>
            <div><span class="n">${NUM[i] || i + 1} ${esc(KIND[s.kind] || s.kind)}</span><b>${esc(s.label)}</b></div></div>
          <select data-step="${esc(s.id)}">${options(s.kind, `${r.provider}|${r.model}`)}</select>
          <span><span class="chip ${p.scope === "local" ? "warn" : "use"}">${svg(ICON[p.scope] || ICON.cloud, 12)}${SCOPE[p.scope] || "—"}</span> <span class="muted mono" style="font-size:11px">${esc(r.model)}</span></span>
        </div>`;
    }).join("");
    document.querySelectorAll("#flow [data-step]").forEach((sel) => sel.addEventListener("change", async () => {
      const [provider, model] = sel.value.split("|");
      try {
        const res = await fetch("/api/routing", {
          method: "PUT",
          headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
          body: JSON.stringify({ step: sel.dataset.step, provider, model }),
        });
        const body = await res.json();
        if (!res.ok) throw new Error(body.error || `HTTP ${res.status}`);
        cfg.routing = body.routing;
        toast(`已設定：${model}`);
        render();
      } catch (err) { toast(err.message, true); renderFlow(); }
    }));
  }

  // 每個模型對應哪些步驟：使用中（藍）／可用於（灰）
  function stepChips(pid, m) {
    const using = cfg.steps.filter((s) => cfg.routing[s.id].provider === pid && cfg.routing[s.id].model === m.id);
    if (using.length) return using.map((s) => `<span class="chip use">使用中：${NUM[cfg.steps.indexOf(s)]} ${esc(s.label)}</span>`).join(" ");
    const can = cfg.steps.filter((s) => s.kind === m.kind);
    return can.length && m.status !== "license"
      ? `<span class="muted" style="font-size:11px">可用於：${can.map((s) => esc(s.label)).join("、")}</span>` : "—";
  }

  const expanded = new Set(), editing = new Set();
  const statusOf = (p) => {
    const sts = p.models.map((m) => m.status);
    if (sts.includes("quota")) return ["warn", "額度上限"];
    if (sts.includes("ok")) return ["ok", "已連線"];
    if (p.key_editable && p.key_state === "missing") return ["warn", "未設金鑰"];
    if (sts.length && sts.every((s) => s === "license")) return ["err", "條款限制"];
    return ["", "未測試"];
  };
  const CHEV = '<path d="m6 9 6 6 6-6"/>';

  function renderProviders() {
    const list = cfg.providers.filter((p) => p.scope === tab);
    document.querySelectorAll("#tabs .tab").forEach((b) => {
      const n = cfg.providers.filter((p) => p.scope === b.dataset.tab).length;
      b.classList.toggle("active", b.dataset.tab === tab);
      b.innerHTML = `${svg(ICON[b.dataset.tab], 16)} ${b.dataset.tab === "cloud" ? "雲端" : "地端"}（${n}）`;
    });
    document.getElementById("providers").innerHTML = list.map((p) => {
      const open = expanded.has(p.id);
      const st = statusOf(p);
      return `
      <section class="card" style="${open ? "grid-column:1/-1" : ""}">
        <div data-toggle="${esc(p.id)}" style="display:flex;align-items:center;gap:10px;cursor:pointer;user-select:none">
          <span class="prov-ico ${p.scope}">${svg(ICON[p.scope] || ICON.cloud, 20)}</span>
          <div style="flex:1;min-width:0">
            <b style="font-size:14px">${esc(p.name)}</b>
            ${p.note ? `<div class="muted" style="font-size:11.5px">${esc(p.note)}</div>` : ""}
          </div>
          <span class="chip ${st[0]}">${st[1]}</span>
          <span class="muted" style="flex:none;transform:rotate(${open ? 0 : -90}deg);transition:transform .15s">${svg(CHEV, 16)}</span>
        </div>
        ${!open ? "" : `
        <div style="margin-top:12px;border-top:1px solid var(--line);padding-top:12px;display:grid;gap:10px">
          <div class="actions" style="margin:0;gap:6px">
            ${p.editable ? `<button class="ghost small" data-edit="${esc(p.id)}">${editing.has(p.id) ? "收起編輯" : "編輯"}</button>` : ""}
            <button class="ghost small" data-test="${esc(p.id)}">${p.scope === "local" ? "測試服務連線" : "測試文字連線"}</button>
            <button class="ghost small" data-del="${esc(p.id)}" style="color:var(--error,#c0392b)">刪除</button>
          </div>
          ${p.editable && editing.has(p.id) ? `
          <div style="display:grid;gap:6px">
            <input class="mono" data-url="${esc(p.id)}" value="${esc(p.base_url)}" placeholder="請求位址" style="font-size:12px">
            ${p.key_editable ? `<input class="mono" data-key="${esc(p.id)}" type="password" autocomplete="off"
              placeholder="${p.key_state === "configured" ? "金鑰已設定（留空＝不更換）" : "貼上 API 金鑰"}" style="font-size:12px">` : ""}
            <div class="actions" style="margin:0;gap:6px">
              <button class="small" data-save="${esc(p.id)}">儲存</button>
              <button class="ghost small" data-edit="${esc(p.id)}">取消</button>
            </div>
          </div>` : ""}
          ${p.extra && p.extra.anthropic ? `<div class="muted mono" style="font-size:11.5px;word-break:break-all">Anthropic 相容：${esc(p.extra.anthropic)}</div>` : ""}
          ${p.editable && !editing.has(p.id) ? `<div class="muted mono" style="font-size:11.5px;word-break:break-all">${esc(p.base_url)}</div>` : ""}
          <div><span class="chip ${p.key_state === "missing" ? "err" : "ok"}">金鑰 ${{ configured: "已設定", optional: "免金鑰", missing: "未設定" }[p.key_state] || "未設定"}</span>
          <span class="mono muted" style="font-size:11.5px">${esc(p.key_mask)}</span></div>
          <table class="map"><tr><th>模型</th><th>類型</th><th>狀態</th><th>對應步驟</th></tr>
            ${!p.models.length && p.kind === "comfyui" ? `<tr><td colspan="4" class="muted" style="font-size:12px">尚未匯入 workflow。ComfyUI 的模型要搭配 workflow 才能生成，請由下方匯入。</td></tr>` : ""}
            ${p.models.map((m) => `<tr><td class="mono">${esc(m.id)}</td><td class="kind">${kindIcon(m.kind)} ${esc(KIND[m.kind] || m.kind)}</td>
              <td>${badge(m.status)}${m.note && m.note !== (STATUS[m.status] || [])[1] ? `<div class="muted" style="font-size:11px;margin-top:2px">${esc(m.note)}</div>` : ""}</td>
              <td>${stepChips(p.id, m)}</td></tr>`).join("")}
          </table>
          ${p.kind === "comfyui" ? `
          <details data-installed style="margin-top:0"><summary class="muted" style="cursor:pointer;font-size:12px">ComfyUI 已安裝模型（載入中…）</summary><div class="mono" style="font-size:11px;margin-top:6px"></div></details>
          <form data-import style="display:grid;gap:6px">
            <div class="muted" style="font-size:11.5px">匯入 workflow：ComfyUI 選單 Workflow → Export (API) 的 JSON</div>
            <input type="file" name="file" accept=".json" required>
            <div class="actions" style="margin:0;gap:6px">
              <input name="id" placeholder="模型 ID，例 flux-dev" required style="flex:1">
              <select name="kind"><option value="image">圖片</option><option value="video">影片</option></select>
              <button class="small">匯入</button>
            </div>
            <input name="note" placeholder="備註（選填）">
          </form>` : ""}
          <div class="muted mono" id="t-${esc(p.id)}" style="font-size:11.5px;white-space:pre-wrap"></div>
        </div>`}
      </section>`;
    }).join("") || '<div class="muted">此分類沒有 Provider</div>';

    const reload = async () => { cfg = await (await fetch("/api/config")).json(); render(); };
    const runTest = async (pid) => {
      const btn = document.querySelector(`[data-test="${pid}"]`);
      const out = document.getElementById(`t-${pid}`);
      if (btn) btn.disabled = true;
      if (out) out.textContent = "測試中…";
      try {
        const res = await (await fetch("/api/config/test", {
          method: "POST",
          headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
          body: JSON.stringify({ provider: pid }),
        })).json();
        const text = res.ok
          ? `✓ ${res.model} 回覆「${res.reply ?? "ok"}」於 ${res.seconds ?? "—"}s`
          : `✗ ${res.error || "失敗"}`;
        if (out) out.textContent = text;
        return res.ok;
      } catch (err) { if (out) out.textContent = `✗ ${err.message}`; return false; }
      finally { if (btn) btn.disabled = false; }
    };
    document.querySelectorAll("[data-toggle]").forEach((el) => el.addEventListener("click", () => {
      const pid = el.dataset.toggle;
      expanded.has(pid) ? expanded.delete(pid) : expanded.add(pid);
      renderProviders();
    }));
    document.querySelectorAll("[data-edit]").forEach((btn) => btn.addEventListener("click", () => {
      const pid = btn.dataset.edit;
      editing.has(pid) ? editing.delete(pid) : editing.add(pid);
      renderProviders();
    }));
    document.querySelectorAll("[data-save]").forEach((btn) => btn.addEventListener("click", async () => {
      const pid = btn.dataset.save;
      const out = document.getElementById(`t-${pid}`);
      const url = document.querySelector(`[data-url="${pid}"]`)?.value ?? "";
      const key = document.querySelector(`[data-key="${pid}"]`)?.value ?? "";
      if (!url.trim() && !key.trim()) { if (out) out.textContent = "沒有變更（網址與金鑰都留空）"; return; }
      try {
        const res = await (await fetch("/api/config/local", {
          method: "PUT", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
          body: JSON.stringify({ provider: pid, base_url: url, api_key: key }),
        })).json();
        if (!res.ok) { if (out) out.textContent = `✗ ${res.error}`; return; }
        await reload();
        const saved = [`網址 ${res.base_url ?? "(未變更)"}`, res.key_mask ? `金鑰 ${res.key_mask}` : null].filter(Boolean).join("；");
        document.getElementById(`t-${pid}`).textContent = `✓ 已存到本機 .env：${saved}；自動測試連結…`;
        await runTest(pid);  // 存完立刻自行測試連結
      } catch (err) { if (out) out.textContent = `✗ ${err.message}`; }
    }));
    document.querySelectorAll("[data-test]").forEach((btn) => btn.addEventListener("click", () => runTest(btn.dataset.test)));
    document.querySelectorAll("[data-del]").forEach((btn) => btn.addEventListener("click", async () => {
      const pid = btn.dataset.del;
      const prov = cfg.providers.find((p) => p.id === pid);
      if (!confirm(`確定刪除「${prov?.name ?? pid}」？\n使用它的步驟會自動改用其他可用廠商${prov?.custom ? "" : "；這是內建供應商，要還原需刪除 data/hidden_providers.json 後重啟"}。`)) return;
      const res = await (await fetch(`/api/providers/${pid}`, { method: "DELETE" })).json();
      if (res.ok) { toast("已刪除"); await reload(); } else toast(res.error || "刪除失敗", true);
    }));
    document.querySelectorAll("[data-import]").forEach((form) => form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const out = document.getElementById("t-local-comfy");
      out.textContent = "匯入中…";
      const res = await (await fetch("/api/comfy/workflows", {
        method: "POST", headers: { "X-Requested-With": "fetch" }, body: new FormData(form),
      })).json();
      if (res.ok) { await reload(); document.getElementById("t-local-comfy").textContent = `✓ ${res.id}\n${(res.log || []).join("\n")}`; }
      else out.textContent = `✗ ${res.error}`;
    }));

    document.querySelectorAll("[data-installed]").forEach(async (box) => {
      const sum = box.querySelector("summary"), body = box.querySelector("div");
      try {
        const res = await (await fetch("/api/comfy/models")).json();
        if (!res.ok) { sum.textContent = `ComfyUI 已安裝模型（✗ ${res.error}）`; return; }
        const groups = Object.entries(res.models);
        sum.textContent = `ComfyUI 已安裝模型（${groups.reduce((n, [, v]) => n + v.length, 0)}）`;
        body.innerHTML = groups.map(([f, v]) => `<div style="margin-top:6px"><b>${esc(f)}</b>（${v.length}）${v.map((x) => `<div class="muted">· ${esc(x)}</div>`).join("")}</div>`).join("");
      } catch (err) { sum.textContent = `ComfyUI 已安裝模型（✗ ${err.message}）`; }
    });
  }

  function render() {
    renderFlow();
    renderProviders();
  }

  document.querySelectorAll("#tabs .tab").forEach((b) => b.addEventListener("click", () => {
    tab = b.dataset.tab; history.replaceState(null, "", `#${tab}`); renderProviders();
  }));

  fetch("/api/config").then((r) => r.json()).then((data) => { cfg = data; render(); });

  // ---- 新增供應商（CC Switch 式：挑選頁 → 詳細表單頁）----
  const addBtn = document.createElement("button");
  addBtn.type = "button";
  addBtn.style.cssText = "border:none;background:transparent;cursor:pointer;font-size:13.5px;color:var(--muted);display:inline-flex;align-items:center;gap:6px;padding:8px 6px";
  addBtn.innerHTML = `${svg('<circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/>', 15)} 新增供應商`;
  addBtn.addEventListener("mouseenter", () => { addBtn.style.color = "var(--accent)"; });
  addBtn.addEventListener("mouseleave", () => { addBtn.style.color = "var(--muted)"; });
  document.getElementById("tabs").appendChild(addBtn);

  const addView = document.getElementById("add-view");
  let pick = { cat: "全部", q: "", v: null };
  const domain = (u) => (u || "").replace(/^https?:\/\//, "").split("/")[0] || "手動填寫";
  const logo = (u, size = 20) => {
    const d = (u || "").replace(/^https?:\/\//, "").split("/")[0];
    return d ? `<img src="https://icons.duckduckgo.com/ip3/${d}.ico" width="${size}" height="${size}" loading="lazy" alt="" style="border-radius:5px;vertical-align:-4px;flex:none">` : "";
  };

  function openAdd() {
    pick = { cat: "全部", q: "", v: null };
    document.getElementById("providers").style.display = "none";
    document.getElementById("tabs").style.display = "none";
    addView.style.display = "";
    addView.style.marginTop = "22px";
    renderPicker();
  }
  function closeAdd() {
    addView.style.display = "none";
    document.getElementById("providers").style.display = "";
    document.getElementById("tabs").style.display = "";
    location.hash = `#${tab}`;
  }

  function renderPicker() {
    const vs = (VENDORS || []).filter((v) =>
      (pick.cat === "全部" || (catOf(v)) === pick.cat) &&
      (!pick.q || `${v.name} ${v.url} ${v.website || ""}`.toLowerCase().includes(pick.q.toLowerCase())));
    const cats = ["全部", ...new Set((VENDORS || []).map((v) => catOf(v)))];
    const count = (c) => (VENDORS || []).filter((v) => c === "全部" || (catOf(v)) === c).length;
    const groups = [];
    for (const v of vs) {
      const c = catOf(v);
      let g = groups.find((x) => x.cat === c);
      if (!g) groups.push(g = { cat: c, items: [] });
      g.items.push(v);
    }
    addView.innerHTML = `
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
        <h3 style="margin:0">新增供應商</h3>
        <input id="pk-q" placeholder="搜尋名稱或網址，例如 kimi、智譜、openrouter" style="flex:1" value="${esc(pick.q)}">
        <button class="ghost small" id="pk-back">返回</button>
      </div>
      <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px">
        ${cats.map((c) => `<button data-cat="${esc(c)}" type="button" style="cursor:pointer;font-size:11.5px;padding:3px 12px;border-radius:999px;
          border:1px solid ${pick.cat === c ? "var(--accent)" : "var(--line)"};
          ${pick.cat === c ? "background:var(--tint-accent);color:var(--accent);font-weight:600" : "background:transparent;color:var(--muted)"}">${esc(c)} ${count(c)}</button>`).join("")}
      </div>
      <div class="grid three" id="pk-grid"></div>`;
    addView.querySelector("#pk-grid").innerHTML = `
      <section class="card" data-pick="__custom" style="cursor:pointer">
        <h3 style="font-size:15px">${svg(ICON.text, 18)} 自訂設定</h3>
        <div class="muted" style="font-size:12px">手動填寫請求位址和 API Key</div>
      </section>
      ${groups.map((g) => `
        <section class="card" style="grid-column:1/-1;background:none;border:none;padding:0;margin-top:6px">
          <h3 class="muted" style="margin:0;font-size:13px">${esc(g.cat)}</h3></section>
        ${g.items.map((v) => `
        <section class="card" data-pick="${esc(v.url)}" style="cursor:pointer">
          <h3 style="font-size:15px;display:flex;align-items:center;gap:8px">${logo(v.website || v.url)}<span>${esc(v.name)}</span></h3>
          <div class="muted mono" style="font-size:11.5px">${esc(domain(v.website || v.url))}</div>
          ${v.own_api ? `<div style="margin-top:6px"><span class="chip warn">自有 API</span></div>` : ""}
        </section>`).join("")}`).join("")}`;
    const q = addView.querySelector("#pk-q");
    q.addEventListener("input", () => {
      pick.q = q.value;
      const caret = q.selectionStart;
      renderPicker();
      const q2 = addView.querySelector("#pk-q");
      q2.focus(); q2.setSelectionRange(caret, caret);
    });
    addView.querySelector("#pk-back").addEventListener("click", closeAdd);
    addView.querySelectorAll("[data-cat]").forEach((b) => b.addEventListener("click", () => { pick.cat = b.dataset.cat; renderPicker(); }));
    addView.querySelectorAll("[data-pick]").forEach((c) => c.addEventListener("click", () => {
      pick.v = c.dataset.pick === "__custom"
        ? { name: "", url: "", website: "", key_url: "", own_api: false }
        : (VENDORS || []).find((v) => v.url === c.dataset.pick);
      renderDetail();
    }));
  }

  function renderDetail() {
    const v = pick.v || { name: "", url: "", website: "", key_url: "", own_api: false };
    addView.innerHTML = `
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;flex-wrap:wrap">
        <button class="ghost small" id="dt-back" type="button">‹ 更換</button>
        <h3 style="margin:0;display:flex;align-items:center;gap:8px">${logo(v.website || v.url, 22)}<span>${esc(v.name || "自訂設定")}</span></h3>
        ${v.website ? `<a class="muted mono" style="font-size:11.5px" href="${esc(v.website)}" target="_blank" rel="noreferrer">${esc(domain(v.website))}</a>` : ""}
      </div>
      <section class="card" style="display:grid;gap:10px;max-width:640px">
        <label class="muted" style="font-size:11.5px">名稱 *
          <input id="dt-name" style="width:100%" value="${esc(v.name)}" placeholder="例如：公司專用帳號"></label>
        <label class="muted" style="font-size:11.5px">備註
          <input id="dt-note" style="width:100%" placeholder="選填"></label>
        <label class="muted" style="font-size:11.5px">API Key *
          <input id="dt-key" class="mono" type="password" autocomplete="off" style="width:100%" placeholder="只需要填這裡"></label>
        ${v.key_url ? `<a class="muted" style="font-size:11.5px" href="${esc(v.key_url)}" target="_blank" rel="noreferrer">取得 API Key ↗</a>` : ""}
        <label class="muted" style="font-size:11.5px">請求位址 *
          <input id="dt-url" class="mono" style="width:100%" value="${esc(v.url)}" placeholder="https://api.example.com/v1"></label>
        <p class="muted" style="font-size:11.5px;margin:0">填寫 OpenAI 相容端點位址，請勿以斜線結尾。按「驗證並新增」時系統先驗連通、抓模型清單，存檔後自動測試連結。</p>
        ${v.own_api ? `<p class="chip warn">⚠ 自有 API（非 OpenAI 相容），後端適配：架構中；仍可先建卡片。</p>` : ""}
        <label class="muted" style="font-size:11.5px">分類
          <select id="dt-scope" style="width:100%"><option value="cloud">雲端</option><option value="local">地端</option></select></label>
        <p class="muted mono" id="dt-out" style="font-size:11.5px;margin:0;white-space:pre-wrap"></p>
        <div style="display:flex;gap:8px;justify-content:flex-end">
          <button class="ghost small" id="dt-cancel" type="button">取消</button>
          <button class="small" id="dt-ok" type="button">驗證並新增</button>
        </div>
      </section>`;
    addView.querySelector("#dt-back").addEventListener("click", renderPicker);
    addView.querySelector("#dt-cancel").addEventListener("click", closeAdd);
    addView.querySelector("#dt-ok").addEventListener("click", async () => {
      const out = addView.querySelector("#dt-out");
      const payload = {
        name: addView.querySelector("#dt-name").value,
        note: addView.querySelector("#dt-note").value,
        base_url: addView.querySelector("#dt-url").value,
        api_key: addView.querySelector("#dt-key").value,
        scope: addView.querySelector("#dt-scope").value,
      };
      if (!payload.base_url.trim()) { out.textContent = "✗ 請填請求位址"; return; }
      out.textContent = "驗證連通中…"; addView.querySelector("#dt-ok").disabled = true;
      try {
        const res = await (await fetch("/api/providers", {
          method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
          body: JSON.stringify(payload),
        })).json();
        if (!res.ok) { out.textContent = `✗ ${res.error || "新增失敗"}`; addView.querySelector("#dt-ok").disabled = false; return; }
        closeAdd();
        tab = payload.scope; location.hash = `#${tab}`;
        cfg = await (await fetch("/api/config")).json(); render();
        if (res.probe?.ok) toast(`✓ 已新增；${res.probe.reply?.slice(0, 60) ?? "連線正常"}`);
        else toast(`已新增；但連線測試未過：${res.probe?.error?.slice(0, 60) ?? res.probe_err ?? "未知"}`, true);
      } catch (err) { out.textContent = `✗ ${err.message}`; addView.querySelector("#dt-ok").disabled = false; }
    });
  }

  addBtn.addEventListener("click", openAdd);
})();

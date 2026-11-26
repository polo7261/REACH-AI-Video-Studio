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
                      aggregator: "第三方平台", cloud_provider: "雲端服務商", local: "跨應用", av: "影音模型" };
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

  function renderProviders() {
    const list = cfg.providers.filter((p) => p.scope === tab);
    document.querySelectorAll("#tabs .tab").forEach((b) => {
      const n = cfg.providers.filter((p) => p.scope === b.dataset.tab).length;
      b.classList.toggle("active", b.dataset.tab === tab);
      b.innerHTML = `${svg(ICON[b.dataset.tab], 16)} ${b.dataset.tab === "cloud" ? "雲端" : "地端"}（${n}）`;
    });
    document.getElementById("providers").innerHTML = list.map((p) => `
      <section class="card">
        <h3 class="prov-head"><span class="prov-ico ${p.scope}">${svg(ICON[p.scope] || ICON.cloud, 20)}</span>${esc(p.name)}</h3>
        ${p.editable
          ? `<div class="actions" style="margin:0;gap:6px"><input class="mono" data-url="${esc(p.id)}" value="${esc(p.base_url)}" placeholder="服務網址" style="flex:1;font-size:12px">
             <button class="ghost small" data-save="${esc(p.id)}">儲存</button></div>
             ${p.key_editable ? `<div class="actions" style="margin:6px 0 0;gap:6px"><input class="mono" data-key="${esc(p.id)}" type="password" autocomplete="off"
               placeholder="${p.key_state === "configured" ? "金鑰已設定（留空＝不更換）" : "貼上 API 金鑰"}" style="flex:1;font-size:12px"></div>` : ""}`
          : `<div class="muted mono" style="font-size:11.5px;word-break:break-all">${esc(p.base_url)}</div>`}
        ${p.extra && p.extra.anthropic ? `<div class="muted" style="font-size:11.5px;margin-top:4px">Anthropic 相容：<span class="mono">${esc(p.extra.anthropic)}</span></div>` : ""}
        <div style="margin:10px 0"><span class="chip ${p.key_state === "missing" ? "err" : "ok"}">金鑰 ${{ configured: "已設定", optional: "免金鑰", missing: "未設定" }[p.key_state] || "未設定"}</span>
        <span class="mono muted" style="font-size:11.5px">${esc(p.key_mask)}</span></div>
        <table class="map"><tr><th>模型</th><th>類型</th><th>狀態</th><th>對應步驟</th></tr>
          ${!p.models.length && p.kind === "comfyui" ? `<tr><td colspan="4" class="muted" style="font-size:12px">尚未匯入 workflow。ComfyUI 的模型要搭配 workflow 才能生成，請由下方匯入。</td></tr>` : ""}
          ${p.models.map((m) => `<tr><td class="mono">${esc(m.id)}</td><td class="kind">${kindIcon(m.kind)} ${esc(KIND[m.kind] || m.kind)}</td>
            <td>${badge(m.status)}${m.note ? `<div class="muted" style="font-size:11px;margin-top:2px">${esc(m.note)}</div>` : ""}</td>
            <td>${stepChips(p.id, m)}</td></tr>`).join("")}
        </table>
        ${p.kind === "comfyui" ? `
        <details data-installed style="margin-top:10px"><summary class="muted" style="cursor:pointer;font-size:12px">ComfyUI 已安裝模型（載入中…）</summary><div class="mono" style="font-size:11px;margin-top:6px"></div></details>
        <form data-import style="margin-top:12px;display:grid;gap:6px">
          <div class="muted" style="font-size:11.5px">匯入 workflow：ComfyUI 選單 Workflow → Export (API) 的 JSON</div>
          <input type="file" name="file" accept=".json" required>
          <div class="actions" style="margin:0;gap:6px">
            <input name="id" placeholder="模型 ID，例 flux-dev" required style="flex:1">
            <select name="kind"><option value="image">圖片</option><option value="video">影片</option></select>
            <button class="small">匯入</button>
          </div>
          <input name="note" placeholder="備註（選填）">
        </form>` : ""}
        <div class="actions"><button class="ghost small" data-test="${esc(p.id)}">${p.scope === "local" ? "測試服務連線" : "測試文字連線"}</button>
          ${p.custom ? `<button class="ghost small" data-del="${esc(p.id)}" style="color:var(--error,#c0392b)">刪除</button>` : ""}</div>
        <div class="muted mono" id="t-${esc(p.id)}" style="margin-top:8px;font-size:11.5px;white-space:pre-wrap"></div>
      </section>`).join("") || '<div class="muted">此分類沒有 Provider</div>';

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
      if (!confirm(`確定刪除「${cfg.providers.find(p => p.id === pid)?.name ?? pid}」？其模型會從流程中移除（步驟自動回落預設）。`)) return;
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

    document.querySelectorAll("[data-test]").forEach((btn) => btn.addEventListener("click", async () => {
      const pid = btn.dataset.test;
      const out = document.getElementById(`t-${pid}`);
      btn.disabled = true; out.textContent = "測試中…";
      try {
        const res = await (await fetch("/api/config/test", {
          method: "POST",
          headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
          body: JSON.stringify({ provider: pid }),
        })).json();
        out.textContent = res.ok
          ? `✓ ${res.model} 回覆「${res.reply ?? "ok"}」於 ${res.seconds ?? "—"}s`
          : `✗ ${res.error || "失敗"}`;
      } catch (err) { out.textContent = `✗ ${err.message}`; }
      finally { btn.disabled = false; }
    }));
  }

  function render() {
    renderFlow();
    renderProviders();
  }

  document.querySelectorAll("#tabs .tab").forEach((b) => b.addEventListener("click", () => {
    tab = b.dataset.tab; history.replaceState(null, "", `#${tab}`); renderProviders();
  }));

  fetch("/api/config").then((r) => r.json()).then((data) => { cfg = data; render(); });

  // ---- 新增供應商 ----
  const addBtn = document.createElement("button");
  addBtn.className = "ghost small"; addBtn.type = "button";
  addBtn.textContent = "＋ 新增供應商";
  document.getElementById("tabs").appendChild(addBtn);

  addBtn.addEventListener("click", () => {
    const vs = VENDORS || [];
    const grouped = [];
    for (const v of vs) {
      const cat = CAT_LABEL[v.category] || "其他";
      let g = grouped.find((x) => x.cat === cat);
      if (!g) grouped.push(g = { cat, items: [] });
      g.items.push(v);
    }
    const vendorOpts = grouped.map((g) =>
      `<optgroup label="${g.cat}">${g.items.map((v) =>
        `<option value="${esc(v.url)}" data-name="${esc(v.name)}" data-cat="${esc(v.category)}" data-own="${v.own_api ? 1 : 0}">${esc(v.name)}</option>`).join("")}</optgroup>`).join("");
    const defaultUrl = (vs.find((v) => v.name === "DeepSeek") ?? vs[0] ?? { url: "" }).url;
    const d = document.createElement("div");
    d.className = "vx-mask";
    d.innerHTML = `<div class="vx" style="width:min(520px,94vw);padding:0 0 4px">
      <div style="padding:16px 18px 4px"><h3 style="margin:0">新增供應商</h3>
      <p class="muted" style="font-size:12px;margin:6px 0 0">目錄照 CC Switch 模板（含影音模型分類）。選大廠自動填網址；按「驗證並新增」時系統先驗連通、抓模型清單，存檔後自動測試連結。</p></div>
      <div style="padding:8px 18px;display:grid;gap:10px">
        <label class="muted" style="font-size:11.5px">供應商
          <select id="ap-vendor" style="width:100%">
            ${vendorOpts}
            <option value="">自訂網址…</option>
          </select></label>
        <label class="muted" style="font-size:11.5px">顯示名稱（留空＝用供應商名）
          <input id="ap-name" style="width:100%"></label>
        <label class="muted" style="font-size:11.5px">請求位址
          <input id="ap-url" class="mono" style="width:100%" value="${esc(defaultUrl)}"></label>
        <label class="muted" style="font-size:11.5px">API 金鑰
          <input id="ap-key" class="mono" type="password" autocomplete="off" style="width:100%"></label>
        <label class="muted" style="font-size:11.5px">分類
          <select id="ap-scope" style="width:100%"><option value="cloud">雲端</option><option value="local">地端</option></select></label>
        <p class="muted mono" id="ap-out" style="font-size:11.5px;margin:0;white-space:pre-wrap"></p>
      </div>
      <div class="vx-foot"><button class="ghost small" id="ap-cancel">取消</button><button class="small" id="ap-ok">驗證並新增</button></div>
    </div>`;
    document.body.appendChild(d);
    d.querySelector("#ap-vendor").addEventListener("change", (e) => {
      const opt = e.target.selectedOptions[0];
      if (e.target.value) {
        d.querySelector("#ap-url").value = e.target.value;
        if (!d.querySelector("#ap-name").value) d.querySelector("#ap-name").value = opt.dataset.name ?? "";
      }
      d.querySelector("#ap-out").textContent = opt.dataset.own === "1"
        ? "⚠ 此廠商為自有 API（非 OpenAI 相容），後端適配：架構中；仍可先建卡片。"
        : "";
    });
    d.querySelector("#ap-cancel").addEventListener("click", () => d.remove());
    d.addEventListener("click", (e) => { if (e.target === d) d.remove(); });
    d.querySelector("#ap-ok").addEventListener("click", async () => {
      const out = d.querySelector("#ap-out");
      const payload = {
        name: d.querySelector("#ap-name").value,
        base_url: d.querySelector("#ap-url").value,
        api_key: d.querySelector("#ap-key").value,
        scope: d.querySelector("#ap-scope").value,
      };
      if (!payload.base_url.trim()) { out.textContent = "✗ 請填請求位址"; return; }
      out.textContent = "驗證連通中…"; d.querySelector("#ap-ok").disabled = true;
      try {
        const res = await (await fetch("/api/providers", {
          method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
          body: JSON.stringify(payload),
        })).json();
        if (!res.ok) { out.textContent = `✗ ${res.error || "新增失敗"}`; d.querySelector("#ap-ok").disabled = false; return; }
        d.remove();
        tab = payload.scope; location.hash = `#${tab}`;
        cfg = await (await fetch("/api/config")).json(); render();
        if (res.probe?.ok) toast(`✓ 已新增；${res.probe.reply?.slice(0, 60) ?? "連線正常"}`);
        else toast(`已新增；但連線測試未過：${res.probe?.error?.slice(0, 60) ?? res.probe_err ?? "未知"}`, true);
      } catch (err) { out.textContent = `✗ ${err.message}`; d.querySelector("#ap-ok").disabled = false; }
    });
  });
})();

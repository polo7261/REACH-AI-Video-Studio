(() => {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const STATUS = { ok: ["ok", "已實測"], quota: ["warn", "額度上限"], untested: ["", "未實測"], license: ["err", "條款限制"] };
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
        <div class="muted mono" style="font-size:11.5px;word-break:break-all">${esc(p.base_url)}</div>
        ${p.extra && p.extra.anthropic ? `<div class="muted" style="font-size:11.5px;margin-top:4px">Anthropic 相容：<span class="mono">${esc(p.extra.anthropic)}</span></div>` : ""}
        <div style="margin:10px 0"><span class="chip ${p.key_state === "configured" ? "ok" : "err"}">金鑰 ${p.key_state === "configured" ? "已設定" : "未設定"}</span>
        <span class="mono muted" style="font-size:11.5px">${esc(p.key_mask)}</span></div>
        <table class="map"><tr><th>模型</th><th>類型</th><th>狀態</th><th>對應步驟</th></tr>
          ${p.models.map((m) => `<tr><td class="mono">${esc(m.id)}</td><td class="kind">${kindIcon(m.kind)} ${esc(KIND[m.kind] || m.kind)}</td>
            <td>${badge(m.status)}${m.note ? `<div class="muted" style="font-size:11px;margin-top:2px">${esc(m.note)}</div>` : ""}</td>
            <td>${stepChips(p.id, m)}</td></tr>`).join("")}
        </table>
        <div class="actions"><button class="ghost small" data-test="${esc(p.id)}">${p.scope === "local" ? "測試服務連線" : "測試文字連線"}</button></div>
        <div class="muted mono" id="t-${esc(p.id)}" style="margin-top:8px;font-size:11.5px"></div>
      </section>`).join("") || '<div class="muted">此分類沒有 Provider</div>';

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
    document.getElementById("raw").textContent = JSON.stringify(cfg, null, 2);
    renderFlow();
    renderProviders();
  }

  document.querySelectorAll("#tabs .tab").forEach((b) => b.addEventListener("click", () => {
    tab = b.dataset.tab; history.replaceState(null, "", `#${tab}`); renderProviders();
  }));

  fetch("/api/config").then((r) => r.json()).then((data) => { cfg = data; render(); })
    .catch((err) => { document.getElementById("raw").textContent = String(err); });
})();

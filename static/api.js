(() => {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const badge = (st) => {
    const map = { ok: ["ok", "已實測"], quota: ["warn", "額度上限"], untested: ["", "未打通"] };
    const [cls, label] = map[st] || ["", st];
    return `<span class="chip ${cls}">${label}</span>`;
  };

  async function load() {
    const cfg = await (await fetch("/api/config")).json();
    document.getElementById("raw").textContent = JSON.stringify(cfg, null, 2);
    document.getElementById("providers").innerHTML = cfg.providers.map((p) => `
      <section class="card">
        <h3>${esc(p.name)}</h3>
        <div class="muted mono" style="font-size:11.5px;word-break:break-all">${esc(p.base_url)}</div>
        ${p.extra && p.extra.anthropic ? `<div class="muted" style="font-size:11.5px;margin-top:4px">Anthropic 相容：<span class="mono">${esc(p.extra.anthropic)}</span></div>` : ""}
        <div style="margin:10px 0"><span class="chip ${p.key_state === "configured" ? "ok" : "err"}">金鑰 ${p.key_state === "configured" ? "已設定" : "未設定"}</span>
        <span class="mono muted" style="font-size:11.5px">${esc(p.key_mask)}</span></div>
        <table class="map"><tr><th>模型</th><th>類型</th><th>狀態</th></tr>
          ${p.models.map((m) => `<tr><td class="mono">${esc(m.id)}</td><td>${esc(m.kind)}</td>
            <td>${badge(m.status)}${m.note ? `<div class="muted" style="font-size:11px;margin-top:2px">${esc(m.note)}</div>` : ""}</td></tr>`).join("")}
        </table>
        <div class="actions"><button class="ghost small" data-test="${esc(p.id)}">測試文字連線</button></div>
        <div class="muted mono" id="t-${esc(p.id)}" style="margin-top:8px;font-size:11.5px"></div>
      </section>`).join("");

    document.querySelectorAll("[data-test]").forEach((btn) => {
      btn.addEventListener("click", async () => {
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
            ? `✓ ${res.model} 回覆「${res.reply}」於 ${res.seconds}s`
            : `✗ ${res.error || "失敗"}`;
        } catch (err) { out.textContent = `✗ ${err.message}`; }
        finally { btn.disabled = false; }
      });
    });
  }
  load().catch((err) => { document.getElementById("raw").textContent = String(err); });
})();

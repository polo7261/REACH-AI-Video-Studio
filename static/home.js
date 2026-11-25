(() => {
  const $ = (s) => document.querySelector(s);
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const t = (k) => window.REACH.t(k);
  const STEP_KEY = { script: "tool.script", character: "tool.character", keyframe: "tool.keyframe", video: "tool.video", tts: "tool.tts" };
  let cfg = null, projects = [];

  function toast(msg, isErr = false) {
    const el = document.createElement("div");
    el.className = "toast" + (isErr ? " err" : ""); el.textContent = msg;
    document.body.appendChild(el); setTimeout(() => el.remove(), isErr ? 6000 : 3000);
  }

  async function start() {
    const idea = $("#hero-idea").value.trim();
    if (!idea) { toast(t("common.needIdea"), true); $("#hero-idea").focus(); return; }
    const btn = $("#hero-start"); btn.disabled = true;
    try {
      const res = await fetch("/api/projects", {
        method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
        body: JSON.stringify({ idea }),
      });
      const body = await res.json();
      if (!res.ok) throw new Error(body.error || `HTTP ${res.status}`);
      location.href = `/studio?pid=${encodeURIComponent(body.plan.id)}`;
    } catch (err) { toast(err.message, true); btn.disabled = false; }
  }

  function renderModels() {
    if (!cfg) return;
    $("#model-strip").innerHTML = cfg.steps.map((s) => {
      const r = cfg.routing[s.id];
      const p = cfg.providers.find((x) => x.id === r.provider) || {};
      return `<a class="model-chip" href="/api-page">
        <span class="muted">${esc(t(STEP_KEY[s.id] || s.label))}</span>
        <b class="mono">${esc(r.model)}</b>
        <span class="chip ${p.scope === "local" ? "warn" : "use"}">${p.scope === "local" ? "LOCAL" : "CLOUD"}</span></a>`;
    }).join("");
  }

  function renderRecent() {
    const box = $("#recent");
    if (!projects.length) { box.innerHTML = `<div class="muted">${esc(t("home.empty"))}</div>`; return; }
    box.innerHTML = projects.slice(0, 8).map((p) => `
      <a class="rcard" href="/studio?pid=${encodeURIComponent(p.id)}">
        <span class="rthumb">${p.cover ? `<img src="/media/${esc(p.id)}/${esc(p.cover)}" alt="" loading="lazy">`
          : '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3z"/></svg>'}</span>
        <span class="rmeta"><b>${esc(p.title)}</b>
          <span class="muted">${esc((p.created_at || "").slice(0, 10))} · ${p.shots} 鏡 · ${p.images} 圖 / ${p.videos} 片</span></span>
      </a>`).join("");
  }

  $("#hero-start").addEventListener("click", start);
  $("#hero-idea").addEventListener("keydown", (e) => { if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) start(); });
  window.REACH.onLang(() => { renderModels(); renderRecent(); });

  fetch("/api/config").then((r) => r.json()).then((d) => { cfg = d; renderModels(); }).catch(() => { $("#model-strip").innerHTML = ""; });
  fetch("/api/projects").then((r) => r.json()).then((d) => { projects = d.projects || []; renderRecent(); }).catch(() => { $("#recent").innerHTML = ""; });
})();

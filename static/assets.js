(() => {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  let items = [], filter = "all";
  function render() {
    const box = document.getElementById("assets");
    const list = items.filter((a) => filter === "all" || a.type === filter);
    if (!list.length) { box.innerHTML = `<div class="muted">${esc(window.REACH.t("assets.empty"))}</div>`; return; }
    box.innerHTML = list.map((a) => `
      <figure class="asset">
        <div class="athumb">${a.type === "image" ? `<img src="${esc(a.url)}" loading="lazy" alt="">`
          : a.type === "video" ? `<video src="${esc(a.url)}" muted preload="metadata" controls></video>`
          : `<audio src="${esc(a.url)}" controls preload="none"></audio>`}</div>
        <figcaption><a href="/studio?pid=${encodeURIComponent(a.project_id)}">${esc(a.project_title)}</a>
          <span class="muted mono">${esc(a.name)} · ${(a.size / 1048576).toFixed(1)} MB</span></figcaption>
      </figure>`).join("");
  }
  document.querySelectorAll("#asset-tabs .tab").forEach((b) => b.addEventListener("click", () => {
    filter = b.dataset.f;
    document.querySelectorAll("#asset-tabs .tab").forEach((x) => x.classList.toggle("active", x === b));
    render();
  }));
  window.REACH.onLang(render);
  fetch("/api/assets").then((r) => r.json()).then((d) => { items = d.assets || []; render(); })
    .catch((err) => { document.getElementById("assets").textContent = String(err); });
})();

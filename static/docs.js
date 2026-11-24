(() => {
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // 極簡 Markdown：標題、清單、程式碼、表格、粗體、行內碼、連結、引用
  function mdToHtml(src) {
    const lines = src.replace(/\r/g, "").split("\n");
    let out = [];
    let inCode = false, codeBuf = [], inList = false, tableBuf = [];

    const flushTable = () => {
      if (!tableBuf.length) return;
      const rows = tableBuf.filter((r) => !/^\|[\s:\-|]+\|$/.test(r.trim()));
      out.push("<table>" + rows.map((r, i) => {
        const cells = r.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
        const tag = i === 0 ? "th" : "td";
        return "<tr>" + cells.map((c) => `<${tag}>${inline(c)}</${tag}>`).join("") + "</tr>";
      }).join("") + "</table>");
      tableBuf = [];
    };
    const inline = (t) => esc(t)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');

    for (const raw of lines) {
      const line = raw;
      if (line.trim().startsWith("```")) {
        if (!inCode) { inCode = true; codeBuf = []; }
        else { inCode = false; out.push(`<pre><code>${esc(codeBuf.join("\n"))}</code></pre>`); }
        continue;
      }
      if (inCode) { codeBuf.push(line); continue; }
      if (/^\s*\|.*\|\s*$/.test(line)) { tableBuf.push(line); continue; }
      flushTable();
      if (/^#{1,6}\s+/.test(line)) {
        const level = line.match(/^#+/)[0].length;
        out.push(`<h${level}>${inline(line.replace(/^#+\s+/, ""))}</h${level}>`);
      } else if (/^\s*[-*]\s+/.test(line)) {
        out.push(`<li>${inline(line.replace(/^\s*[-*]\s+/, ""))}</li>`);
      } else if (/^\s*>\s?/.test(line)) {
        out.push(`<blockquote>${inline(line.replace(/^\s*>\s?/, ""))}</blockquote>`);
      } else if (/^---+$/.test(line.trim())) {
        out.push("<hr>");
      } else if (line.trim() === "") {
        out.push("");
      } else {
        out.push(`<p>${inline(line)}</p>`);
      }
    }
    flushTable();
    return out.join("\n");
  }

  async function open(slug) {
    document.querySelectorAll("#doclist .pitem").forEach((el) => el.classList.toggle("active", el.dataset.slug === slug));
    const title = document.getElementById("doc-title");
    const body = document.getElementById("doc-body");
    body.innerHTML = '<div class="muted">載入中…</div>';
    try {
      const data = await (await fetch(`/api/docs/${slug}`)).json();
      title.textContent = slug;
      body.innerHTML = mdToHtml(data.markdown || "");
    } catch (err) { body.innerHTML = `<div class="muted">讀取失敗：${esc(err.message)}</div>`; }
  }

  document.querySelectorAll("#doclist .pitem").forEach((el) => el.addEventListener("click", () => open(el.dataset.slug)));
  const first = document.querySelector("#doclist .pitem");
  if (first) open(first.dataset.slug);
})();

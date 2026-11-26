(() => {
  const $ = (sel) => document.querySelector(sel);
  const state = { pid: null, plan: null, polls: new Set(), cfg: null };
  const PROJECT_STEPS = ["script", "character", "keyframe", "tts"];

  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  function toast(msg, isErr = false) {
    const el = document.createElement("div");
    el.className = "toast" + (isErr ? " err" : "");
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), isErr ? 7000 : 3500);
  }

  async function api(path, options = {}) {
    const res = await fetch(path, {
      headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
      ...options,
    });
    let body = null;
    try { body = await res.json(); } catch { body = null; }
    if (!res.ok) throw new Error((body && body.error) || `HTTP ${res.status}`);
    return body;
  }

  const statusChip = (s) => {
    const map = { planned: "", image_ready: "warn", video_queued: "warn", video_ready: "ok" };
    return `<span class="chip ${map[s] || ""}">${esc(s)}</span>`;
  };

  // ------------------------------------------------------------- projects
  async function loadProjects() {
    const data = await api("/api/projects");
    const box = $("#projects");
    if (!data.projects.length) { box.innerHTML = '<div class="muted">尚無專案</div>'; }
    else {
      box.innerHTML = data.projects.map((p) => `
        <div class="pitem ${p.id === state.pid ? "active" : ""}" data-pid="${p.id}">
          <div><b>${esc(p.title)}</b><span>${esc(p.style)} · ${esc(p.ratio)} · ${p.duration_seconds}s</span></div>
          <span>${p.images} 圖 / ${p.videos} 片</span>
        </div>`).join("");
      box.querySelectorAll(".pitem").forEach((el) => el.addEventListener("click", () => openProject(el.dataset.pid)));
    }
    renderJobs(data.jobs || []);
  }

  function renderJobs(jobs) {
    const box = $("#jobs");
    if (!box) return;
    const cnt = document.getElementById("jobs-count");
    if (cnt) cnt.textContent = jobs.length ? `（${jobs.length}）` : "";
    if (!jobs.length) { box.innerHTML = '<div class="muted">—</div>'; return; }
    box.innerHTML = `<table class="map"><tr><th>任務</th><th>鏡頭</th><th>模型</th><th>狀態</th></tr>` +
      jobs.map((j) => `<tr><td class="mono">${esc(j.id)}</td><td>${esc(j.shot_id)}</td><td class="mono">${esc(j.model)}</td>
        <td>${j.state === "succeeded" ? '<span class="chip ok">succeeded</span>' : j.state === "error" ? `<span class="chip err">error</span> <span class="muted">${esc(j.message || "")}</span>` : `<span class="chip warn">${esc(j.state)}</span>`}</td></tr>`).join("") +
      "</table>";
  }

  async function createProject() {
    const payload = {
      title: $("#f-title").value.trim(),
      idea: $("#f-idea").value.trim(),
      style: $("#f-style").value.trim(),
      duration: Number($("#f-duration").value || 24),
      ratio: $("#f-ratio").value,
      character: $("#f-character").value.trim(),
      location: $("#f-location").value.trim(),
    };
    if (!payload.idea) { toast("請先輸入一句話故事", true); return; }
    const btn = $("#btn-create");
    btn.disabled = true;
    try {
      const data = await api("/api/projects", { method: "POST", body: JSON.stringify(payload) });
      $("#f-idea").value = "";
      $("#f-title").value = "";
      toast(`已建立：${data.plan.title}（${data.plan.shots.length} 鏡）`);
      await loadProjects();
      await openProject(data.plan.id);
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; }
  }

  async function openProject(pid) {
    try {
      const data = await api(`/api/projects/${pid}`);
      state.pid = pid;
      state.plan = data.plan;
      renderDetail(data.plan, data.timeline);
      document.querySelectorAll("#projects .pitem").forEach((el) => el.classList.toggle("active", el.dataset.pid === pid));
      $("#detail").style.display = "";
      $("#st-empty").hidden = true;
      $("#narration-text").value = data.plan.narration || "";
      renderUploads();
      renderFlow(data.plan);
      renderModelBar(data.plan);
    } catch (err) { toast(err.message, true); }
  }

  // ------------------------------------------------------------- 專案模型選擇
  async function renderModelBar(plan) {
    const box = $("#model-bar");
    try {
      if (!state.cfg) state.cfg = await api("/api/config");
    } catch (err) { box.innerHTML = `<div class="muted">模型清單讀取失敗：${esc(err.message)}</div>`; return; }
    const cfg = state.cfg;
    const own = plan.models || {};
    const scopeName = { cloud: "雲端", local: "地端" };
    box.innerHTML = cfg.steps.filter((s) => PROJECT_STEPS.includes(s.id)).map((s) => {
      const g = cfg.routing[s.id];
      const cur = own[s.id] ? `${own[s.id].provider}|${own[s.id].model}` : "";
      const groups = ["cloud", "local"].map((scope) => {
        const opts = cfg.providers.filter((p) => p.scope === scope).flatMap((p) =>
          p.models.filter((m) => m.kind === s.kind && m.status !== "license").map((m) => {
            const v = `${p.id}|${m.id}`;
            const mark = m.status === "ok" ? "✓ " : m.status === "quota" ? "⚠ " : "· ";
            return `<option value="${esc(v)}" ${v === cur ? "selected" : ""}>${mark}${esc(m.id)}（${esc(p.name)}）</option>`;
          }));
        return opts.length ? `<optgroup label="${scopeName[scope]}">${opts.join("")}</optgroup>` : "";
      }).join("");
      return `<div><label>${esc(s.label)}</label>
        <select data-model-step="${esc(s.id)}">
          <option value="" ${cur ? "" : "selected"}>沿用全域（${esc(g.model)}）</option>${groups}
        </select></div>`;
    }).join("");
    box.querySelectorAll("[data-model-step]").forEach((sel) => sel.addEventListener("change", async () => {
      const [provider = "", model = ""] = sel.value ? sel.value.split("|") : [];
      try {
        const res = await api(`/api/projects/${plan.id}/models`, { method: "PUT",
          body: JSON.stringify({ step: sel.dataset.modelStep, provider, model }) });
        plan.models = res.models;
        toast(model ? `本專案改用：${model}` : "已改回沿用全域設定");
      } catch (err) { toast(err.message, true); }
    }));
  }

  async function renderFlow(plan) {
    const box = $("#cast");
    const cast = plan.cast || [];
    if (!cast.length) { box.innerHTML = '<div class="muted">尚無角色（先建立角色設定圖）</div>'; return; }
    box.innerHTML = cast.map((c) => `
      <div style="display:flex;gap:10px;align-items:flex-start;margin:8px 0">
        <img src="/media/${plan.id}/${c.sheet}" style="width:110px;border-radius:6px;border:1px solid var(--line)">
        <div style="flex:1">
          <b>${esc(c.id)} ${esc(c.name)}</b>
          <span class="chip ${c.status === "approved" ? "ok" : "warn"}">${esc(c.status)}</span>
          <div class="muted" style="font-size:11.5px">${esc(c.description)}</div>
          <div class="actions" style="margin-top:6px">
            <button class="ghost small" data-approve="${c.id}">${c.status === "approved" ? "已確認" : "確認角色"}</button>
            <button class="ghost small" data-regen="${c.id}">重生</button>
          </div>
        </div>
      </div>`).join("");
    box.querySelectorAll("[data-approve]").forEach((b) => b.addEventListener("click", async () => {
      try { await api(`/api/projects/${plan.id}/characters/${b.dataset.approve}/approve`, { method: "POST", body: "{}" }); toast("角色已確認"); await openProject(plan.id); }
      catch (err) { toast(err.message, true); }
    }));
    box.querySelectorAll("[data-regen]").forEach((b) => b.addEventListener("click", async () => {
      b.disabled = true; b.textContent = "重生中…";
      try { await api(`/api/projects/${plan.id}/characters/${b.dataset.regen}/regenerate`, { method: "POST", body: "{}" }); toast("角色圖已重生"); await openProject(plan.id); }
      catch (err) { toast(err.message, true); b.disabled = false; b.textContent = "重生"; }
    }));
  }

  async function addCharacter() {
    const desc = $("#char-desc").value.trim();
    if (!desc) { toast("請填角色描述", true); return; }
    const btn = $("#btn-char"); btn.disabled = true; btn.textContent = "生成中…";
    try {
      await api(`/api/projects/${state.pid}/characters`, { method: "POST",
        body: JSON.stringify({ name: $("#char-name").value.trim() || "角色", description: desc }) });
      $("#char-desc").value = ""; $("#char-name").value = "";
      toast("角色設定圖已生成，確認後再產劇本");
      await openProject(state.pid);
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; btn.textContent = "生成角色設定圖"; }
  }

  async function expandScript() {
    const btn = $("#btn-script"); btn.disabled = true; btn.textContent = "編寫中…";
    try {
      const data = await api(`/api/projects/${state.pid}/script/expand`, { method: "POST", body: "{}" });
      toast(`劇本與 ${data.plan.shots.length} 鏡分鏡完成（${data.source}）`);
      await openProject(state.pid);
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; btn.textContent = "② 生成劇本與分鏡"; }
  }

  function renderDetail(plan, timeline) {
    $("#d-title").textContent = plan.title;
    $("#d-meta").textContent = `${plan.style} · ${plan.ratio} · ${plan.duration_seconds}s · ${plan.shots.length} 鏡`;
    const ready = plan.shots.filter((s) => s.status === "video_ready").length;
    $("#d-status").textContent = `完成 ${ready}/${plan.shots.length} 鏡`;
    $("#timeline").innerHTML = timeline.map((t) => `<div class="${esc(t.status)}" title="${esc(t.shot_id)} · ${esc(t.camera)}"></div>`).join("");

    const cams = ["locked", "pan", "tilt", "dolly_in", "dolly_out", "tracking", "crane", "orbit_180", "orbit_360", "bullet_time", "dolly_zoom", "whip_pan", "pov", "handheld", "drone"];
    $("#shots").innerHTML = plan.shots.map((s) => `
      <article class="shot" data-sid="${s.id}">
        <div class="head"><span>${esc(s.id)} · ${esc(s.beat)} · ${esc(s.camera_zh)}</span>${statusChip(s.status)}</div>
        <div class="body">
          <div class="thumb" data-thumb>${s.video
            ? `<video src="/media/${plan.id}/${esc(s.video)}" controls muted loop></video>`
            : s.image ? `<img src="/media/${plan.id}/${esc(s.image)}" alt="">` : `<span>${s.framing || "no frame"}</span>`}</div>
          <select data-cam>${cams.map((c) => `<option value="${c}" ${c === s.camera ? "selected" : ""}>${c}${c === s.camera ? " · " + esc(s.camera_zh) : ""}</option>`).join("")}</select>
          <textarea data-prompt rows="4">${esc(s.positive_prompt)}</textarea>
          <div class="actions" style="margin-top:0">
            <button class="ghost small" data-act="img">生成關鍵影格</button>
            <select data-provider style="max-width:150px">
              ${[["minimax", "MiniMax H3 ✅"], ["volcano", "火山 Seedance（待開通）"], ["local-comfy", "地端 ComfyUI（240）"], ["local-ltx", "地端 LTXV（219）"], ["local-wan", "地端 Wan（慢）"]]
                .map(([v, label]) => `<option value="${v}" ${(s.video_provider || "volcano") === v ? "selected" : ""}>${label}</option>`).join("")}
            </select>
            <button class="small" data-act="vid">生成影片</button>
          </div>
        </div>
      </article>`).join("");

    document.querySelectorAll(".shot").forEach((card) => {
      const sid = card.dataset.sid;
      card.querySelector("[data-cam]").addEventListener("change", async (e) => {
        try { await api(`/api/projects/${plan.id}/shots/${sid}`, { method: "PATCH", body: JSON.stringify({ camera: e.target.value }) }); await openProject(plan.id); }
        catch (err) { toast(err.message, true); }
      });
      card.querySelector("[data-prompt]").addEventListener("change", async (e) => {
        try { await api(`/api/projects/${plan.id}/shots/${sid}`, { method: "PATCH", body: JSON.stringify({ positive_prompt: e.target.value }) }); toast("Prompt 已儲存"); }
        catch (err) { toast(err.message, true); }
      });
      card.querySelector('[data-act="img"]').addEventListener("click", (e) => genImage(sid, e.target));
      card.querySelector("[data-provider]").addEventListener("change", async (e) => {
        try {
          await api(`/api/projects/${plan.id}/shots/${sid}`, { method: "PATCH", body: JSON.stringify({ video_provider: e.target.value }) });
          toast(`已記住 ${sid} 的影片來源：${e.target.value}`);
        } catch (err) { toast(err.message, true); }
      });
      card.querySelector('[data-act="vid"]').addEventListener("click", (e) =>
        genVideo(sid, e.target, card.querySelector("[data-provider]").value));
    });
  }

  async function genImage(sid, btn) {
    btn.disabled = true; btn.textContent = "生成中…";
    try {
      const data = await api(`/api/projects/${state.pid}/shots/${sid}/image`, { method: "POST", body: JSON.stringify({}) });
      toast(`關鍵影格完成（${data.provider}/${data.model}）`);
      await openProject(state.pid);
    } catch (err) { toast(err.message, true); btn.disabled = false; btn.textContent = "生成關鍵影格"; }
  }

  async function genVideo(sid, btn, provider = "volcano") {
    btn.disabled = true; btn.textContent = "送出中…";
    try {
      const data = await api(`/api/projects/${state.pid}/shots/${sid}/video`, { method: "POST", body: JSON.stringify({ provider }) });
      toast(`影片任務已建立：${data.job.task_id}`);
      await openProject(state.pid);
      pollJob(data.job.id);
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; btn.textContent = "生成影片"; }
  }

  async function pollJob(jid) {
    if (state.polls.has(jid)) return;
    state.polls.add(jid);
    for (let i = 0; i < 90; i++) {
      await new Promise((r) => setTimeout(r, 5000));
      try {
        const { job } = await api(`/api/jobs/${jid}`);
        if (job.state === "succeeded") { toast(`影片完成：${job.shot_id}`); await openProject(state.pid); await loadProjects(); state.polls.delete(jid); return; }
        if (job.state === "error" || job.state === "failed") { toast(`影片失敗：${job.message || job.state}`, true); state.polls.delete(jid); return; }
      } catch { /* keep polling */ }
    }
    state.polls.delete(jid);
  }

  async function tts() {
    const btn = $("#btn-tts");
    btn.disabled = true; btn.textContent = "合成中…";
    try {
      const text = $("#narration-text").value.trim();
      await api(`/api/projects/${state.pid}/narration`, { method: "POST", body: JSON.stringify({ text }) });
      const data = await api(`/api/projects/${state.pid}/tts`, { method: "POST", body: JSON.stringify({ text, voice: $("#tts-voice").value }) });
      $("#tts-out").innerHTML = `<audio controls src="${data.audio_url}" style="width:100%"></audio>`;
      toast(`配音完成（${(data.bytes / 1024).toFixed(0)} KB）`);
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; btn.textContent = "生成配音"; }
  }

  async function aiScript() {
    const btn = $("#btn-ai-script");
    btn.disabled = true; btn.textContent = "重寫中…";
    try {
      const data = await api(`/api/projects/${state.pid}/script`, { method: "POST", body: JSON.stringify({}) });
      toast(`分鏡已由 ${data.source} 重寫`);
      await openProject(state.pid);
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; btn.textContent = "AI 重寫分鏡"; }
  }

  async function uploadFiles() {
    const input = $("#upload-input");
    if (!input.files.length) { toast("請先選擇檔案", true); return; }
    const fd = new FormData();
    [...input.files].forEach((f) => fd.append("files", f));
    const btn = $("#btn-upload"); btn.disabled = true; btn.textContent = "上傳中…";
    try {
      const res = await fetch(`/api/projects/${state.pid}/uploads`, {
        method: "POST", body: fd, headers: { "X-Requested-With": "fetch" },
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`);
      toast(`已上傳 ${data.uploads.length} 個檔案`);
      input.value = "";
      await renderUploads();
    } catch (err) { toast(err.message, true); }
    finally { btn.disabled = false; btn.textContent = "上傳到專案"; }
  }

  async function renderUploads() {
    if (!state.pid) return;
    const box = $("#uploads");
    try {
      const data = await api(`/api/projects/${state.pid}/uploads`);
      const cnt = document.getElementById("uploads-count");
      if (cnt) cnt.textContent = data.uploads.length ? `（${data.uploads.length}）` : "";
      if (!data.uploads.length) { box.innerHTML = '<div class="muted">尚無上傳</div>'; return; }
      box.innerHTML = data.uploads.map((u) => {
        const ext = u.name.split(".").pop().toLowerCase();
        const media = ["mp4", "mov", "webm"].includes(ext) ? `<video src="${esc(u.url)}" muted preload="metadata"></video>`
          : ["png", "jpg", "jpeg", "webp"].includes(ext) ? `<img src="${esc(u.url)}" loading="lazy" alt="">`
          : '<span class="muted">♪ 音訊</span>';
        return `<a class="up-item" href="${esc(u.url)}" target="_blank" title="${esc(u.name)}">
          <span class="up-thumb">${media}</span>
          <span class="up-name">${esc(u.name)}</span><span class="muted up-size">${(u.size / 1048576).toFixed(1)} MB</span></a>`;
      }).join("");
    } catch { box.innerHTML = '<div class="muted">讀取失敗</div>'; }
  }

  $("#btn-create").addEventListener("click", createProject);
  $("#btn-new-toggle").addEventListener("click", () => {
    const f = $("#st-new"); f.hidden = !f.hidden;
    $("#btn-new-toggle").textContent = f.hidden ? "＋ 新專案" : "收合";
    if (!f.hidden) $("#f-idea").focus();
  });
  $("#st-tabs").addEventListener("click", (e) => {
    const b = e.target.closest("[data-pane]"); if (!b) return;
    document.querySelectorAll("#st-tabs .tab").forEach((x) => x.classList.toggle("active", x === b));
    document.querySelectorAll(".st-pane").forEach((p) => { p.hidden = p.dataset.pane !== b.dataset.pane; });
  });
  $("#btn-upload").addEventListener("click", uploadFiles);
  $("#btn-char").addEventListener("click", addCharacter);
  $("#btn-script").addEventListener("click", expandScript);
  $("#btn-tts").addEventListener("click", tts);
  $("#btn-ai-script").addEventListener("click", aiScript);
  loadProjects()
    .then(async () => {
      // 自動打開最新專案，避免只看到表單
      const want = new URLSearchParams(location.search).get("pid");
      if (want) { await openProject(want); return; }
      if (!state.pid) {
        const first = document.querySelector("#projects .pitem");
        if (first) await openProject(first.dataset.pid);
      }
    })
    .catch((err) => toast(err.message, true));
})();

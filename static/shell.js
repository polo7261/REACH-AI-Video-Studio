// 共用外框：亮／暗主題、語系（繁／簡／英）、設定選單
(() => {
  const DICT = {
    "zh-Hant": {
      "nav.home": "首頁", "nav.projects": "專案", "nav.assets": "素材庫", "nav.skills": "Skill 庫", "nav.create": "創作",
      "nav.workbench": "Skill 工作台", "nav.director": "AI 導演", "nav.canvas": "無限畫布", "nav.timeline": "時間軸剪輯", "tag.soon": "即將推出",
      "nav.settings": "設定", "nav.api": "API 與網址", "nav.docs": "技術文件",
      "nav.plugins": "插件", "nav.pluginBlender": "Blender 插件", "nav.pluginLibtv": "LibTV Plugin", "tag.external": "外部", "tag.download": "下載",
      "plugins.title": "Blender 插件下載", "plugins.sub": "在 Blender 內完成白模影片，一鍵上傳到 LibTV 生成成片。選擇你的作業系統版本（目前 0.1.26）。",
      "plugins.mac": "macOS 版", "plugins.win": "Windows 版（x64）",
      "plugins.nolinux": "官方目前未提供 Linux 版。安裝方式請參考安裝指南。",
      "plugins.auto": "下載即自動安裝（一鍵腳本）", "plugins.autoHint": "下載腳本後執行：它會自己找 zip 與 Blender，安裝、啟用並驗證。",
      "theme.toLight": "切換為亮色", "theme.toDark": "切換為暗色",
      "home.heroTitle": "一句話，開始一部片", "home.heroPh": "例：一名少女在雨夜的霓虹街道上追逐一枚飄走的紙鶴",
      "home.start": "開始創作", "home.tools": "創作工具", "home.models": "目前使用模型", "home.edit": "調整",
      "home.recent": "最近專案", "home.viewAll": "查看全部", "home.empty": "還沒有專案，從上方輸入一句話開始。",
      "tool.script": "劇本生成", "tool.character": "角色設計", "tool.keyframe": "分鏡出圖", "tool.video": "影片生成",
      "tool.tts": "旁白配音", "tool.edit": "智慧剪輯",
      "assets.title": "素材庫", "assets.sub": "所有專案產生與上傳的圖片、影片、音訊。",
      "assets.all": "全部", "assets.image": "圖片", "assets.video": "影片", "assets.audio": "音訊", "assets.empty": "尚無素材",
      "studio.title": "影片工作室", "api.title": "API 與網址", "docs.title": "技術文件",
      "common.creating": "建立中…", "common.needIdea": "請先輸入一句話故事",
    },
    "zh-Hans": {
      "nav.home": "首页", "nav.projects": "项目", "nav.assets": "素材库", "nav.skills": "Skill 库", "nav.create": "创作",
      "nav.workbench": "Skill 工作台", "nav.director": "AI 导演", "nav.canvas": "无限画布", "nav.timeline": "时间轴剪辑", "tag.soon": "即将推出",
      "nav.settings": "设置", "nav.api": "API 与网址", "nav.docs": "技术文档",
      "nav.plugins": "插件", "nav.pluginBlender": "Blender 插件", "nav.pluginLibtv": "LibTV Plugin", "tag.external": "外部", "tag.download": "下载",
      "plugins.title": "Blender 插件下载", "plugins.sub": "在 Blender 内完成白模视频，一键上传到 LibTV 生成成片。选择你的操作系统版本（目前 0.1.26）。",
      "plugins.mac": "macOS 版", "plugins.win": "Windows 版（x64）",
      "plugins.nolinux": "官方目前未提供 Linux 版。安装方式请参考安装指南。",
      "plugins.auto": "下载即自动安装（一键脚本）", "plugins.autoHint": "下载脚本后执行：它会自己找 zip 与 Blender，安装、启用并验证。",
      "theme.toLight": "切换为亮色", "theme.toDark": "切换为暗色",
      "home.heroTitle": "一句话，开始一部片", "home.heroPh": "例：一名少女在雨夜的霓虹街道上追逐一枚飘走的纸鹤",
      "home.start": "开始创作", "home.tools": "创作工具", "home.models": "当前使用模型", "home.edit": "调整",
      "home.recent": "最近项目", "home.viewAll": "查看全部", "home.empty": "还没有项目，从上方输入一句话开始。",
      "tool.script": "剧本生成", "tool.character": "角色设计", "tool.keyframe": "分镜出图", "tool.video": "视频生成",
      "tool.tts": "旁白配音", "tool.edit": "智能剪辑",
      "assets.title": "素材库", "assets.sub": "所有项目生成与上传的图片、视频、音频。",
      "assets.all": "全部", "assets.image": "图片", "assets.video": "视频", "assets.audio": "音频", "assets.empty": "暂无素材",
      "studio.title": "视频工作室", "api.title": "API 与网址", "docs.title": "技术文档",
      "common.creating": "创建中…", "common.needIdea": "请先输入一句话故事",
    },
    en: {
      "nav.home": "Home", "nav.projects": "Projects", "nav.assets": "Assets", "nav.skills": "Skills", "nav.create": "Create",
      "nav.workbench": "Skill Workbench", "nav.director": "AI Director", "nav.canvas": "Canvas", "nav.timeline": "Timeline", "tag.soon": "Soon",
      "nav.settings": "Settings", "nav.api": "APIs & Endpoints", "nav.docs": "Docs",
      "nav.plugins": "Plugins", "nav.pluginBlender": "Blender Plugin", "nav.pluginLibtv": "LibTV Plugin", "tag.external": "External", "tag.download": "Download",
      "plugins.title": "Blender Plugin Download", "plugins.sub": "Finish white-model videos in Blender, then send them to LibTV in one click. Pick your OS build (currently 0.1.26).",
      "plugins.mac": "macOS", "plugins.win": "Windows (x64)",
      "plugins.nolinux": "No official Linux build yet. See the install guide for setup.",
      "plugins.auto": "Auto-install after download (one-click script)", "plugins.autoHint": "Run the script after downloading: it locates the zip and Blender itself, installs, enables and verifies.",
      "theme.toLight": "Switch to light", "theme.toDark": "Switch to dark",
      "home.heroTitle": "One sentence. One film.", "home.heroPh": "e.g. A girl chases a drifting paper crane down a neon street on a rainy night",
      "home.start": "Create", "home.tools": "Tools", "home.models": "Models in use", "home.edit": "Edit",
      "home.recent": "Recent projects", "home.viewAll": "View all", "home.empty": "No projects yet — type an idea above to start.",
      "tool.script": "Script", "tool.character": "Characters", "tool.keyframe": "Keyframes", "tool.video": "Video",
      "tool.tts": "Voice-over", "tool.edit": "Smart edit",
      "assets.title": "Assets", "assets.sub": "Images, videos and audio generated or uploaded across all projects.",
      "assets.all": "All", "assets.image": "Images", "assets.video": "Videos", "assets.audio": "Audio", "assets.empty": "No assets yet",
      "studio.title": "Video Studio", "api.title": "APIs & Endpoints", "docs.title": "Docs",
      "common.creating": "Creating…", "common.needIdea": "Please enter a one-line story first",
    },
  };
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch { /* 無痕或受限環境 */ } },
  };
  const root = document.documentElement;
  let lang = DICT[store.get("reach.lang")] ? store.get("reach.lang") : "zh-Hant";
  const listeners = [];
  const t = (key) => (DICT[lang] && DICT[lang][key]) || DICT["zh-Hant"][key] || key;

  function applyLang() {
    root.lang = lang;
    document.querySelectorAll("[data-i18n]").forEach((el) => { el.textContent = t(el.dataset.i18n); });
    document.querySelectorAll("[data-i18n-ph]").forEach((el) => { el.placeholder = t(el.dataset.i18nPh); });
    document.querySelectorAll("#lang-menu [data-lang]").forEach((b) => {
      const on = b.dataset.lang === lang;
      b.classList.toggle("on", on); b.setAttribute("aria-checked", String(on));
    });
    syncThemeTitle();
    listeners.forEach((fn) => fn(lang));
  }

  function syncThemeTitle() {
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.title = t(root.dataset.theme === "light" ? "theme.toDark" : "theme.toLight");
  }

  document.getElementById("theme-toggle")?.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";
    store.set("reach.theme", root.dataset.theme);
    syncThemeTitle();
  });
  // 語系：圖示按鈕 → 簡約下拉選單
  const langBtn = document.getElementById("lang-btn");
  const langMenu = document.getElementById("lang-menu");
  const setMenu = (open) => { langMenu.hidden = !open; langBtn.setAttribute("aria-expanded", String(open)); };
  langBtn?.addEventListener("click", (e) => { e.stopPropagation(); setMenu(langMenu.hidden); });
  langMenu?.addEventListener("click", (e) => {
    const b = e.target.closest("[data-lang]");
    if (!b) return;
    lang = b.dataset.lang; store.set("reach.lang", lang); applyLang(); setMenu(false);
  });
  document.addEventListener("click", (e) => { if (langMenu && !langMenu.hidden && !e.target.closest(".menu-wrap")) setMenu(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && langMenu && !langMenu.hidden) { setMenu(false); langBtn.focus(); } });
  document.getElementById("settings-toggle")?.addEventListener("click", (e) => {
    const btn = e.currentTarget, menu = document.getElementById("settings-menu");
    const open = menu.hidden;
    menu.hidden = !open; btn.classList.toggle("open", open); btn.setAttribute("aria-expanded", String(open));
  });
  document.getElementById("plugins-toggle")?.addEventListener("click", (e) => {
    const btn = e.currentTarget, menu = document.getElementById("plugins-menu");
    const open = menu.hidden;
    menu.hidden = !open; btn.classList.toggle("open", open); btn.setAttribute("aria-expanded", String(open));
  });

  // 插件下載：Blender 插件 zip 改走 Google Drive 連結。
  // ★ 在此兩行貼上你的 Google Drive 連結即生效；未貼（仍是 PASTE_GD_LINK）時
  //   自動退回包內本機 zip /static/downloads/。
  const PLUGIN_DOWNLOADS = {
    macos: "PASTE_GD_LINK_HERE",   // ← blender-macos.zip 的 Google Drive 連結
    windows: "PASTE_GD_LINK_HERE", // ← blender-windows-x64.zip 的 Google Drive 連結
  };
  const isSet = (u) => u && !u.includes("PASTE_GD_LINK");
  const pluginDl = document.querySelector("[data-plugin-dl]");
  if (pluginDl) {
    const ua = navigator.userAgent;
    pluginDl.href = /Mac/i.test(ua)
      ? (isSet(PLUGIN_DOWNLOADS.macos) ? PLUGIN_DOWNLOADS.macos : "/static/downloads/blender-macos.zip")
      : /Win/i.test(ua)
        ? (isSet(PLUGIN_DOWNLOADS.windows) ? PLUGIN_DOWNLOADS.windows : "/static/downloads/blender-windows-x64.zip")
        : "/plugins";
  }
  // /plugins 頁按鈕：有 GD 連結就覆寫 href
  document.querySelectorAll("[data-gd-dl]").forEach((a) => {
    const u = PLUGIN_DOWNLOADS[a.dataset.gdDl];
    if (isSet(u)) { a.href = u; a.removeAttribute("download"); }
  });

  window.REACH = { t, get lang() { return lang; }, onLang(fn) { listeners.push(fn); } };
  applyLang();
})();

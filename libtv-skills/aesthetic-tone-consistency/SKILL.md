---
name: aesthetic-tone-consistency
description: "sref 一碼鎖定全片影調,美學不跑偏,逐鏡成片調性如一"
---

---

## name: aesthetic-film\\

namespace: industry\
title: "美學定調短片"\
description: "以 Midjourney 美學風格（sref 定調）為核心的藝術短片：先用 MJ 鎖定全片視覺調性，再由 Seedance 逐鏡成片。適用於「用一套統一的電影級美學基調把一個短故事/氛圍片做成成片」。兩種模式——A：每鏡 MJ 直出關鍵幀 → Seedance；B：MJ 出元素基準畫板 → Nano Banana 輕改合成 key_frame → Seedance。純圖片美學（不成片）→ image-generation；通用多鏡敘事（非 MJ 美學定調）→ cinematic-flow。"\
version: 3

# aesthetic-film

做**以 Midjourney 美學風格（sref 定調）為核心的藝術短片**時用本 skill：先用 MJ 把全片視覺調性鎖死成一個統一基準，再由 Seedance 逐鏡生成成片。核心不是敘事複雜度，而是**美學一致性**——整片靠一套 sref / 風格描述維持同一影調。本 skill 自足：sref 定調機制、鏡頭設計、電影化提示詞、Seedance 序列、音訊與合成規則全部內聯，不外包給別的 skill。

## 兩種模式

- **模式 A（MJ 直出關鍵幀，源 #16）**：每鏡用 MJ 直接生成關鍵幀圖 → Seedance 成片。適合以 MJ 出圖質感直接驅動畫面的場景。
- **模式 B（MJ 基準畫板 → Nano 精修，源 #17）**：MJ 出**元素基準畫板**（外觀由 sref 錨定），再用 Nano Banana 在 MJ 參考圖上做**輕量合成/微調**得到每鏡 key_frame → Seedance 成片。適合敘事化、需要按分鏡精確排布主體位置/姿態、但要嚴守 MJ 風格鎖的場景。

模式選擇在規範定稿階段與使用者確認；兩模式共用下面的 sref 定調、鏡頭設計、提示詞與合成規則。

## 階段（按 SP 全流程）

不要一次跑完全部階段。在每個關鍵階段（規範定稿 / 風格路徑確認 / 故事板確認 / 元素圖完成 / 關鍵幀完成 / 逐鏡影片後 / 音訊後）暫停，用 `ask_human` 或卡片邀請使用者確認後再進下一步。繼續前用卡片或回覆邀請使用者審閱。

1. **規範定稿**：寫 `Final_Video_Spec.md`（標題、型別、比例、時長、視覺風格、語言、模型偏好）→ `write_file_v2`。同時**確認美學風格路徑**（見「風格路徑與 sref 定調」）與模式 A/B。
2. **故事板**：生成 shot_list + audio_layers（模式 B 另含關鍵元素設計）→ 見「故事板設計」。
3. **元素/關鍵幀圖**：模式 A 每鏡出一張關鍵幀圖；模式 B 先出 MJ 元素基準畫板，再 Nano 精修出各鏡 key_frame → `generate_image_v3`（見「元素與關鍵幀生成」）。已有使用者素材先 `get_node_info` 繫結到對應故事板位置，不重複生成。
4. **逐鏡影片**：`generate_video_v3` 逐鏡，`reference_nodes` 引關鍵幀 / 元素圖、`{{NodeKey}}` 繫結；單鏡 ≤15s（引擎單次上限）。提示詞按「逐鏡影片提示詞」內聯規則寫。
5. **音訊層**：`generate_audio` 生成所有獨立音訊層（≥1 全域性 BGM；長片可多段 BGM 各帶 `audio_id` 與範圍；有解說 / 旁白設 narration 層）。
6. **合成**：`composite_video` 按故事板與時間軸順序拼成成片，引導使用者匯出。

**階段依賴**（源 Flova #16/#17）：2→1；3→2；4→3；5→2；6→2,3,4,5。

**使用者已有素材**（主要影響步驟 3–5）：在填充生成內容前，先用 `get_node_info` 把使用者提供 / 現有素材繫結並分配到對應故事板位置；避免重複生成使用者已給的素材。

## 風格路徑與 sref 定調（核心工藝）

規範定稿與素材生成前，**先與使用者確認用 MJ 生成美學風格圖的路徑**（兩選一）：

- **路徑一（風格描述詞）**：用提示詞描述確定風格。使用者明確了風格專有名詞或偏好時，把風格描述記入 `Final_Video_Spec`，並在**後續所有元素生成中始終複用**這套風格描述詞。
- **路徑二（sref code 定調）**：用 `--sref` 程式碼作為風格標杆來構建故事板內容，而**不是**把 `Final_Video_Spec` 的風格重寫進每一條 MJ 提示詞。

`--sref` **選擇規則（路徑二）**：

- 先問使用者是否有 Midjourney `--sref` 風格程式碼。沒有則由代理自選一個程式碼（通常取 **0–4294967295** 的整數，隨機 / 貼合內容均可）；**記錄所用程式碼，並在專案內後續所有 MJ 呼叫中複用**，除非使用者更改。
- 語法 `--sref <code1> <code2> …`，token 之間**空格分隔**（如 `--sref 5877700996 4815442863`）。每個值必須是 0–4294967295 的整數。**多個程式碼可堆疊**；使用者給了多個就記錄完整列表並全程複用。無使用者偏好而自行發明程式碼時，除非使用者明確要求堆疊，**優先單個自動整數以保簡潔**。

**工具適配**：MJ 圖由 `generate_image_v3`（`ai_model` 指定 `Midjourney V8.1`）生成。**若當前引擎不支援** `--sref` **引數**：降級到路徑一（風格描述詞複用）+ 把風格基準圖作 `reference_nodes` 的風格參考傳入——機制（全片一套風格鎖、跨鏡複用）保留，落點適配。

## 故事板設計

### 關鍵元素設計（模式 B / 有復現元素時）

- 覆蓋**關鍵主體**（角色、物體）、**關鍵地點 / 場景**、**關鍵道具**（如有）。
- **角色多狀態顯式分列**：角色在專案中有多個造型 / 外觀（不同服裝、年齡）時，在描述裡明確寫出（造型 1：…；造型 2：…）。
- **場景內物體位置朝向**：描述重要物體（尤其道具、發生主要動作 / 表演的區域）的位置和朝向。
- **使用者素材必須匹配**：使用者提供並指定為關鍵元素的素材，描述**必須與之匹配**，不得與所見 / 所聽矛盾。

### 鏡頭設計（每鏡三要素）

每個鏡頭描述必須含：

- **場景**：引用地點 / 佈景，用場景元素 ID（如 `[Element_Office_Noir]`）。
- **敘事內容**：角色與關鍵物體的動作 / 動態、臺詞與表演，寫出**確切臺詞**（口述對白或內心獨白 / OS），用元素 ID 引用角色。
- **鏡頭語言（攝影）**：景別（全景 / 中景 / 特寫）、機位角度（仰拍 / 俯拍）、運鏡（固定 / 搖攝 / 推軌）。

### 獨立音訊設計

- **背景音樂**：至少設計一段全域性 BGM。影片較長（如 ≥3 分鐘）且有明顯幕間 / 轉折點時，可規劃多段音樂（每段帶自己的 `audio_id` 與作用範圍）。
- **旁白**：用畫外音 / 旁白推進故事時在此設計（型別 `narration`）：定義聲音特徵、語氣、確切指令碼；用 `layout_instruction` 把它限定在相關鏡頭範圍內。

## 元素與關鍵幀生成

### 關鍵元素圖（MJ 基準，兩模式共用）

載入使用者選定的風格路徑（路徑一：用 `Final_Video_Spec` 記錄的風格描述；路徑二：用 `--sref` 定調）。

- 用 `generate_image_v3`（`Midjourney` 系引擎）出**風格 / 場景、角色 / 道具基底、大場景**。
- **提示詞規則**：描述內容（人物 / 事物 / 地點、可辨識輪廓、環境），按上文規則附加 `--sref`。**不要**把規範裡"預想影片 / 影象風格"的長篇文案塞進 MJ，也不要把 MJ 步驟當成必須執行該文件的環節——**sref + 主體 / 場景描述就足夠**。

### MJ 基準畫板定位（模式 B）

- MJ 畫板是**外觀的事實來源**（source of truth）：外觀由 `--sref` 錨定。
- MJ 在模式 B 裡是後續 Nano 工作的**基準工廠（reference board）**，**不是最終裝配時的調色步驟**——不要指望 MJ 一步出成品幀。

### Nano Banana key_frame 精修（模式 B 核心·反模式）

- 用 `generate_image_v3` 圖生圖（`Nano Banana Pro` 系引擎），出**每鏡第一幀**，與故事板中的鏡頭描述對齊；解析度按專案規範設 **2K–4K**。
- **輸入**：按鏡路由的場景 / 風格 / 角色 / 道具元素參考（`reference_nodes`）。
- **提示詞必須簡潔**：指定**哪張參考圖提供環境 / 紋理**、**哪張提供風格 / 光照詞彙**，**只**關聯故事板指令碼所要求的內容（姿勢、佈局、誰拿著什麼）。**禁止**貼上重新描述調色 / 光照 / 電影參考 / 情緒的段落——**那會強制模型完全重繪、削弱對 MJ 參考圖的依從**。Nano 只做在 MJ 參考圖之上的**輕量合成 / 微調**，不是從長提示詞重建整張圖。

## 逐鏡影片提示詞（全量內聯，不外包）

### 語言規則（最高優先）

使用者用中文輸入或載入中文語言環境時，提示詞用**中文書寫**；但提示詞裡的旁白 / 對話內容嚴格遵循 `Final_Video_Spec` 的 Output Language。

### 影象提示詞 6 大核心規則（寫 MJ `key_element` 元素圖時全域性套用）

提示詞不只是描述"圖裡有什麼"，而是像專業電影導演 + 調色師給團隊下指令。把這 6 條寫成**流暢自然的英文段落**、**編織在一起**，不要輸出為帶標籤分節：

1. **專業風格錨點**：結合專業藝術 / 電影術語與風格詞；引入"作者"與具體電影視覺錨點（如 `Neo-Noir style, David Fincher Style, inspired by Se7en`），不要泛泛只說 `Neo-Noir`。
2. **構圖與鏡頭**：明確電影化構圖（`Over-the-shoulder shot` / `Dutch angle`）與景別（`Close-up` / `Medium shot`）。
3. **光影（含負光）**：詳述主光並重點強調"負光"以產生對比與戲劇性（`Strong chiaroscuro contrast` / `dramatic interplay of light and shadow` / `deep facial shadows emphasizing facial structure`）。
4. **調色（90% 單主色·禁紅藍霓虹）**：高階好萊塢剋制調色（`deep teal-cyan shadows dominating 90%, zero warm fill` / `muted watercolor wash`）；除非使用者明確要求，**永不用紅藍霓虹衝突**（禁 `crimson bleed`、霓虹洋紅 vs 青）；畫面約 90% 區域只用**一種主導色調**，極度剋制。
5. **視覺渲染**：描述整體視覺質量與紋理（精細渲染、豐富錯綜的細節、帶細微高斯模糊的柔焦）。
6. **氛圍與潛臺詞**：描述角色"潛臺詞"與微表情，把動作定格在戲劇性瞬間（`oppressive suffocation` / `no mercy` / `predatory stillness`）；無生命物體描述其狀態（宿命感 / 穿透力的注視 / 寒冷疏離）。拒絕僵硬擺拍。

- **條件元素·畫面內文字**（僅相關時）：場景出現文字（如螢幕文字）時自然整合，用**引號**包裹要渲染的確切文字，如 `A neon sign in the background reads "DANGER".`。

### key_frame 專節（模式 B · 不套 6 原則）

- `key_frame`**（Nano Banana）是例外**：**不**套用冗長的 6 大核心原則——沉重的電影化文字會讓 Banana 忽略 / 對抗 MJ 參考圖、導致重繪。優先只用"**插槽標籤 + 故事板對齊**"。
- **核心規則**：故事板裡的鏡頭描述就是這張靜態圖"必須發生什麼"（誰 / 哪裡 / 動作 / 鏡頭節奏）的指令碼。提示詞只需加**最少的路由文字**，讓模型以 MJ 元素圖為參考、針對該節奏微調——而不是用文字對內容和風格做第二次全面處理。你越詳盡地描述期望外觀與內容，Banana 越傾向重新生成、丟掉 MJ 風格鎖。
- **理想短提示詞模式（示例）**：`Reference environment texture Element_Dark_Void_img, and style Element_Glowing_Cube_img.`（然後僅追加故事板要求的內容，如主體位置或 `cube centered, static, push in before`——保持簡短。）

### key_element 提示詞結構（寫元素定義時）

圍繞：**主體與身份**（角色 / 道具 / 場景 / 生物是什麼；角色含年齡、體型、種族（如指定）、顯著特徵、聲音）→ **特徵細節**（優先跨鏡必須一致的特徵：角色寫面部特徵 / 妝造 / 服裝配飾的材質剪裁顏色狀況；道具寫形狀 / 材質 / 顏色 / 尺寸 / 狀況新舊 / 獨特標記）→ **氛圍情感基調**（緊張 / 憂鬱 / 希望 / 寧靜 / 不安 / 溫暖 / 壓抑 / 恐懼 / 懷舊 / 孤立 / 親密…）。路徑二時在主提示詞後附 `--sref`（驗證每 token 在 0–4294967295、標準化為空格分隔；未設則選一個程式碼記錄並全程複用）。

### 影片提示詞 · 參考圖命名

先**為每張參考圖示記角色**，讓 Seedance 正確讀取面部與造型：用 `reference_nodes` 傳參考圖、`{{NodeKey}}` 引用節點。模板：Subject 1 — 面部特徵參考 `{{Face_1}}`（頭部特寫）；髮型 / 妝容 / 服裝參考 `{{Body_1}}`（全身照）。Subject 2 繼續編號。

### 影片提示詞 · Seedance 四層順序（鏡頭 → 主體 → 空間 → 音訊）

按此順序追加動作 / 動態提示：

1. **鏡頭**：運動或攝像機 / 剪輯變化（`static → push in`、`cut to new angle`、`orbit`、`pan`）。
2. **主體**：動作與表情（誰做什麼、面部神態）。
3. **空間**：位置 / 環境變化（主體或相機相對空間的位置、背景運動、深度 / 佈局轉換）。
4. **音訊**：對話（如有）、音效，及模型缺音樂時的備註（見負面約束）。

- **動作細節**：基於**具體身體部位**（手 / 腿 / 頭 / 肩），加**程度**（幅度 / 速度 / 力度，如 `slowly raises one hand`、`snaps head left`、`pushes hard off the ground`）；一個提示詞多節拍時，按故事時序列**主要動作 → 次要動作**。
- **多節拍**：工具接受長提示詞時，可在單次生成裡標 **Shot 1 / Shot 2 / Shot 3** 表示鏡頭或故事節拍序列。
- **禁逐秒時鐘計時**：精確時鐘（"0–3 s"、"在 2 s 時…"）**無法可靠執行**——不要按確切秒數硬拆、不寫逐秒計劃；描述**按順序發生的事**，而非按時間劃分的鏡頭清單。
- **可選潤色**（真人實拍簡報時）：可加輕微手持微震 / 細微膠片顆粒，保持從屬於上述四層順序。

### 包裝符約定（Seedance 引擎語法）

引擎接受自然語言，這些包裝符幫模型區分音樂 / 音效 / 對話 / 螢幕文字：

- **音樂**（描述播放內容）：`(...)`，如 `(fast-paced rock playing in the background)`。
- **音效**：`<...>`，如 `<distant dog barking>`。
- **口述對話**：`{...}`，如 `{Hello, world}` —— 臺詞不是專案主要語言時，在花括號前標語言，如 `Says in Japanese: {こんにちは}`。
- **螢幕標題 / 章節 / 字幕文字**：`【...】`，如 `【Chapter One: Departure】`。

### cut to 多階段動作

單鏡內高度複雜 / 多階段動作時，**按順序**描述序列，用 `cut to` 標籤表示過渡（shot A…, cut to shot B…, cut to shot C…）。示例：\
`Shot1: {{image_1}} his hands carefully open a dusty wooden box, with the sound of a soft creak. {{image_1}} His expression is focused and curious. The camera is a fixed shot, and the background attic is static. Shot2: cut to a bright blue light emanates from the artifact inside, casting an ethereal glow on his face and creating long, shifting shadows in the room. {{image_1}} His expression changes from focused to shocked awe as the camera begins a slow zoom in on his face. Shot3: cut to {{image_1}} he looks up with determination, the blue light reflecting in his eyes, as he slightly turns his head to the left to look past the camera. (no dialogue, no music, no subtitles)`

### 三條負面約束（始終寫進影片提示詞）

- 分鏡表明該鏡有**單獨旁白音軌**時，影片提示詞裡**不寫旁白文字**，避免音訊衝突。
- 為防模型加不想要的 BGM，**幾乎總是**包含 `no music`。
- 字幕後期加，**始終**包含 `no subtitles`。

## 合成（靜音嵌入音訊規則）

`composite_video` 按故事板與時間軸順序組裝所有鏡頭、旁白音軌與 BGM，剪輯就緒後引導使用者匯出。**若最終鏡頭沒有鏡頭內對話或旁白，把該鏡頭 / 影片層的嵌入音訊靜音**，只依賴設計好的**音訊層**（BGM / SFX），這樣鏡頭自帶的音效不會與混音衝突。

## 變體與邊界（勿用本 skill，改道）

- **純圖片美學（不成片，只出美學靜圖）** → image-generation。
- **通用多鏡敘事短片（非 MJ 美學定調、故事 / 人物 / 對白驅動）** → cinematic-flow。

（本 skill 自足，無源生跨 skill 依賴，故無「配合」宣告表。生成基元 = `generate_image_v3` / `generate_video_v3` / `generate_audio` / `composite_video` / `write_file_v2` 等工具呼叫，非跨 skill 依賴。）
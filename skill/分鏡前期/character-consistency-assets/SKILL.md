# 角色一致性資產工作流 3.0（中文釋出版）

本 Skill 構建可複用的寫實角色資產：中文確認，交付英文 Prompt。能建立模型節點時須核對顯示名；不能繫結時只交付 Prompt，不能聲稱已呼叫。

## 五類主模式與模型路線

- **Mode 0 定臉：** Lib navo pro 直出，或 Lib Image／Style Image V8.2 候選後由 Lib navo pro 建卡。
- **Mode 1 服裝定妝：** 使用 Lib navo pro 建立單張全身服裝基準；必要時用 Lib Image 製作 Mode 1B 造型細節卡。
- **Mode 2 角色表：** Lib navo pro 三格：無頭正面、帶頭背面、唯一正臉錨點。
- **Mode 3 高精度面部特寫：** 使用 Lib Image 製作臉部、肩上或胸像細節參考。
- **Mode 4 兩參考圖換裝：** 使用 Lib navo pro；第一張圖提供服裝與姿勢，第二張圖提供人物身份。

## 權威預設值

- 預設寫實攝影；其他風格須明確要求。
- Mode 0 正式卡、Mode 1 單步、Mode 2 使用 18% 中性灰與 Flat Grade；候選不追加；白底僅按明確要求替換。

## 總工作流

### 1. 先確認角色狀態

狀態不明時問：**“角色已經有穩定參考圖，還是要從零建立？”** 已說明則不重複問。

- 已有角色：上傳參考圖，回述身份特徵並確認。
- 新角色：先確認文字規格，再進 Mode 0。

新角色規格：臉部骨相、眼形眼色、眉鼻唇、膚色膚質、頭髮、體型比例、預設表情、永久紋身及位置、疤痕、美人痣、固定穿孔。候選路線可把未定臉部項標為“探索軸”，但共享不變數須確認。妝面、美甲和可替換首飾在 Mode 1 鎖定；標誌性常戴配飾在 Mode 0 登記、Mode 1 渲染鎖定。

候選模板編譯時，共享不變數填入；探索軸寫成一至兩個有界可見方向，或連同連線詞整段省略，不得偽裝成已確認事實。

依賴順序：`文字規格 → Mode 0 → Mode 1 →（Mode 1B 按需）→ Mode 2`；Mode 3、4 按需。已有穩定參考可跳過 Mode 0，但須先確認身份。

### 2. 每個完整 Prompt 都要先確認

完整 Prompt 前確認：

- **已附參考圖：** 第一項，逐張列出；沒有則寫“無，純文字構建”
- **角色與造型：** 身份關鍵項及本次要鎖定的 Look
- **背景：** 預設 18% 中性灰；候選臉為 neutral mid-gray
- **構圖：** 僅在非預設時列出

最後問：**“以上鎖定，可以開始寫 Prompt 嗎？”** 未確認不輸出完整 Prompt。

已批准 Prompt 的輕微修改可直接修訂；新角色、新 Look 或新模式須重確認。

### 3. Agent 執行協議

每次觸發模型前給出路由卡：

- **當前模式與步驟：** 例如 Mode 0／選項 2／第一步試臉
- **模型與參考圖：** 精確顯示名；逐張職責或“無，純文字構建”
- **本步產物：** 候選、權威身份卡、服裝基準、角色表、細節卡或換裝結果

不能繫結或核對模型時停止自動執行，只交付 Prompt，並寫“尚未呼叫模型”。

Mode 0 的選項 2、3 必須分步執行：先用所選模型生成候選，等待使用者選定唯一一張，再建立 Lib navo pro 標準身份卡節點。不得同時建立兩步或自動替使用者選擇。候選圖不能進入 Mode 1／2；只有使用者批准的唯一權威身份卡可以繼續。

每次只推進已確認步驟，不預建後續節點；只有出現結果資產才能說“已生成”。

## 參考圖職責

- 角色表只保留一個清楚人臉錨點，不得在無頭正面格加入第二張臉。
- 只寫可見資訊，不猜測、用姓名或重複長述；不寫真實品牌、受保護 IP 或具體年齡，候選可用 `adult`。
- 除 Mode 4 編號外，只用職責描述，如 `the attached character reference`。

## 通用 Prompt 規則

- 中文互動，英文 Prompt；不寫數值畫幅，只寫 full body、chest-up 等構圖。
- 預設中性閉唇；不輸出獨立 Negative Prompt。
- 每個 Prompt 一個程式碼塊；批次逐項編號。交付前替換或刪除全部引數槽。
- 不新增使用者未確認的首飾、紋身、妝面或服裝細節。

## 角色資產 Flat Grade（Mode 0 正式身份卡、Mode 1 單步、Mode 2）

Mode 0 的正式標準身份卡、Mode 1 單步定妝和 Mode 2 的最終 Prompt 必須原樣展開以下英文塊：

```text
Background is an even 18% neutral gray seamless, one completely flat uniform value corner to corner, with no seam line, gradient, hotspot, vignette, or falloff. Relight from scratch with completely flat shadowless illumination: one enormous soft frontal source at camera position and matched equal fill from camera-left, camera-right, above, and below, so both sides of the face and body read at identical brightness. No key-to-fill ratio, shadow side, rim light, hair light, kicker, or specular hotspot. Zero shadow cast onto the background, no contact shadow beneath the feet or hem, and no ambient occlusion. Extremely low contrast, even, milky, catalogue-flat. Skin and fabric remain matte and render at their true natural tones, never washed out or cool-shifted by the background. Real fine even pore texture, peach fuzz, subtle subsurface scattering, strand-level hair, real fabric weave and drape, soft natural film grain. Fine, flattering, photographed realism — never plastic, waxy, glass-skin, harsh, or clinically detailed. Photographed on a clean 50mm-equivalent prime with even sharpness. Photographed, not generated.
```

白底例外只把首句替換為 `Pure white seamless studio background, perfectly even, with no gradient or seam line.`，其餘條款不變。

方括號是內部引數槽，交付前必須替換或刪除。Mode 0 正式身份卡、Mode 1 單步和 Mode 2 拼接 Flat Grade；兩條候選臉路線、Mode 1B、Mode 1 兩步合成、Mode 3 和 Mode 4 使用各自專屬結尾。

---

## Mode 0：定臉與身份鎖定

### 進入條件

只用於沒有穩定身份參考的新角色。目標是得到後續服裝、角色表和特寫都能引用的標準身份卡。

正式標準身份卡使用 plain black thin-strap camisole（女性）、plain black ribbed tank（男性）或 plain black crew-neck top（中性人物），採用中性基礎修飾，不帶 Look 妝面或可選首飾。候選路線統一用黑色圓領上衣。

胸像外的永久標記保留在中文身份賬本，待 Mode 1 露出並由 Mode 1B 按需驗證；不得聲稱標準身份卡已視覺鎖定畫面外細節。

完成中文文字規格的回述與確認後，主動展示三個選項並等待使用者選擇：

1. **Lib navo pro 標準定臉：** 純文字直接建立標準身份卡。
2. **Lib Image 網感試臉後鎖定：** 探索候選，選一張後由 Lib navo pro 標準化。
3. **Style Image V8.2 高階感試臉後鎖定：** 探索候選，選一張後由 Lib navo pro 標準化。

若使用者已明確指定，不重複詢問。不得把“網感／高階感”當成承諾；它們只是探索方向，最終以實際候選結果和使用者選擇為準。

確認：

- **路線與模型：** 選項 1 為 Lib navo pro；選項 2 為 Lib Image → Lib navo pro；選項 3 為 Style Image V8.2 → Lib navo pro
- **參考圖：** 第一步無參考；候選路線第二步列唯一獲選圖
- **角色身份：** 骨相、膚色、頭髮、眼睛與全部已確認身份標記
- **服裝與構圖：** 正式卡用指定黑色基礎上衣；候選用黑色圓領上衣；均為臉佔主體的胸像
- **背景：** 正式卡 18% 中性灰；候選 neutral mid-gray

### 標準身份卡英文模板

選項 1 直接使用；選項 2、3 選定候選後使用，並以 `the same character shown in the approved exploratory face reference` 開頭。

```text
A clean high-fidelity character identity reference, framed from just above the head to the upper chest with the face dominant in the frame. [IDENTITY: heritage appearance, build, exact natural skin tone and matte finish, face structure, eye shape and exact eye color, hair color, length and texture, and every approved identity marker visible within this crop with precise placement]. [She wears a plain black thin-strap camisole / He wears a plain black ribbed tank / They wear a plain black crew-neck top], with neutral base grooming, no look-specific makeup, and no optional jewelry beyond confirmed identity-defining piercings. Body squared to camera, head level, eyes directly to camera, lips closed, neutral controlled expression.

High face fidelity: soft fine even pores, fine peach fuzz along the jaw and upper lip, subtle subsurface scattering at the cheeks, ear edges, nostrils and eye sockets, individual lash separation, real iris moisture and pattern, natural lip lines, and strand-level hair with baby hairs and flyaways. Keep every feature flattering and natural, with no harsh clinical texture.
```

### Lib Image 網感試臉後鎖定

第一步須核對節點為 `Lib Image`。它讀取已確認規格，只出非權威候選，不用標準身份卡長模板或 Flat Grade。公眾人物／偶像參照先轉成使用者確認的可見五官、妝發與氣質，不寫姓名。

```text
Contemporary photorealistic casting portrait of one adult [CONFIRMED HERITAGE APPEARANCE] [woman / man / person] with [CONFIRMED NATURAL SKIN TONE AND UNDERTONE], [CONFIRMED FACE SHAPE AND MODERATE BONE STRUCTURE], [CONFIRMED EYE SHAPE AND COLOR], [CONFIRMED BROWS, NOSE AND LIPS], and [CONFIRMED HAIR COLOR, LENGTH AND TEXTURE]. [LARGE VISIBLE IDENTITY MARKERS ONLY]. [CONFIRMED CONTEMPORARY BEAUTY DIRECTION AS VISIBLE MAKEUP AND GROOMING]. One person only, centered head-and-shoulders framing, face dominant, body square to camera, head level, direct gaze, calm closed-lip expression, plain black crew-neck top. Seamless neutral mid-gray background, soft even frontal studio light, low contrast, natural flattering skin and hair texture, polished contemporary portrait photography.
```

選中唯一候選後切換 Lib navo pro，以獲選圖為唯一探索參考建立標準卡；批准後才成為權威資產。必要時再用 Lib Image 精修一次，批准結果替代前卡。

### Style Image V8.2 試臉後鎖定

第一步必須顯式選擇並回讀 `Style Image V8.2`。模型列表或節點未顯示該精確名稱時立即停止；不得用其他模型頂替。

本步讀取同一份已確認中文規格，但須單獨編譯短英文 Prompt，不能複用標準身份卡或 Flat Grade。它只負責胸像候選：保留可見臉部、膚色、頭髮、剋制妝面與標記；體型留在中文賬本。不得追加微觀皮膚、複雜布光或否定清單。

Style Image V8.2 必須透過人像安全編譯器。不得複製或自由潤色使用者原話；先把確認規格規範成封閉欄位，每項最多一個可見名詞短語：

- 單個明確成年人、性別表達，以及可選的已確認族裔／地域外觀；後者不得用於推斷其他特徵。
- 膚色與底色；臉型、下頜、顴骨；眼形眼色；眉、鼻、唇形與標準顏色。
- 頭髮顏色、長度、紋理與分縫；當前胸像可見的明顯身份標記。
- 妝容僅拆成部位、普通顏色、強度與質地；歧義俗稱先規範化。

風格或氣質標籤、人物比喻、真人／團體／品牌指代、模仿關係、身體評價、年齡曖昧與不可見設定都不是 Prompt 欄位。能轉成可見屬性時先用中文確認，否則整項省略；胸像不寫體型。未確認欄位連同連線詞刪除，不得補寫。

專屬內部編譯模板如下。交付結果最多三句、最多 100 個英文詞；這是本 Skill 的候選人像安全上限，不是平臺官方長度宣告：

```text
Studio portrait of one adult [CONFIRMED SUBJECT TERM] with [CONFIRMED SKIN TONE, FACE, EYES, BROWS, NOSE, LIPS AND HAIR]. [OPTIONAL CONFIRMED VISIBLE IDENTITY MARKER AND MAKEUP EXPRESSED ONLY AS AREA, STANDARD COLOR, INTENSITY AND FINISH]. Centered head-and-shoulders framing, direct gaze, calm closed-lip expression, plain black crew-neck top, seamless neutral mid-gray background, soft even frontal studio light, low contrast, natural skin and hair texture, 85mm portrait photography.
```

提交或建立節點前執行失敗關閉檢查，任一項不透過都不得輸出 Prompt、建立節點或呼叫模型：

1. 僅一名明確成年人；全部可變描述可追溯到確認欄位，且只寫胸像可見資訊。
2. 無真人、團體、品牌、受保護形象、模仿關係、風格標籤、人物比喻、年齡曖昧或身體評價。
3. 妝容符合封閉欄位；最終文字只寫期望畫面，不含否定清單、模型／平臺名、引數、中文、冒號式長清單或未替換槽位。
4. 最多三句、100 個英文詞；固定保留單人胸像、黑色圓領上衣、中灰背景、柔和均勻正面光與低對比度。

失敗時從封閉欄位重編一次；仍不合格則停止並說明“V8.2 人像 Prompt 未透過提交前檢查”。透過後內部記錄 `V8.2 portrait lint: PASS`，不寫入 Prompt。畫幅與 Raw 只透過介面控制項設定。

建立節點後回讀實際模型名、Prompt、畫幅與 Raw。Prompt 必須與檢查透過版逐字一致；若被再次翻譯、潤色或刪改，立即停止，不得生成。

錯誤必須按介面證據分流，不得混為一類，也不得連續自動重試：

- 明確出現 `AI Moderator`、`unsure about this prompt` 或同義稽核提示：記為“稽核不確定性攔截”，不能聲稱使用者違規。用上方模板僅保留成年人、核心臉部欄位、頭髮與固定構圖環境；透過提交前檢查後，只交付一次修訂版供使用者確認，不得自動重試。
- 只出現 `Failed to submit`、`Creation failed unexpectedly` 等通用提交錯誤：不能先改 Prompt，也不能推斷是稽核。先核對實際節點仍顯示 `Style Image V8.2`、平臺提交狀態，以及在能夠訪問權威狀態來源時核對服務狀態；無法核實時明確寫“原因無法確認”。使用者確認後最多原樣重試一次。
- 權威狀態來源明確顯示服務異常：停止並報告，不改 Prompt、不重試、不切模型。
- 任一分支在一次經使用者確認的重試後仍失敗：停止並回報介面原始錯誤、實際模型節點名稱和已執行的檢查；不得靜默切換模型。

使用者選中唯一探索結果後，第二步必須顯式切換到 Lib navo pro，並把獲選圖作為唯一探索參考。回到標準身份卡模板，補齊精確眼色、臉型和當前裁切可見標記，並回歸中性基礎修飾。第二步經批准後才成為唯一權威身份卡，其他候選不得繼續引用。

如果第二步完成後，眼色、穿孔、美人痣、細小疤痕、唇紋或髮際線仍未達到使用者要求，可詢問是否使用 Lib Image 進行一次按需精修。精修必須以上一步標準身份卡為唯一身份參考，不得重新發明人物；使用者批准精修結果後，它替代上一步成為唯一權威身份卡。

---

## Mode 1：服裝定妝

### 進入條件

必須已有使用者確認的角色身份參考。每套新服裝先獲得一張使用者滿意的單人定妝圖，之後才能製作 Mode 2。

先鎖定完整 Look：服裝、鞋、首飾、配件、妝面、髮型／髮飾、美甲和可見永久標記。身份卡登記永久標記的位置，Mode 1 決定是否可見；標誌性常戴配飾須與身份登記一致。

- **Lib navo pro 單步定妝：** 預設路線，直接用角色參考和文字規格完成。
- **Lib navo pro 兩步合成：** 僅限複雜服裝且介面支援雙參考；先做普通模特 Look，再替換為鎖定角色。

確認：

- **模型：** Lib navo pro
- **角色參考與路線：** 已批准身份卡；單步或兩步
- **完整 Look：** 服裝、鞋、首飾、配件、妝面、髮型／髮飾、美甲、可見永久標記
- **姿勢與構圖：** 預設全身，手與鞋完整可見
- **背景：** 18% 中性灰無縫背景

### 單步定妝

預設全身、輕微轉角、中性表情，手鞋完整可見。

```text
The same character shown in the attached identity reference. Preserve the face, bone structure, body proportions, natural skin tone, base hair identity and every approved permanent identity marker. The character wears [COMPLETE APPROVED WARDROBE FROM HEAD TO TOE: garments, fabric, color, fit, construction, layering, footwear, jewelry and accessories]. Apply [APPROVED MAKEUP, HAIRSTYLE OR HAIR ACCESSORIES, AND NAIL LENGTH, SHAPE, COLOR OR ART]. Keep every approved permanent marker visible at its exact placement wherever the outfit exposes it. [POSE: body angle, weight distribution, hand position, gaze and neutral controlled expression]. [FULL-BODY / WAIST-UP / HEAD-TO-SHOULDERS FRAMING].
```

把角色資產 Flat Grade 原樣拼接在該模板末尾。

### 兩步合成

僅在雙參考可用時提供。第一步用 Lib navo pro 製作普通修長模特 Look；頭髮須與獲批發型相容，人物正面中性站立。

```text
A slim [woman / man] stands straight-on to camera in a relaxed neutral stance, weight even across both feet, arms relaxed at the sides, shoulders level, eyes to camera, lips closed. [SIMPLE NEUTRAL HAIR COMPATIBLE WITH THE APPROVED STYLING], clean even features, neutral natural skin tone. The figure wears [COMPLETE APPROVED OUTFIT, FOOTWEAR, JEWELRY AND ACCESSORIES] with [APPROVED MAKEUP, COMPATIBLE HAIR STYLING, HAIR ACCESSORIES AND NAILS]. Full-body framing with all footwear visible. Background is an even 18% neutral gray seamless with no seam line, gradient, hotspot, or vignette. Soft broad frontal studio illumination keeps the complete look clean, matte, evenly readable, and true in color. No dramatic shadow, rim light, or background cast shadow. Real fabric weave, weight and drape; natural skin texture; soft film grain. Photographed, not generated.
```

第二步繼續用 Lib navo pro，參考順序與 Mode 4 相同：

- **reference image 1：** 第一步生成的普通模特服裝圖，提供完整 Look 與姿勢。
- **reference image 2：** 鎖定角色身份參考，提供臉、骨相、比例、膚色、基礎頭髮身份和永久標記。

```text
Replace the person in reference image 1 with the person from reference image 2. Keep the complete outfit, footwear, jewelry, accessories, makeup, hair accessories, nails and pose from reference image 1 exactly. Recreate the approved compatible hair arrangement while preserving the hair color, length, texture, density and hairline from reference image 2. Match the face, bone structure, body proportions, natural skin tone and permanent identity markers from reference image 2. Clean neutral mid-gray seamless studio background, soft large-source studio lighting, true natural colors, natural film grain, full-body framing.
```

第二步不重寫長描述、不追加 Flat Grade；兩張參考圖承擔資訊。

---

## Mode 1B：造型細節卡（可選）

使用 Lib Image，以批准的 Mode 1 服裝基準圖為主參考；支援雙參考時再附權威身份卡。僅在全身圖看不清或使用者要求時進入。每張只放大一個區域：美甲／戒指／手鍊、紋身、耳飾、項鍊、鞋或服裝工藝；多區域分開生成。臉為主體用 Mode 3，飾品或身體部位為主體用 Mode 1B。

若細節在 Mode 1 中錯誤或缺失，先回 Mode 1 修正並重新批准；Mode 1B 只放大已批准但尺寸太小的細節。

```text
A high-fidelity styling detail reference of the same character and look shown in the approved outfit reference. [IF ATTACHED: the approved identity reference controls body proportions, natural skin tone, base hair identity and permanent markers only.] Tight close-up of [ONE APPROVED BODY OR WARDROBE AREA]. Preserve the exact natural skin tone, anatomy, garment context and every permanent marker visible in this crop. Show [APPROVED NAILS, JEWELRY, TATTOO, PIERCING, FOOTWEAR OR GARMENT-CONSTRUCTION DETAIL] with its exact color, material, pattern, scale and placement. Neutral mid-gray seamless studio background, soft even frontal light, low contrast, true colors, realistic skin and material texture. Include only the approved design with no extra symbols, accessories or decoration.
```

細節卡僅作輔助，不替代身份卡或服裝基準圖。

---

## Mode 2：三格角色表

### 進入條件與佈局

使用 Lib navo pro，必須已有批准的 Mode 1 單張定妝圖。左格去掉低解析度小臉，右格是唯一高解析度人臉錨點；不得把頭加回左格。

固定一張橫圖、三個等寬豎格：

1. 左：無頭正面全身，保留正常頭頂留白，不是裁掉頭。
2. 中：帶頭背面全身，後發、服裝背部、下襬和鞋完整。
3. 右：頭頂上方至鎖骨的緊胸像，不得放寬為腰上。

### Mode 2 專屬確認

確認：

- **模型：** Lib navo pro
- **參考圖：** 批准的服裝基準圖與所需身份參考
- **三格：** 左格領口變體、中格背面全身、右格緊胸像
- **Look：** 三格完全一致
- **背景：** 三格統一的 18% 中性灰無縫背景
- **畫幅比例：** 16:9 橫屏

建立或呼叫 Mode 2 影象節點時，必須顯式設定為 16:9；建立後回讀節點顯示比例，若不是 16:9，停止生成並先修正比例。

### 左格無頭變體

- 閉合或有結構領口用 ghost mannequin hollow；抹胸、掛脖、細肩帶、深挖領用 clean neck cut。

```text
LEFT PANEL — full-body front view, no head, no neck, and no hair. The body stands squared to camera from the shoulders down to [THE SHOES / THE HEM], arms relaxed at the sides, hands open and loose, weight even across both feet. Nothing rises above the shoulder line, and no hair falls across the chest or shoulders. The [COLLAR TYPE] of the [GARMENT] holds its own shape and opens into an empty dark hollow looking down into the inside of the garment, with the inner back fabric faintly visible. The outfit keeps full three-dimensional shape, natural drape, and real fabric tension as if worn by an invisible body, but nothing emerges from the neckline. [IF A NECKLACE IS APPROVED: the necklace remains arranged around the empty collar opening and rests naturally on the garment.] No stump, skin, cut edge, anatomy, blood, gore, blur, fade, smoke, ghosting, or transparency in the body. Preserve generous empty headroom above the shoulders so the figure sits at the same scale and position as a normal full-body portrait; the head is removed from the body, not cropped by the frame. Keep the complete footwear or hem fully visible.
```

```text
LEFT PANEL — full-body front view, headless. The full figure stands squared to camera from the shoulders down to [THE SHOES / THE HEM], arms relaxed at the sides, hands open and loose, weight even across both feet. There is no head and no hair; no hair falls across the chest or shoulders. The neck rises a short way from the shoulders and terminates in a clean, flat, sharply defined horizontal edge at the base of the throat, exactly like a headless dress-form mannequin. Above that crisp sculptural edge there is only empty gray background. No blood, gore, anatomy detail, stump, blur, fade, smoke, ghosting, or transparency. Preserve generous empty headroom above the shoulders so the figure sits at the same scale and position as a normal full-body portrait; the head is removed from the body, not cropped by the frame. Keep the complete footwear or hem fully visible.
```

### 三格總模板

```text
A three-panel character reference sheet in one horizontal frame, divided into three equal vertical panels with thin clean separation. The same figure and the same outfit remain identical across all three panels.

[IDENTITY ONCE: build, exact natural skin tone, hair, makeup, identity markers and nails]. [WARDROBE ONCE: complete outfit, materials, construction, footwear, jewelry and accessories].

[INSERT THE CORRECT LEFT-PANEL BLOCK, FILLED WITH GARMENT DETAILS].

CENTER PANEL — full-body rear view, head attached, standing straight with arms relaxed. Show the complete hair fall, garment back construction, hem and footwear.

RIGHT PANEL — tight chest-up identity portrait from just above the head to the collarbones and the very top of the garment. The face fills most of the panel; body squared to camera, eyes to camera, lips closed, neutral controlled expression.

Apply the authority flat grade identically across all three panels. Keep the same gray value, shadowless light and zero cast shadow in every panel. Skin remains identical in value and hue across face, back, arms and hands; garment colors, body proportions and identity remain identical in every panel.
```

展開 Flat Grade 到三格；只輸出一個 Prompt 和一個結果。

## Mode 3：高精度面部特寫

使用 Lib Image，僅在使用者要求臉部、肩上或胸像細節時進入。它不重建身份；權威身份卡回 Mode 0，非臉部細節用 Mode 1B。構圖可選 chest-up、shoulders-up、forehead-to-collarbone。

確認：

- **模型：** Lib Image
- **身份參考：** 已批准的角色身份圖
- **裁切：** chest-up、shoulders-up 或 forehead-to-collarbone
- **細節：** 眼色、妝面、唇部、耳飾、服裝上緣、身份標記、視線和微表情
- **背景與燈光：** 中性灰背景、剋制柔和人像光

```text
A high-fidelity [CHEST-UP / SHOULDERS-UP / FOREHEAD-TO-COLLARBONE] identity-reference portrait of the same character shown in the attached identity reference. Preserve the face, bone structure, exact natural skin tone, hair and every approved identity marker visible within this crop. [VISIBLE HAIR, MAKEUP, EYE COLOR, LIP DETAIL, EAR AND COLLAR JEWELRY, AND WARDROBE WITHIN THE CROP]. [HEAD ANGLE, GAZE AND NEUTRAL MICRO-EXPRESSION].

Neutral mid-gray seamless studio background with no visible seam or distracting gradient. A broad diffused source from camera-left and slightly above gives a gentle natural wrap across the face, balanced by soft frontal fill so the off-light side remains open and readable. No harsh shadow, dramatic contrast, hard rim, kicker, or glossy beauty glare. Skin stays matte and true to its natural tone.

Extreme face fidelity: soft fine even pores, peach fuzz, subtle subsurface scattering, individual lashes, real iris moisture and pattern, natural lip lines, strand-level hair with baby hairs and flyaways, and visible collar fabric weave. Keep the result flattering and natural, never harsh or clinically detailed.

Soft natural film grain, gentle highlight roll-off, photographed on a clean portrait prime. Photographed, not generated.
```

Mode 3 不追加角色資產 Flat Grade；上面的背景、燈光和細節段就是完整專屬結尾。

---

## Mode 4：兩參考圖換裝

使用 Lib navo pro。只有當前介面確認可以同時附加兩張參考圖時才進入；若只能附加一張圖，明確說明能力不足，不假裝完成身份與服裝的雙重鎖定。

### 固定參考圖語義

- **reference image 1：** 服裝、配飾、美甲與姿勢來源。
- **reference image 2：** 人物身份來源，保留臉、骨相、體型、身體比例、膚色、基礎頭髮身份和永久標記。

順序不可顛倒。確認模型、逐張職責與預設完整全身灰底輸出；Prompt 只用自然語言編號。

```text
Replace the character in reference image 1 with the character in reference image 2. Keep the outfit, footwear, jewelry, accessories, nails and pose from reference image 1 exactly. Match the face, bone structure, body type, body proportions, skin tone, base hair identity and permanent identity markers from reference image 2. Clean mid-gray seamless studio background, even neutral mid-gray with no seam line, soft large-source studio lighting, true natural skin and outfit colors, natural film grain, full-body framing.
```

Mode 4 只換裝；不重寫長描述或追加 Flat Grade，兩張參考圖承擔資訊。

## 交付前檢查

- 依賴與節點顯示名正確；候選先選唯一圖，再由 Lib navo pro 建標準卡。
- Style Image V8.2 Prompt 已透過人像安全編譯器：欄位可追溯、最多三句與 100 個英文詞、無開放審美措辭或未填槽位；建立節點後實際 Prompt 與批准文字逐字一致。
- Mode 1 鎖定完整 Look；Mode 1B 一卡一區；參考圖已確認。
- Mode 2 只輸出三格；左格領口變體、手腳、重心、頭頂留白正確，右格是唯一正臉錨點。
- Flat Grade 僅用於正式卡、Mode 1 單步和 Mode 2；Mode 3 只做臉，Mode 4 圖 1 管造型姿勢、圖 2 管身份。
- 最終 Prompt 無模型／平臺名、姓名、品牌、具體年齡、畫幅數字或未填引數；候選可用 `adult`。
- 使用者已透過確認門。

## 最終交付格式

使用者確認後，只輸出完全編譯、必需英文塊已展開的英文程式碼塊；批次時逐項編號。
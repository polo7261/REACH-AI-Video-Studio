---
name: casting-director
description: "你的專屬選角導演，一鍵為你挑選最合適的角色"
---

## 一、審美準則

### A. 長相定位

**精緻中式漫感**：主體一律寫 `Chinese`（不寫 East Asian，易偏韓）。骨相清晰、上鏡化，中和一點寫實感，不要過度漫畫假感。

### B. 皮膚（硬規則）

寫實但細膩乾淨。關鍵詞：`smooth clean realistic skin with a refined natural finish, subtle fine texture and minimal barely-visible pores, looking real but polished like high-end editorial retouching, never plastic, never rough bumpy blemished`。不用 `lots of visible pores`（坑窪），也不用 `flawless glass-skin`（塑膠）。目標：`smooth but natural`。

### C. 反廉價四原則

①寫實膚質 ②柔性體積光（額頭/鼻樑/顴骨高光+臉側陰影）③暖調通透有subsurface透光感 ④細節真實不過度銳化。

### D. 兩條統領原則

- 冷暖對比=高階感（冷調膚+暖調唇眼）
- 去標籤化=通用性（無logo、無強時代符號、配飾剋制）

### E. 純白背景（最高硬規則）

**所有資產背景必須純白 #ffffff**，任何情況不例外。正向：`plain seamless pure white #ffffff studio background`。否定：`no grey, no off-white, no coloured or textured background`。

### F. 五官（按性別分流）

**最高臉型硬規則（全形色，反派也不例外）**：臉型骨相清晰利落、協調上鏡，下頜線乾淨不鬆垮，不寬不方不肉，上下臉協調。**臉由「五官」+「整體氣質」欄位驅動，服裝風格絕不介入臉（見第五節）**。

通用錨定：

- 女：`slim refined oval face with a clean sharp well-defined jawline, harmonious proportions, NOT wide, NOT square, NOT a heavy or sagging jaw`
- 男：`long clean face with a sharp angular well-defined jawline, NOT wide, NOT round, NOT a soft sagging jaw`

**女性五官**：偏窄長臉+平直微挑眉+長眼微上揚+臥蠶+高挺鼻+豆沙唇；妝：偽素顏上鏡感（底妝發光+輕修容+臥蠶高光）。

**男性五官**：長流暢臉+劍眉+深邃桃花眼+高挺鼻+暖紅潤唇+黑色碎髮中分；三檔氣質參考（僅參考不是模板）：奶狗初戀/禁慾總裁/成熟熟男——同型角色務必分化，不套同一套五官表情。

### G. 差異化引導（柔性，agent自判）

- **多角色**：拉開臉型骨架/五官量感/氣質，每人提煉1-2個專屬記憶點寫進CHARACTER段。
- **單角色**：優先服從角色卡個性，不收斂成標準網紅美人。
- **素人**：允許非標準五官（圓臉/寬臉/塌鼻/單眼皮等），不套美人共性。
- **鐵律**：①差異化只作用於不同角色；同一角色多資產必須同臉（資產參考鎖身份）。②角色卡指明相似關係時讓位於角色卡，不硬掰兩極。③不破壞單角色高審美底線。

---

## 二、核心翻譯原則

1. 主體寫 `Chinese`
2. 氣質用狀態化語言（白切黑→`hiding her sharpness`；深情隱忍→`a deep restrained gaze holding quiet emotion`）
3. 臉型用對比+否定式卡死
4. 保留電影術語（halation/anamorphic/bokeh/aegyo-sal不譯）
5. 皮膚永遠寫實（準則B），與漫感程度無關
6. 去標籤化+冷暖對比（準則D）

---

## 三、定臉生成

一次影象生成能力呼叫。prompt拼接順序：

```
CHARACTER: [年齡+Chinese+氣質狀態化+臉型(對比+否定式)+眉/眼/鼻/唇，按性別套準則F]

SKIN (priority, refined realistic): [smooth clean realistic skin, refined natural finish, minimal barely-visible pores, polished like editorial retouching, never plastic+妝+髮型]

OUTFIT: [按第五節推理的完整造型，上衣絕不塞進下裝，無logo，配飾剋制]

[COMPOSITION鎖定塊，原封不動]
[RENDERING鎖定塊，原封不動]
[SHARPNESS鎖定塊，原封不動]
```

```
影象生成能力(prompt="...", title="<角色名>定臉", tag="character")
→ 返回資產歸檔標記（記下，供後續引用）
```

---

## 四、鎖定塊（逐字複製禁止改動）

### 身份引用語（墊圖時放prompt開頭，首次定臉不放）

```
以〈定臉資產歸檔標記〉作為該角色的身份參考，生成同一人物的全新影象，保持臉型骨相、下頜線、眼型、五官結構與參考完全一致。從頭渲染一張全新影象，不得直接複製或貼上參考圖。
```

### COMPOSITION

```
構圖（嚴格鎖定，逐條執行，標準證件照美顏近景）：
- 景別：頭頸緊景特寫。發頂緊貼畫框頂邊，頭頂上方無留白。畫框底邊切於鎖骨/上胸口。臉部高度約佔畫框垂直高度的55–60%。NOT拉遠至顯示肩膀、西裝身段或半身。
- 居中：頭部水平居中，面部中線（鼻樑）與畫框垂直中線精確對齊。臉在畫框內垂直居中。
- 髮型裁切：頭髮自然垂落兩側，左右兩側髮絲被畫框邊緣自然裁切——頭髮整體寬度超出畫框，只露出內側部分。
- 朝向：完全正面視角，頭部絕對水平，零偏轉零旋轉，雙眼直視鏡頭，下頜微收，頸部完整可見至鎖骨。
- 表情：[按角色氣質填寫分化，不套同一種表情。清冷女：神情平靜內斂，嘴唇輕合，不笑。治癒男：表情溫和放鬆，嘴角帶輕微自然微笑。]
- 畫幅：豎向3:4畫幅，左右對稱構圖。
```

### RENDERING

```
渲染：純淨無縫純白#ffffff背景。柔和電影感美顏布光，面部有自然的明暗塑形——額頭、鼻樑、顴骨保留清晰高光，臉側有柔和陰影，呈現三維立體體積感，NOT平光NOT均勻補光。皮膚溫潤通透，有豐富的subsurface透光感與自然膚色漸變，高階雜誌級寫實質感，豎向3:4畫幅。
```

### SHARPNESS

```
清晰度：將整個頭部渲染在同一個清晰焦平面內——臉部、眼睛、睫毛、耳朵、耳飾、髮際線及所有髮絲（包括頭部兩側的頭髮）全部同等清晰、對焦準確、細節完整，從臉部正面到兩側髮絲保持同等精細度。皮膚質感乾淨細膩，有自然肌理與極細微幾乎不可見的毛孔，真實但經過高階修圖級潤色。頭髮與耳朵NOT模糊NOT虛焦NOT失焦。透過高解析度與精細細節渲染實現均勻清晰，NOT靠壓平光影或降低對比度來實現。始終保留柔和電影感光線、臉側體積陰影與溫潤通透膚色。no淺景深效果，no模糊髮絲，no平板均勻布光，no灰白髮死的膚色，no粗糙坑窪皮膚，no重度放大毛孔，no過度磨皮塑膠感。
```

> **禁用詞**：prompt中嚴禁 `narrow aperture / large depth of field / no soft-focus / no bokeh on the face`——會觸發全域性平光、膚色發灰。全臉清晰只靠SHARPNESS塊。

---

## 五、服裝推理

**三步推理**：①看「適用人物」定品類（霸總→商務正裝；素人→精緻休閒；古風→漢服；甜妹→清新明快）②看「整體氣質」定調性（冷感→利落剪裁；治癒→柔軟針織）③統一升檔（高階/有質感/無logo/配色剋制）。

**硬規則**：

- **服裝風格絕不汙染臉**：OUTFIT調性只作用於服裝推理，絕不外溢到臉的骨相/五官/表情/肌膚。例外：角色卡在五官/氣質欄位直接寫了臉的特徵，或隨服裝配套的髮型/頭飾/妝容年代感（屬造型層不在遮蔽範圍）。
- **上衣絕不塞進下裝**：`untucked, worn loose over the waistband, never tucked into trousers or skirt`
- **男性褲型預設**：直筒或微闊垂墜長褲、褲長蓋腳面。`NOT tapered, NOT cropped, NOT skinny, ankles not exposed`。角色卡明確要求可破例。
- 無logo、配飾剋制（珍珠/銀/鑽/簡約表等）。反派可穿窮酸破舊。

**備選庫**：清冷千金→象牙白西裝+真絲內搭；霸總→硬挺黑/炭灰西裝+白襯衫領口微開；治癒熟男→燕麥針織或淺灰休閒西裝；甜妹→奶油色/淡彩針織；素人→質感純色T/白襯衫；古風→立領或交領漢服；長輩→軟肩西裝/優雅針織。

---

## 六、身材氣質校準（全身圖核心）

全身圖必須按角色定位自動校準四變數：①頭身比 ②身材量感 ③姿態氣場 ④服裝廓形。

### 頭身比（必須寫成實句，不能只寫數字）

- **女性統一7頭身**（禁止超8）：`natural well-balanced 7-heads-tall female proportion, the head about one seventh of the full body height`
- **男主/古風男/素人男：8頭身**：`well-proportioned 8-heads-tall figure`
- **霸總/強勢男：8.5–9頭身**（僅此型）
- **反派：不最佳化**：`realistic everyday body proportion, minimum 7 heads tall, NOT idealised or stretched, NOT a squashed compressed body, NOT an oversized head on a short stocky frame`（臉型骨相質量仍按準則F）
- **兒童：3–4頭身**：`cute chibi-leaning proportion, about 3 to 4 heads tall`

**雙向否定式（必寫）**：`keep the specified head-to-body ratio strictly; NOT a large head on a short body, NOT an exaggerated 8.5-9 heads elongated frame unless a 霸總-type male lead. Shoulders natural width (female ~1.6 head-widths, male ~2 head-widths).`

### 校準表

角色型身材量感姿態氣場服裝廓形**霸總/強勢男**tall slender 8.5-9 heads, long lean torso, long legs, low relaxed shoulder, lean NOT muscularcool languid editorial, weight on one leg, shoulders dropped, aloof gaze, one hand in pocketoversized dropped-shoulder suit, wide-leg trousers, NOT slim fitted**治癒/溫潤男**tall steady, naturally broad shoulders, healthy solidupright relaxed, warm easysoft knit/blazer, straight full-length trousers**高階素人男**natural healthy fitrelaxed naturalquality casual, straight full-length trousers**千金/清冷女**slim slender elegant, delicate uprightpoised cool composed, aloofminimalist sharp tailoring**甜妹/少女**petite slim youthfulsweet relaxed lightfresh light layered**高階素人女**natural healthy slimrelaxed naturalquality casual basics**古風男/女**upright dignified / slender gracefulserene classical poisehanfu robe, flowing**長輩男/父**mature slight fullness, solidcalm dignifiedrefined sober blazer, straight trousers**長輩女/母**mature graceful, slight softnesscalm gentle uprightelegant knit/blouse**反派男**per card, realistic NOT idealisedslack or stiff, petty mean airdated/cheap/shabby**反派女**per card, realisticsour stiff or slackgarish/shabby**兒童**chubby soft 3-4 headplayful childlikecute kidswear

**霸總氣場三要素（僅男主/霸總，絕不套女性）**：①大廓形服裝（oversize落肩西裝）②拉長比例（8.5-9頭身）③慵懶疏離姿態（重心偏一側/微slouch/aloof gaze/單手插兜）。女性統一7頭身，不拉長。

**男主身材原則**：氣場來自骨相+眼神+疏離姿態，不是肌肉。預設清瘦挺拔有骨相，不做健碩猛男（除非角色卡明確要求）。

---

## 七、全身立繪（一步法）

> 前置條件：定臉已透過確認門。

一次影象生成能力，資產參考傳入定臉資產歸檔標記，prompt開頭寫`〈定臉資產歸檔標記〉`鎖臉，畫幅`aspect_ratio: "3:4"`。

```
影象生成能力(
  prompt="Using〈定臉資產歸檔標記〉for face identity，同一人的全身站姿立繪，<頭身比實句+身材量感+姿態氣場+服裝廓形（第六節）>，雙向比例否定式，vertical 3:4 full-body portrait, head-to-toe inside frame, centered, plain seamless pure white #ffffff background，<SKIN/SHARPNESS鎖定塊>",
  title="<角色名>全身立繪", tag="character", aspect_ratio="3:4",
  資產參考=["<定臉資產歸檔標記>"]
)
```

比例壓不住退兩步法：先單獨生比例正確的全身模板資產節點，再連同定臉節點墊圖重出。

---

## 八、人物三檢視（可選）

16:9分屏：左半=全身三檢視（正面/側面/背面），右半=面部特寫。同時墊定臉+全身兩個資產歸檔標記。

```
影象生成能力(
  prompt="16:9 split-screen character board。使用〈定臉資產歸檔標記〉鎖面部身份、〈全身資產歸檔標記〉鎖身材/服裝/比例。左半屏三張等大全身圖並排—front/full profile/back，standard upright model stance；右半屏單張正面大臉特寫。same one person, identity consistent, identical face hairstyle outfit skin tone, plain seamless pure white #ffffff background.",
  title="<角色名>人物三檢視", tag="character",
  資產參考=["<定臉資產歸檔標記>","<全身定稿資產歸檔標記>"]
)
```

> 能力邊界項，可能需多跑或退分塊方案（左右各自單獨出再拼）。

---

## 九、表情九宮格（可選）

3×3九表情，畫幅`aspect_ratio: "3:4"`，墊定臉資產歸檔標記。

**預設表情順序**：面無表情/喜(抿嘴微笑)/怒/哀/樂(露齒)/悲(含淚)/震驚/憤怒/迷茫。

**關鍵規則**：近義表情做強度區分；頭全部擺正（不歪頭）；每格居中不切頂；防大小眼；一致性約束（same one person）；加深景深。

```
影象生成能力(
  prompt="使用〈定臉資產歸檔標記〉作為身份參考，same person in every panel, identical face hairstyle skin tone across all panels。九宮格：3x3 grid，每格只有表情不同：<九表情順序>。頭擺正/居中不切頂/防大小眼/近義表情強度區分/一致性/深景深。vertical 3:4 format, 3x3 grid evenly fills canvas. plain seamless pure white #ffffff background.",
  title="<角色名>表情九宮格", tag="character", aspect_ratio="3:4",
  資產參考=["<定臉資產歸檔標記>"]
)
```

> 能力邊界項，臉飄時降級：分兩次各出部分表情，或單表情逐張生成再拼。

---

## 十、補丁塊（按需追加）

### 補丁A · 純白底+髮絲邊緣

```
BACKGROUND (strict pure white with clean hair edges): completely clean seamless pure solid white #ffffff backdrop, no gradient, no grey, no off-white. Subject cleanly separated from background with sharp clean edges. Hair, hairline and outer strands must have clean sharp well-defined edges — NO wispy strands fading into background, NO semi-transparent hair edges, NO grey halo, NO foggy fringe. Keep natural volumetric light on face.
```

### 補丁B · 皮膚平整（僅皮膚髮糙時救急，必須配C一起用）

```
SKIN (smooth and even): clean smooth even-toned skin, minimal barely-visible pores, no rough bumpy surface, no visible blemishes, no enlarged pores — premium editorial skin, still looking real NOT plastic NOT waxy. Keep natural skin tone and soft volumetric light.
```

### 補丁C · 皮膚真實肌理（配B用或單用救"皮膚太平"）

```
SKIN (refined but real): clean translucent skin keeping real natural texture — fine subtle pores, soft surface micro-detail, healthy natural sheen, looking like genuine high-end-retouched real skin, NOT flat smoothed waxy plastic, NOT over-airbrushed poreless. Skin reads as real human skin, clean and free of blemishes but not perfectly smooth.
```

---

## 十一、3D漫劇質感補丁（「漫劇」觸發，與真人完全隔離）

觸發詞：「漫劇」「3D漫劇」「3D角色」「三維」「CG」「三渲二」——「漫劇」單獨出現即觸發。未觸發一律真人寫實，本節全部忽略。

**鐵律**：①整段替換，絕不把真人質感詞和3D質感詞混寫同一條prompt。②只覆蓋質感層，結構層（構圖/純白底/頭身比/確認門/資產參考）照常適用。③真人prompt絕不出現3D詞。

### 11.1 3D質感目標

- **畫風定性**：`high-end 3D CG character render, cinematic game-quality rendering, realistic-stylised 3D in the style of high-budget game cinematics or animated feature films, clearly a rendered CG character not a photograph, not flat 2D anime, not cartoonish`
- **皮膚-女性**：`semi-realistic 3D CG skin, between photorealistic and stylised — smooth clean surface with subtle subsurface scattering warmth, soft natural skin luminance, very fine barely-visible micro-texture and pores (present but refined, not raw), rendered skin that reads as beautiful and slightly elevated beyond real but clearly not a photograph — NOT flat poreless cartoon skin, NOT fully photoreal human skin, NOT wax or plastic finish, NOT milky white 2D-anime complexion, NOT flawless glass-skin with zero texture`
- **皮膚-男性**：`semi-realistic 3D CG skin with natural micro-detail, visible fine pores and subtle surface texture, warm subsurface scattering, rendered quality clearly above photographic — slightly elevated and refined but grounded in realism, NOT flat cartoon skin, NOT fully photoreal`
- **頭髮**：`3D-modelled hair with clean defined strands, soft specular sheen and structured flow, clearly CG-rendered, NOT photoreal flyaway hair, NOT flat 2D hair`
- **眼睛**：`luminous CG eyes with crisp catchlights, clear layered iris depth, slightly enhanced beyond real, clearly rendered not photographic`
- **光影/背景**：`clean three-dimensional CG studio lighting, clear volumetric light-and-shadow modelling, plain seamless pure white #ffffff background`

**3D質感校準線（介於真人與漫畫之間）**：目標質感參考——影視級遊戲CG（如《黑神話》《原神》高精度渲染檔位），皮膚有微細節但比真人更乾淨精緻，有subsurface但不是透明瓷感，明顯是渲染而非照片。**必須遠離**：①純白無瑕零質感的二次元瓷肌（太漫畫）②真實毛孔坑窪的寫真質感（太真人）③蠟像/塑膠感（過度磨皮）。

### 11.2 覆蓋表（啟用3D時）

真人原段3D替換為RENDERING裡photorealistic詞`high-end 3D CG character render, cinematic game-cinematic quality, clearly a rendered CG character not a photograph`SKIN段寫實膚質詞按性別取11.1皮膚詞（女性含NOT否定式必須完整寫入）SHARPNESS裡realistic skin一句換對應性別3D皮膚句，其餘清晰度內容保留準則E的85mm鏡頭質感`rendered with a virtual 3D camera, cinematic CG framing`

### 11.3 臉型（3D模式）

**防崩底線**（替代真人準則F強規則）：

```
FACE (minimal integrity floor only): both eyes present and roughly level, features not melted or fused, face not grossly distorted. NOT an overly long lower face, NOT an excessively elongated chin pulling the lower third too deep. Do NOT impose any preferred face shape or proportion. Let face shape vary freely per character.
```

**高審美導向**（必寫，與防崩底線並列）：

```
AESTHETIC (high-end, striking, memorable): a strikingly beautiful high-fashion-caliber CG face with a distinctive memorable look and strong screen presence, refined elevated features, editorial model-tier attractiveness — not a plain safe generic pretty face, each character visually distinct and unforgettable.
```

**差異化引導**（柔性，同真人準則G邏輯，分寸鐵律相同）：多角色拉開/單角色防模板/素人放開非標準五官。

### 11.4 3D模式呼叫示例（定臉）

```
影象生成能力(
  prompt="<CHARACTER:年齡+Chinese+氣質+五官+專屬記憶點，中文> <FACE防崩底線> <AESTHETIC高審美導向> <按性別取11.1皮膚詞> <3D頭髮詞> <3D眼睛詞> <OUTFIT中文> high-end 3D CG character render, cinematic quality, clearly CG not a photograph, not flat 2D anime. <COMPOSITION鎖定塊原文> <RENDERING鎖定塊：photorealistic詞換3D定性句> <SHARPNESS鎖定塊：realistic skin句換3D皮膚句> plain seamless pure white #ffffff background.",
  title="<角色名>定臉（3D漫劇）", tag="character"
)
```

全身/三檢視/九宮格3D版：在各自節基礎上按覆蓋表替換質感段，臉型換用11.3兩塊，其餘照舊。

---

## 十二、執行流程

1. **對齊方向**：讀取劇本基準檔案 `cast-style-{劇本名}.json`（存在則載入質感引數，不重新推理質感層；不存在則此為第一個角色）→ 定質感模式（真人or3D，見漫劇觸發規則）→ 判差異化（多角色拉開/單角色防模板）→ 欄位缺失用 向使用者提問確認 對齊，否則說明補全內容直接執行。

2. **拼prompt生成定臉**：按第三節拼接，三個鎖定塊逐字寫入，tag `"character"`，記錄資產歸檔標記。

3. **【確認門·硬性卡點】**：向使用者提問確認面部是否滿意，未明確透過前絕不生成後續資產。不滿意則改prompt重出再回確認門。多角色時全部面部確認後才統一往下。

4. **【4.5 劇本質感存檔】**（首個角色且基準檔案不存在時）：確認透過後立即用寫入檔案存檔 `cast-style-{劇本名}.json`，內容：質感模式/皮膚基準詞/渲染定性詞/3D檔位。劇本名取不到時向使用者提問確認。

5. **多選資產**：向使用者提問確認（multi_select）詢問要生成哪些：全身立繪/表情九宮格/人物三檢視。三檢視依賴全身，勾了三檢視未勾全身則先補全身。

6. **按選生成**：全身→第七節（3:4，墊定臉）；九宮格→第九節（3:4，墊定臉）；三檢視→第八節（16:9，墊定臉+全身）。

7. **收尾**：簡述每個產出（角色名+資產型別+資產歸檔標記），提示OUTFIT塊可替換造型重生成。

---

## 十三、邊界與硬規則彙總

- **純白#ffffff**：最高硬規則，所有資產所有步驟。
- **臉型骨相**：清晰利落下頜、上下臉協調，全形色（含反派）不降。服裝風格絕不汙染臉，只由五官+氣質欄位驅動。
- **頭身比**：女性統一7頭身（禁超8）；男主8/霸總8.5-9/素人男8/反派最低7/兒童3-4。必寫雙向否定式。
- **男褲**：預設直筒/微闊垂墜蓋腳面，禁束腳（角色卡明確要求可破例）。上衣絕不塞進下裝。
- **時裝大片拉長比例**：僅限男主/霸總，絕不套女性。
- **反派護欄**：NOT idealised只管身材量感/氣場，絕不波及臉型骨相。
- **確認門**：硬性卡點，未透過絕不生成後續資產。
- **鎖定塊**：寫入prompt時原封不動，不改不精簡。
- **劇本質感鎖定**：同一劇本所有角色質感統一，靠 `cast-style-{劇本名}.json` 檔案跨對話鎖定；後續角色讀取檔案複用質感層，不重新推理。

**臉型崩壞排查**：下半臉寬/方/鬆垮→①檢查準則F臉型詞是否寫入；②檢查反派NOT idealised是否誤外溢到臉；③加重否定式 `NOT a wide square heavy jaw, NOT a bottom-heavy sagging lower face`。

**虛焦/構圖排查**：頭髮耳朵虛焦→查SHARPNESS塊是否完整寫入；構圖漂移→查COMPOSITION塊+資產參考引用是否正確。prompt禁用 `narrow aperture / large depth of field`。
---
name: midjourney-wong-kar-wai-shanghai-elite-prompt
description: "Midjourney v8.2 繁花/王家衛風格轉譯層——把影視劇組語言（曖昧、窺探感、冷暖對撞、名媛與老錢風）翻譯成 MJ 真正接得住的名詞化提示詞。MJ 對「有哪些概念」敏感、對「概念之間是什麼關係」不敏感，必須有這一層轉譯。專精：七類轉譯對照表、前 1/3 權重前置、正向禁否定句、九十年代滬港精英造型錨定、950 字元嚴格限制與極簡引數尾。本 skill 負責把使用者想法翻譯成 MJ 聽得懂的純英文名詞集合。"
version: 3.3.1
product: SZDSAI
---

# Midjourney 繁花/王家衛光影生圖 Skill

**這是一層轉譯。**

使用者給出的是**拍攝想法**——曖昧、孤獨、紙醉金迷、光照在酒杯上、顏色壓到復古紅綠金。這些想法專業，但直接寫進提示詞，MJ 一句都接不住。

> **本 skill 乾的事只有一件：把所有的情感與關係，翻譯成具體的名詞與光影事實。**

## 一、工作流程

1. 接收使用者的畫面需求（包括：拍什麼、光給誰、佔比多少、幾個顏色、什麼在動、畫風等）。
2. 按七類轉譯對照表，將想法逐條翻譯成 MJ 能理解的名詞化描述。
3. 按 MJ 的組裝順序（主體→環境與光→動態事件→人物→表情與視線→鏡頭→引數尾）組合成完整提示詞。
4. 執行自檢，遇到細節過多時必須大刀闊斧地砍減次要元素，確保總字元數符合規則。
5. **輸出硬性要求**：輸出可直接複製使用的純英文提示詞（含引數尾），不附帶任何解釋、確認或選擇項。**最終輸出的全部英文提示詞（含引數尾，計空格）必須嚴格控制在 950 字元以內**。

## 二、七類轉譯對照表（核心資產）

### 統一原則：凡是「關係」，都要翻譯成「名詞」。

### 第一類：情緒／氛圍 → 畫面裡的動靜

**MJ 接不住的原因**：抽象情緒沒有對應的視覺實體。

使用者想法轉譯後的名詞化描述紙醉金迷中的孤獨她獨自坐在昏暗的卡座裡，畫面最前方是一個極度失焦的水晶威士忌酒杯，擋住了她一半的身體。曖昧、欲言又止煙霧在琥珀色的燈光中緩慢上升，她是畫面中唯一沒有移動的物體。

### 第二類：否定式指令 → 肯定的具體動作

**MJ 接不住的原因**：否定語義不可靠，寫 `not X`，模型經常直接把 X 畫出來。

❌ 否定式 (使用者想法)✅ 肯定式 (轉譯後)不要現代網紅臉她的面部極具九十年代復古特徵：濃密的波浪捲髮、深紅色的嘴唇與清晰的下頜線。不要死板的均勻打光一束溫暖的鎢絲硬光擦過他的側臉，將他的另一半臉完全隱入深邃的陰影中。

### 第三類：注意力物件 → 畫面最亮的那個名詞

使用者想法轉譯後的名詞化描述光照在酒杯上，人是暗的The crystal glass on the table catches a brilliant reflection—the brightest thing in the frame, brighter than his face, which remains in shadow.

### 第四類：相對佔比 → 百分比 + 畫面位置

使用者想法轉譯後的名詞化描述人物佔三分之一，要有窺探感she occupies about thirty percent of the frame, placed far right of centre, shot through a rain-streaked glass pane.

### 第五類：色板 → 兩個顏色 + 明度定位

❌ 錯誤寫法✅ 正確寫法繁花復古色調、低飽和Only three colors dominate the frame: warm amber gold, deep emerald green, and dark charcoal. Her red lips are the only saturated color in the shadow.

### 第六類：攝影哲學句 → 轉成畫面事實

使用者想法轉譯後的名詞化描述讓黑暗吞沒他The background remains completely unlit, wrapping his dark suit in pure silhouette.

### 第七類：想法順序 → 按權重重排

從左到右遞減：1 主體情境 → 2 環境光影 → 3 動態 → 4 人物造型 → 5 視線表情 → 6 鏡頭 → 7 引數尾。

## 三、六條鐵律

1. **正向裡絕不寫否定句**：要排除什麼，就去正面描述它的反面。
2. **總字元數（計空格）必須 ≤ 900 字元**：MJ 權重從左遞減，長文字會把關鍵決策稀釋。寫完必須合併同類項，刪減多餘描寫，確保加上尾部引數後總和絕不超過 900 字元。
3. **引數尾極簡**：**絕不允許**在末尾新增冗長的 `--no` 負向指令或版本引數，必須保持尾部絕對乾淨。
4. **場景型別決定一切**：寫錯環境錨點（如 bright modern cafe），堆多少復古詞彙都沒用。
5. **交付前掃敏感詞**。
6. **公式用來診斷圖，不用來生成圖**：先想具體畫面，再回頭套公式。

## 四、九十年代滬港名媛與精英（繁花光影）專項

此為本 Skill 的靈魂模組，用於錨定特定年代（如《繁花》中的黃河路、和平飯店）的階層質感、街頭煙火氣與王家衛式光影。遇到相關需求時，**直接從以下素材庫中提取純英文名詞短語進行組合**。

### （一）核心視覺語言：遮擋、窺探感與距離感

不要直接寫 "Wong Kar-wai style"。用具體的**機位與前景遮擋**製造氛圍：

- **玻璃與水汽**：`shot through a rain-streaked glass pane`（透過被雨水沖刷的玻璃拍攝）、`out-of-focus ribbed glass partition`（失焦的長條紋毛玻璃隔斷）、`shot through an out-of-focus ribbed glass partition`（透過失焦的長條紋玻璃拍攝）、`foreground blurred by a vintage wall sconce`（被複古壁燈失焦遮擋的前景）。
- **光斑與前景**：`heavy bokeh of warm neon signs in the extreme foreground`（極度前景處溫暖的霓虹燈失焦光斑）、`a plume of cigarette smoke drifting in the extreme foreground, partially obscuring the face`（極度前景處繚繞的香菸煙霧，半遮掩面部）。
- **線條切割**：`looking through half-closed Venetian blinds`（透過半閉的百葉窗窺探）、`a beaded curtain obscuring the lens`（遮擋鏡頭的珠簾）、`reflection in a vintage mirror`（老式鏡子裡的倒影）、`shooting from a dimly lit hotel corridor`（從昏暗的走廊深處拍攝）。

### （二）光影紀律：硬光、極暗部與冷暖色光對撞

徹底拋棄均勻打光。使用區域性硬光切碎畫面，讓大部分區域隱沒。

- **切割與輪廓**：`cinematic high-contrast chiaroscuro lighting`（電影級高反差明暗光）、`a harsh slit of light cutting across the eyes`（一道切過雙眼的銳利硬光）、`a warm amber tungsten lamp creates a glowing rim light on her hair`（琥珀色鎢絲燈在髮絲邊緣打出輪廓光）、`heavy side light illuminating only half of the face`（強烈的側光僅照亮半張臉）、`subject emerging from deep shadow`（主體從濃重的陰影中浮現）。
- **色彩對撞**：`warm tungsten practical lights contrasting with cool cyan street neon`（室內暖鎢絲燈與室外冷青色街頭霓虹的對撞）。
- **深邃暗部**：`deep emerald green-tinted shadows`（泛著深翡翠綠的暗部）、`background wrapped in pure silhouette`（背景隱沒在純粹的剪影中）。

### （三）造型錨點：精英的剋制 vs 名媛的張力

精準到材質和剪裁，避免使用現代服飾詞彙。

- **男（老錢/寶總風）**：
  - **服裝**：`tailored dark charcoal double-breasted wool suit with wide peak lapels`（深灰雙排扣寬戧駁領羊毛西裝）、`classic pinstripe suit`（經典細條紋西裝）、`camel hair overcoat draped over the shoulders`（披在肩上的駝色大衣）、`crisp white shirt with a subtly patterned silk tie`（白襯衫配暗紋真絲領帶）、`He wears a tailored dark charcoal double-breasted wool suit with wide peak lapels, a crisp white shirt, and a subtly patterned silk tie. His hair is slicked back cleanly with pomade.`（深灰雙排扣寬戧駁領羊毛西裝、白襯衫、真絲領帶、髮膠大背頭）。
  - **髮型與細節**：`hair slicked back cleanly with pomade`（一絲不苟的髮膠大背頭）、`vintage mechanical watch on the wrist`（手腕上的復古機械錶）、面部輪廓凌厲（`sharp jawline`）。
- **女（名媛/老闆娘/李李風）**：
  - **服裝**：`tailored black velvet evening dress with structural shoulder pads`（黑絲絨墊肩晚禮服）、`luxurious black faux fur coat`（奢華的黑色環保皮草大衣）、`elegant backless design`（優雅的大露背設計）、`deep red silk cheongsam`（深紅色真絲旗袍）`backless black velvet dress with gold chain draped across the bare back`（帶有金鍊垂墜的露背黑絲絨裙）、`black silk qipao with gold embroidery`（黑絲綢金線刺繡旗袍）、`floral silk cheongsam`（繁花絲綢旗袍）、`black chiffon blouse with heavy silver sequin plunging V-neck`（重工銀色亮片深V黑雪紡衫）、`abstract patterned silk slip dress`（抽象印花絲綢吊帶裙）。
  - **髮型與妝容**：`classic 1990s Hong Kong voluminous wavy curls`（90年代港風蓬鬆大波浪卷/手推波紋）、`deep matte red lips`（深紅啞光唇）。
  - **珠寶配飾**：`heavy diamond choker`（重工鑽石頸鍊）、`bold vintage gold earrings`（誇張的復古金耳環）、`emerald rings`（祖母綠戒指）、`layered silver necklaces`（層疊的銀色項鍊）。

### （四）場景物料：屬於那個時代的質感錨

用具體的年代物件錨定空間，拒絕現代極簡。

- **繁華內景（和平飯店/至真園/私密包間）**：`heavy crystal whiskey glass catching the light`（折射光線的水晶威士忌杯）、`vintage fringed lampshades`（復古流蘇檯燈）、`dark mahogany wood panels`（深色桃花心木護牆板）、`ornate patterned wallpaper in deep shadow`（隱沒在暗部的繁複花紋壁紙）、`leather booth seating`（真皮卡座）、`dark staircase with patterned carpet`（鋪著花紋地毯的幽暗樓梯）、`vintage oil painting with an ornate gold frame`（帶有華麗金框的復古油畫）、`carved wooden desk`（雕花木書桌）、`deep red bedsheets on a classic wooden bed`（古典木床與深紅色床單）。
- **煙火街頭（黃河路夜市）**：`out-of-focus glowing neon shop signs with traditional characters`（失焦發光的繁體霓虹招牌）、`steaming food stalls in the background`（背景中冒著熱氣的小吃攤）、`wet asphalt reflecting warm streetlights`（反射著暖色路燈的潮濕柏油路）`out-of-focus glowing neon shop signs with traditional characters`（失焦發光的繁體霓虹招牌）、`steaming food stalls in the background`（背景中冒著熱氣的小吃攤）。

## 五、MJ 的提示詞結構與強制砍伐優先順序

當生成的提示詞**逼近或超過 900 字元（計空格）**時，按以下順序無情砍伐：

1. 徹底刪除任何攝影哲學句、渲染約束意圖宣告（最先砍）。
2. 徹底刪除環境中無助於表達情緒的次要陳設。
3. 徹底刪除服裝的非關鍵花紋、材質等細枝末節描寫。\
   **永不砍**：第一句畫面 · 光與最亮處 · 動態事件 · 佔比與 off centre · 核心造型。

## 六、Midjourney 參數列（嚴格鎖定長尾）

**預設引數尾（固定，直接附加在提示詞最後，不加任何額外解釋）：**`--ar 16:9 --hd --s 250`

*注：除上述三項外，嚴禁系統自動追加* `--v 8.2`*、*`--exp`*、以及任何以* `--no` *開頭的負向詞彙，確保字元預算留給畫面描述。*

## 七、自檢清單（內部強制執行）

輸出前進行終極檢查，如有違規立刻重寫：

- \[ \] **最終輸出的全部英文提示詞加上引數尾的總字元數（計空格）是否嚴格控制在 900 字元以內？（超過必須刪減次要物品細節）**
- \[ \] **引數尾是否只含純淨版的** `--ar 16:9 --hd --s 250`**？（絕對不能有** `--v`**、**`--exp` **或** `--no` **片語）**
- \[ \] 正向裡沒有任何 `not / no / without` 句式。
- \[ \] 第一句是完整的畫面事實。
- \[ \] 有明確的前景遮擋物或失焦的光斑。
- \[ \] 明確了極亮與極暗處的對比（如 rim light, deep shadow）。
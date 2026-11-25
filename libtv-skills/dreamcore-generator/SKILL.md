---
name: dreamcore-generator
description: "從概念到成片一體化創作夢核視覺短片"
---

## 一套夢核 look + 三檔情緒(開拍前卡選情緒檔,全片統一)

dreamcore 只有**一套 look**(低飽和、低對比、抬黑位、高柔光、35mm 顆粒、超現實但寫實),靠**情緒檔**調粉/藍配比與冷暖。下面英文子句直接取用:**「調色子句」用於 MJ 場景圖,「前置風格句」放在 Seedance prompt 第一句。**

### 甜暖懷舊(warm,偏粉)

- 調色子句:`dreamcore aesthetic, surreal yet photorealistic, desaturated washed-out pastel grade leaning blush-pink and cream, warm hazy afternoon glow, soft diffused light with gentle bloom, lifted matte blacks, low contrast, fine 35mm film grain, gentle soft focus`
- 前置風格句:`Warm dreamcore music video frame, surreal yet photorealistic, blush-pink and cream desaturated pastel palette, soft hazy afternoon glow with gentle bloom, lifted matte blacks and low contrast, fine 35mm grain, weightless dreamy slow motion.`

### 空靈純淨 / 失重憂鬱(cool,偏藍)

- 調色子句:`dreamcore aesthetic, surreal yet photorealistic, desaturated washed-out pastel grade leaning powder-blue and lilac, cool misty pale silvery light, soft diffused glow, lifted matte blacks, low contrast, fine 35mm film grain, gentle soft focus`
- 前置風格句:`Cool ethereal dreamcore music video frame, surreal yet photorealistic, powder-blue and lilac desaturated pastel palette, cool misty pale light with soft glow, lifted matte blacks and low contrast, fine 35mm grain, weightless dreamy slow motion.`

### 微寒夢魘(uneasy,灰藍)

- 調色子句:`dreamcore aesthetic, surreal yet photorealistic, muted desaturated palette leaning grey-blue, flat overcast soft light, faint emptiness and stillness, lifted matte blacks, low contrast, fine 35mm film grain, gentle soft focus`(仍柔光低飽和,靠空曠/靜止表達不安,不加恐怖元素)
- 前置風格句:`Faintly uneasy dreamcore music video frame, surreal yet photorealistic, muted grey-blue desaturated palette, flat overcast soft light, a sense of empty stillness, lifted matte blacks and low contrast, fine 35mm grain, weightless slow motion.`

---

## 固定種子與出圖規格(速查)

> **全域性預設**:MJ 畫質"自適應"、Lib Image"標準畫質";**每條 MJ prompt ≤ 1024 字元**;所有 MJ 場景圖統一 **V8.2**。提示詞**英文書寫**(引數/種子程式碼保持原樣)。

- **造型圖 = Seedream 5.0 Pro**(**2K、無任何尾串/引數**):出**一張 16:9、白底的造型圖,從左到右橫排 4 個全身造型、4 套明顯各不相同**,真人模特、臉與全身清晰;使用者從這 4 個裡**選 1 個**(選中鎖為全片主造型)。**有造型參考圖則作 Seedream 的圖參考;人像/人臉參考圖一律不喂 Seedream。** prompt 英文自然語言(性別/人種/造型方向 + 著裝/人物底線),**不帶任何** `--sref` **/** `--ar` **/** `--v` **/** `--no` **尾串**。\
  示例:`one 16:9 2K white-background styling sheet; the same [gender] [ethnicity] real adult model shown as four different full-body looks side by side, four clearly distinct outfits, all in the chosen mood's dreamcore styling direction (甜美懷舊 sweet doll / 空靈純淨 all-white nightwear+JK / 微寒夢魘 icy powder-blue — 見「造型語言」); for a male subject swap any skirt for trousers, keep the same fabrics and elements; clear face and full body, natural hands; modest tasteful fully-covered outfit, high modest neckline, opaque non-transparent fabrics, knee-length or longer skirt (or with matching modesty shorts); clean skin with no tattoos and no piercings; pure white seamless background, even soft studio light, photographic`
- **三檢視 = Lib Image**(強制,預設**標準畫質**),造型確認後**據所選那套全身造型擴寫 16:9 白底全身三檢視**。**硬性:必須把使用者選定的那張 Seedream 造型圖作為圖輸入 / 參考連線接入 Lib Image**——不連線三檢視會另起爐灶、與所選造型對不上,整步作廢;三檢視的**款式 / 顏色 / 廓形 / 面料 / 比例(及無人像時的臉)必須與所選造型圖逐項一致**,只補出側 / 背視角。**真人模特**;**排版強制:所有內容在一張圖內、16:9,全身左/中/右三視(正/側/背),不放頭部特寫/大頭**;**有人像參考圖→三視人臉用純白圓形貼紙完全遮住 + 右下角中文小字「人臉單獨提供 · 此圖僅用於服裝造型參考」**(真臉由原圖在 Seedance 鎖)、**無人像參考圖→保留所選那套 Seedream 造型的臉**(臉即身份)。\
  要點:`using the selected styling image as image input/reference, expand it into a single 16:9 white-background turnaround; keep the exact same outfit (style / color / silhouette / fabric) and proportions as the input, only three full-body views — left / center / right (front / side / back) of the same real adult photographic model, no head close-ups, infer side and back consistently, clean skin no tattoos no piercings, pure white seamless background, even soft studio light, photographic`。**有人像參考圖時**:`cover each face with a plain solid white circular sticker, add a small Chinese caption at the bottom-right: 人臉單獨提供 · 此圖僅用於服裝造型參考`(無人像則保留臉、不加貼紙與標註)。
- **場景圖 = Midjourney V8.2**(預設**自適應**,prompt ≤ 1024 字),**固定 dreamcore 種子** `--sref 4658243766 --profile yp7vzjb`,**全景無人、零文字、超現實但寫實**。\
  尾串:`… --sref 4658243766 --profile yp7vzjb --ar <16:9|4:3|9:16> --v 8.2 --no text, words, letters, numbers, captions, signage, logo, watermark, extra patterns, cartoon, illustration`
- **影片 = Seedance 2.5**,輸入 = 場景圖 + 白底三檢視(鎖造型/身形)+ **人臉參考**(有人像參考圖→原圖/影片;無人像→所選那套 Seedream 造型的臉;**人像參考圖不喂造型模型、只在此處喂**)+ **對口型段的音訊切片(連線到音訊輸入口)**。

---

## 流程(逐階段暫停確認)

### 階段 0 · 開拍前(一張問詢卡,問完停下等上傳)

**開拍前問詢卡(下面每一問都是「獨立一問」,同一張卡里一問接一問;絕不把兩問揉進同一問的選項,也不拆多張卡;條件問不適用時讓使用者"留空/跳過")。問完停下等使用者上傳音訊/參考圖。**

1. **音訊(單選)**:你有現成的歌曲 / BGM 嗎?——`我有,稍後上傳` / `沒有,幫我生成`。
2. **歌曲風格 + 主題(自由輸入;僅第 1 問選"沒有"時填,有音訊留空)**:想要什麼風格與主題?(dreamcore 曲風走 **dream pop / ambient / bedroom pop**,朦朧慢板大混響)
3. **人聲(性別 + 語言)**:人聲用哪種?**性別(男 / 女)+ 演唱語言**(中文 / 英文 / 韓文 / …)。(上傳音訊可聽辨預填,可改)
4. **有無人像 / 造型參考圖**:有人臉參考圖(或 &lt;15s 影片)/ 造型參考圖嗎?——**只要有人像參考圖 → 主角性別、人種一律以參考圖為準,第 5 問留空**;沒有則第 5 問照填。
5. **角色人種(自由輸入;僅第 4 問"沒有人像參考圖"時填)**:按第 3 問語言推薦(中文→亞洲、英文→歐美、韓文→亞洲…),可改。
6. **字幕**:成片要不要字幕?要→選語言;不要→無字幕。(字幕只在階段 5 疊加,生成畫面永遠零文字)
7. **情緒檔**:甜暖懷舊 / 空靈純淨 / 微寒夢魘(定粉/藍配比)。
8. **畫幅**:16:9 / 4:3 / 9:16?
9. **畫質**:480p / 720p / 1080p?

> **結論**:**主角性別 = 人聲性別**;**人種 = 有人像參考圖→隨參考圖(第 5 問留空)/ 無→按語言推薦並經使用者確認**;**不單獨問性別/人種,時長也不問**(由【選段】定)。9 問全在這一張卡里、一問一件事、各給各的乾淨選項。

**音訊就緒 / 音樂確認(先於切片)**:

- **有音訊** → 用使用者上傳的音訊。
- **無音訊** → 按風格/主題 + 人聲(性別/語言)生成一版帶歌詞人聲(**曲風走 dream pop / ambient / bedroom pop**)→ **生成後暫停,等使用者確認音樂滿意**(可重做/微調),滿意才切片。(生成時風格欄位與歌詞欄位分開,別把描述詞當歌詞唱;音樂提示詞 ≤ 1024 字。)

**音訊確認後必做兩步(先於分鏡與生影片)**:

- **① 音訊切片(+ 拿歌詞)**:切成**多段連續、每段 ≤15s 的切片**(按對應影片秒數切分),同時**拿準確歌詞——只供內部對齊口型/選段,絕不寫進任何發給模型的 prompt**;對口型段每段切片將作**音訊錨點連線喂 Seedance 2.5 驅動口型**。**切完停下等使用者確認切片。**
- **② 選段**:問"**你想用哪幾段來做這支 MV?**"。**推薦連續的幾段(每段 ≤15s)**(便於段間銜接);**推薦挑有人聲/歌詞的段做對口型,純器樂段預設不做 lipsync**(器樂段只做夢核表演、不唱)。**選完即自動算出時長(= 各段秒數之和 = 影片段數),不再問"想做多長"**;段數由此步確定。

**造型分流(按 Q4 有沒有上傳人像 / 造型參考圖,走四種情況;都先"理解造型方向 + 結合下方造型語言補寫成完整 spec",不丟圖照搬。統一流程:Seedream 出一張 16:9 白底 2K 橫排 4 造型 → 使用者選 1 → Lib Image 據所選造型擴寫三檢視)**:

> **鐵律:人像/人臉參考圖一律不喂造型模型(Seedream)**(Seedream 只接受**造型參考圖**作圖參考);**人臉參考圖只在最後 Seedance 生影片時**與三檢視一起喂(鎖真臉;**髮型由使用者選:保持參考圖髮型 / 換成三檢視髮型**)。**三檢視人臉怎麼處理只看"有沒有真人像參考圖":有→純白圓貼遮臉 + 右下角中文小字標註,無→保留所選 Seedream 造型的臉。**

- **① 只有人像參考圖**:人像**不喂 Seedream**;Seedream 按文字 spec 出四造型(無尾串)→ 選 1 → Lib Image 三檢視、**人臉純白圓貼完全遮住 + 右下角中文小字「人臉單獨提供 · 此圖僅用於服裝造型參考」**;人像**僅 Seedance 時**與三檢視一起喂(鎖真臉;**髮型使用者選**)。
- **② 只有造型參考圖**:造型圖**作 Seedream 圖參考** + 補寫 spec → Seedream 出四造型 → 選 1 → Lib Image 據所選造型**人臉+造型**出三檢視、**人臉不打碼**(所選造型的臉即身份、也作 Seedance 人臉參考)。
- **③ 人像 + 造型都有**:**只把造型圖作 Seedream 圖參考、人像不喂** + 補寫 spec → Seedream 出四造型 → 選 1 → Lib Image 三檢視、**人臉純白圓貼遮住 + 右下角中文小字標註**;人像**僅 Seedance 時**與三檢視一起喂(鎖真臉;**髮型使用者選**)。
- **④ 都沒有**:用**據人聲語言+性別推薦、使用者確認過的人種 + 性別** + 補寫 spec,Seedream 出四造型(無尾串)→ 選 1 → Lib Image 三檢視、**人臉不打碼**(所選造型的臉即身份、並作 Seedance 人臉參考)。**不單獨問性別/人種。**

**dreamcore 造型語言(補寫 spec 時對齊;英文書寫;按三檔情緒各一套、彼此拉開區分;全性別通用——男生把裙裝一律換成褲裝,面料/元素/色系不變;皮膚無紋身無穿孔;裙長守底線=及膝或更長 / 或配同色系安全褲)**:

- **甜美懷舊(warm,偏粉 / 杏 / 奶)** — 參考:娃娃領、蕾絲紗裙、瑪麗珍娃娃鞋、可愛頭飾:\
  `nostalgic sweet doll styling — peter-pan / doll collar blouse, layered tulle tutu skirt (knee-length or with matching modesty shorts) or soft layered chiffon skirt, mary-jane doll shoes, striped or lace knee socks, ribbons / bows / patchwork hair accessories, soft bangs; warm pastel palette (blush-pink, apricot, cream); vintage doll-like sweetness`男:裙 → `soft tailored pastel trousers or cropped pants`,保留娃娃領上衣、緞帶/蝴蝶結髮飾(從簡)、瑪麗珍風鞋,同色系與面料不變。
- **空靈純淨(白色系為主)** — 參考:睡衣元素、jk 校服元素、純白層疊:\
  `ethereal all-white styling — nightwear-inspired layered white blouse with lace-trim bloomers, plus JK school-uniform elements (knee-length pleated skirt, sailor / doll collar, ribbon tie), soft chiffon layers, white knee socks, delicate white hair piece; pure innocent airy vibe; monochrome white / off-white / cream palette`男:裙 → `white JK-style shirt with ribbon tie and tailored white trousers, or white pajama-style layered shirt with lace-trim trousers`,同為純白、睡衣/校服元素與柔紗面料。
- **微寒夢魘(淡藍 / 冷色系為主)** — 參考:淡藍按扣背心裙、荷葉泡泡袖、手套、星星髮飾:\
  `cool-toned dreamcore doll styling in icy powder-blue — button-front pinafore or vest over a white ruffle puff-sleeve top, matching gloves, star / snowflake hair clips, pleated hem (knee-length or with matching modesty shorts); faintly cold pristine uneasy mood; cool pastel palette (powder-blue, ice-blue, cool grey)`男:裙 → `icy powder-blue button-front vest over a ruffle-cuff shirt with matching tailored trousers and gloves`,同為冷調淡藍、按扣/荷葉元素。

最多一個稍亮點綴色,其餘壓在該檔色系裡;守著裝底線(端莊全覆蓋、無紋身穿孔、穿裙配同色系安全褲)。**這三套造型與上面三檔情緒的「調色子句/前置風格句」一一對應**。

### 階段 1 · Final_Video_Spec(已併入開拍前卡)

情緒檔 / 畫幅 / 畫質**已在開拍前那張卡里問過**(第 7\~9 項),此處不再另開卡。**時長不問——段數/總長由【選段】確定**(選了幾段 ≤15s = 幾段影片 = 總長),每段 = 一條 ≤15s,裝配順接。粗糲/夢感靠顆粒與調色,不靠低解析度。

> spec 隨卡一併確認,無需單獨暫停。

### 階段 2 · 故事板

- **造型圖**:按四種情況用 **Seedream 5.0 Pro 出一張 16:9 白底 2K、橫排 4 個不同全身造型**(**無尾串**;只造型參考圖作圖參考、人像不喂)→ 使用者**從 4 個裡選 1** → **暫停確認** → 用 **Lib Image 據所選造型擴寫 16:9 白底三檢視**(**硬性:必須把選定的那張 Seedream 造型圖作為圖輸入/參考連線接入 Lib Image**,不連線三檢視會跑偏、與所選造型不一致、整步作廢;三檢視款式/顏色/廓形/面料/比例與所選造型圖逐項一致;真人模特;**一張圖內、全身左/中/右三視、不放大頭**;**有人像參考圖→人臉純白圓貼遮 + 右下角中文小字標註、無→保留臉**)→ **再暫停確認**。**造型守底線**(端莊全覆蓋、不大面積透明、高領、裙及膝或更長、皮膚無紋身無穿孔)。**全片服裝造型鎖定不變;僅使用者明確要求換裝時才再出"造型1/造型2"**。

- **場景**(緊接三檢視確認後):按選定段數(= 地點數)**先給 3–4 個開放場景選項、也允許自描述 → 使用者選定用哪幾個場景後立即按階段 3 出圖**;自描述則照其意 + 套情緒檔調色 + 零文字 + 全景無人 + 超現實但寫實。同一地點多分鏡共用選中那 1 張。

- **分鏡指令碼(生影片前必出、需確認,用表格)**:逐段逐鏡列,列固定為 **段/鏡號 | 音訊切片(段級) | 畫面(角色表演 + 場景 + 裂縫)| 時長(s)| 運鏡(手持/升格)| 表演/表情 | 與上下段銜接**。**每段第一列後緊跟「音訊切片」列,寫清本段用**哪條切片\*\*(切片編號)+ **有人聲(→對口型)/ 器樂(→不對口型)**——生影片時照此把該切片連線接入 Seedance,把音訊寫進表能顯著降低"漏連音訊、口型/BGM 全丟"的機率。示例:

  段/鏡音訊切片畫面時長(s)運鏡表演/表情銜接1-1切片①(有人聲→對口型)主角已在泳池間水面上,近景,開口跟唱4慢 push-in緩睜眼、輕呼吸、口型對上歌詞開場即含人、不空鏡1-2↑ 同段切片①連續運鏡升起,中景4升格髮絲飄動、若有所思承上鏡方向連續運鏡2-1切片②(器樂→不對口型)走入花海,中景4慢平移不唱、輕旋身承 1 段末鏡:主體位置/運鏡方向延續

  **每 15s ≥4 鏡**,標升格落點;**第一鏡不要空鏡——角色一開始就在畫面**;**多段時每上下兩段(上段末鏡 ↔ 下段首鏡)必須有邏輯 / 鏡頭語言關聯**(動作承接、構圖呼應、運鏡方向、主體位置/情緒銜接),讓段間乾淨切也順;**全片不疊化**。**每段的「音訊切片」是階段 4 連線的依據——按表把對應切片連到 Seedance 音訊輸入口(硬性)。**

- **音樂(階段 0 已就緒:繫結/生成 + 切片 + 選段)**:此處按**所選各切片**的節拍標轉場/升格落點;並標出**哪些段做對口型(有人聲)、哪些器樂段不做**。

> 暫停確認(造型圖 + 三檢視 + 場景圖 + 分鏡指令碼 +(無音訊時)音樂)。

### 階段 3 · MJ V8.2 場景圖(在三檢視確認後緊接執行)

描述選定的全景空場景(空間型別 + 佈局 + 重要物體 + **一道超現實裂縫** + 構圖),**超現實但照片級寫實、不含人、零文字/logo/圖案**,套所選情緒檔調色子句,接場景種子尾串(見速查)。**使用者選定用哪幾個場景後立即出圖**:各地點各 1 組 4 張全景,**可一次性同時生成多組**,不必逐個序列等待;生成後**每個地點各自四選一**。同一地點多分鏡共用選中那 1 張。

> **每個地點都必須四選一確認**(可一起出、分別選);所有場景確認後再進入下一階段。

### 階段 4 · Seedance 2.5 影片(每段一條,時長=該段音訊向上取整後裁剪,一條一條生)

prompt 結構(順序,英文書寫):

1. **前置風格句**(按情緒檔取甜暖/空靈/微寒,全片統一)。
2. **角色組裝 + 首幀含人物**:三檢視鎖造型/身形 + 人臉參考(**有人像參考圖→原圖/影片鎖真臉;髮型先問使用者:保持參考圖髮型 / 換成三檢視髮型,按選擇寫進 prompt。無人像→以三檢視為主,臉與髮型取自它**)。寫明"臉取自人臉參考、造型取自三檢視、髮型按使用者所選、放進場景圖,保留真實長相"。**場景圖當"空間/風格參考",不要當成必走的空場首幀——第一鏡角色就在畫面裡**,prompt 明確 `the character is already present in the very first frame, open on the subject (medium/close), do NOT begin with an empty room establishing shot`,避免開頭空鏡。**合規**:端莊全覆蓋、不大面積透明、高領、裙不過短、皮膚無紋身無穿孔;**穿裙寫** `wearing matching-tone modesty shorts underneath, fully covered and modest`。**服裝造型與三檢視完全一致、全片全程不變。**
3. **對口型 + 音訊連線(有人聲的段)**:**照分鏡表格該段「音訊切片」列,把對應切片節點連線到 Seedance 2.5 的音訊輸入口**——硬性,不連線口型驅動與 BGM 都拿不到、整段廢掉(表裡已寫清用哪條切片、是否對口型,照做即可)。把該段 **≤15s 音訊切片作音訊錨點接入**,人物**嘴型/下巴與傳入音訊完全一致**(`lips and jaw precisely synced to the incoming audio, natural gentle singing expression, dreamy and soft`);**嚴禁把真實歌詞寫進 prompt**;**純器樂段角色不唱、但該段切片仍連線接入並作 BGM 保留**(`no singing, dreamy performance only`——不要寫任何"無音樂/無 BGM")。
4. **分鏡**:`Shot1 …(camera continues / slowly moves to)… Shot2 …`,一條連續(時長=該段音訊向上取整)、**≥4 鏡**;鏡頭間靠**連續運鏡/緩慢移動銜接**或少量**乾淨卡切**;**禁止寫 dissolve / 疊化 / 淡入淡出 / morph**(AI 生成疊化通常糊髒)。每鏡 = 景別 + 運動(慢手持/升格)+ 表演。
5. **運動**:`slow dreamy camera, natural handheld with subtle breathing motion`;升格鏡 `slow motion / overcranked, weightless floating`;一鏡到底僅按需。
6. **音訊 + 時長 + 零文字**:生成畫面**始終零文字/logo/無燒錄字幕**(字幕如需在階段 5 按所選語言疊加)。**每段靠連線接入的音訊切片驅動口型 + 作 BGM**;**prompt 絕不出現** `no music` **/** `no audio` **/** `no sound` **/** `no BGM` **/** `無音樂` **這類字樣**(會壓掉口型與 BGM);傳入音樂一律作 BGM 保留、不改原音訊、**不寫真實歌詞**;器樂段只寫"角色不唱、只做表演"。**時長 = 該段音訊向上取整到整秒**,階段 5 再按音訊實際時長裁剪。負面 `text, words, letters, numbers, logo, watermark, extra patterns, cartoon, illustration, stiff, rigid, frozen, robotic motion, dissolve, crossfade, fade transition, morph, tattoo, piercing`(合規靠**正向詞**實現,負面**不寫**任何涉黃/暴露敏感詞、也**不寫 no music/no BGM**)。

**表演預設**(使用者沒寫時按 dreamcore 注入,每鏡≥1 表情+1 動作,慢/輕):`serene wistful presence, slow ethereal movement, gentle gaze drifting, weightless dreamlike detachment, soft turning of the head, dress and hair drifting`。\
**通用治僵硬(每鏡都加)**:`subtle breathing with chest gently rising and falling, hair and fabric micro-movement, expression slowly shifting (e.g. serene → faintly wistful), a slow soft blink, relaxed natural posture, natural unhurried lifelike movement easing in and out`(對口型時 `jaw and lips actually moving to the incoming audio`)。

> 一條一條生,逐條確認。

### 階段 5 · 裝配(video_assembler)

多段順接時,**每兩段銜接處用乾淨切,但靠邏輯 / 鏡頭語言承接**(匹配動作 / 構圖 / 運鏡方向 / 主體位置 / 情緒,見分鏡指令碼)讓切口順;**全片不允許出現疊化 / 溶解 / cross-fade**(夢核也不閃切、不閃大字);**字幕/標題只疊加、絕不燒進生成畫面**;logo PNG 可疊;**每段按該段音訊實際時長裁剪**(生成時向上取整、此處裁回)。**音樂:不要把原音樂當單獨一軌再拼進去——直接沿用各段生成影片裡已自帶的音樂**(生成時喂入並原樣保留的那段音訊),各段連自帶音軌一起順接即成連續配樂,口型與音樂完全對應、全片連續。**字幕(僅當卡里選了"需要")**:按所選語言把字幕**疊加**在成片上(只疊加、不燒進畫面)。引導匯出。

---

## 參考資料

### 節奏 → 每 15s 鏡數(dreamcore 版,硬底線 ≥4,以連續運鏡銜接為主)

情緒/節奏鏡數轉場與手法極慢空靈4一鏡流動式連續運鏡為主、幾乎不切;長鏡 + 升格,靠微動與表演不滯留慢板抒情4–5連續運鏡銜接為主,偶爾乾淨卡切;升格落點明確中速律動5–6連續運鏡 + 少量卡拍乾淨切;長短鏡交替

> 無論幾鏡,都在一條 ≤15s 裡一次性生成;**鏡頭間靠連續運鏡銜接,全片不做疊化/溶解**;段間靠承接的乾淨切,別全程生硬硬切。

### 場景庫(每情緒檔取傾向,均為全景無人、含一道超現實裂縫、超現實但寫實)

- **甜暖懷舊**:懷舊少女臥室 · 室內泳池間 · 花海/草地 · 舊商場中庭 · 陽光客廳。裂縫:水面映出不存在的雲、漂浮的泡泡、過曝到發光的窗。
- **空靈純淨 / 失重憂鬱**:雲朵/天空臥室 · 無盡白走廊 · 水下房間 · 鏡面無盡空間 · 紗幔房間。裂縫:失重漂浮、走廊無限延伸、水與空氣界限消失。
- **微寒夢魘**:空教室 · 舊 CRT 客廳 · 鏡屋 · 霧中空曠場 · 靜止的遊樂場。裂縫:會動的靜物、停住的舊鐘、鏡中慢半拍的倒影、霧裡的靜止。

> "超現實裂縫" = 反常倒影/漂浮物/無盡延伸/會動的靜物/過曝光斑等(超現實但寫實,不血腥不驚悚)。長片地點不夠可重訪同一地點(換光線/裂縫)。

### 注意

- **開拍前只用一張問詢卡**(音訊有無 → 曲風+主題\[僅無音訊\] → 人聲性別+語言 → 有無人像/造型參考圖 → 人種\[僅無人像\] → 字幕 → 情緒檔 → 畫幅 → 畫質);**主角性別=人聲性別、人種按語言推薦、時長由選段定,都不單獨問**;問完停下等上傳。
- **無音訊先生成音樂(dream pop/ambient)→ 暫停等使用者確認滿意 → 才切片**;切完確認切片,再選段。風格欄位與歌詞欄位分開,別把描述詞當歌詞唱;音樂提示詞 ≤ 1024 字。
- **音訊·口型·BGM(核心)**:切片(≤15s、連續)+ **拿準確歌詞僅內部對齊、絕不寫進 prompt** → 選段定時長;**生影片必須把選定音訊切片連線到 Seedance 2.5 音訊輸入口(硬性)**、作音訊錨點驅動口型;prompt 只寫"口型與傳入音訊一致"、**不寫真實歌詞**;**傳入音樂作 BGM 保留、不改原音訊、prompt 不寫 no music/no BGM**;**生成時長=音訊向上取整→按實際裁剪**;器樂段不唱但切片仍連線作 BGM。**最終合成用各段生成影片自帶音樂、不拼原音樂單獨軌。**
- **模型**:造型圖 = **Seedream 5.0 Pro**(2K、無尾串、橫排 4 造型、四選一);三檢視 = **Lib Image**(16:9、全身左/中/右三視、無大頭;**硬性:必須把選定的 Seedream 造型圖作圖輸入/參考連線接入,不連則三檢視跑偏、與所選造型不符、作廢**;款式/顏色/廓形/比例與所選造型逐項一致;有人像→白圓貼遮臉+右下角中文小字,無→保留臉);場景圖 = **MJ V8.2**(固定 dreamcore 種子 `--sref 4658243766 --profile yp7vzjb`);影片 = **Seedance 2.5**。**人臉參考圖不喂造型模型、只在 Seedance 喂;造型參考圖才作 Seedream 圖參考。**
- **髮型**:有人像參考圖時,生影片前問使用者"髮型用參考圖的 / 用三檢視的",按選擇寫 prompt;無人像時以三檢視髮型為主。
- **服裝造型全片鎖定不變**(每條 prompt 強調與三檢視一致);僅使用者明確要求換裝時例外。
- **造型合規 + 人物底線**:端莊全覆蓋、不大面積透明、高領、裙及膝或更長、非性化;**皮膚乾淨無紋身、無穿孔**(戒指/項鍊/髮飾 OK);穿裙帶同色系防走光安全褲;合規用正向詞、負面區不寫涉黃敏感詞,`紋身/穿孔` 中性詞可進負面。
- **三檢視排版**:一張圖內、16:9,只全身正/側/背三視、去掉所有大頭;有人像→白圓貼遮臉 + 右下角中文小字「人臉單獨提供 · 此圖僅用於服裝造型參考」。
- **字幕**:僅當卡里選"需要"時,階段 5 按所選語言疊加(不燒進生成畫面)。
- 不寫真實偶像/歌手姓名、不寫真實 MV 名當 prompt,復現美學不復現具體作品/某人;風格錨點用描述性詞。
- 使用者只要片段/單鏡、或已指定場景造型時,在不破壞 每段≤15s且時長=音訊向上取整後裁剪/口型與音訊一致/不寫真實歌詞/不改原音訊/音樂用生成影片自帶不拼單獨軌/服裝造型全程鎖定/主角性別=人聲/每15s≥4鏡/全片不疊化/零文字規則下按需做。
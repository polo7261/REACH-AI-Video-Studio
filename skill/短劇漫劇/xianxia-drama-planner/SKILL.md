---
name: xianxia-drama-planner
description: "一站式生成東方巨構美學短劇"
---

## 一套仙俠底質 + 一句可選主色(階段 1 提煉,全片統一)

全片一套渲染底質(極致宏大尺度、含建築地點的白玉超巨構、鏡面對稱、電影級空氣透視),**場景圖不套用風格種子,靠同一段共享風格描述文字反覆套用來保持統一**;**全片影調最終以使用者確認的那組場景圖調性為準**,人物圖/道具圖/影片生成時都需向已選場景圖的色彩基調看齊。從劇本情緒再提煉一句主色附到場景圖 prompt。

- **共享風格描述(場景與 Seedance 通用基底,任何地點都適用,精簡版,中文)**:`東方神話巨構主義電影畫面。晴朗淡青藍天空,雲層保持中性偏白,右側可有剋制的淡金逆光輪廓,不做整體暖橙濾鏡。極致遠景或強透視構圖,人物或近景元素僅佔畫面高度0.3%-0.8%。近景、中景、遠霧、極遠景四層空氣透視,體積雲,電影級寫實質感,HDR,8K細節,結構可信、重量真實,尺度遼闊。`
- **建築子句(僅當該地點劇本設定含建築/宮闕/殿宇時才追加,不含建築的地點絕不套用)**:`一座漢白玉超巨構建築或天宮從雲海中升起,建築佔畫面高度60%以上甚至越出邊緣;巨牆、深色木構樑架、層疊斗拱、寬闊飛簷,鎏金剋制、不做滿金。`
- **場景圖額外追加**:`85-100mm中長焦壓縮空間(或50-70mm強烈一點透視,視構圖需要二選一)`,接共享描述(+ 建築子句,如適用)後,再接該地點自身的地貌/環境細節(如冰原、竹林、荒漠等,見場景清單描述)與主色。**室內場景**(宗門大殿內部、洞府內部等屬於"含建築"類)沿用同一套光線/色調/電影質感語言,尺度感按該室內空間本身的規模呈現,不強求做到"超巨構"。
- **Seedance 前置風格句額外追加**:`真人實拍電影質感,廣袖服裝隨風飄動,戰鬥/情緒高潮處慢鏡升格,人物在巨構長廊或大殿中行走時保持畫面中極小比例的全景構圖,鏡頭運動流暢但鏡頭切換隻用硬切、不出現任何轉場特效。`,放在 Seedance prompt 第一句,接共享描述之後。
- **可選主色傾向(接底質描述後,任選一句或另寫)**:仙氣冷調「淡玉色、月白、霧青」;天火暖調「熔金、赤色雷光、深紫風暴雲」;青綠山水「石綠、石青、暖金夕陽」;魔道幽冥「血色、玄黑、病綠瘴氣」。

---

## 固定種子與出圖規格(速查)

- **場景/影調圖 = Midjourney V8.2**(**必須指定該版本;Midjourney V8.2 無法連線時唯一備用為 V8.1,不用其他版本或其他工具**),**不套用風格種子**(不加 `--sref`/`--profile`),全景無人無道具、零文字。**每地點出 1 組 4 張**,四選一。Prompt = 共享風格描述(通用)+ **該地點含建築才追加建築子句,不含建築絕不追加** + 場景圖額外追加 + 該地點自身地貌描述 + 主色 + 畫幅要求(用文字描述,如"16:9橫構圖")+ 精簡負面詞(用文字描述寫在正文裡,不用 `--no` 字首;不含建築的地點不需要"不要普通小宮殿代替"這類建築相關負面詞,按場景實際情況取捨;通用負面詞如不要大人物、不要濃霧遮擋、不要整體橙色濾鏡、不要文字水印logo)+ **尾串僅保留** `--v 8.2`(V8.2 不可用則改 `--v 8.1`,不加其他 flag)。**整條 prompt(描述句+負面詞+尾串)≤ 1024 字元**,超了只精簡描述句,不動關鍵負面詞與尾串;建築描述僅在需要時出現;**一致性靠每次完整套用同一段共享風格描述文字 + 向已選場景圖調性對齊**。
- **人物+三檢視 = Seedream 5.0 Pro**(人物專用):所有角色一次性出——每角色**一張 16:9、單一純白底連續畫布**,內含 4 套正面全身造型(**必須全身入鏡,不得半身或大頭**;整套搭配+髮型髮飾明顯不同,禁止只換袍色其餘不變),**四套之間不設分隔線/邊框,視覺上是一整張連續白底照片而非拼接的四張圖**→ 一次性四選一確認 → 選定圖作參考圖輸入只補生側/背,出**16:9 單張純白底三檢視,排版按有無原臉分兩種**:**無原臉(Case1 無臉/Case3)**→ 左側為正面大頭特寫(近景頭肩)+ 右側全身三檢視(正面/側面/背面並排),整張連續無拼接縫,臉保留可見(臉即身份);**有原臉參考(Case2)**→ **只出全身三檢視(正面/側面/背面並排),不含左側大頭特寫面板**,頭部區域用**圓形貼紙完全遮住**,**右下角小字標註**(按使用者語種)"人臉單獨提供·僅供服裝參考",身份以原臉圖/影片在 Seedance 端鎖定。**四選一渲染檔(必疊,強調電影級而非短劇感)**:反油皮膚 `matte realistic skin, visible pores, no retouching, subtle film grain`;電影感 `cinematic film still, filmic contrast, luminous colour grade, movie-grade cinematography`;電影級選角與妝造 `a real film-actor face with dignified screen presence, NOT a modern idol/K-beauty/short-drama influencer face, no glass-skin filter, no heavy web-drama makeup, natural film-grade styling`;排版正向詞補充 `single seamless white background canvas, no panel dividers, no borders between poses, continuous studio photograph, not a collage`。維護 **cast sheet**。Seedream 無 `--sref`,一致性靠角色卡+參考圖。
- **道具錨點圖 = Lib Image**(僅需跨鏡鎖定的核心道具才出,**獨立生成,不引用人物或場景圖作參考**,直接依據道具卡文字描述生成):16:9 純白底單張連續畫布,內含道具正面全圖+三檢視細節(正面/側/背,法寶可加 1–2 處紋樣/機關特寫貼角),無分隔線拼接感。排版指令(i2i,英文基底):`pure white seamless background, product-style photography, single continuous canvas with no panel dividers; main panel shows the exact prop large and centred (front view); to the right, smaller side and back views; add close-up insets for intricate details if present; replicate every detail 1:1, do not redesign; no text, no watermark`。維護 **道具單(props sheet)**:道具名/歸屬角色/【鎖定/不鎖定】/三檢視連結。
- **影片 = Seedance 2.5(強制,不得替換成其他版本)**,單次最長 **30s**,內部鏡頭切換隻用硬切、不生成任何轉場特效或字幕。輸入 = 該段涉及地點的場景圖(跨地點多張、單地點一張,含室內場景)+ 每角色**同一張三檢視**(鎖臉+服裝)+ 每件鎖定道具**同一張三檢視**(不鎖定道具不出圖,靠文字帶出)+(有原臉時)原臉圖作身份錨點。

---

## 流程(逐階段暫停確認)

### 階段 0 · 開拍前問詢卡(一次性問完,不逐條停)

一張卡問 4 項(**角色造型、道具、口語語言不在此問,階段 1 解析劇本自動提煉**):

1. **劇本/文字**:完整劇本?一句話想法(據此草擬)?還是完全沒有想法?上傳後階段 1 自動解析人物/道具/場景/語言。**若完全沒有劇本/想法,先問使用者想要的風格基調**(如仙俠愛情、仙俠打鬥/熱血、仙俠懸疑/復仇、仙俠成長/頓悟、仙俠家國大義等,可多選或另寫),**再據此基調 + 使用者補充的隻言片語草擬仙俠短劇本**;若已有一句話想法則直接據此草擬,不必再問基調。
2. **字幕**:要/不要,要則選簡體/繁體/英文/雙語(階段 6 直接按此加,不再問)。
3. **畫幅**:16:9/4:3/1:1/9:16 平等列出、不作推薦,必須使用者自選。
4. **時長**:30s/60s/90s/自定義(填空,如 150s→按 30s 向上取整分 5 段)。

> **解析度不問,預設 720p**。草擬劇本(人物/門派/場景/節拍反轉/聲音分工,貼合已定風格基調,可摻渡劫飛昇、法寶認主、宗門大比、身世之謎、天劫倒計時、魔道入侵、轉世前身、靈根覺醒等鉤子)→使用者確認→進階段 1。

**角色造型三 Case(階段 1 出人物清單時才問,不在此問)**:Case1 有造型參考圖→參考圖+補 spec 生成,無原臉,三視為左大頭特寫+右全身三檢視;Case2 有人臉無造型→人臉參考+補 spec,原臉帶入 Seedance 鎖臉,**三視只出全身三檢視(不含大頭特寫面板),頭部圓形貼紙遮擋+右下角小字標註**;Case3 都沒有→按劇本身份/門派/性別補 spec 直接生成,無原臉,三視為左大頭特寫+右全身三檢視,臉即身份。三 Case 均要求電影級選角與妝造,避免短劇網紅臉。

**仙俠古風服裝語言(補 spec 時用,不鎖朝代,按性別)**:女 `flowing wide-sleeve hanfu or Taoist robe, silk ribbon sash drifting, layered cloud-shoulder cape, jade or gold hairpin, flowing high bun`;男 `Taoist/cultivator robe with wide sleeves, waist sash with jade pendant or sword tassel, topknot with jade or wooden hair crown`;共通 `real silk/brocade/gauze textures with natural drape, no contemporary fabric/cut/accessories`。身份門派可微調配色紋樣(魔道偏暗、正道偏素雅明亮),不改造型基線。

### 階段 1 · 劇本解析 + Final_Video_Spec

讀取全文解析為敘事結構+人物/道具/場景三表,**輸出表格停一次,不生成任何圖片**。

- **去重合並**:同一實體反覆出場合併成一條,補充描述併入最終描述。
- **資訊不足必須停下問,不能瞎補**:外觀描述缺失的條目標記 **⚠️資訊不足**,列出需補充的具體問題,等使用者補充後才進入該條設計;"完整"條目不受影響。
- **輸出格式**:先報"識別到 X 人物/Y 場景/Z 道具",附敘事結構一句話(節拍數按時長:30s 取 1–2 拍,60s 取 2–3 拍,以此累加);人物表(編號/姓名/出場場次/身份門派關係外觀/狀態)、道具表(編號/名稱/歸屬/出場/外觀/鎖定判斷/狀態)、場景表(編號/名稱/出場/室內或室外/**是否含建築**/環境描述/是否專用空鏡/狀態)。**場景表須包含劇本里出現的全部室內場景**,不因為室內不易呈現巨構感而省略。**"是否含建築"按該地點劇本描述判斷**:宮闕、殿宇、長廊、洞府等填【含建築】,荒野、冰原、山川、竹林、海洋等純自然環境填【不含建築】——決定階段 3 出圖時是否追加建築子句。
- **道具鎖定判斷**:法寶本命法器、關鍵信物、反覆出現兵器預設【鎖定】;一次性擺設、群體背景預設【不鎖定】;拿不準預設不鎖定。
- **口語語言**:預設劇本本身寫作語言;混用/不明確才追加一句詢問。
- **人臉參考圖問題**(此處問,非階段0):對人物清單問"有沒有想指定的人臉參考圖/影片?沒有則按劇本+仙俠服裝語言原創設計(電影級選角),首版確認後作後續一致性基準"。
- **旁白/心聲獨白/對白逐句提煉**:與三表一併展示——旁白(第三人稱說書人,交代背景/因果/時間跳躍)、心聲獨白(第一人稱情緒)、對白(標說話人,冗長臺詞精簡為強節奏短句需說明確認)、每拍聲音分工(旁白/獨白/對白/疊用)、情緒反轉基調、一句主色傾向。
- **分批處理**:人物/道具/場景任一類超 8 個自動分批,每批≤8,按首次出現順序,表格下方註明分批計劃;**影響階段 2/2.5/3 節奏**——每批做完停一次問是否繼續,除非使用者說明不用逐批確認。
- **Final_Video_Spec**:畫幅(階段0第3問)/解析度(預設720p)/時長(階段0第4問,每30s一段)。

> 暫停確認(三張表+狀態標註+人臉參考圖問詢+spec 一次性一起停)。

### 階段 2 / 2.5 / 3 · 角色·道具·場景資產生成(三線並行發起,確認順序不變)

> **三條生產線(人物/道具/場景)可以同時發起生成呼叫以節省時間**,互不依賴、互不參考;但**給使用者看結果與逐一確認的順序仍按 2→2.5→3 進行**,不因為並行生成就打亂確認節奏。各類超 8 個均按階段 1 分批計劃走,每批做完停一次問是否繼續。

**階段 2 · 角色設計(Seedream 5.0 Pro)**:每角色寫角色卡 → 一起出全部角色四選一造型圖(**16:9、單張純白底連續畫布,4 套均須全身入鏡**,差異明顯,電影級選角基線,無拼接縫)→ 一次性四選一確認 → 選定圖作參考圖輸入只補生側/背,一起出全部三檢視(16:9 單張純白底無拼接縫;**無原臉角色**=左大頭特寫+右全身三檢視;**有原臉角色**=只出全身三檢視、頭部圓形貼紙遮擋+右下角小字標註)→ 逐項核對臉/服裝,漂移則以選定圖重補,反覆漂則拼版 → 一次性確認全部三視。維護 cast sheet;換裝再出新一版。

> 四套須整體搭配+髮型都拉開區別(如①正式道袍高發髻 ②戰甲束髮 ③素色襦裙垂髮簪花 ④華麗禮服複雜髮飾),禁止只換袍色其餘不變;人物長相與妝造須走電影質感,避免網紅臉/短劇感;**畫面必須是單張連續白底,不能出現分欄/邊框/拼接的四宮格或三宮格感**。

**階段 2.5 · 道具設計(Lib Image,僅鎖定道具需要,與人物圖/場景圖完全獨立)**:【不鎖定】道具跳過,留到分鏡/場景階段文字帶出;【鎖定】道具逐樣出圖——寫道具卡(材質/紋樣/尺寸/關鍵機關)→ **直接依據道具卡文字描述生成,不引用任何人物三檢視或場景圖作參考**→ 一次性出全部鎖定道具單張純白底連續畫布(正面圖+三檢視細節,無拼接縫)→ 一次性確認(核對材質紋樣比例)→ 偏差則以正面圖重生側/背。維護道具單。中途新增道具隨時補出。

**階段 3 · 場景影調圖(Midjourney V8.2,不可用則 V8.1,不套用風格種子)**:按場景清單一起出(不要一場出完再出下一場):每地點(含室內場景)**各出 1 組 4 張**,**按場景表"是否含建築"取用對應模板**——【含建築】接共享風格描述+建築子句+該地點自身細節;【不含建築】只接共享風格描述+該地點自身地貌細節(荒原、冰川、竹林等),**絕不強行套用建築子句**;接主色+畫幅文字描述(如"16:9橫構圖")+僅 `--v 8.2`(不可用則 `--v 8.1`)的尾串,**prompt 保持精簡(≤1024 字元)**。**場景圖按「地點」出全景,一個地點一組、跨鏡跨段複用,一段影片可以涉及多個地點、不限制每 30s 只對應一個場景圖**;不為特寫/區域性單獨出圖,這些交 Seedance 在同一全景上取景;組數=去重後的地點數(含室內)。專用空鏡地點在場景清單特別標註。**全部出齊 → 一次性暫停讓使用者逐地點四選一**(標明 1 左上/2 右上/3 左下/4 右下)→ 收齊才進階段 4,嚴禁未經四選一就往下走。**該場景圖確定後的調性即為全片影調基準**,後續人物/道具/影片生成都需向其色彩質感看齊。\
**全部出齊 → 一次性暫停讓使用者逐地點確認**(滿意則透過;不滿意可指出問題重新生成該地點這一張,不做四選一)→ 收齊確認才進階段 4。

### 階段 4 · 分鏡表格(生影片前必出、需確認)

**一次性出全部分鏡表**(按段數,不要一段一停),每段一表,列:鏡號/時長/景別(空鏡/巨構人物運鏡/近景特寫/其他)/畫面(排程表演構圖)/**道具錨點**(該鏡用到的道具單編號,用於繫結道具三檢視)/**場景錨點**(該鏡所在地點的場景表編號,用於繫結場景圖)/聲音層(旁白·獨白·對白,原文+語氣)/運動。**轉場統一為硬切,不設轉場列**。"景別"列填四選一:純空鏡/巨構人物運鏡/近景特寫/其他——**每段至少各出現 1 次純空鏡與 1 次巨構人物運鏡,二者不可互相替代;聲音層為"對白"的鏡頭景別預設填近景特寫**(展現說話角色的表情口型,不預設用空鏡/巨構人物運鏡表現對白瞬間),其餘鏡頭按劇情需要在近景特寫與大遠景間交替,避免整段被大遠景堆滿。空鏡行畫面列只寫景觀排程、聲音層可留白僅環境音效、道具錨點留空;巨構人物運鏡行需寫明人物在長廊/大殿/天橋中的具體排程與佔比。\
表格下方附**連戲 bible**(不進表):角色身份門派造型手持道具/180°軸線與站位/場景主色光效時辰/當前節拍情緒反轉/多段時尾幀→頭幀銜接。\
每段每 30s ≥3 鏡、至少 1 空鏡、至少 1 巨構人物運鏡;逐句記錄口語原文供階段 6 做字幕。

> **暫停確認(一次性)**:全部分鏡表+造型圖+三檢視+道具圖+場景圖一起停。**分鏡表一次性全出只停一次;影片(階段5)相反——逐段生成逐段確認**。

### 階段 4b · 多段尾幀續接(60s+ 關鍵機制,逐條生)

每生完一條 seg_n → 停下等確認 → 抽尾幀解析(站位/表情/光線/景別/道具狀態)→ 按分鏡宣告的接縫模式生 seg_n+1。接縫模式:**(A)連續動作**——尾幀作起始幀無縫續上;**(B)換場**——尾幀僅作連戲參考(角色/服裝/道具/色板/光線一致),新構圖,以**硬切**相接(不用任何風格化轉場特效)。

### 階段 5 · Seedance 2.5 影片(強制該版本,每段一條 30s,逐條生)

prompt 結構:①前置風格句;②**組裝**——喂該段涉及地點的場景圖(按分鏡"場景錨點"取用,含室內場景)+ 每角色三檢視(鎖臉鎖造型,不再用四選一圖)+ 每件鎖定道具三檢視(按分鏡"道具錨點"取用,不鎖定道具靠文字帶出)+ 有原臉時原臉圖另作身份錨點,寫明"臉與造型取自三檢視、道具形制取自道具三檢視";③**分鏡**:`Shot1…hard cut to Shot2…`,一條連續 30s、鏡數達標、至少 1 空鏡 + 至少 1 巨構人物運鏡,**鏡頭切換隻用硬切,絕對不允許出現疊化/交叉溶解/淡入淡出等任何轉場動畫或特效畫面,沒有例外**;④**口語層**:按該鏡聲音層分工填入——旁白/獨白(無需對嘴)、對白(標說話人、口型同步),提示詞按使用者語種、臺詞填劇本原文;⑤**運動**(含巨構人物運鏡、對白近景與戰鬥專屬關鍵詞,按每鏡景別對應選用):`sweeping wide-angle and aerial epic vista shots, two tiny figures walking along a vast palace corridor or hall high above the clouds occupying a very small fraction of the frame, medium close-up or close-up on the speaking character with the vast background softly blurred during dialogue, flying-sword or floating traversal within a single continuous shot, camera moving through drifting mist as part of one shot, fast whip-pan between combatants with motion blur, low-angle shot conveying dominance, speed ramping between slow-motion and real-time at the moment of impact, close tracking shot following rapid close-quarters combat, camera pushes back sharply as a shockwave of energy erupts, glowing spirit-qi and sword-qi trails, orbiting camera during power reveal or combat exchange, high bird's-eye shots`;⑥**音訊+文字規則**:正面寫旁白/獨白/對白+場景音效;負面追加標準負面詞庫(已覆蓋 BGM/字幕/轉場特效/人潮/現代元素等)。\
**表演**:逐鏡≥1 表情+1 動作,按劇本情緒反轉賦予,電影級表演質感。**通用治僵硬(每鏡加)**:`natural subtle atmospheric sway, breathing on wide/close shots, micro head movement, natural blink, expression shifting per scene emotion, robes/sleeves/ribbons/hair/mist drifting subtly`。

> **分段生成+強制確認門**:一段一段生,每段生完必須停下等確認才生下一段,嚴禁不經確認連續生。\
> \*\***旁白/獨白兜底**:若模型對無對嘴 VO 支援不穩,退回裝配階段做 TTS/錄音疊加,其餘規則不變。

### 階段 6 · 裝配

1. **順接**:各段以**硬切**拼接,**絕對不允許出現疊化/交叉溶解/淡入淡出等任何轉場特效,沒有例外**;片段已含人聲+音效、無 BGM、無轉場畫面。
2. **合成前一步**:①**加字幕** `add_subtitle`——按階段0已確認語種直接加(可編輯疊加層,不燒進幀);**樣式固定**:純白字、**無描邊(不加黑邊/無 outline/stroke)**、字號 **28px**、**單行不換行**(超長臺詞需精簡至單行能容納的長度,精簡方式同階段1臺詞精簡原則)、字型 **思源宋體**(Source Han Serif,襯線體;伺服器無 SimSun 時以此作為最接近的替代字型);②**鋪國風配樂**——古箏/簫笛/編鐘/恢弘絃樂或空靈吟唱,隨節拍起伏,只描述風格不指定具體曲目,音量讓人聲清晰;③**疊圖**——片名/時間戳/credits/logo PNG(不燒進生成畫面)。
3. **合成匯出**:壓平合成為成片。

---

## 參考資料

### 鏡頭詞彙表(轉場統一為硬切,不再單列轉場詞條)

鏡頭用途關鍵詞極致遠景巨構(尺度對比)交代天地規模(紅線①必用)`extreme wide/aerial shot, colossal white-jade megastructure rising from cloud sea, figures at 0.3%-0.8% frame height`巨構人物運鏡(強制,區別於空鏡)人物在長廊/大殿中行走,佔比極小`wide static or slow tracking shot, two small figures walking along a vast palace corridor high above the clouds, figures occupy a tiny fraction of the frame`對白近景/特寫(強制,平衡大遠景佔比)角色說對白時的預設景別`medium close-up or close-up on the speaking character, natural eye level, shallow depth of field with the vast background softly out of focus, clear focus on facial expression and lip-sync`甩鏡對切(戰鬥專屬)攻防雙方快速切換,增強速度感`fast whip-pan between the two combatants, motion blur trailing the camera move, sharp reaction cut`低角度壓迫仰拍(戰鬥專屬)展現氣勢壓制/強者姿態`low-angle shot looking up at the character, sense of dominance and power, dramatic sky or architecture backdrop`速度漸變(戰鬥專屬)同鏡內速度忽快忽慢強化打擊感`speed ramping within a single continuous shot, shifting between slow-motion and real-time speed at the moment of impact`近身纏鬥跟拍(戰鬥專屬)貼身打鬥的連貫跟隨`close tracking shot following rapid close-quarters combat, camera weaving with the fighters' movement, controlled dynamic camera motion`衝擊波推鏡(戰鬥專屬)劍氣/法力爆發的衝擊力`camera pushes back sharply as a shockwave of energy erupts, dust and mist blown outward, impact-driven camera shake`一點透視甬道/天橋極致縱深感(標誌性)`strong one-point perspective corridor or sky-bridge, vanishing point composition, repeating architectural elements receding into distance`鏡面對稱/倒影世界宮闕迴廊/仙台錯覺(標誌性)`reflective floor or still water, architecture echoed by inverted reflection below`御劍凌空/凌波運鏡輕功/御劍移動(同鏡內運鏡)`flying-sword or floating traversal within one continuous shot, camera gliding alongside subject`雲霧穿梭(運鏡非轉場)同一鏡頭內揭示下一處景物`camera moves through drifting mist within a single continuous shot, revealing more of the scene`劍氣/靈氣光效特寫法力/戰鬥爆發`close-up glowing sword-qi or spirit-energy trail, particles swirling`慢鏡升格戰鬥/情緒/渡劫高潮`slow-motion, robes and hair flowing dramatically`環繞運鏡身份揭示/法力覺醒`orbiting camera as energy erupts around subject`俯瞰鏡頭天地遼闊/宗門全景`high bird's-eye establishing shot`中長焦壓縮空間空間壓縮、層次堆疊`85-100mm compressed telephoto perspective, layered atmospheric depth`

### 節奏 → 每 30s 鏡數(硬底線,鏡頭切換一律硬切)

節奏鏡數說明宏大空鏡2–3(下限,須含空鏡+巨構人物運鏡)長鏡頭+慢搖;硬切敘事推進4–6對白/獨白以近景特寫為主,穿插大遠景交代環境;硬切衝突/反轉爆發6–8(取上限)甩鏡對切+低角度壓迫+速度漸變+衝擊波推鏡+近身纏鬥跟拍,至少交替 3 種;硬切混合4–5空鏡與近景交替;環繞運鏡+硬切

> 每 30s 不得少於 3 鏡(唯一例外:使用者明確點名一鏡到底);每 30s 至少 1 純空鏡 + 1 巨構人物運鏡(二者不可互相替代);對白節拍其餘鏡頭以近景/特寫為主,與大遠景交替;衝突/反轉爆發節拍取鏡數上限並至少交替 3 種戰鬥專屬運鏡(見鏡頭詞彙表),不能只靠慢鏡升格撐場;所有鏡頭切換隻用硬切,不設風格化轉場。

### 場景庫(巨構主義)

**標誌性巨構/鏡面場景(優先用於開篇/關鍵轉折)**:雲海之上的白玉超巨構天宮(建築越出畫面頂部)、一點透視的白玉天橋/甬道(消失點構圖,適合放巨構人物運鏡)、巨構建築內部向外的開放大殿(人物極小立於門洞前)、懸浮宮闕長廊(倒影對稱,適合放巨構人物運鏡)、廊下遠眺懸崖仙台(人物極小)。\
**常規場景(含室內)**:雲海仙山之巔、瀑布秘境洞天、上古遺蹟廢墟、竹林劍冢、九重天宮闕樓閣、渡劫雷雲戰場、宗門大殿廣場(室內)、丹爐洞府(室內)、星野天河、桃花幻境、荒漠魔域、結界秘境入口、懸崖棧道雲梯、古鎮市集、宗門寢殿/書閣(室內)。長片可重訪同一地點換光線/機位/時辰。

### 道具庫參考(鎖定判斷)

通常鎖定:主角法寶/本命法器、關鍵信物(玉佩/古卷/傳送陣圖)、反覆出現的兵器。通常不鎖定:一次性擺設、群體背景道具。拿不準預設不鎖定。

### 注意

- 不寫真實門派/作品/演員姓名當 prompt;仙俠感靠描述詞承擔。
- 畫面禁現代元素(強制,見標準負面詞庫),適用於全部工具。
- 人物圖固定用 Seedream 5.0 Pro,場景圖固定用Midjourney V8.2(不可用則 V8.1),道具圖固定用 Lib Image,影片固定用 Seedance 2.5,均不得替換。三者出圖/出影片均不生成轉場特效或文字/字幕,人物/道具的四選一圖與三檢視都必須單張無拼接縫,場景圖每地點一組 4 張四選一。
- 使用者只要片段/單鏡、或已指定場景造型時,在不破壞紅線與核心規則下按需靈活處理。
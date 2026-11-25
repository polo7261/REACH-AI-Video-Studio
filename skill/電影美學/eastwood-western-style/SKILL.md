---
name: eastwood-western-style
description: "極靜對峙瞬間爆發的槍戰大片"
---

# eastwood-western-style

做萊昂內荒涼美學 + 伊斯特伍德式反英雄西部片時用本 skill。劇情**完全依據使用者指令碼/劇本框架**。**風格致敬,不宣稱是其本人作品。** 本 skill 自足,場景工藝全內聯。

> 本環境適配(Flova→我方 13 工具):GPT Image 2/TextToImage/ImageToImage → `generate_image_v3`;Seedance 2.0/MultiModalToVideo → `generate_video_v3`;Suno/ElevenLabs/MiniMax(BGM/口哨/風鈴/馬刺/旁白) → `generate_audio`;text_editor → `write_file_v2`;video_assembler → `composite_video`;`<<<image_n>>>` → `reference_nodes` + `{{NodeKey}}`。**源"僅 GPT Image 2 / 僅 Seedance 2.0"模型唯一性 + 會員鑑權降級 = 本環境無該概念,刪(用預設引擎)**;**super_resolution 超分/插幀(MediaKit)= 無該能力,刪**——但"避免高幀率、保 35mm 膠片質感"的意圖作為風格約束保留。**詞棧/黃金模板原文英文保留**;composite_video 支援 per-track dB 與 clip trim(照搬),**變速(speed 1.5-2x)/黑場時長 composite_video 無原生引數 → 降級為剪輯指導性描述〔適配改寫〕**。

## 流程(每生成新資產前暫停確認)

1. **全域性設定(Final_Video_Spec)**〔`write_file_v2`〕:劇情**完全依據使用者指令碼**。8 欄位模板:
   - **Title**:專案名/決鬥主題
   - **Type**:動作/心理對峙/修正主義西部片
   - **Aspect Ratio**:16:9(預設電影寬畫幅)或 9:16(移動端,同步調整構圖)
   - **Resolution**:720p(預設)
   - **Output Language**:旁白與角色臺詞的目標輸出語言(English / Chinese)
   - **Visual Style**:荒涼滄桑美學(Sergio Leone style, 褪色膠片, 特藝七彩, 逆光體積光)
   - **Audio Tone**:莫里康內交響樂聲學(Ennio Morricone, 孤獨口哨, 風鈴, 鑄鐵馬刺)
   - **Story Outline**:宿命決鬥起承轉合核心劇情梗概
2. **設計故事板**〔暫停〕:核心角色/場景作 key_element;鏡頭遵循**極靜(蓄勢對峙)→極動(瞬間爆發)**,融眼部特寫/超廣角遠景/低角度仰拍/緩慢推鏡。遠距離決鬥先建**對峙空間鎖**(見下)。
3. **元素資產獲取與校驗**〔暫停鎖定〕:見下"元素資產管理"。**全面核檢機制**:資產建立完畢後,**逐一核對故事板所有 key_element(角色+場景)是否都成功繫結 asset_id;任何遺漏或未繫結成功嚴禁進入影片生成步驟**。
4. **分鏡影片**〔暫停·附對齊核檢〕:`generate_video_v3`,單鏡 **4–15s(嚴禁<4s)**;**雙重強基準繫結**(角色 node + 場景四宮格 node)。**提示詞對準與防漏檢視**:生成每鏡前對照分鏡指令碼多維核檢——場景參考、人物參考(佔位符繫結)、臺詞對白全部精準對齊無遺漏;每鏡強制繫結所屬場景 key_element 四宮格作 reference_image(防背景漂移/跳畫);無場景繫結的分鏡絕不允許。強連貫鏡可綁前鏡末幀作 reference_video。含對白綁角色 key_element_audio 保音色一致。
5. **音訊**〔暫停〕:見下"音訊資產"。
6. **合成**〔暫停·先展示所有單項成果〕:`composite_video` 蒙太奇拼貼,見下"合成與剪輯動律"。

## 對峙空間鎖(獨特鐵律)

任何遠距離決鬥場景,故事板**必須先用遠景/OTS 建立"對峙空間鎖"**:A 方站位、B 方站位、兩人距離、面對方向、螢幕左右/縱深軸線、**鏡頭軸線、子彈方向、中彈倒地方向**。後續所有 ECU/CU 區域性特寫**只能改變鏡頭尺度,不能改變角色間真實距離或站位**。

## 多模態分析(使用者參考材料)

- **角色全身三檢視檢測**:檢查上傳是否為含正/側/背的**全身**三檢視。是→提取各角度形體比例/面部輪廓/髮型/膚質/經典服飾細節(披風/氈帽/槍套)/配色/獨特標記(傷疤/胡茬),合併輸出高完整性描述。**若非三檢視或為半身照/頭像 → 判"格式不匹配",啟動重構。**
- **場景參考圖檢測**:檢查是否為**無人物、多角度"標準四宮格"**(4 獨立分格)。提取空間佈局/核心建築/代表性道具(吧檯/墓碑)/色調(褪色大地色)/光影(強對比)。
- **美學契合度驗證(核心)**:評估是否具備西部片底色(高硬度對比光/沙塵感/風化材質/滄桑感);格式硬校驗(角色須全身三檢視,場景須無人物四宮格)。契合→標可直接繫結;**不契合(風格不符/角色非全身三檢視/場景不合四宮格或含人物)→ 判"格式/風格不匹配",制定"西部片風格轉換與格式重構方案"**(見下四宮格四格固定分配)。
- **人聲分析**:分析聲音是否沙啞/深沉/乾癟/帶滄桑感,錄入 key_element_audio 維持配音一致。
- **參考影片動態分析(三項,寫入 shot 描述)**:①**鏡頭運動軌跡**(極慢面部推焦 Slow Zoom-in/Push-in、低角度平移 Low-angle Pan/Dolly);②**物理運動反饋**(拔槍動作瞬態頻率、槍口煙霧擴散速率、受擊身體物理震顫幅度);③**光影明暗質感**(強對比硬光比例 Chiaroscuro、空氣塵埃密度)。

## 元素資產管理(key_element 視覺定義)

**處理策略(兩路徑)**:
- **路徑 A 使用者已提供參考圖**:完全契合(角色標準全身三檢視 + 場景無人物四宮格 + 風格相符)→ 直接註冊 asset_id 繫結。**不契合/格式不符 → 絕不直接繫結**,用 `generate_image_v3`(ImageToImage)以使用者上傳圖為物理/面部參考重構:角色重構為西部片規範全身三檢視(並排正/側/背全身立繪,融寬沿氈帽/重胡茬/墨西哥斗篷/皮套/皮靴,極力保留原圖面部標誌);場景重構為無人物標準四宮格。
- **路徑 B 使用者未提供**:`generate_image_v3`(TextToImage),16:9。

**角色三檢視構圖規範**:強制**同一畫布並排正/側/背全身立繪**(定格臉部/警惕眼神/胡茬帽沿陰影/斗篷披風/腰間槍套/皮靴及整體剪影),展示 360° 服飾武器細節,**嚴禁半身照/頭部特寫/重疊畫面**。

**★三檢視 prompt 五處硬約束(實測反覆驗證,缺一處必翻車)**:
1. **寫實錨點**:開頭必須出現 `photorealistic`(不是 "portrait"/"reference sheet" 就自動等於寫實——這兩個詞中性,不帶任何傾向)。
2. **負向排除渲染風格**:結尾必須加 `No illustration, no anime, no cartoon.`——這條跟"no half-body/no cropping"這類**構圖**約束是兩回事,**構圖約束管切法,這條管像照片還是像畫**,必須都寫、不能互相替代。**實測教訓**:同一版本 prompt 只把 "illustration of" 換成 "reference sheet of"、不加這句負向排除,照樣會生成卡通感結果——只要通篇沒出現 `photorealistic` + `No illustration, no anime, no cartoon`,不管用詞多含蓄,都等於沒做防護。
3. **面板數量硬鎖**:必須顯式宣告面板總數(預設 3:正/側/背;需要脫帽/摘配飾做面部基準時可擴到 4,第 4 格明確寫成"脫帽頭像特寫"並註明與前三格同光同膚質)——`Exactly N panels only, no additional close-up insets beyond the N specified below`,否則模型會自己加臉部特寫小格把排版擠亂。
4. **等比對齊**:顯式寫 `same character scale and same camera distance across all views, evenly spaced with equal margins`,否則三個檢視大小/站位高度容易不一致。
5. **純色背景+防真人臉**:背景寫 `flat solid neutral grey background, no gradient, no vignette`(不是單寫 "neutral background" 就夠,防止出現暖色調/暗角);人物描述前置一句 `Completely original fictional face, not based on any real person or celebrity`——**實測發現不加這句,"Sergio Leone spaghetti western" 這類強關聯風格詞會把臉直接生成得跟歷史真實演員高度相似**。

標誌性配飾(帽子/頭巾等)**必須寫進角色描述鎖定清單,不得省略**——省略會導致同一角色不同批次"戴不戴帽子"隨機不一致。

**場景四宮格構圖規範(四格固定分配,最大化資訊密度)**:
- **左上(全景定場 Establishing Shot)**:荒涼廣闊西部全景/建築,死寂空無一人,木板暴曬彎曲開裂。
- **右上(陳設特寫 Props Close-up)**:風化木質傢俱/老槍/沙龍吧檯;僅單枚生鏽鐵釘支撐吱呀作響的斑駁木招牌、佈滿銅綠的生鏽馬栓。
- **左下(縱深透視 Depth Perspective)**:強線條透視的漫天沙塵街道/峽谷小道,乾枯龜裂泥地滾動風滾草(Tumbleweeds)、廢棄小巷風沙旋渦(Dust devils)。
- **右下(氣氛光效 Atmospheric Lighting)**:強硬正午直射光/夕陽逆光/飛揚塵埃,地平線夕陽強逆光下橙金光暈、浮塵與破舊黑布獵獵作響。

## 角色肖像級 key_element 方法

為**每個主要角色建立肖像級 key_element**:面容 / 服飾裝束 / 武器配件 / 冷酷馬刺與動作聲效,**中文描述 + 英文視覺片語**並列,粒度到可跨鏡鎖定的具體特徵。場景按四宮格四要素寫足質感。
> 精簡樣例(示範顆粒度,非固定人設,按使用者指令碼替換):鏢客——飽經風霜深褐皮膚(Weathered sun-bronzed skin)、冰冷灰藍眼眸(Squinting piercing steel-blue eyes)、乾裂脫皮嘴唇、斜叼半燃雪茄頭(Half-burnt cigarillo);褪色墨西哥條紋羊毛斗篷(Faded Mexican striped wool poncho)+舊皮革馬甲;系滿黃銅子彈槍帶與柯爾特左輪槍套、綴齒輪做舊黃銅馬刺皮靴(clinking brass spurs)。反派——鷹隼兇眼半隱純黑牛仔帽寬簷陰影(Hawk-like eyes half-hidden in the deep shadow of the cowboy hat brim)、瞳緣冷冽金屬反光、八字鬍;沾塵黑色雙排扣長風衣(Dusty black double-breasted duster coat)+暗紅絲綢馬甲;雕花雙槍皮套與銀光左輪(Engraved silver-plated revolvers)、黑色鑄鐵馬刺(dark cast-iron spurs)。完整肖像詞棧見 `references/character-scene-portraits.md`。

**★服裝錨定文字鎖宕機制（實測發現的漏洞修補）**：無使用者參考圖、走"路徑B TextToImage 原創設計"時，角色的服飾/道具描述**在生成三檢視前必須先寫成一句定稿的錨定文字**（格式同上面精簡樣例的服裝部分，中文+英文片語各一遍），寫入 Final_Video_Spec 與該角色的 key_element 記錄，視為**跟三檢視影象本身同等級別的錨點**——**不是"示範顆粒度"的參考，是逐字鎖死、後續每一鏡都要原樣複述的文字**。之前實測出現過同一決鬥短片裡，主角從"黑色風衣+雪茄"中途變成"墨西哥斗篷+子彈帶"的服裝錯亂，根源就是沒有先寫死這句錨定文字、只靠"絕不寫與元素圖矛盾的外觀"這條軟性提醒，模型在沒有強文字約束時會在不同鏡頭裡各自"合理發揮"。**任何一鏡的提示詞只要涉及該角色的服裝/道具，必須原樣複製這句錨定文字，不得改寫、簡寫或憑記憶重新描述。**

## 鏡頭設計、節奏與動作邏輯

- **極靜→極動節奏**:對峙階段優先極淺景深長焦特寫(眼部/手部懸空/馬刺),靠視線博弈(Eyeline Match)與極低攝像機運動幅度拉滿張力。
- **區域性特寫同框關係宣告**:凡區域性特寫同時提到"雙方/兩人/彼此"的身體部位/武器/動作,**必須明確"同一畫面同框"還是"交叉剪輯"**。遠距離決鬥的手部/馬刺/眼神/槍套特寫預設寫成 **intercut close-ups / hard cuts**;**禁用"雙方的手""兩人的槍套"等模糊表述**描述單一近景,除非劇情明確要求近距離同框。
- **極簡臺詞停頓美學**:臺詞極其剋制(人狠話不多),禁長篇大論;**有意識加破折號/省略號 ...**(如 `{No... I don't think so...}`)引導配音模型產生戲劇停頓與呼吸感的滄桑咬字。

## 雙階段八鏡頭決鬥藍圖(標準決鬥模板)

設計對決故事板須按此"雙階段八鏡頭"邏輯與臺詞細節編排(臺詞正規化為示例,可微調):

**第一階段 · 對視對峙(極致心理張力)**
1. **鏡頭1(空間鎖建立 OTS)**:**135mm+ 長焦中景(MS/OTS)** 在雙方間交替剪下,明確建立空間鎖(二人分立主街兩端/縱深兩側、相距較遠、面對面、軸線/左右/縱深/朝向在後續保持不變);風沙漫天,斗篷/風衣熱浪中微抖,空間壓縮窒息對視。
2. **鏡頭2(眼神博弈 ECU 交叉剪輯)**:**極寫特寫 ECU** 在雙方瞳孔/眼部微表情間快速直切(Eyeline Match);是 **intercut close-ups 非同框**,每個 ECU 只呈現一個角色區域性五官,繼承鏡頭 1 的遠距離關係。
3. **鏡頭3(手部蓄勢/馬刺 交叉區域性特寫)**:**非"雙人手部同框"**,拆 3A/3B/3C 或描述明確 hard cut/intercut——3A 只鎖鏢客右手/Colt 槍柄/皮套/子彈帶(畫面不得出現反派身體);3B 只鎖反派手指/黑槍套/黑靴/鑄鐵馬刺,提跟摩擦沙土金屬迴響(畫面不得出現鏢客身體);3C 3A 與 3B 間高壓硬切交替,維持鏡頭 1 空間關係。
   - **對峙臺詞停頓藍圖**(極簡冰冷、大量氣口 `...`):反派正規化 `{There are two kinds of people in this world... those with loaded guns... and those who dig...}`(極慢氣音金屬沙啞);鏢客正規化 `{You... dig...}`(極乾燥滄桑低沉鼻音)。

**第二階段 · 出擊爆發(電光石火瞬態)**
4. **鏡頭4(極速拔槍 quick-draw)**:**1.5s 瞬態極寫**(裝配剪為 1s–1.2s);手部極速下沉貼合雕花槍柄,左輪爆炸速度滑出。
5. **鏡頭5(槍火硝煙 muzzle-flash)**:**中近景仰拍 MCU**;扣扳機,槍口橙金火光吐信,青白濃密槍煙伴 0dB 雷鳴槍聲炸裂。
6. **鏡頭6(子彈擦帽微距慢動作)**:**微距慢動作 Macro Close-up**;高溫子彈擦過氈帽邊緣,衝擊波撕裂呢料,碎纖維飛濺,帽受力傾斜旋轉飛落。
7. **鏡頭7(中彈倒地 collapse)**:**低角度中全景 MWS**;**必須繼承鏡頭 1 空間鎖**:中彈者正面朝射手、子彈從射手方向擊中胸口、身體沿受力方向**向後仰倒(遠離射手方向)、背部先接觸地面,不能向射手/鏡頭前撲**;雙膝癱軟、物理慣性後倒、背重擊沙土悶響、地面炸開厚重沙塵圓環。
8. **鏡頭8(收尾剪影 aftermath)**:**慢速拉遠 WS/EWS**;鏢客淡然緩慢將冒煙左輪插回皮套(清脆金屬扣合聲),血色殘陽低懸、深橙緋紅天空、勝者孤獨剪影被狂風無限拉長、斗篷獵獵。

## 影片提示詞寫作規範(Seedance 風格,全內聯)

- **對白語言字首標籤(首要聲學機制)**:`{...}` 包裹對白時**必須強制加語言字首**——英文 `{en: "verbatim dialogue line"}`、中文 `{zh: "一字不差的臺詞"}`;**嚴禁省略字首**(否則口型同步/發音漂移)。
- **佔位符與描述一致性**:用 `{{NodeKey}}` 綁角色/場景;提示詞只描述瞬態動作/微表情/環境互動,**絕不寫與元素圖矛盾的外觀**(圖裡黑帽子就不要寫 "brown hat")。
- **多角色同屏物理隔離三條**:①**實體與佔位符強繫結**(佔位符緊跟角色名詞/稱謂,如 `The weathered hero {{Node1}} and the cold-eyed outlaw {{Node2}} face each other`);②**空間方位硬性區隔**(寫絕對左右/景深,如 `{{Node1}} stands on the left in close-up, while {{Node2}} is positioned on the right in medium shot`);③**拒絕模糊複數**(禁 are/they/both,單體分開描述各自動作,實現絕對物理隔離)。
- **繼承空間鎖與交叉剪輯結構**:故事板已宣告遠距離對峙/intercut/hard cut/3A-3C 時,影片提示詞**忠實保留結構,不得把多角色的手/槍套/馬刺/眼睛/身體區域性合併成同一近景同框**;單次生成含交叉特寫須明寫 `a sequence of hard-cut intercut close-ups` 且逐段宣告每子鏡頭只出現一個角色區域性;若引擎更宜單鏡頭穩定輸出則拆成多個 shot 由 `composite_video` 硬切拼接。
- **動作向量三重錨定**:中彈/倒地/拔槍/衝撞/閃避時,動作方向**同時錨定三種關係**——角色身體方向(向背後倒)、對手/射手方向(遠離射手)、鏡頭/螢幕方向(toward background / away from camera / screen left);**避免只寫 backward/forward/left/right 單一相對詞**。
- **提示詞對照核檢(雙向)**:①場景/人物引用比對(提示詞含指令碼所有 key_element 佔位符);②臺詞對白比對(所有對白一字不漏用 `{...}` 嵌入啟用口型同步,環境音特效用 `<...>`)。
- **防四宮格影片機制(Grid Reference Disambiguation)**:呼叫四宮格場景參考圖生成分鏡影片時,為**徹底防止模型生成帶四格的分裂畫面**,必須:①**語義解構宣告**(`{{Node}} is a 4-quadrant reference sheet containing establishing shot, props, depth, and lighting.`);②緊跟**顯式單畫幅鏡頭指令**(`Generate a single-camera shot focusing on the depth perspective of the street and the atmospheric dust from the reference sheet {{Node}}. Do not generate a split screen or 4-grid video. Single view only.`)。
- **鏡頭運動與動作堆疊(Camera → Action → Environment)**:按鏡頭運動→主體動態→物理環境層次編寫,精確控制動作幅度(Motion Amplitude)與攝像機軌跡。極寫用 `135mm+ telephoto lens, extremely shallow DoF, cinematic lens blur, blurred background bokeh`;宏大場面用 `extreme wide shot (EWS), low-angle perspective`;動態爆發可引 `whip pan`。
- **面部特寫防漂移機制(Facial ECU Control)**:生成眼部/面部微表情大特寫時**即便不展現全身也必須強制繫結角色全身三檢視**作 reference;提示詞明確鏡頭對準 `{{Node}}` 特定五官、微表情限制在面部區域,**絕不允許在提示詞中描寫全身/四肢/大尺度動作**(防塞多餘身體構圖導致人臉拉伸畸變);寫法示例 `135mm telephoto extreme close-up (ECU) of {{Node}}'s face, razor-sharp focus on the squinting steel-blue eyes and sun-cracked lips, micro-expression of the face, completely ignoring the rest of the body.`
- **近身拔槍三階段防畸變(Anti-Distortion Syntax)**:表現手指微動/按壓/滑出槍套時,**同時傳入角色全身三檢視 + 場景四宮格(陳設特寫分格)雙向參考**;**嚴禁一句話概括的高頻躍變詞**(如 `he draws the gun directly`),必須"懸空蓄勢→觸達貼合→極速滑出"三階段解構手部物理過渡(狀態到狀態位移),給引擎流暢軌跡差值依據:①`hovering inches above the leather holster, fingers spread wide`;②`fingers wrapping firmly around the engraved silver grip`;③`sliding smoothly out of the holster with explosive velocity`。
- **聲音嵌入標記**:背景音/音效 `<...>`(如 `<wind howling, squeaking wooden saloon door>`,拔槍鏡加 `<loud gunshot echoing, metal spurs clinking>`);極簡對白 `{...}`(字首語言)。
- **否定指令**:加 `no music`(音樂由全域性軌道處理)與 `no subtitles`。
- **★風格錨定詞逐條複述(實測發現的漏洞修補)**:**每一條**分鏡影片生成 prompt 正文**末尾必須原樣複述**精簡錨定詞(見 references/prompt-word-stacks.md 開頭★生產驗證版),**不能只靠 `{{Node}}` 引用參考圖隱式攜帶風格**。實測反例:某測評案例影象階段(角色三檢視/場景四宮格)質感詞寫得很全,但 9 條影片 prompt 正文一條都沒複述錨定詞、只引用了 `{{Node}}` 場景圖,最終整體風格判定不如同題基線——而該基線的 12 條影片 prompt **每一條**都在正文裡逐字重複了錨定詞。影象階段把風格焊進參考圖,只解決角色/場景外觀一致;**每一鏡的色調/膠片顆粒/光影質感必須靠影片 prompt 正文裡再寫一遍錨定詞來保證**,兩者缺一不可。

**影象詞棧六組 + 三檢視/四宮格英文模板 + 四個影片黃金模板**全文見 `references/prompt-word-stacks.md`(原文英文保留)。

## 音訊資產

- **音訊資產複用去重(最高優先順序)**:使用者已上傳 BGM/VO/特定音效 → **強制直接繫結複用,嚴禁無視使用者資產觸發 AI 重生成**;僅使用者未提供時才觸發下列生成。
- **獨立音軌生成**(`generate_audio`,四條詞棧原文保留,見 references):①交響 BGM(Spaghetti Western orchestral, epic acoustic guitar, dramatic high-register trumpet, crescendo, Sergio Leone style);②孤獨口哨主題(solo human whistle, haunting melancholic, high cathedral reverb, Ennio Morricone aesthetic);③沙塵風鈴環境(desolate howling desert wind, sparse metallic rusty wind chimes, no musical melody);④馬刺沉重腳步節奏(dry acoustic percussion, heavy boot thuds, metallic clinking brass spurs, ticking clock tension)。
- **旁白 VO**:英文預設沙啞低沉顆粒感伊斯特伍德式音色;中文/多語言選相應音色。作獨立 audio_layer。

## 合成與剪輯動律(video_assembler → composite_video)

- **剪輯動律四階段(對峙段)**:①環境定場 EWS ≈**10s**;②雙人對視 OTS/MS 交替、每鏡 ≈**8s**;③區域性極寫 ECU/手部槍套特寫交替、頻率縮至 **4–5s**;④爆發前夕極限變頻快剪:主角雙眼(2s)→反派雙眼(2s)→主角懸空手指微動(1.5s)→反派緊握槍柄(1.5s),物理鏡頭長度指數級遞減至絕對窒息。
- **爆發段快剪蒙太奇(1s–2s)**:引擎最低 4s,生成端無法出超短鏡頭 → **裝配階段對 4s+ 源片段做 `composite_video` 的 startPosition/endPosition 高精度 Trim 擷取**,按四快剪結構拼貼:①(1.0s)特寫手掌按壓左輪極速滑出+槍口火光前 24 幀;②(1.0–1.2s)低角度側中景開火+青白槍煙炸裂;③(1.0s)極寫中彈瞳孔放大/碎布飛濺/帽被掀飛;④(1.5–2.0s)中遠景仰拍身體後倒塵土揚起。〔**區域性變速 Speed up 1.5–2x composite_video 無原生引數 → 降級為剪輯指導性描述·適配改寫;Trim 用 startPosition/endPosition 原生照搬**〕。爆發後餘韻重放緩,收槍/硝煙散去/地平線剪影定格 **5s+** 歸蒼涼寂靜。
- **五軌垂直疊層 dB 電平表**(`composite_video` audioList 每軌 `decibel` + `videoVolume:0` 靜音影片原聲):
  1. **Track1 環境鋪底(風沙+風鈴)**:全片迴圈,**-15dB 到 -20dB**,低頻物理聲場背景。
  2. **Track2 物理擬音(重步履+馬刺)**:**-6dB 到 -10dB**,隨角色行止動態淡入淡出(行走推高、停步衰減至 -30dB 掛底)。
  3. **Track3 主題旋律(口哨)**:**-8dB 到 -12dB**,加深混響營造空靈縱深。
  4. **Track4 交響 BGM**:對峙靜默期 **-18dB 到 -24dB** 掛底;決鬥高潮/瞬間爆發以 **+6dB** 急劇漸強直推 **0dB** 爆裂。
  5. **Track5 人聲/旁白**:**0dB 到 -3dB** 優先清晰;有人聲吐字時 Ducking 將 BGM 與環境音臨時壓低 **-6dB**。
  〔dB 與 Ducking:composite_video 支援 per-track `decibel`,靜音影片原聲用 `videoVolume:0`,照搬;Ducking 的動態壓低若無原生自動側鏈 → 以分段 audioList dB 近似或標剪輯指導·適配改寫〕。
- **聲學留白/破冰**:爆發前 3–4s 聲學戲劇性漸弱/截斷——BGM 交響與口哨在槍聲前 **2s 驟淡出至無聲(Fade to -inf)**,僅留極輕沙沙風聲+一聲孤獨風鈴微響;拔槍開火**第 1 幀槍響 SFX 以 0dB 飽和瞬態爆發**,同時 Track4 重音銅管爆發,與拔槍視覺瞬間**幀級對齊**實現"極靜到極動瞬間破冰"。
- **轉場規鎖**:主體剪輯全部**高對比無縫直切(Hard Cut)**(即 composite_video 按序拼接,60 年代義大利西部片冷峻硬核氣質關鍵);**嚴禁**溶解 Dissolve/劃像 Wipe/光暈閃爍/3D 翻轉;**僅大跨度空間位移或大尺度時間跳躍**才允許淡入淡出黑場(Fade to Black/in),黑場時長 **1.5s–2s**〔黑場轉場 composite_video 無原生引數 → 大跨度切換時插黑場素材或標剪輯指導·適配改寫〕。
---
name: blogger-outfit-video
description: "一鍵生成小紅書博主穿搭種草影片。"
---

`# FitCast · 穿搭種草影片`

` `

`流程：服裝解析+模特設定→服裝白底圖(打底+目標)/預設近景人物三檢視(如無使用者模特)→場景圖→動作指令碼→影片Prompt（無聲）→BGM合成`

`**核心調性**：小紅書博主真實感，杜絕AI感/油膩感/電影感，全程手機隨手拍質感。`

` `

`---`

` `

`## STEP 0：開場問答`

```` ``` ````

`①請選擇模特：1. AI自動匹配模特 / 2. 上傳模特圖`

`②品牌/內容定位 ③目標受眾 ④場景空間：客廳/臥室/玄關`

`⑤輸出：15秒單鏡影片（接衣→貼身變身→定點pose→展示三拍→定格），影片本身無聲（不含音效/口播），最終合成階段疊加BGM`

```` ``` ````

` `

`---`

` `

`## STEP 1：服裝解析+模特設定`

`解析輸出：品類/風格標籤/主色調/材質/版型/單品件數/配飾清單（如有）`

` `

`A路徑按風格+受眾匹配模特：極簡通勤→溫柔知性 / 甜酷Y2K→元氣愛笑 / 法式復古→慵懶親切 / 街頭機能→陽光爽朗 / 度假森系→溫暖治癒 / 居家→放鬆隨和`

` `

`**預設真實模特庫（選擇"AI自動匹配模特"且未指定具體形象時使用，性格氣質仍按上方風格標籤匹配；此庫用於生成STEP2③預設近景人物三檢視）**：`

`女模：亞洲女生，165-172cm，自然妝感，毛孔質感+淡雀斑，非CG/非磨皮，髮絲自然不齊整，五官清爽非網紅臉，鬆弛感>擺拍感。`

`男模：亞洲男生，175-182cm，短髮或微卷劉海，自然毛孔質感，非CG網感，氣質介於校園與都市之間，五官清爽不過度精緻。`

` `

`B路徑：解析使用者模特圖，識別身材/膚色/髮型/五官，輸出特徵卡（使用者上傳的模特原圖後續直接作為影片生成階段的人物強參考源，見STEP5，無需AI二次生成）`

` `

`---`

` `

`## STEP 2：服裝白底圖（均無人物）+ 預設近景人物三檢視（僅無使用者模特時需要）`

```` ``` ````

`①打底服裝三檢視：緊身寬肩帶背心（遮腹不露胸）+夏季膝上緊身騎行褲，白底、無人物，正/側/背三視角，僅展示服裝本身版型細節。`

` `

`②目標服裝三檢視：若使用者已上傳服裝三檢視，跳過此步直接使用；若使用者上傳的是單品圖/平鋪圖，則生成白底、無人物、正/側/背三檢視，僅展示目標服裝本身。生成後可手動微調服裝細節（如裙長），調整結果由此三檢視承載，供STEP5引用。`

` `

`③（僅Case B，選擇"AI自動匹配模特"時需要）近景人物三檢視：白底、正/側/背三視角胸像（不做全身，生成Prompt內用"胸像"作為精準景別描述），呈現STEP1預設真實模特庫設定的五官/髮型/膚質。`

` `

`①②統一：photorealistic garment-only photography on white background, no model/person, no text/watermark/logo/shadow, accurate fabric texture/color/cut`

` `

`③統一：photorealistic white background bust portrait, no text/watermark/logo/shadow, soft natural frontal fill light on face (no backlight/shadow on face), skin strictly follows預設模特庫設定 (no added dark circles/dullness/redness/blemishes), matte skin—no shine/gloss but pores/texture retained (not smoothed/CG/plastic), light natural makeup not bare-faced, alert expression no tired look/under-eye bags`

```` ``` ````

`確認①：✅繼續 / ✍️修改[服裝/模特/打底裝]`

` `

`---`

` `

`## STEP 3：場景圖（純場景，無人物）`

` `

`風格（固定）：**Mid-century Modern Mix**，歐洲老公寓質感，按空間選對應版本，光線統一避免與人物光線衝突。`

` `

`**客廳**：白色啞光牆+深色實木地板，低矮儲物櫃/鋼框架椅，幾何地毯（邊角自然捲起，非完全平整），2-3幅70s裝裱畫，暖木色+芥末黃/磚紅/鈷藍點綴，綠植（葉片朝向不完全對稱）；沙發抱枕隨意斜靠/非對稱擺放，搭毯自然堆疊而非疊整齊。`

`**臥室**：暖白牆+深胡桃木床頭板，撞色抱枕，陶瓷檯燈，1-2幅裝裱畫，棕櫚植物，深胡桃木+暖黃/磚紅/藍灰點綴；**床單/被面帶輕微自然褶皺（非熨燙平整感）**，枕頭不完全對稱碼放、可有輕微凹陷壓痕，床尾可搭一件隨手放置的薄外套或毛毯。`

`**玄關**：啞光白牆+深色實木地板，懸空腿玄關櫃，異形掛鏡，1幅裝裱畫，綠植/乾花，深木色+啞光金屬+1個點綴色；櫃面可有隨手放置的鑰匙/包/一雙鞋，避免絕對整潔的擺拍感。`

` `

`**生活痕跡（三版統一要求）**：所有場景須保留輕微生活痕跡（褶皺、非對稱擺放、隨手物品），避免過度精緻/完全對稱/樣板間感，營造"真實有人居住"而非"攝影棚佈景"的觀感；但不做髒亂/雜亂堆積，痕跡感須剋制、自然。禁止畫面出現重複克隆元素（如葉片/地磚等圖案雷同、疑似圖章複製痕跡）。`

` `

`光線（統一三版）：自然日光感明亮通透(high-key airy daylight)，室內柔散光，均勻不過曝，正面順光，避免單一硬光源區域性反光；禁止昏暗/低曝光/moody色調——暗調會連帶把人物拖暗、放大黑點/噪點。`

` `

`調整方式：上傳家中實拍圖，AI識別其美學結合Mid-century Modern Mix融合復刻，光線仍按上方基調。`

` `

```` ``` ````

`生成[客廳/臥室/玄關]，不含人物。[對應場景基調][統一光線基調]`

`9:16豎構圖，如有參考圖則融合其美學生成。`

`shot on smartphone, bright airy daylight, natural indoor lighting, no text/watermark/logo, no cinematic lighting, no moody/dim tone`

```` ``` ````

`確認②：✅進入影片階段 / ✍️修改[場景元素/光線]（確認後為全片唯一標準）`

` `

`---`

` `

`## STEP 4：動作指令碼（單鏡15秒）`

` `

`**神態基準**：漫不經心自信 / 俏皮輕笑 / 眼神放鬆直視鏡頭（轉身/背對除外）。`

` `

`**變身機制**：單品從畫面外拋入/遞入（非"飛入自動上身"），雙手接住→雙手開啟展示衣物本身——上裝/下裝/外套均一視同仁，下裝不得跳過展示環節直接丟下/套入。展示後貼身瞬間完成變身：單件/連體——吊帶+騎行褲同步消失；多件——逐件重複該機制，上裝貼身僅消吊帶、下裝貼身僅消騎行褲（分部位消除，非同步）。下裝穿戴後須與上裝同等穩固貼合，全程不得出現下滑/鬆脫畫面。`

` `

`全部穿好後：**定點pose**（配飾同步展示，如有）→**展示三拍**：鏡頭固定不動，博主原地逆時針旋轉（非鏡頭環繞博主），保持自然重心轉移、髮絲與衣襬隨動，同步腿部微移步與手部擺動（撩發/觸擺/叉腰）；停頓為呼吸感自然停留而非雕塑定格——正面（配飾簡短互動）→側面停頓卡點→背面停頓卡點→回正面，連續無跳切→**定格ending**：走向鏡頭互動或原地定點pose收尾。`

` `

`時長參考：單件——變身~3-4s/定點pose~1-2s/展示三拍~6-7s/定格~2-3s；多件——每件變身~2.5-3s，其餘同單件版但相應壓縮。`

` `

`**配飾**：預設不主動新增，僅使用者對話明確要求時才呈現。`

` `

`確認③：✅生成Prompt套裝 / ✍️修改[動作/節奏]`

` `

`---`

` `

`## STEP 5：影片Prompt（影片本身無聲）`

`工具：優先Seedance 2.0，效果不理想改用Kling 3.0 Pro。`

` `

`**參考圖分工（原則：強參考源取代際最少的圖，減少AI生成疊加的失真偽影）**：`

` `

`- **Case A（使用者上傳模特圖）**：固定上傳：使用者模特原圖+打底服裝三檢視+服裝三檢視+場景圖。人物→使用者模特原圖；打底服裝外觀→打底服裝三檢視；目標服裝形態→服裝三檢視；環境→場景圖。`

`- **Case B（AI自動匹配模特）**：固定上傳：預設近景人物三檢視+打底服裝三檢視+服裝三檢視+場景圖。人物→預設近景人物三檢視；打底服裝外觀→打底服裝三檢視；目標服裝形態→服裝三檢視；環境→場景圖。`

`**IPHONE-CANDID美學基準**：`

```` ``` ````

`避雷：no cinematic lighting, no hyper-realistic, no 8k/masterpiece, no oversharpening, no blown-out highlight noise across frame`

`鏡頭：static shot, phone on stand, no camera movement/zoom, consistent medium shot down to below knee/calf, centered with negative space, stable background, soft focus falloff`

`色調：warm neutral white balance, soft creamy undertone, gently muted tones, VSCO-style not cinematic grade, mild contrast, avoid muddy grey midtones`

`光線：soft diffused bright indoor lighting, gentle highlight falloff (no blown highlights), soft natural frontal fill light on face (no backlight/shadow on face), no hard specular source, no backlight/silhouette`

`質感：shot on smartphone, subtle sensor noise/grain, matte skin (no shine, pores/texture retained, not smoothed), skin strictly follows reference (no added dark circles/dullness/redness/blemishes), natural hair strands, unposed candid feel`

```` ``` ````

` `

`### 影片 Prompt`

```` ``` ````

`⚠️硬性約束（生成前自查，優先順序最高）：`

`①禁止分段：Step1-4是同一固定機位內的連續動作序列，須作為一個不間斷的15秒長鏡頭一次性生成，禁止拆分為多個片段/分段生成，嚴禁將變身與展示三拍拆成兩段分別輸出。`

`②景別鎖定：全程保持中景（可到小腿以上），人物始終為畫面主體、佔比穩定，不得因旋轉/走動/展示動作而拉遠至全身或遠景，鏡頭位置與焦段全程不變。`

`③禁止服裝三檢視滲透：打底服裝三檢視/服裝三檢視僅用於提取服裝的形態/版型/長度等細節資訊，不得將三檢視本身的畫面元素（白底背景、平鋪/懸掛式構圖）帶入影片；全程只呈現家中場景，不得出現白底/攝影棚畫面。`

`④人物站位：博主須站在場景中光線最均勻充足、面朝主光源方向的順光受光區，避免站位處於暗角/背光位置。`

` `

`基於參考圖（按STEP5參考圖分工執行）：人物身份以強參考源為準（Case A用使用者模特原圖，Case B用預設近景人物三檢視），場景以場景圖為準，打底服裝外觀以打底服裝三檢視為準，目標服裝最終形態（含手動調整如裙長）以服裝三檢視為準（wearing the complete outfit from 服裝三檢視，範圍限定見約束③）；套用IPHONE-CANDID基準。`

`Step1：單品（多件按序如上裝→下裝[→外套]）從畫面外拋入/遞入（非飛入自動上身），雙手接住後雙手開啟展示（下裝同樣須展示，不得直接丟下/套入）；貼身瞬間完成變身（單件時吊帶+騎行褲同步消失；多件時逐件重複，上裝貼身僅消吊帶、下裝貼身僅消騎行褲，且下裝同等穩固不下滑）。`

`Step2：全部穿好後做俏皮定點pose（如有配飾同步展示look）。`

`Step3：展示三拍，鏡頭固定不動，博主原地逆時針連續旋轉（非鏡頭環繞博主），重心自然轉移、髮絲與衣襬隨動，同步腿部微移步與手部擺動/觸擺動作，停頓為呼吸感自然停留而非僵硬定格——正面（配飾互動）→側面停頓卡點→背面停頓卡點→回正面，連續無跳切，全程維持中景（小腿以上）不拉遠。`

`Step4：定格ending——走向鏡頭互動（不改變景別）或原地定點pose收尾，眼神看鏡頭。`

`[頭髮/面料物理反饋][情緒：漫不經心自信/俏皮輕笑]`

`影片本身不含任何音訊（無音效、無口播、無BGM），靜音生成，音樂在STEP6單獨生成後於成片階段合成。`

`9:16, ~15s, single continuous unbroken shot, no scene splits, medium shot down to below knee/calf throughout, no text/watermark/logo, silent/no audio`

```` ``` ````

` `

`## STEP 6：BGM風格庫（4類）+ 自動匹配`

`影片本身無聲（不含音效/口播/BGM）。生成後另呼叫音樂工具生成BGM（時長匹配~15s），與影片合成成片。`

` `

`**自動匹配邏輯**：依據STEP1解析出的服裝風格標籤自動匹配對應BGM型別（使用者可對話覆蓋）：`

` `

`| 服裝風格標籤 | 匹配BGM型別 |`

`|---|---|`

`| 極簡通勤 | A 成熟性感 |`

`| 甜酷Y2K / 居家 | B 可愛清新韓系 |`

`| 法式復古 / 度假森系 | C 度假法式鬆弛 |`

`| 街頭機能 | D 街頭酷 |`

` `

`### A｜成熟性感`

`風格參考：Ravyn Lenae《Love Me Not》（復古流行+indie-rock質感R&B）`

```` ``` ````

`風格：retro-pop / indie-rock R&B，60s girl-group甜蜜律動+indie-rock粗顆粒吉他，非電子流行編曲`

`節奏：114 BPM，4/4拍，簡單幹脆鼓型（非密集切分），Motown-style handclaps，prominent groovy bassline`

`和聲：C大調，簡單和絃（I-IV為骨架，可借一個副屬和絃）`

`樂器：吉他主導——清亮jangle吉他+輕微失真gritty guitar多軌疊加；bass清晰託底；handclaps+簡單鼓組；不用合成器堆疊`

`情緒：輕盈甜蜜+一點灑脫，鬆弛感>緊繃感，不做舞曲式催促感`

`質感：溫暖復古，模擬老錄音棚毛邊感`

`人聲：instrumental only；時長：~15s`

```` ``` ````

` `

`### B｜可愛清新韓系`

`風格參考：AKMU（樂童音樂家）式韓系小清新acoustic-pop`

```` ``` ````

`風格：韓系小清新acoustic-pop，原聲吉他為骨架，旋律輕快帶俏皮感，非厚重電子編曲`

`節奏：100-112 BPM，4/4拍，輕快彈性節奏，鼓組輕巧，可加清脆拍手/木琴點綴`

`和聲：明亮大調，簡單幹淨和絃，避免憂鬱小調`

`樂器：原聲吉他主導+清脆鍵盤/木琴點綴，弱化厚重bass，整體輕盈通透`

`情緒：治癒+校園清新+微俏皮，非性感/非厚重`

`質感：乾淨清透，輕微原聲錄音感`

`人聲：instrumental only；時長：~15s`

```` ``` ````

` `

`### C｜度假法式鬆弛`

`風格參考：法式chill/lounge，nu-disco式慵懶律動`

```` ``` ````

`風格：法式pop/chill lounge，慵懶鬆弛的度假感，不催促`

`節奏：90-104 BPM，慢悠搖擺感，鼓點鬆散，真實鼓+輕電子鼓混合`

`和聲：溫暖大調帶輕微jazz色彩(如加7th)`

`樂器：清亮/微失真吉他+溫暖bass，可加輕電子鍵盤或口琴點綴`

`情緒：鬆弛愜意+陽光感，不激烈不著急`

`質感：溫暖模擬感，比A組更鬆散慵懶`

`人聲：instrumental only；時長：~15s`

```` ``` ````

` `

`### D｜街頭酷`

`風格參考：alt-rock/街頭搖滾（適配15s短片強度，非極端重金屬）`

```` ``` ````

`風格：alt-rock，失真電吉他riff驅動，帶衝擊感但不壓迫`

`節奏：120-140 BPM，強勁直給鼓點，軍鼓+踩鑔驅動`

`和聲：小調/power chord為主`

`樂器：失真電吉他主導，緊實鼓組，電貝斯增強厚度`

`情緒：叛逆自信+張揚，衝擊力強但剋制在短片BGM尺度內`

`質感：現代搖滾混音感，punchy有力`

`人聲：instrumental only；時長：~15s`

```` ``` ````

` `

`確認④：✅按匹配型別生成BGM / ✍️指定其他型別[A/B/C/D]`
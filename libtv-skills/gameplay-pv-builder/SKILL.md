---
name: gameplay-pv-builder
description: "自制多類遊戲PV，UI 畫素錨定不形變，打造3A級遊戲效果"
---

name: game-promo-video\\

namespace: industrytitle: "遊戲宣傳 Demo 影片"description: "遊戲宣傳 Demo 影片設計師——含兩種玩法：① 三段式實機演示（Video A 引導流/Video B 劇情流/Video C 戰鬥流，各 15 秒共 45s），角色原畫→四檢視→3D 形象卡資產鏈、UI 畫素錨定禁形變區、色彩 LUT 三段一致；② 開放世界都市類 gameplay 短片（角色原型庫+場景模板、雙路徑原型/使用者照片、快節奏事件 4-Cut 公式與單鏡生活切片、5 類專有視角、卡點式剪輯節奏）。用 generate_image_v3 + generate_video_v3 + composite_video。"version: 3

game-promo-video

做原創/使用者自有遊戲的宣傳 Demo / 實機演示 / 開放世界類 gameplay 短片時用本 skill。含兩種玩法，按使用者需求二選一：

玩法一·三段式實機演示：Video A 引導流 / Video B 劇情流 / Video C 戰鬥流，各約 15s、總 45s，每段單鏡時長 ≤15s。全流程 = 背景風格定調 → 三段式劇本拆解 → 元素設計（角色原畫→四檢視→3D 形象卡 + UI/場景關鍵幀）→ 逐段影片生成 → 全段合片。

玩法二·開放世界都市類 gameplay 短片：借鑑開放世界犯罪/都市題材的視覺語法、鏡頭組織與角色型別（只借鑑視覺語法/城市氣質/鏡頭組織/角色型別，不復刻任何官方鏡頭、Logo、UI、商標、車牌或具體臺詞，不指名任何商業遊戲 IP），產出 30-60s 的混合體驗短片：熱帶度假廣告感 + 犯罪紀錄片質感 + 社媒荒誕感 + 開放世界城市展示。全流程 = 全域性設定 → 雙路徑角色資產 → 分鏡敘事（快節奏事件 or 單鏡生活切片）→ 逐鏡影片生成 → 音訊層 → 剪輯合成。

本 skill 自帶戰鬥動態/鎖 UI/畫素錨定/類 gameplay 鏡頭語言/卡點剪輯節奏等全部工藝，不外包給其它 skill。

本環境適配（源模型名 → 13 工具/SP）：image2 出圖（畫質引數由 Ask 使用者確認） → 全部走 generate_image_v3（同一影象引擎保三段一致）；四檢視/3D 形象卡可配 character_turnaround_3view 玩法；Seedance 2.0 → generate_video_v3；三段拼接 → composite_video（video layer + audio layer 均開）；Final_Video\_[Spec.md](http://Spec.md) / 規範文件 → text_editor（寫檔案）；storyboard_designer → 內部分鏡階段；multimodal_analyze_tool → 多模態讀圖（3D 材質分析 / UI 畫素錨定 / LUT 提取 / 使用者照片特徵提取）；Image_A1…A5 節點引用 → reference_nodes + {{NodeKey}} 佔位符；暫停/審閱 → reply_to_user 或卡片；使用者照片 ImageToImage 變角色 → reference_nodes 圖生圖路徑。源無付費/會員語義需剝離（含"高階會員 1080p"）。

生圖前，必須 Ask 使用者確認本次用 image2 模型的什麼畫質引數釋出，詢問 4 個選項：1，2k標準畫質（價效比高）；2，2k高畫質（價效比適中）；3，4k高畫質（土豪請隨意）；4，其他。

生影片前，必須 Ask 使用者確認本次用什麼影片解析度引數釋出，詢問 3 個選項：1，720p（價效比高）；2，1080p（價效比始中）；3，其他。

玩法一·三段式實機演示

流程與暫停

不要一次性跑完。 在每一關鍵階段後停下、與使用者確認再進下一步（可用卡片或 reply_to_user 邀請審閱）：規格定稿後 → 故事板完成後 → 元素（角色卡+關鍵幀）完成後 → 分段影片生成後 → 音訊/合片後。

1. 背景與風格定調

接收使用者主題關鍵詞，自動設定故事背景、確立全域性遊戲風格（如寫實 / 奇幻 / 賽博等）。撰寫 Final_Video\_[Spec.md](http://Spec.md)（text_editor），欄位：標題、型別、畫幅比、時長、視覺風格、語言。

2. 三段式劇本拆解（核心骨架）

將演示內容劃分為三段（各 15s）結構化指令碼，逐段秒級 timeline：

Video A（15s）引導流 — 系統互動與覺醒

0–3s：封面圖，模擬呼吸燈光效，執行 \[Start\] 按鈕互動。

3–10s：選人/技能展示，模擬滑鼠懸停高亮，展示角色 3D 待機 Pose 或招牌動作。

10–15s：第一人稱 POV，場景切入，從特定視點（甦醒/轉場）過渡到廣闊環境的 HDR 效果。

Video B（15s）劇情流 — 敘事互動與追蹤

15–25s：NPC 互動，撥出對話 UI，文字逐字顯示，背景保持環境動畫。

25–30s：場景追蹤，鏡頭跟隨角色快速移動至特定視覺地標，製造遭遇感。

Video C（15s）戰鬥流 — 核心戰鬥與結算

30–40s：實機戰鬥，快節奏對抗，UI 血條與技能槽實時動態變化。

40–45s：戰鬥結算，Boss 擊敗動作，彈出獲勝 UI 及獎勵結算特效。

3. 元素設計（資產鏈：原畫 → 四檢視 → 3D 形象卡 + 關鍵幀）

角色設計（核心邏輯）

原畫：出角色大師級 2D 設計原畫（主角 / Boss）。

角色四檢視：基於原畫 ImageToImage 生成白底四檢視（推薦 2K）。佈局規則：左側為面部特寫圖（捕捉面部細節、皮膚質感、妝容），右側依次排列全身正面圖、全身背面圖、全身側面圖（捕捉形體比例與裝備層級）。所有檢視須與原畫造型、配色、材質嚴格一致（可配 character_turnaround_3view 玩法）。

3D 形象卡：將四檢視轉換為 3D 真實感人物形象卡。

UI/場景關鍵幀：生成全鏈路一致的遊戲 UI 介面與場景關鍵幀，覆蓋：開始介面 / 選人介面 / 載入介面 / 第一人稱起手視角 / 第三人稱觀察場景 / 進入 Boss 戰。所有圖強制同一影象引擎保一致。

Video A：出 5 張關聯圖（封面、選人頁、技能頁、場景起手點等）。

Video B/C：出對話 UI 圖、行進場景圖、帶 HUD 的戰鬥首尾幀、結算圖。

4. 分析約束（多模態讀圖，供影片生成用）

3D 資產分析：深度分析 3D 形象卡的材質（金屬反射 / 皮膚質感 / 服飾紋理），產出光影描述引數。

UI 畫素錨定（核心）：分析帶 HUD 截圖，記錄血條、技能欄、對話方塊的精確畫素位置，將其設為「影片生成禁止形變區」。

色彩與光影一致（LUT）：提取全域性色彩傾向，確保三段影片從頭到尾色調、亮度高度一致，防止偏色。

5. 逐段影片生成（generate_video_v3）

詳細編寫每一場景的呈現內容、模擬滑鼠點選後高亮的 UI 反饋、以及高強度 Boss 戰鬥動作。四條提示詞指令：

互動段落指令（Video A）：以 Image_A1…A5（reference_nodes+{{NodeKey}}）為節點，模擬真實鍵鼠互動反饋（點選、高亮、光效），保持 3D 模型在各介面視覺一致。

敘事對話指令（Video B）：對話 UI 絕對清晰、不顫抖、不模糊，文字顯示與角色狀態同步。

動作戰鬥指令（Video C）：以戰鬥對峙圖為首幀、獲勝結算圖為尾幀。

核心指令（貫穿全段）：強制鎖定 UI，禁止血條和技能圖示產生任何位移、偽影或形變（對齊第 4 步禁形變區）；動作描述包含高頻位移、粒子特效、震屏打擊感。

6. 全段合片與音訊（composite_video）

將三段 15s 影片按邏輯拼接為完整實機演示 Demo，統一輸出高畫質（設定解析度、幀率、動作平滑度渲染標準）。合片時同步匹配對應音效：UI 音、環境音、打擊音。video layer 與 audio layer（背景音樂）均開啟。

玩法二·開放世界都市類 gameplay 短片

面向"開放世界都市犯罪/街頭題材類 gameplay 實機感短片"的獨立玩法：只借鑑公開題材通用的視覺語法、城市氣質、鏡頭組織和角色型別，不復刻任何官方鏡頭、Logo、UI、商標、車牌或具體臺詞，不指名任何商業遊戲 IP。

1. 全域性設定初始化

建立並鎖定 Final_Video\_[Spec.md](http://Spec.md)（text_editor）：畫面比例預設 16:9；主題定位為"受開放世界犯罪/街頭題材啟發的主題影片、分鏡、提示詞和視覺審查"。視覺風格不是單純"霓虹犯罪"，而是"熱帶度假廣告 + 真實犯罪紀錄片 + 社交媒體荒誕短影片 + 開放世界城市展示"的混合體：畫面表層熱鬧、性感、陽光、誇張；底層始終有追捕、債務、人情、走私、音樂產業、幫派和情侶逃亡的壓力。時長預設 30-60s 的小篇幅遊戲實機展示 demo，除非使用者明確要求更長故事。

2. 雙路徑角色資產

設計分鏡大綱時，角色創作提供兩條路徑，由使用者選擇：

方案一（經典角色原型）：使用內建角色原型庫建立人物（見下方原型庫），直接生成符合本風格、3D 遊戲實機質感的 3D 渲染參考圖（generate_image_v3）。

方案二（使用者定製角色）：使用者上傳個人照片（僅作創意參考）。多模態分析只提取性別與大概形象/氣質（如：性別、大致年齡範圍、面部大致輪廓或核心神態眼神），不描述或提取髮型、妝容、服裝穿著、配飾等具體細節——生圖階段由 ImageToImage 視覺參考路徑（reference_nodes 圖生圖）自適應提煉這些細節，無需在提示詞中生硬規定。輸出極簡英文特徵詞，例如：A Hispanic male in his 20s, with sharp facial features and determined eyes。強調將使用者現實基礎形象抽象為"該風格 3D 遊戲角色、第三人稱遊戲實機、UE 渲染"的底色，剔除照片背景與光照干擾。若使用者另上傳第三方影片/動圖作為動作或色調參考，需分析其鏡頭運動（第三人稱跟隨、低機位車輛追逐等）和色彩成分，轉寫供故事板與生成階段使用。

3. 角色原型庫 + 場景模板庫

設計故事板 key_elements 時，可預定義以下高頻角色、場景原型，支援靈活自定義擴充套件（原型均為通用化命名，非專案專屬）：

角色原型庫

MALE_LEAD：典型男主角（如熱血駕駛者、街頭青年），結實、疲憊警覺，擅長極限臨場反應。

FEMALE_LEAD：典型女主角（如冷靜決策者、幹練女強人），強硬、果斷，在困境中尋找出路。

UNDERGROUND_BOSS：地下產業巨頭/幕後大佬，常戴墨鏡、穿著奢華，眼神深不可測。

INFLUENCER_STREET：社媒網紅/街頭喧囂者，追求流量與關注，經常舉手機直播或熱衷派對。

MASTERMIND_PLANNER：行事縝密的行動策劃者，經驗豐富，老練且難以捉摸。

REGIONAL_SMUGGLER：老派海島/邊界走私者，粗糲、不羈，代表舊時代的犯罪遺留規則。

PARANOID_MONITOR：偏執監聽者，鬆弛體態，擅長在滿是螢幕與電臺的暗室中獲取線索。

CUSTOM_USER_HERO（方案二專用）：根據使用者照片分析轉換而來的定製主角，繼承使用者核心外形與眼神特徵，具有極強的身份代入感。

場景模板庫

METROPOLIS_NEON：熱帶霓虹都市、繁華海灘、高架橋樑、粉紫街道、積水路面。

COASTAL_ISLANDS：海島走私帶、藍綠海水、碼頭、白色遊艇、黃昏跨海長橋。

WILD_SWAMP：溼地荒野、沼澤蘆葦、直升機探照燈、泥水霧氣。

DECAYED_HARBOR：廉價港口城、汽車旅館、Motel 停車場、舊加油站。

INDUSTRIAL_TOWN：工業外圍鎮、鋼架廠房、煙囪、摩托車隊、滾滾塵土。

STORMY_MOUNTAIN：山地國家公園、森林幽暗山路、暴雨閃電。

4. 敘事結構（二選一）

分鏡數量預設控制在 1-3 個 shot，除非使用者明確要求更長更復雜劇情，優先精簡體量以保證渲染效率和單鏡質量。

結構 A：快節奏事件敘事（多切鏡組合，適合預告片或動作場面）——與使用者確認核心劇情後按三段展開：

開場段落·氛圍鋪墊：多用廣角俯視、天際線慢移，聲音融入環境音、遠處警笛或電臺，展現"平靜外表下的暗流湧動"。

中段段落·衝突失控：動作區域性特寫、角色爭執、追逐碰撞，穿插社交媒體手持/直播視角。節奏由平緩切到高頻，多機位頻繁切鏡。

收尾段落·懸念懸掛：特寫眼神、車門關閉、倒後鏡等，音樂突歇，只留引擎、呼吸或單調音效，留下戲劇懸念。

結構 B：單鏡頭生活/玩法切片（一鏡到底，5-12s）：強調高可讀性、單一連貫動作（如：給車加油、站在積水路口看棕櫚樹、在影院門前步行、慢速車輛碰撞金屬擠壓物理瞬間、手機拍攝遊戲螢幕的"洩露質感"）。必須嚴格規範：單鏡頭內禁止切換時空或拼接蒙太奇，保持極度流暢的類遊戲第三人稱跟隨相機延遲。

5. 五類專有視角

鏡頭語言分類，按敘事需要選用：

類 gameplay 第三人稱視角：機位偏低、偏側，處於角色身後，保留第三人稱空間感，帶有輕微延遲，隱去遊戲 UI。

車載/車旁混合視角：鏡頭處於副駕駛肩後、後視鏡、或後保險槓極低位置，前景為車體，霓虹燈光在溼車身和玻璃上高速滑過。

社交媒體豎屏視角：模擬手機自拍、手持直播，偶發抖動、短暫失焦與邊緣失真，畫面長寬比可轉為 9:16 插入。

監控/警方 bodycam 視角：CCTV 固定廣角、帶壓縮與噪點；bodycam 強烈晃動、帶有近距離魚眼畸變。

親密逃亡雙人視角：車窗、Motel 門框、百葉窗遮擋構圖，營造"犯罪壓力下的溫情與防備"。

音訊層：全域性配置一條主題音樂音軌（BGM：合成器波、現代說唱、南部電臺搖滾）；對話使用 key_element_audio 保持主角嗓音的粗糲/沙啞或拉丁語調。

6. 單鏡設計規則 + 多切鏡規則（4-Cut 公式）

單鏡頭一鏡到底（生活切片/單一動作）設計規則：

核心設計意圖：適合 5-12 秒的穩定短鏡頭，核心是"一件事從開始到結束"，動作絕不復雜，鏡頭絕不亂切，以此建立開放世界的真實生活與 gameplay 質感。

動作設計限制：只保留 1 個主行為（例如：給車加油、遞熱狗、拿啤酒、開啟車門、掃碼付款、擦擋風玻璃、點菸、把現金塞進口袋）。禁止在單鏡頭內同時設計多項並行或連貫的複合劇烈動作（如不要讓角色在加油的同時打電話、掏槍、奔跑）。

鏡頭運鏡限制：只保留 1 種運動方式（如慢速推近、側向橫移跟拍、類 gameplay 固定或浮動視角、車內輕微手持搖晃）。

音訊配合設計：音軌需提供極具臨場感的環境音錨點，如車流聲、遠處警笛、夜店低音、便利店門鈴、加油槍滴答聲。

多切鏡事件（追逐/衝突/搶劫/混亂事件）設計規則：

核心設計意圖：推薦將每個多切鏡事件統一設計為 15s 的單個 shot，最大化發揮影片生成模型在單次 15 秒生成中產出豐富內部切鏡、流暢場景過渡和飽滿資訊密度的最佳效能。

分鏡結構公式（4-Cut 經典流）：

Shot 1（環境與威脅）：交代所處場景、地點環境以及面臨的突發威脅/對手。

Shot 2（動作細節特寫）：展示高動態動作區域性特寫（如猛踩油門、換擋、推搡、槍栓拉動）。

Shot 3（反應與阻礙）：展現角色的受阻反應、路人荒亂、物理撞擊或警燈閃爍等不同機位畫面。

Shot 4（懸念/終局衝擊）：展現逃脫、撞擊瞬間或極具張力的定格畫面，留下懸念鉤子。

空間連續性限制：高動態鏡頭必須維持空間、時間、光影的一致。角色、車輛須在相同街區或空間，朝一致方向運動，避免畫面跳躍穿幫。

切鏡與音訊配合：每個短鏡頭只承載 1 個明確的資訊點。鏡頭要全景、車內、低機位、特寫、社媒畫面交替混剪，併為每次碰撞、轟鳴、破碎聲在音軌中預留精準的音效對齊點（如引擎轟鳴、玻璃碎、警用廣播、輪胎摩擦）。

7. 逐鏡影片生成繫結規則（generate_video_v3）

角色 3D 渲染優先用 generate_image_v3；方案二在圖生圖路徑下輸入使用者照片，生成定製主角的專屬 3D 渲染全身照與面部側寫。

Shot 影片統一生成時長 15s（多切鏡事件），以發揮最出色的多鏡頭內部切鏡與自然轉場渲染效果；解析度預設 720p（源"高階會員優先 1080p"語義剝離，不落地）。

參考繫結規則：

視覺參考：必須繫結鏡頭內出現的角色 asset_id（自定義主角或經典原型）；必須繫結當前所在的場景 asset_id。

連續性參考：若屬高強度多切鏡追趕/撞車場景，生成 Shot N 時須繫結 Shot N-1 的影片作為參考，確保車輛顏色、受損程度和光影平滑過渡。

聲音繫結：若鏡頭內包含角色對鏡頭說話，須在音訊資訊中繫結該角色專屬聲線資產，實現音畫同步。

8. 提示詞構建（write_the_prompt）

通用構建原則：絕對禁止包含具體商業遊戲名稱、版權標誌或品牌 Logo；採用"導演與調色師"視角，多用動作描述和具象材質詞，不寫情緒猜測。

四色調口訣：

都市霓虹夜晚：pink and purple neon, wet black asphalt reflections, cyan highlights, dynamic sodium lights

熱帶海岸黃昏：golden hour glow, teal sea, distant silhouette of palms, hazy sunset sky

晨霧溼地沼澤：olive green muddy water, dense morning fog, silver gray, intense helicopter searchlight beam cutting through haze

白日光照：harsh tropical sunlight, overexposed edges, deep dark hard shadows, heat shimmer

角色 3D 渲染 prompt 結構：統一採用該風格、3D 遊戲、第三人稱遊戲、UE 渲染的高畫質寫實 3D 遊戲質感風格，生成一張全身+側面特寫的"角色 3D 實機渲染圖表"（horizontal side-by-side layout）：

A 3D game character render of \[character name\], a \[gender\] with \[hair/face features\], wearing \[outfit\], open-world game style, 3D game model, third-person game gameplay character, Unreal Engine 5 render, high fidelity, realistic game engine shaders, wet skin texture, high contrast tropical lighting.

影片 prompt 結構：統一格式化為 鏡頭機位 + 視覺參考佔位符 + 動作運動堆疊 + 環境聲學標記。

格式範例：\[Camera: third-person trailing angle with slight delay\] &lt;&lt;&lt;image_1&gt;&gt;&gt; \[Character: young male protagonist\] is fueling his dusty muscle car at a neon-lit gas station, simple action of holding the gas nozzle. \[Background: wet asphalt, pink and cyan glowing neon signs, swaying palm trees, humid metropolis night atmosphere\]. \[Audio: (ambient club bass), &lt;distant police siren&gt;\]

運動堆疊設計：從相機運動（Camera）開始描述，接著是主體人物/載具動作（Action），再到空間環境變化（Environment），最後用括號包裝音效或對白細節。影片內對白用 {dialogue} 包裹（例：{We are in this together, okay?}）；音樂氛圍聲用 (music) / (ambient club bass)；動作音效用 &lt;tire screech&gt; / &lt;siren&gt;；影片 prompt 尾部預設帶 no music, no subtitles, no logo, no branding, photorealistic game trailer concept 負向過濾詞，背景音樂交由音訊軌道統一合成，防止音訊重疊。

9. 配方庫（單鏡/多切鏡模板 + 高頻鏡頭配方）

單鏡頭一鏡到底配方

結構公式：one continuous shot, single simple action, \[角色\] 在 \[地點\] 做 \[動作\], camera \[單一運鏡\], background shows \[代表性環境元素\], humid realistic tropical metropolis atmosphere, no cuts, no montage, no logo

Prompt 模板：One continuous cinematic shot in an open-world inspired metropolis. A \[character type\] performs one simple action: \[action\]. Location: \[place\]. Camera: \[slow push-in / side tracking / fixed CCTV-like frame / handheld phone follow\]. Background: palm trees, humid neon, wet asphalt, traffic, random NPCs, distant police siren. Keep the action simple and readable, no cuts, no montage, no official logos, no readable real brands.

應用例項（方法級示例，照搬可直接改詞替換）：

加油：One continuous cinematic shot in a neon-lit metropolis gas station at night. A young male protagonist refuels a dusty muscle car, one simple action from grabbing the nozzle to putting it into the tank. Camera slowly tracks sideways from the rear wheel to his face, wet asphalt reflecting pink and cyan lights, palm trees and traffic in the background, distant police siren, humid air, no cuts, no montage, no logos.

賣熱狗：One continuous street-life shot in sunlit coastal city. A hot dog vendor hands a wrapped hot dog to a tourist while scooters and beachgoers pass behind them. Camera is fixed at chest height with slight handheld sway, bright tropical sun, palm shadows, ocean breeze, colorful NPC crowd, simple readable action, no cuts, no montage, no official logos.

第三人稱溼路步行：One continuous game-inspired third-person gameplay shot. A young man in a sleeveless shirt stands on a wet boulevard after rain, then slowly starts walking forward. Camera follows from behind at shoulder height with slight floating game-camera movement. The road is covered with puddles reflecting high-rise hotels, palm trees, neon signs, traffic lights and passing cars. Keep one simple movement, no cuts, no montage, optional minimal HUD feeling, no official logos.

夜街娛樂區探索：One continuous third-person exploration shot in a humid entertainment district at night. A playable character walks toward a bright movie theater entrance, passing food stalls, NPC crowds, LED billboards and glossy wet pavement. Camera stays behind the character with a slow forward follow, like open-world gameplay with cinematic lighting. No cuts, no combat, no logos, no readable real brands.

多切鏡事件配方

結構公式：multi-shot sequence, 4 fast cuts, same event continuity: Shot 1 establish location and threat, Shot 2 close-up action detail, Shot 3 reaction / obstacle, Shot 4 escape / impact / hook. Keep same characters, same location, same time of day, no official logos.

Prompt 模板：Create a crime-action inspired multi-shot sequence with 4 quick cuts, same characters and same location continuity. Shot 1: \[wide establishing shot, location, threat\]. Shot 2: \[close-up action detail\]. Shot 3: \[reaction or obstacle, different camera angle\]. Shot 4: \[escape / impact / cliffhanger\]. Style: humid metropolitan realism, handheld urgency, low vehicle angles, wet reflections, social media chaos in background. No official logos, no real brands, no gore.

應用例項（方法級示例）：

追逐：Create a high-speed multi-shot chase sequence with 5 quick cuts, same car and same street continuity. Shot 1: wide night street outside a neon motel, a muscle car suddenly reverses as police lights appear. Shot 2: close-up on tense driver slamming the gear shift, dashboard shaking. Shot 3: low rear bumper camera as the car fishtails across wet asphalt, pink neon reflections stretching behind it. Shot 4: vertical phone video from a bystander as the car blasts past a hot dog stand and people jump back. Shot 5: car interior rear-view mirror showing police headlights closing in. Style: humid metropolitan night, handheld urgency, fast cuts, tire smoke, sirens, no logos, no gore.

打架：Create an action-heavy multi-shot motel fight sequence with 4 quick cuts, same parking lot continuity. Shot 1: wide shot of a cheap neon motel parking lot, two men arguing beside a pickup truck. Shot 2: handheld close-up as a sharp female protagonist grabs one attacker by the shirt. Shot 3: low angle as the attacker hits the car door and beer cans scatter on wet pavement. Shot 4: male partner opens the passenger door and shouts for her to get in as police sirens rise. Style: gritty coastal harbor night, sodium lights, wet asphalt, fast handheld cuts, no gore, no logos.

車輛碰撞物理：Create a high-fidelity vehicle collision sequence with 4 quick cuts, same highway continuity. Shot 1: side-rear camera of a sports car scraping against a police cruiser on a sunlit highway. Shot 2: close-up of crumpling metal, shattered headlight glass and tire smoke as the vehicles grind together. Shot 3: overhead tracking shot as both cars drift across lanes, the police car pushing into the sports car's rear quarter. Shot 4: low bumper camera as the sports car breaks free and accelerates, leaving debris and skid marks behind. Style: realistic in-game vehicle physics, hard sunlight, road vibration, metal deformation, fast but readable cuts, no logos.

8 個高頻鏡頭配方（可直接參考或呼叫）：

城市開場：Metropolis-inspired coastal city at dusk, palm trees, high-rise hotels, neon signs turning on, wet asphalt, traffic and pedestrians, humid air, distant police siren, slow aerial push-in to street level, saturated but realistic, no logo, no real brands.

雙人逃亡：two fugitives in a motel parking lot at night, young tense couple, muscle car idling, pink neon reflected on wet pavement, cash bag and old phone, handheld camera, intimate criminal tension, police lights far away, cinematic game trailer realism.

夜店/社媒奇觀：Coastal city nightclub exterior, crowd livestreaming with phones, luxury cars, pink and cyan neon, police cruiser nearby, people laughing and arguing, social media chaos, stabilized tracking shot through the crowd, humid night reflections, no logo.

溼地追捕：Tropical swamp at dawn, fog over muddy water, reeds in foreground, airboat cutting through, helicopter searchlight far away, two fugitives hiding near abandoned boat, handheld low camera, tense quiet, olive green and gold sunrise palette.

港口交易：night port deal between shipping containers, sodium orange lights, wet concrete, trucks and cranes, duffel bag exchange goes wrong, fast lateral tracking shot, sparks and police radio fragments, gritty realistic crime trailer.

類 gameplay 車戲：Open-world inspired third-person gameplay-like driving shot, UI hidden, camera mounted low behind the side of a muscle car, driving through a humid coastal metropolis at night, wet asphalt reflecting pink neon and police lights, camera follows with slight delay and realistic shake, not a clean car commercial, cinematic in-game footage feel, no logos.

手機圍觀：vertical phone livestream from a random bystander in a neon city, crowd filming a police chase outside a nightclub, shaky imperfect framing, people blocking the lens, pink and cyan neon, wet street reflections, comments implied but no readable UI text, chaotic social media realism, no official logos.

監控荒誕事件：fixed CCTV camera inside a small convenience store, humid night outside, an absurd incident suddenly enters frame, compressed surveillance texture, wide-angle corner view, fluorescent lights, reflections on glass doors, grounded dark comedy, no gore, no logos.

10. 剪輯合成三段節奏（composite_video）

快節奏事件敘事（多切鏡組合）：開場階段單鏡頭時長 4-5 秒，畫面淡入淡出，切鏡平緩；中段關係網失控，剪輯點密集（0.8-1.5 秒一剪），採用無過渡硬切與閃白，模擬高速心跳；結尾逃亡懸念，鏡頭拉長到 6-8 秒，淡出至黑色。

類 gameplay 生活切片：一鏡到底，全長 5-12 秒無任何剪輯點。

音影片精確對齊：音軌 1（環境音效/SFX）——槍聲、碰撞聲、引擎轟鳴與影片畫面動作發生幀嚴格對齊，車輛物理碰撞瞬間音量瞬時調大 6dB 並加低音震動效果；音軌 2（對話語音/Narration）——對話開始前 0.3 秒 BGM 自動衰減 12dB（Ducking），對話結束後 0.5 秒平滑回升；音軌 3（背景音樂/BGM）——影片最後 10 秒（懸念部分）BGM 突然抽空或做低通濾波處理，僅留沉重呼吸聲與單調警笛殘音，強化末路張力。

輸出規格：匯出階段嚴格遵循 Final_Video\_[Spec.md](http://Spec.md) 中的引數，不允許包含黑邊或拉伸畫面。

邊界（勿用本 skill，改道）

2D 動畫風格宣傳 → cartoon-flow。

特定商業遊戲 IP 復刻（官方鏡頭 / Logo / UI / 商標 / 車牌 / 臺詞）→ 拒絕；本 skill 只做原創或使用者自有遊戲。
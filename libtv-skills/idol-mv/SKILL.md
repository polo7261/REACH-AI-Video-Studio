---
name: idol-mv
description: "校園青春濾鏡，一鍵出片女團MV"
---

# idol-mv

做平成 AKB48 風格青春偶像 MV 時用本 skill。核心氣質:**日系膠片質感 + 紀錄片手持攝影 + 校園青春敘事 + 女子團體群像感**,以 2009–2014 黃金年代為審美基準。核心基準:所有設計對齊"平成時代 AKB48 黃金年代青春偶像 MV"——**不是完美偶像,而是正在發光的普通成員**。

> 本環境適配:Seedance/MultiModalToVideo → `generate_video_v3`;元素圖/TextToImage/ImageToImage → `generate_image_v3`;BGM/VO/text_to_instrumental/text_to_narration → `generate_audio`;text_editor → `write_file_v2`;video_assembler → `composite_video`;`<<<image_n>>>`/asset_id 槽位 → `reference_nodes`+`{{NodeKey}}`;里程碑確認 → `ask_human`。**prompt 寫法與運鏡詞彙全部內聯本 skill,不外包 image-prompt-director / cinematic-motion-language**。適配點:Seedance wrapper 語法((...)音樂/<...>音效/{...}對白/【...】字幕)按 `generate_video_v3` 提示詞能力適配,無對應則改為音效意圖描述並註明;refer_type 引數(Kling 3.0 Omni 非會員備用)、會員分支、超分(Jimeng SR/MediaKit)本環境無對應→正當刪除、見對賬;Midjourney 禁用於一致性一條轉為"探索圖不作一致性錨"方法保留;模型專名按本環境生成面適配改寫(非刪除)。

## 流程(5 里程碑暫停,不一次跑完;用 `ask_human` 展示 review 清單獲明確確認再續)

1. **Final_Video_Spec**(`write_file_v2`):鎖定全域性引數——畫面比例(預設 16:9)、目標時長、輸出語言(日語/中文歌詞)、視覺風格基調(平成膠片偶像 MV)、色彩系統(夏日青春膠片)。
2. **分鏡**(`storyboard`):先建 key_element(成員角色+核心場景+關鍵道具),再按固定結構**日常→放學→友情→練習→歡笑→舞臺→青春高潮→黃昏收尾**規劃 shot 列表,同步 audio_layer(BGM+可選 VO)。
3. 完成分鏡後,**掃描已有使用者上傳素材**,將匹配資源繫結至對應 Storyboard 槽位,避免重複生成。
4. **元素形象圖**(`generate_image_v3`):生成所有 key_element 形象圖(角色參考圖**雙格:半身+全身**、場景參考圖示膠片基調)。
5. **逐 shot 影片**(`generate_video_v3`):優先以 element 圖為視覺參考。
6. **音訊**(`generate_audio`):BGM + 音效/VO 音訊層。
7. **合成**(`composite_video`):時間線剪輯匯出成片。
> 依賴:2→1;3→2;4→2;5→4;6→2;7→4,5,6。**暫停節點 A–E 逐項展示清單與提問話術見** `references/pause-nodes-and-vertical.md`(5 節點全文+豎版專屬暫停 V-A/V-B+豎版短時長通用排程)。使用者上傳素材優先繫結為對應 key_element 資產,不重複生成已有內容。

## 素材分析(`analyze` · 將所有輸入解讀為"AKB48 黃金年代青春偶像 MV 素材")

**基礎分析視角**:角色——識別氣質分層(center girl 核心能量/shy 害羞/genki 元氣/cool beauty 清冷/emotional supporter 感情擔當),評估自然妝容程度/青春笑容真實感/服裝風格(校服/夏裝/舞臺服)/群像化學反應;場景——識別青春時空(放學教室/天台/夏日操場/電車站臺/河堤/夏祭/便利店門口/黃昏籃球場),分析光線質感(夏日自然光/黃金時刻暖光/教室熒光燈感/潮溼夏日空氣感);攝影/影像——識別膠片感(柯達 Gold 200 暖調/富士 Pro 400H 冷柔調/軟顆粒/高光溢位/過曝區域/褪色感),評估拍攝方式(手持紀錄片感/偷拍式青春視角/自然 vs 商業構圖);音訊(如有)——BGM 風格(上進 J-Pop/青春吉他/idol 合唱/nostalgic 明亮旋律),環境音(蟬鳴/電車過道/操場歡笑/社團練習聲/運動鞋踩地)。**輸出重點**:轉化為可直接注入 Storyboard 的語言(角色/場景 element 描述、shot 情緒標註、audio_layer 風格指引)。

**上傳素材處理三套流程**(照片 identity anchor 四步 / 音訊型別判定四步 / 場景 lighting+spatial anchor 五步):全文見 `references/upload-analysis.md`。

## 設計 key_element

**角色 element character**:每位成員須含 氣質標籤/妝容/髮型/服裝/標誌性動作或表情/禁止事項。若使用者提供參照圖,角色描述必須與圖中所見一致,氣質模板僅作格式參照、不覆蓋使用者上傳的真實面部特徵。
- **禁止(所有角色通用)**:高階時裝感、歐美超模臉、AI 網紅妝、強烈性感化。
- **允許(所有角色通用)**:稍亂的髮絲、不均勻的動作、自然反應、業餘魅力。
- **五大氣質型別設計模板**(Center Girl / Genki / Shy / Cool Beauty / Emotional Supporter,各含外貌錨點/服裝設計/標誌性動作與表情/prompt 氣質詞四小節):全文見 `references/character-templates.md`。

**場景 element scene**:優先場景池 13 個——放學後的教室、學校天台、夏日操場、河堤、電車站、社團教室、校園走廊、櫻花街道、夏祭、海邊、東京街頭、便利店門口、黃昏籃球場。每場景須描述:光線來源(夏日斜陽/熒光燈/祭典燈籠)、空間細節(黑板上的字/腳踏車/鐵絲網)、環境音暗示。**禁止**:豪華現代建築、歐美夜店、賽博朋克城市、高階時裝秀場。
- **八大核心場景標準化模板**(教室/天台/操場/河堤/夏祭/電車站臺/練習室/走廊,各含光線錨點/空間細節錨點/膠片色調基準/環境音暗示):全文見 `references/scene-templates.md`。實際創作可微調、不必逐字照搬;使用者提供真實場景照片時以照片特徵為準覆蓋對應欄位。

**道具 element prop**:常用標誌性道具須單獨建 element prop 供 shot 直接引用,避免每次重描外觀。每道具須含 外觀描述(形狀/顏色/材質)、使用方式(持握/佩戴/放置)、出現段落建議、禁止搭配寫法。
- **七個道具 element 模板**(髮飾/書包/應援棒/線香花火/腳踏車/筆記本/冰棒):全文見 `references/prop-templates.md`。

## 季節限定變體(觸發時對場景池的色調基準/空間細節/環境音做對應替換,其餘角色規則與 MV 結構不變)

三變體——🌸 櫻花季(春)/🌊 海邊(夏末)/🎑 文化祭(秋),各含 觸發條件/色調基準替換/場景細節替換/情緒傾向調整/prompt 附加詞彙/環境音替換:全文見 `references/seasonal-variants.md`。

## 短片版本結構(30s/60s/3min · 按優先順序剪枝而非等比壓縮保持敘事完整;八段式完整結構僅用於 3min 以上版本)

- **30s(28–33s)**:保留 3 段——歡笑高潮(段 5,能量頂點不可刪,壓 2–3 shot 約 8–10s)、舞臺表演(段 6,偶像核心,1–2 shot 約 6–8s)、黃昏收尾(段 8,情緒落點,1 shot 約 8–10s);刪除日常/放學/友情/練習/青春高潮。節奏:歡笑高潮 shot 壓 1.5–2.5s 快切開場;舞臺 2–4s 直接承接不做過渡;黃昏留足 8s 唯一留白;BGM 從 chorus 爆發點起、不用 intro/verse。shot 總數 4–6。
- **60s(55–65s)**:保留 5 段——日常(段 1,壓 2–3 shot 約 8–10s,優先空鏡+1 角色近景)、友情(段 3,2–3 shot 約 8–10s,正反打對切優先)、歡笑高潮(段 5,3–4 shot)、舞臺(段 6,2–3 shot 約 10–12s)、黃昏收尾(段 8,1–2 shot 約 10–12s);刪除優先順序:練習(段 4)>放學(段 2)>青春高潮(段 7),仍超則日常壓至僅 1 空鏡(約 3s)。節奏:日常→友情→歡笑三段連續、由慢(3–4s)→中(2–3s)→快(1.5–2.5s)遞進;BGM 從 intro 末進 verse、歡笑高潮前踩 chorus 爆發;舞臺與 chorus 節拍對位,黃昏在 outro 漸弱完成。shot 總數 10–14。
- **3min(2:50–3:15)**:用完整八段式,各段 shot 數參考標準模板。段落時長分配參考:日常 20–25s/5–7 shot、放學 15–20s/4–5、友情 20–25s/5–6、練習 20–25s/4–5、歡笑高潮 15–20s/4–6、舞臺 25–35s/5–7、青春高潮 20–25s/3–4、黃昏收尾 25–35s/3–4。節奏壓縮優先順序(超時則):先壓練習(5→3 shot,去腳步特寫保鏡子全景與表情中景)、再壓放學(去書包收拾近景、從推門過曝直接奔跑跟拍)、最後壓日常(減至純空鏡建立 2–3 shot);**不壓縮**歡笑高潮/青春高潮/黃昏收尾(情緒核心)。shot 總數 30–40。
- **跨版本通用**:①開場原則——任何版本第一個 shot 必須前 3 秒內建立視覺記憶點(逆光剪影/笑容特寫/標誌場景空鏡),禁用對話或說明性畫面開場;②結尾原則——任何版本最後一個 shot 都必須是黃昏收尾類(定格笑容或夕陽剪影)、時長不少於 5s,soft fade to warm white 收尾;③BGM 對位——分鏡階段即標註各段對應 BGM 結構段(intro/verse/chorus/outro),確保歡笑高潮踩 chorus 爆發點、黃昏收尾落 outro 漸弱區間;④**不可拆分 shot 對**——放學後奔跑(段 2)與天台推門過曝(段 2)為強連續對,裁剪時要麼都保留要麼都刪除。
- **Reels 短時長 BGM 結構標註規範**(15s/30s Reels,分鏡階段須在每 shot 旁註明對應 BGM 時間戳區間與節拍標記):見 `references/short-version-and-vertical-shot.md`。

## 豎版(9:16)專項(在標準分鏡規則基礎上疊加,不替換)

構圖適配 5 原則、字幕安全區 4 區(核心表達區 70%×65%)、運鏡適配 4 規則、豎版 shot 時長調整、豎版短時長版本段落裁剪優先順序(15s/30s Reels):全文見 `references/short-version-and-vertical-shot.md`。要點:主體居中縱向(上下各留約 15% 安全邊距);豎版幀寬僅橫版 56%、優先中景近景特寫、全景須站立居中;同框建議不超 2 人、3 人及以上須縱向錯落或拆多單人近景快切;人物眼睛落畫面上方 1/3;空鏡優先縱深感強構圖(走廊透視/河堤延伸/電車軌道消失點)。**字幕安全區**:上方 8–10%(平臺標題欄,禁重要面部/道具特寫)、下方 20–25%(平臺文字/音樂/互動按鈕,禁主要表情/關鍵動作)、右側 10–12%(點贊評論分享縱列,主體/關鍵道具不可貼右緣)、核心表達區中央 70%(水平)×65%(垂直)、所有情緒高點/關鍵手勢/笑容定格幀必須落此區。

## 八段式 MV 標準 Shot 模板(每段:節奏基調/景別搭配/運鏡節奏/示例 shot;實際按人數場景調整,不必逐字照搬)

**每個 shot 必須包含**:場景(關聯 element scene ID)、故事節拍(角色動作與情緒引用 element character ID、臺詞/內心旁白如有)、攝影語言(景別全景/中景/近景/特寫+機位角度低角/平視/俯拍+運鏡手持遊移/軟變焦/跟拍/固定偷拍)、時長參考(青春蒙太奇節奏單 shot 4–10s,情緒收尾 shot 可延長至 12–15s)。**禁止**:黑暗概念風、強劇情反轉、賽博未來感。

八段(1 日常片段 / 2 放學後 / 3 友情時刻 / 4 練習場景 / 5 歡笑高潮 / 6 舞臺表演 / 7 青春高潮 / 8 黃昏收尾)每段的節奏基調+景別搭配+運鏡節奏+示例 shot 全文:見 `references/eight-part-shot-templates.md`。

## 元素圖與 shot 影片生成(`generate_image_v3` / `generate_video_v3`)

**角色/場景形象圖**(`generate_image_v3`,`ai_model` 指定 `LibNavo Pro`):源推薦 Nano Banana Pro(2K,跨圖面部一致性最強,適合角色參考圖雙格構圖及多角色聯合生成);風格探索階段可額外用探索模型生成氣質參考,但**探索圖不作一致性錨點、不用於角色主圖**(源 Midjourney 禁用於一致性一條的方法保留)。同一角色多造型/多場景版本用圖生圖以首版參考圖為基準保持面容氣質連貫。角色參考圖預設橫向雙格構圖:左=半身頭肩特寫(面部識別錨點),右=全身造型(服裝/髮型/配飾完整呈現)。

**shot 影片生成**(`generate_video_v3`):
- 預設路徑 MultiModalToVideo(源 Seedance 2.0,720p)。每 shot 參考輸入:①**element 影象(必須)**——該 shot 出現的所有角色 element 圖+場景/道具 element 圖;②**前一 shot 影片(可選)**——僅當與前 shot 強連續性(同場景連續動作/情緒直接承接)時才加,通常跳過影片參考保持青春蒙太奇切割感。
- 需帶同步音效/對白的 shot(如舞臺表演)切換至 FirstFrameToVideo(源 Veo3.1 Fast,720p),避免與獨立 narration VO 軌道疊加衝突(本環境按 `generate_video_v3` 的首幀/音訊能力對映)。
- **豎版專項生成路徑**(原生 9:16 優先:Wan2.6 無音效需求 / Kling 3.0 Audio 需同步對白音效;Seedance 橫版生成→中心裁切 56% 備用方案含構圖預置詞/裁切錨點/損失評估重生成表;非會員豎版):全文見 `references/vertical-shot-generation.md`。會員分支/refer_type/超分為本環境無對應的適配點,見對賬。

**跨 shot 角色面部一致性保障**:
- **一致性檢查表**(每完成一批 shot 即每 3–5 shot 或每段落結束時,繼續前執行,不透過則先重生成):

| 檢查項 | 透過標準 | 不透過判定 |
|---|---|---|
| 面部識別錨點 | 臉型、眼型、髮色與 key_element 參考圖對應,肉眼可辨同一人 | 五官結構明顯漂移、髮型/膚色突變 |
| 妝容與髮型 | 劉海形狀、髮量感與 element 描述一致 | 劉海型別改變(軟劉海變中分)、髮色階躍 |
| 服裝連貫性 | 同段落內同一角色服裝與 element 描述一致 | 段落內服裝款式或配色無劇情原因變化 |
| 氣質基調 | 面部表情與氣質標籤(元氣/害羞/清冷等)保持對齊 | 角色氣質與設定明顯偏離(如元氣型變冷漠型) |

- **重生成判據**:必須重生成——面部識別錨點不透過(臉型/眼型明顯走樣)、同段落內服裝無劇情原因變更;建議重生成——氣質基調偏離超 1 檔、髮型突變影響辨識度;可接受保留——輕微手持運動瞬間失焦、光線變化引起的自然膚色細微差異、表情在合理情緒範圍內的自然波動。重生成優先調 prompt(強化面部特徵詞/換 seed/減 shot 時長)而非直接換模型;同 prompt 連續兩次仍不透過再考慮切 FirstFrameToVideo 以 keyframe 強控首幀外貌。
- **多成員同框 shot 參考圖繫結策略 5 條**:①為每位出現成員各繫結獨立參考圖(左格半身特寫優先作面部錨,用 `{{Node1}}`/`{{Node2}}` 依次繫結,prompt 中明確每佔位符對應成員及參照側重-面部/全身/服裝);②成員數量上限——單 shot 建議同框不超 3 人,超 3 人易混淆面部、優先拆多個近景/中景切換,群像全景可放寬至 5 人但降個體面部精度預期;③主角優先——有明確 center girl 或情緒焦點成員時將其參考圖放第一個佔位符(模型對首圖權重更高);④避免參考圖衝突——髮型/服裝色系相近時用方位詞區分(「畫面左側成員參照 `{{Node1}}`」),仍混淆可先生成單人 shot 再合成多人;⑤團體群像全景——成員多且面部識別非主要要求(遠景奔跑/舞臺全景)時用多角色聯合參考圖(橫向多格構圖)替代多張獨立參考圖,僅適用於全景/遠景、中景及以內仍須獨立繫結。

**BGM 生成**(`generate_audio`):源 Suno 5(備選 Mureka 8)。**不寫知名音樂人/樂隊名稱**(高失敗率)——用風格描述替代(如"upbeat J-Pop idol chorus, bright acoustic guitar, nostalgic synth, cheerful melody")。BGM prompt 詳細寫法見"提示詞寫法"節 BGM 專項。

## 提示詞寫法(全部內聯,不外包)

**最高優先順序(全域性)**:使用者中文互動時 prompt 正文以中文撰寫;若有日語對白/歌詞臺詞按原語言保留在對應位置。

**影象 prompt 與膠片視覺基準詞、角色/場景/光線描述錨點、Nano Banana Pro 雙格構圖指令+identity anchor block 格式+多角色聯合圖+場景圖寫法**:全文見 `references/image-prompt.md`。要點:導演+攝影師聯合描述(自然語言主體+動作+環境、短語風格色彩光線構圖);膠片參考 Kodak Gold 200 暖調/Fuji Pro 400H 冷柔調、soft grain 輕微過曝高光柔化溢位、允許輕微漏光鏡頭眩光軟焦感、**禁 HDR 銳化感/超清 CG 感/商業級銳化**;角色氣質詞 youthful awkwardness/idol smile/natural reaction/genuine laughter/amateur charm、**禁性感化/高冷時尚感/歐美超模氣質**。

**影片 prompt(運動層疊順序、青春紀錄片運鏡詞彙、AKB 風格動作詞彙、Seedance 2.0 Wrapper 完整語法+兩個完整示例-天台奔跑/舞臺表演、季節變體 prompt 補充、豎版 prompt 專項+固定負向組)**:全文見 `references/video-prompt.md`。運動層疊順序:攝影機運動(手持遊移/軟推進/跟拍)→主體動作(動作幅度+情緒節拍)→空間排程(人物位置/場景變化)→音效提示(如有同步對白/音效用 wrapper)。**固定負向提示(每條影片 prompt 末尾)**:no music(BGM 走獨立音軌)、no subtitles(字幕後期)、風格負向 no K-pop precision choreography/no high-fashion styling/no commercial stabilizer movement/no cyberpunk or dark concept/no EDM energy/no luxury architecture。

**BGM 生成 prompt(四段式寫法結構、BPM 描述速查、樂器組合推薦表、禁止樂器風格、完整示例 A/B/C、Suno/Mureka 差異表)**:全文見 `references/bgm-prompt.md`。四段式=[情緒定位]+[BPM/節拍感]+[主要樂器層]+[情緒弧線/段落結構];禁止樂器/風格詞:EDM drop / trap hi-hat / 808 bass / dubstep wobble / dark orchestral / heavy metal guitar。

## 合成(`composite_video`)

**剪輯氣質基準**:"青春碎片感"——像平成偶像 MV 的蒙太奇,而非商業廣告精剪。
- **節奏與時長**:日常/友情段落快切蒙太奇單 shot 1.5–3s;情緒/黃昏收尾段落放慢單 shot 4–8s 留白;舞臺表演跟隨 BGM 節拍剪下、動作高點對應切換點。
- **轉場偏好**:優先 soft dissolve(青春懷舊感)/handheld smash cut(自然切換)/freeze frame on smile(定格笑容);允許膠片時間碼閃切/VHS 輕故障轉場/DV 錄影感疊化;**禁止**精準商業特效轉場/K-pop 風格 RGB 描邊切換/賽博視覺故障特效。
- **音訊層混合**:BGM 主軌貫穿全片、黃昏收尾段漸弱淡出;環境音(蟬鳴/電車/歡笑)在日常/友情段疊於 BGM 之下、音量約 BGM 的 20–30%;有 narration VO 時 VO 期間 BGM 小幅壓低(duck 至約 -6dB)、VO 結束後恢復;帶內建音效的影片 shot(FirstFrameToVideo 生成)注意與 VO 軌不重疊。
- **畫面處理**:整體色調統一到"夏日青春膠片"色系(pastel 暖調、軟對比)避免色調跳變;允許保留輕微手持晃動/偶發失焦(青春紀錄片質感、不做穩定處理);片尾建議黃昏定格幀 soft fade to warm white 或 nostalgic film burn out。
- **Reels 豎版 BGM 擷取點與節拍對位規範(15s/30s)+ 豎版快切 BPM 節拍速查表 + 豎版剪輯專項(時間線 1080×1920/720×1280、禁 letterbox、字幕安全帶、節奏收緊 20–25%、禁橫滑轉場)**:全文見 `references/assembler-reels-vertical.md`。豎版音訊混合規則與橫版相同、無豎版特殊調整。

## 相關

邊界:演唱對口型 MV → singing-mv;插畫編舞 → dance-mv;史詩電影感 → epic-mv;日漫 OP/ED → anime-op-ed。路由入口:music-video-flow。
---
name: life-observed-doc
description: "先拍人不拍城，剋制不煽情"
---

# documentary-flow

做**人文紀錄短片**——全球國際統一審美、聚焦真實人類生活的觀察性影像——時用本 skill。核心是**觀察生活而非拍故事**：真實感與人文情緒 > 強戲劇衝突。用首幀設定圖作視覺錨點，再以微動態圖生影片生成剋制運鏡的紀錄片鏡頭。

> 本環境適配：GPT Image 2（首幀/元素圖）→ `generate_image_v3`（2K）；Happy Horse FirstFrameToVideo（首幀圖生影片）→ `generate_video_v3`（首幀驅動路徑，720p 起）；ElevenLabs 旁白 / Suno·Mureka 器樂 BGM → `generate_audio`；Final_Video_Spec.md 與結構化文字 → `write_file_v2`；故事板設計 → 分鏡階段內做；video_assembler → `composite_video`；`@資產`/asset 繫結 → `reference_nodes`+`{{NodeKey}}`；會員/積分類無。**敘事/運鏡/畫面質感/寫提示詞工藝全部內聯本 skill，不依賴外部工藝 skill，無源生跨 skill 依賴。**

## 一、流程（分階段暫停確認，不得一次性跑完）

1. **階段 0 · Final_Video_Spec**：`write_file_v2` 建 Final_Video_Spec.md，鎖：片名、題材地域、畫幅比例、目標時長、視覺風格、輸出語言（見二）。
2. **階段 1 · 參考素材解析**（若使用者上傳參考圖/影片）：提取訊號供下游用（見三）。
3. **階段 2 · 故事板**〔暫停〕：出關鍵元素、鏡頭列表、音訊層（見四、五、六）。故事板就緒後**掃描上下文**，查詢使用者已提供或此前生成、與故事板條目匹配的資產（元素圖/BGM 等）；對每個匹配項，在生成前先透過 `reference_nodes` 把資產**繫結到對應故事板槽位**，避免重複生成使用者已有內容。呈現確認。
4. **階段 3 · 設定元素**〔暫停〕：使用者已上傳元素資源（角色圖/參考角色）→ 直接綁為對應 key_element 的資產；否則為所有元素 `generate_image_v3` 生成圖（見七）。
5. **階段 4 · 首幀圖**〔暫停〕：為每個鏡頭 `generate_image_v3` 生成 start_frame，須與鏡頭描述景別/光線/主體姿態一致，作視覺錨點（見七、八）。
6. **階段 5 · 鏡頭影片**〔暫停〕：參考步驟 4 首幀圖，以 start_frame 作首幀輸入 `generate_video_v3` 生成微動態影片（見八、九）。
7. **階段 6 · 音訊層**〔暫停〕：`generate_audio` 生成旁白（如有）/ BGM（見六、七）。
8. **階段 7 · 組裝交付**：`composite_video` 完成全片時間線組裝（見十）。

**依賴順序**：階段 2→0；3→2；4→2；5→4；6→2；7→5,6。
**暫停節點**：在故事板完成、元素圖/首幀圖完成、影片完成、音訊生成後各暫停，等使用者確認再繼續。
**已有素材優先**（主要影響階段 3–5）：填充生成內容前，先繫結並分配到合適故事板位置，不重複生成使用者已提供的內容。

## 二、Final_Video_Spec 建立指南

1. **片名**：契合"人文紀錄片"調性，避免過度商業或浮誇的命名。
2. **題材地域**
   - **地域限定範圍**：引導使用者在以下區域中選擇——亞洲、非洲、中東、南美、東歐、東南亞、海島國家、發展中國家。
   - **題材核心限制**：題材必須聚焦"**真實的人**"與"**普通人的生活**"，**拒絕"城市宣傳片"**。
3. **畫幅比例**：推薦 16:9 橫屏，或紀錄片常見的 2.35:1 寬銀幕。
4. **視覺風格（四參考鎖定 + 避雷清單）**：鎖定為"像真實攝影師長期駐紮拍攝"、"像奧斯卡/國際電影節紀錄片"、"Netflix 紀錄片風格"或"國家地理式觀察影像"。**明確"不做"的風格（避雷清單）：嚴禁 AI 感、商業廣告感、強戲劇感、網紅風。**
5. **畫面質感要求**
   - **空氣感**：灰塵、水汽、潮溼、熱浪、風。
   - **光線限定**：僅限自然光（晨光、黃昏、陰天、窗邊光）。
   - **保留不完美**：允許並刻意保留輕微失焦、曝光波動、真實混亂感。

## 三、參考素材解析規則

若使用者上傳參考圖片或影片，提取以下訊號供下游使用，**輸出結構化描述，不做主觀評價**：
- 主體身份與外貌特徵；
- 場景地點與環境氛圍；
- 光線條件（方向 / 色溫 / 質感）；
- 畫面色調與飽和度風格。

## 四、敘事規範（storyboard 核心）

### 4.1 核心敘事理念：觀察生活，而非"拍故事"
- **去戲劇化**：摒棄強戲劇衝突、商業廣告式的劇情設計。重點不在"講一個起承轉合的故事"，而是呈現"真實世界的人類生活"。
- **偶發感**：場景和事件不應有"導演刻意安排"的痕跡，必須營造"攝影師長期駐紮時偶然觀察到"的自然狀態。
- **全球紀錄片統一審美**：如 Netflix 紀錄片或國家地理式觀察影像，打造全球觀眾都能理解共情的人文敘事，避免刻板的單一地域風（純網紅風、純歐美風）。

### 4.2 敘事主體與切入點：先拍"人"，不拍"城"
- **拒絕宣傳片邏輯**：永遠不要把"城市面貌"或"宏大景觀"作為首要表現物件——這不是城市宣傳片。
- **聚焦真實人類**：劇情永遠從"人"切入，透過普通人的真實生活狀態折射其背後的文化與環境。

### 4.3 劇情細節與動作設計（最易共情的描寫點）
撰寫劇本與場景描述時，著重刻畫以下細節動作，而非宏大事件：
- **聚焦手部勞作**：做飯、縫紉、洗衣、寫字、手工勞動。
- **人物背影與狀態**：多用"背影"作主視覺——比直接展現正臉更具高階感和故事留白感。
- **日常微小動作**：點菸、喝茶、發呆、看窗外——用這些無特定目的的"小動作"構建時間流動的真實感。

## 五、按地域劃分的場景/題材規劃庫

為不同發展中國家或地區規劃劇本時，直接選用以下最能體現當地原生人文氣息的場景和事件：
- **亞洲題材**：清晨的早餐攤、老茶館裡的閒談、熙熙攘攘的傳統市場、原生態的漁村、老舊的鐵路邊。
- **非洲題材**：黃昏塵土下的歸途、熱鬧的集市、奔跑的孩子、雨季的日常、傳統的手工勞動。
- **南美題材**：隨性的街頭音樂表演、充滿生活氣息的老城區、海邊日常、街頭/土路足球場、夜市的煙火氣。
- **中東題材**：陽光穿透的傳統市場、專注的手工藝製作過程、虔誠的祈禱時刻、沙塵環境下的生活常態。

## 六、關鍵元素與音訊層設計

### 6.1 關鍵元素設計
- 優先設計**人物元素**（年齡、外貌、著裝、正在做的事）和**場景元素**（地理環境、時段、光線條件、空氣質感）。
- 道具元素只在對多個鏡頭一致性有實質影響時才單獨建立。
- 使用者提供參考素材時，元素描述必須與參考內容一致，不得矛盾。

### 6.2 音訊層設計
- **BGM（可選）**：若使用，選擇極簡器樂或無調性環境音景；**禁止流行音樂節奏**。
- **不以對白驅動敘事。**

## 七、分鏡鏡頭設計原則（★ 觀察式紀實工藝核心）

- **時長**：每個鏡頭 **6–12 秒**，**不做短於 5 秒**的鏡頭。
- **觀察性敘事**：鏡頭不"設計故事"，而是"偶然看見生活"。優先拍手部勞動、背影、微小日常動作（點菸、喝茶、發呆、看窗外）；避免正面表演式構圖。
- **運鏡極簡（按優先順序排序）**：一個分鏡只描述一個鏡頭。
  1. 固定鏡頭（最推薦）
  2. 微弱手持（僅呼吸感 / 輕微漂移）
  3. 極慢推進 或 極慢橫移
  - **禁止**：旋轉、快速推拉、無人機飛行、炫技運鏡、切鏡。
- **每個鏡頭描述必須包含**：
  - **Scene**：引用場景元素 ID，說明時段與光線；
  - **主體動作**：人物正在做的微小動作，以肢體和神態為主，**無需臺詞**；
  - **攝影語言**：景別（特寫 / 中景 / 遠景）+ 運鏡型別 + 焦點策略。
- **畫面質感**：
  - **自然光優先**：晨光、黃昏、陰天散射光、窗邊側光；禁止人工補光感。
  - **空氣感必須體現**：灰塵、水汽、熱浪、潮溼、輕霧中選一種寫入鏡頭描述。
  - **允許不完美**：輕微失焦、曝光輕微波動、人物短暫停頓均為真實感加分項。
- **色調體系**：
  - 低飽和、高層次感：高光柔和不過曝，暗部有細節不死黑，膚色真實。
  - 參考色彩風格：**Kodak Vision3 / Fuji Eterna / ARRI Alexa Natural**。
- **影片中的聲音設計**：市集噪聲、風聲、雨聲、街道聲等。

## 八、首幀提示詞寫作規範（`generate_image_v3`）

**核心邏輯**：聚焦"決定性瞬間"的捕捉、膠片色彩質感、真實的光影與空氣感。**摒棄任何運鏡和節奏詞彙。**

**萬能公式**：
> [畫面主體與微小動作] + [環境與空氣感] + [光線狀態] + [攝影機語言與景別] + [色彩體系與膠片質感] + [核心精神關鍵詞與大師參考]

**核心模組與詞彙庫**：
- **主體與微動作**：人物背影 / 抽菸的雙手 / 凝視窗外 / 停頓的發呆瞬間。
- **環境與空氣感**：瀰漫的灰塵 (dusty air)、清晨的水汽 (morning mist)、潮溼感 (dampness)、風吹動衣角 (wind blowing)。
- **光線狀態**：自然光 (natural light)、窗邊柔和側光 (soft window light)、陰天漫反射 (overcast diffused light)。
- **攝影語言**：Medium shot (中景) / Close-up (特寫) / 極簡構圖 / 留白 (negative space)。
- **色彩體系（原樣直出）**：Kodak Vision3, Fuji Eterna, ARRI Alexa Natural, low saturation, soft highlights, detailed shadows, real skin tone.
- **風格與大師參考**：Magnum Photos, Leica Documentary, National Geographic, 是枝裕和 (Hirokazu Kore-eda), 賈樟柯 (Jia Zhangke).

**示例（方法級模板，替換主體/地域即可複用）**：
> (EN) A medium shot of an old man's weathered hands rolling a cigarette, sitting in a dimly lit traditional tea house. Morning mist and dust particles floating in the soft window light. Kodak Vision3 film stock, low saturation, soft highlights, real skin tone. Magnum Photos style, Leica Documentary, observational, honest, real, quiet, timeless. Hirokazu Kore-eda aesthetic.
> (ZH) 中景，一位老人在昏暗的老茶館裡捲菸的滄桑雙手。晨霧和灰塵顆粒在柔和的窗邊光線中漂浮。柯達 Vision3 膠片質感，低飽和度，高光柔和，真實的膚色。馬格南攝影風格，徠卡紀錄片，觀察性，誠實，真實，安靜，永恆。是枝裕和美學。

**首幀圖與視覺錨點**：首幀圖須與故事板鏡頭描述的景別、光線、主體姿態一致，作為影片生成的視覺錨點。若使用者已上傳參考圖（人物/場景），將其註冊為錨點（`reference_nodes`）並繫結至對應元素或鏡頭槽位，優先用於替代生成（ImageToImage 路徑）。

## 九、影片提示詞寫作規範（`generate_video_v3`，首幀驅動）

**核心邏輯**：聚焦"時間的流動"、"極慢的節奏與運鏡"、"環境的微小變化"以及"長鏡頭觀察感"。以對應鏡頭的 start_frame 作首幀輸入。

**萬能公式**：
> [極其剋制的鏡頭運動] + [主體持續的微小動作] + [環境與光線的微小流逝/變化] + [色彩體系] + [紀錄片節奏與電影級參考] + [核心精神關鍵詞]

**核心模組與詞彙庫**：
- **鏡頭運動（必須剋制）**：Fixed camera (固定鏡頭) / Slight handheld breathing (微弱手持呼吸感) / Extremely slow push-in (極慢推進) / Extremely slow pan (極慢橫移)。
- **動作與環境流逝**：持續的微小動作 (continuous subtle movement) / 光影隨時間緩緩移動 (light shifting slowly) / 持續的微風 (continuous gentle breeze)。
- **節奏與剪輯指令**：Long take (長鏡頭) / Slow pacing (慢節奏) / No fast cuts (禁止快剪) / Breathing space (呼吸感留白)。
- **色彩體系**：Sony Venice Documentary LUT, ARRI Alexa Natural, cinematic color grading, cinematic shadows.
- **影片風格與參考**：Netflix Documentary (Chef's Table, Our Planet), Oscar Documentary (Nomadland, Honeyland), 侯孝賢 (Hou Hsiao-hsien) pacing.

**示例（方法級模板）**：
> (EN) Fixed camera with slight handheld breathing. A slow long take of a South American woman washing clothes by the river. Her back is to the camera. The damp morning air slowly blows her hair. Natural overcast light with subtle environmental shifts. ARRI Alexa Natural, Sony Venice Documentary LUT, low saturation, soft highlights. Cinematic pacing, breathing space, no fast cuts. Nomadland and Honeyland style, Netflix documentary vibe, observational, slow, human, quiet, timeless.
> (ZH) 固定鏡頭帶有微弱的手持呼吸感。一個緩慢的長鏡頭：一位南美婦女在河邊洗衣服，背對鏡頭。潮溼的晨風緩緩吹動她的頭髮。自然的陰天光線，帶有微妙的環境變化。ARRI Alexa Natural，索尼威尼斯紀錄片 LUT，低飽和度，高光柔和。電影級節奏，呼吸感留白，無快剪。無依之地與蜂蜜之地風格，Netflix 紀錄片氛圍，觀察性，緩慢，人文，安靜，永恆。

## 十、素材生成與失敗處理

- **元素圖/首幀圖**：`generate_image_v3`，2K；首幀圖作視覺錨點（見八）。使用者已上傳參考圖 → 註冊 `reference_nodes` 繫結，優先替代生成。
- **鏡頭影片**：`generate_video_v3`，720p 起，以對應鏡頭的 start_frame 作首幀輸入（FirstFrameToVideo 意圖）。
- **音訊層**：旁白（如有）`generate_audio`；BGM `generate_audio`，風格描述為極簡器樂 / 環境音景，**不生成歌詞類音樂**。
- **失敗處理**：若影片生成失敗，**優先以同引數在同一路徑重試**，不擅自切換到風格差異大的替代路徑；重試仍失敗則**停止並告知使用者**，不靜默降級換模型。

## 十一、剪輯與輸出（`composite_video`）

**節奏原則**：
- **長鏡頭優先**，保留完整的時間流動感；**不為追求"有趣"而剪短鏡頭**。
- 鏡頭間可用 **0.5–1s 的黑場或聲音延續過渡**，製造呼吸感。
- **禁止快剪、音樂卡點、特效轉場、TikTok 節奏。**

**音畫關係**：
- BGM（如有）音量**低於影片層聲音**；淡入淡出，不搶畫面。
- **不做強制音畫同步**；畫面與聲音各自自然流動。

## 相關

- **邊界（勿用本 skill，改道）**：強戲劇敘事/起承轉合短片 → cinematic-flow；城市記憶/舊街區具體人物空間（80/20 平敘+高動態配比）→ city-memory-film；東亞文藝片（情緒驅動/全片平敘微動態/聲畫分離）→ east-asian-mood-film；傳統工藝紀錄（文獻解析→六格分鏡矩陣圖→逐組 15s）→ craft-documentary；名導紀實風格（賈樟柯式）→ auteur-style-director 路由。
- 本 skill 自足內聯，**無源生跨 skill 依賴，不設配合表**。
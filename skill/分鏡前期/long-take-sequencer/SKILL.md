---
name: long-take-sequencer
description: "Use when planning or generating an AI video that should feel like one continuous long take, especially when character identity, props, movement, spatial relations, or camera direction must persist across a long timeline or generation boundaries."
---

# 連續長鏡頭導演

把長影片規劃成一條統一時間軸，使用少量關鍵幀、連續運動路徑和狀態傳遞，優先透過原生長影片生成或對同一影片持續續寫，形成同一個連續世界中的完整長鏡頭。

最終目標是讓普通觀眾相信人物、空間、道具和事件一直存在於同一個連續世界。技術上是否由一次生成完成，不作為成功標準。

## 適用範圍

在使用者要求連續長鏡頭、統一長影片、角色或道具跨時間軸一致、動作接續或影片續寫時使用本 Skill。

V0 只負責連續性規劃、統一時間軸生成、必要的影片續寫、狀態更新和錯誤判斷。不要自行增加配音、自動剪輯、資產管理、釋出或其他產品能力。

## INPUT INTERPRETATION

使用者不需要提供標準影片 Prompt。預設假設使用者提供的是自然語言描述、故事梗概、小說片段、劇情創意、簡單需求、劇本或已有影片 Prompt。

首先判斷輸入類型。如果輸入是已經結構化的影片 Prompt，保留其中明確設定並進入狀態提取。如果輸入屬於 RAW STORY / IDEA，不要要求使用者重新寫成影片 Prompt，先提取以下內容。

### NARRATIVE FACTS

記錄使用者明確規定、不能擅自改變的劇情事實。

### CHARACTERS

識別所有重要人物及其在故事中的身份。

### EVENT CHAIN

按因果順序整理故事實際發生的事件。

### LOCATIONS

識別涉及的空間、空間之間的關係以及人物如何移動。

### KEY PROPS

識別會影響後續劇情或連續性的物體。

### STATE CHANGES

識別人物、道具和環境在故事中發生的狀態變化。

### VISUAL MOMENTS

識別必須透過畫面表現的內容。

### NON-VISUAL CONTENT

識別心理活動、背景說明和抽象描述等不能直接拍攝的內容，並把它們轉換成可見、可表演的動作或環境反應。

例如，“她開始感到不安”不能直接作為影片動作。可以轉換為以下可見表現。

- 她盯著不斷下降的樓層數字。
- 呼吸逐漸急促。
- 手指反覆按開門按鈕。
- 身體向電梯角落退去。

轉換時允許補充視覺動作，禁止改變原故事的核心事實、人物關係、事件順序和因果關係。

## DIRECTORIAL AUTOFILL

對於使用者沒有規定、但影片生成必須確定的資訊，由 Skill 自主補齊。

- 人物具體視覺形象
- 服裝
- 基礎場景設計
- 光線
- 攝影機位置
- 景別
- 運鏡
- Clip 長度
- 環境細節

所有補充優先服務使用者指定的題材、情緒和故事。不要為了增強電影感而增加重要人物、改變結局、增加重大劇情事件或改變故事因果。

導演補全的內容應明確標記為 Skill 補充。使用者可以在規劃確認階段修改這些內容。

## USER INTENT PRIORITY

發生衝突時，按照以下順序決定採用哪項資訊，越靠前優先順序越高。

1. 使用者明確要求
2. 使用者上傳的參考素材
3. 原始故事中的事實
4. Skill 的導演判斷
5. 預設視覺方案

低優先順序內容不得覆蓋高優先順序內容。導演補全只處理尚未被高優先順序資訊確定的空白。

## MULTI-SHOT REPRESENTATION

在建立 Master State 前，先把輸入整理成全域資訊和逐鏡頭資訊。兩者職責不同，不要把全部角色外觀和歷史劇情重複寫進每個鏡頭。

### GLOBAL STORY CAPTION

用一個簡潔段落描述整段影片長期穩定的資訊。

- 主要主體及穩定外觀
- 故事涉及的總體環境
- 長期視覺風格
- 使用者明確鎖定的敘事事實

GLOBAL STORY CAPTION 不描述某個 Clip 的臨時動作、表情或機位。它是全片共同基線，不是劇情摘要的重複副本。

### SUBJECT REGISTRY

為重要人物、動物、車輛和會獨立行動的核心物體分配穩定 Subject ID。

```text
SUBJECT REGISTRY
- Subject 1 / 唯一名稱 / 穩定身份描述 / 參考素材
- Subject 2 / 唯一名稱 / 穩定身份描述 / 參考素材
```

- 同一主體跨鏡頭始終使用同一 Subject ID。
- 一個 Subject ID 只表示一個實體。
- 不因角度、服裝損傷、情緒或動作變化建立新 ID。
- 普通背景物件不進入 SUBJECT REGISTRY。影響劇情且需要唯一狀態的物體同時進入 PROP DEFINITIONS。
- 逐鏡頭規劃不能建立未在故事或導演補全階段建立的新主體。

### VISIBLE SUBJECT SET

每個 Shot 或 Clip 明確列出當前畫面實際出現的 Subject ID 和核心 Prop ID。

- 逐鏡頭描述只引用當前可見的主體。
- 不把未出鏡角色的完整描述塞入當前生成提示。
- 遠處、模糊且不影響當前事件的主體可以不列入。
- 下一規劃單元會直接使用的主體或道具，應根據 HANDOFF 需要在當前 END STATE 中進入畫面。

### CURRENT SHOT CAPTION

每個鏡頭使用一個局部描述，內容只覆蓋當前可見主體、動作、表情、場景狀態、構圖和攝影機運動。

```text
CURRENT SHOT CAPTION
- VISIBLE SUBJECT SET
- 當前動作與表情
- 當前場景和狀態變化
- 攝影機位置、景別和運動
- 與前後鏡頭有關的方向和交接資訊
```

CURRENT SHOT CAPTION 使用 Subject ID 引用全域身份，不重新改寫主體外觀。角色外觀只有發生劇情允許的可見變化時才更新 Continuity Ledger。

### VARIABLE SHOT DURATION

根據當前事件負載、動作複雜度和模型能力分配鏡頭時長。不同 Clip 可以使用不同長度。

- 簡單反應、視線或建立鏡頭可以較短。
- 穿越空間、道具交接和完整動作需要足夠時間展示因果過程。
- 一個 Clip 無法穩定完成全部動作時，拆成多個連續階段。
- 總時長由使用者要求控制。不要為了平均分配而強迫所有 Clip 等長。

以上結構借鑑多鏡頭生成研究中的全域描述與逐鏡頭描述分工。它只能改善 Skill 層的資訊組織，不能替代底層模型的聯合多鏡頭生成、參考注入或跨鏡頭位置編碼能力。

## UNIFIED VIDEO TIMELINE

把整部影片視為一個持續發展的時間軸。Shot 或 Clip 是規劃動作、狀態和風險的內部單元，預設不等於要分別生成並在最後拼接的獨立影片檔案。

```text
UNIFIED VIDEO TIMELINE
- Total Duration
- Continuous Spatial Route
- Event and Action Timeline
- Camera Trajectory
- Temporal and Environment Progression
- Narrative Keyframes
- Generation Mode
```

- `Continuous Spatial Route` 說明人物和攝影機如何在已建立的三維空間中連續移動。
- `Event and Action Timeline` 按時間安排事件、動作階段和因果，不把動作重置在規劃單元邊界。
- `Camera Trajectory` 是全片連續路徑。機位變化必須在畫面中發生。
- `Temporal and Environment Progression` 繼承已鎖定的時間、光線、天氣和環境狀態。
- 先完成全片時間軸，再決定底層模型如何生成。不能因為模型單次時長較短，就先把故事設計成互相獨立的鏡頭。

### NARRATIVE KEYFRAME PLAN

關鍵幀是統一時間軸上必須到達的敘事和空間狀態，不是預設要分別生成的靜態首幀。

```text
NARRATIVE KEYFRAME [ID]
- Timeline Position / 時間點或時間範圍
- Narrative Purpose / 當前必須成立的劇情事實
- Character and Prop State
- Spatial Position and Screen Direction
- Camera Position and Trajectory
- Environment and Time Condition
- Incoming Motion
- Outgoing Motion
- Transition Path from Previous Keyframe
```

- 只為身份建立、空間轉折、關鍵動作結果、道具狀態變化或劇情拐點設定關鍵幀。
- 相鄰關鍵幀必須能由一個連續可見的 `Transition Path` 連線，說明人物、攝影機和環境如何從前一狀態到達後一狀態。
- 不按固定秒數機械增加關鍵幀。過密關鍵幀會壓縮自然動作並誘發擺拍、瞬移或畫面變形。
- 相鄰關鍵幀的姿勢、位置和機位差異超過當前模型能夠自然完成的範圍時，調整動作路徑或增加必要的中間里程碑。
- 若模型支援多個關鍵幀輸入，才把規劃關鍵幀繫結到對應控制槽位；否則關鍵幀只用於時間軸和提示詞規劃，不能虛構平臺不存在的控制能力。

## VISUAL ASSET BIBLE

在寫影片生成提示前，先規劃整部作品需要的視覺參考資產。參考資產用於鎖定角色身份、服裝版本、場景空間、核心道具和視覺風格。

只規劃故事和鏡頭實際需要的參考。不要為短暫出現的角色或從未被攝影機看到的角度機械生成完整資產集。

### MEDIA ROLE CONTRACT

每個參考資產必須只有一個明確的媒體角色。生成節點和素材輸入槽位必須按角色繫結，不得因為畫面看起來相似而互相替代。

| Media Role | 用途 | 禁止用途 |
|------------|------|----------|
| `style_reference` | 色彩、光線、材質、寫實程度 | 首幀、場景、人物或道具參考 |
| `character_reference` | 角色身份、臉部、體型和服裝版本 | 場景或首幀替代 |
| `location_reference` | 建築、空間佈局、場景角度和環境狀態 | 風格錨點或連續邊界替代 |
| `prop_reference` | 核心道具外觀和狀態版本 | 人物、場景或首幀替代 |
| `transition_reference` | 兩個場景之間的出入口和空間連線 | 普通風格參考 |

- 素材名稱、說明和 REFERENCE MANIFEST 都必須寫出 Media Role。
- `style_reference` 只能進入風格參考槽位。
- `location_reference` 只能進入場景或環境參考槽位。
- 當前模型沒有對應槽位時，不得把素材塞進含義不同的槽位。應採用明確降級方案或停止生成。

### CHARACTER REFERENCE PACK

為每個會跨多個鏡頭出現的重要角色建立參考包。

```text
CHARACTER REFERENCE PACK
- Subject ID
- Primary Identity / 全身正面、中性姿勢、乾淨背景
- Face 3/4 / 頭肩三分之四角度
- Story-required Side or Back Views
- Wardrobe Variants / 每套劇情服裝獨立版本
- Expression Set / 僅故事實際需要的關鍵表情
- Action Poses / 僅身份容易在動作中漂移時使用
- Source / 使用者上傳或 Skill 生成
```

- Primary Identity 是該角色的身份主參考。
- Face 3/4、側面、背面、服裝和動作版本都應從 Primary Identity 派生，不能相互獨立生成。
- 所有派生圖保持同一臉部、髮型、體型和身份標記。
- 服裝版本使用穩定版本 ID。衣物淋溼、汙損、破裂和血跡作為連續狀態版本，不建立新角色。
- 主要角色通常需要 Primary Identity 和 Face 3/4。只有鏡頭實際會看到時才增加側面或背面。
- 功能性配角可只使用一張主參考。背景群眾不要求獨立身份包。
- 使用者上傳的角色參考優先於 Skill 生成的參考。

### LOCATION REFERENCE MATRIX

為重複出現、發生空間移動或會改變狀態的重要地點建立參考矩陣。

```text
LOCATION REFERENCE MATRIX
- Location ID
- Location Condition ID
- Primary Establishing View
- Story-required Angles
- Entry and Exit Views
- Lighting / Weather Variants
- Narrative State Variants
- Non-negotiable Spatial Anchors
- Temporal Environment Lock
- Environment Element Inventory
- Source / 使用者上傳或 Skill 生成
```

- Primary Establishing View 鎖定建築、材質、尺度和主要佈局。
- 其他角度從主參考派生，並保持門窗、傢俱、走廊和出入口關係。
- 只建立鏡頭計劃真正訪問的角度、光線、天氣和劇情狀態組合。
- 損壞、火災、積水、物件移動等變化建立狀態版本，並明確哪些變化不可逆。
- Environment Map 記錄空間拓撲，LOCATION REFERENCE MATRIX 負責提供對應的視覺依據。

LOCATION CONDITION ID

每組場景參考使用唯一條件版本，包含 Location ID、故事時間、晝夜、天氣、季節、劇情狀態和版本號。例如 `FOREST_SUNSET_CLEAR_INTACT_V1` 表示同一片夕陽、晴朗、尚未受損的樹林。

所有屬於同一 LOCATION CONDITION ID 的全景、入口、出口和路線檢視必須繼承相同條件。只有劇情明確發生時間、天氣、季節或環境狀態變化時，才能建立新版本。不得為了生成新角度而靜默建立夜景、不同季節或另一套環境。

TEMPORAL ENVIRONMENT LOCK

同一 LOCATION CONDITION ID 鎖定以下資訊。

```text
TEMPORAL ENVIRONMENT LOCK
- Story Time
- Time of Day
- Sun Position
- Sky State
- Shadow Direction and Length
- Colour Temperature
- Exposure Level
- Weather and Atmosphere
- Season
```

- “夕陽”要求所有派生參考保持相近太陽高度、天空顏色、陰影方向和暖色溫。
- 攝影機換角度可以改變太陽在畫面中的位置，不能把夕陽改成正午、藍調時刻或夜景。
- 未經劇情授權的晝夜、天氣和季節變化屬於阻斷錯誤。
- 劇情確實跨越時間時，為每個時間狀態建立命名版本，並說明變化發生在哪個 Clip。

ENVIRONMENT ELEMENT INVENTORY

記錄觀眾會在不同視角中辨認的自然元素、固定物件和可移動佈景。

```text
ENVIRONMENT ELEMENT INVENTORY
- Vegetation State / 植物種類、密度、顏色、季節和健康狀態
- Terrain State / 地面材質、坡度、積水、泥土、落葉和雪
- Fixed Natural Anchors / 主要樹木、岩石、河流和山體
- Fixed Built Anchors / 門、路牌、圍欄、建築和固定傢俱
- Movable Dressing State / 箱子、椅子、工具、散落物和其他可移動物件
- Damage and Depletion State / 燃燒、破損、消耗和清理狀態
```

- 同一場景不同角度保持植物種類、季節、整體密度和顏色一致。
- 顯眼樹木、岩石、路牌、門和其他空間標誌保持位置關係。
- 風可以讓枝葉運動，不能無理由改變樹種、樹木數量或季節顏色。
- 可移動物件只有在畫面中被移動後才能改變位置。
- 物件、植被或環境發生劇情變化時，更新 Environment State，並建立對應狀態版本。

LOCATION MASTER

同一場景先建立一張無人全景或廣角主參考，鎖定建築、地形、門窗、固定傢俱、材質、尺度和主要空間比例。

- LOCATION MASTER 必須是空場景，不得出現可識別人物。
- 不得出現只屬於某個 Clip 的臨時動作、手持道具或臨時特效。
- 固定建築和永久佈景可以出現。
- 同一場景的其他視角與狀態必須從 LOCATION MASTER 派生，不能分別獨立重新設計。
- LOCATION MASTER 必須繫結一個 LOCATION CONDITION ID。所有派生檢視繼承其 TEMPORAL ENVIRONMENT LOCK 和 ENVIRONMENT ELEMENT INVENTORY。

LOCATION VIEW SET

從 LOCATION MASTER 派生鏡頭實際需要的角度。

- 全景建立檢視
- 角色入口檢視
- 角色出口檢視
- 正向路線檢視
- 反向路線檢視
- 劇情需要的細節檢視

派生檢視必須保持相同門窗位置、路徑方向、建築結構、固定傢俱和尺度關係。不同檢視可以改變攝影機位置，不能改變場景結構。

派生檢視還必須保持同一時間、天氣、季節、植被和物件狀態。換角度不能觸發環境重新設計。

LOCATION GRAPH

把所有場景視為具有方向的空間節點和連線邊。

```text
LOCATION GRAPH
- Location A
- Connection / 門、走廊、樓梯、道路、邊緣或其他通道
- Location B
- Travel Direction
- Exit View in A
- Entry View in B
- Persistent Weather / Light / Time State
```

- 同一場景內移動使用 LOCATION MASTER 和 LOCATION VIEW SET 保持結構一致。
- 不同場景之間必須說明人物透過什麼連線、沿哪個方向離開和進入。
- 門的 A 面與 B 面、樓梯底部與頂部、走廊兩端等連線必須能在三維空間中互相解釋。
- 場景切換不能憑空改變時間、天氣、光線方向或人物運動趨勢。

TRANSITION ANCHOR

跨場景移動時，為連線邊建立成對參考。

```text
TRANSITION ANCHOR
- From Location / Exit View
- Connection Object or Route
- To Location / Entry View
- Character Travel Direction
- Camera Direction
- Shared Light / Weather / Time State
```

出口和入口參考必須共享同一連線物、方向和環境狀態。TRANSITION ANCHOR 只負責證明空間連線，不能替代角色、場景或風格參考。

### PROP REFERENCE PACK

為核心道具和觀眾會反覆辨認的視覺元素建立參考包。

```text
PROP REFERENCE PACK
- Prop ID
- Primary View / 三分之四角度、乾淨背景
- Detail View / 鏡頭會特寫的結構
- In-context View / 需要確認環境內比例時使用
- State Variants / 完整、損壞、開啟、耗盡等
- Source / 使用者上傳或 Skill 生成
```

- 故事關鍵且跨鏡頭出現的道具需要主參考。
- 派生檢視和狀態版本從主參考生成。
- 道具參考鎖定外觀，Prop State 繼續負責持有者、左右手、位置和當前狀態。
- 反覆出現且觀眾會注意其變化的傢俱、裝置、標誌或佈景，也可以建立唯一參考 ID。

### STYLE ANCHOR

使用一至兩張能夠代表全片色彩、光線、材質和寫實程度的參考圖作為 STYLE ANCHOR。

- STYLE ANCHOR 不得出現人物、角色服裝、劇情道具、文字或可識別的具體故事地點。
- STYLE ANCHOR 應使用中性的材質、色板、光線或非劇情環境表達視覺風格。
- STYLE ANCHOR 應在角色、場景和道具派生圖之前確定。
- 後續參考和鏡頭畫面使用同一風格依據。
- 劇情需要另一種明確視覺狀態時，建立有名稱的風格版本，不能在鏡頭之間靜默漂移。
- STYLE ANCHOR 只能標記為 `style_reference`，不得放入首幀或場景槽位。

### REFERENCE MANIFEST

每個時間軸規劃單元都要列出實際需要的參考資產及其職責。

```text
REFERENCE MANIFEST FOR PLANNING UNIT [N]
- `character_reference` / 對應 Subject ID 與服裝版本
- `location_reference` / 對應 LOCATION MASTER、角度、光線、天氣和劇情狀態
- `location_condition_id` / 當前時間、天氣、季節和環境狀態版本
- `prop_reference` / 當前可見的核心 Prop ID
- `style_reference` / 只進入風格槽位
- `transition_reference` / 跨場景邊界使用
- Missing critical references
```

- 只附加當前生成範圍真正需要的參考。
- 使用者提供的參考素材按 USER INTENT PRIORITY 處理。
- 參考數量超過當前模型可用上限時，按當前主體、核心道具、當前場景和風格的順序保留，並向使用者說明被省略的約束。

### REFERENCE PREFLIGHT

生成完整影片、初始影片或執行續寫前檢查當前範圍的 REFERENCE MANIFEST。

1. 當前角色是否使用正確 Subject ID、身份主參考和服裝版本。
2. 場景參考是否匹配當前角度、光線、天氣和劇情狀態。
   - 當前場景是否使用正確 LOCATION CONDITION ID。
   - 時間、太陽、天空、陰影、色溫和曝光是否與 TEMPORAL ENVIRONMENT LOCK 一致。
   - 植物、地形、固定物件和可移動佈景是否與 ENVIRONMENT ELEMENT INVENTORY 一致。
3. 當前可見核心道具是否使用正確 Prop ID 和狀態版本。
4. STYLE ANCHOR 是否一致。
5. 當前模型是否能接收所需參考類型和數量。
6. 每張素材是否進入與 Media Role 相同的槽位。

缺少會導致角色身份、空間或核心道具不可控的參考時，停止當前生成範圍。先補齊參考、調整鏡頭方案或向使用者說明能力限制，不能靜默放棄關鍵約束。

參考圖生成後，先比較角色身份、服裝、場景佈局、道具外觀和風格。明顯不一致的參考不能進入影片生成。

## 開始前收集資訊

從使用者輸入和當前可用素材中確認以下資訊。已經明確的內容不要重複追問。

- 創意與劇情目標
- 總時長和期望節奏
- 畫幅、風格和類型
- 主要角色及角色參考
- 核心道具
- 關鍵空間及其連線關係
- 當前可用的影片模型能力
- 是否支援角色參考、目標時長、多關鍵幀控制和影片續寫

缺少一般細節時，採用最保守且容易保持連續的設定繼續規劃。缺少會改變角色身份、核心道具或空間關係的資訊時，先向使用者確認。

## GENERATION MODE SELECTION

先核實當前 LibTV 工作流和所選模型實際提供的時長、關鍵幀輸入與影片續寫能力，不根據模型名稱或宣傳文案猜測節點能力。

按以下優先順序選擇執行模式。

### MODE A / NATIVE LONG VIDEO

當模型單次生成能夠覆蓋目標時長，並能接受統一時間軸所需的控制資訊時，優先一次生成完整長影片。

- 輸入完整 `UNIFIED VIDEO TIMELINE`、Master State、必要參考和適量關鍵幀約束。
- Shot 或規劃單元只用於規劃和檢查，不建立獨立影片節點。
- 生成後按關鍵幀位置和全片連續性檢查真實結果。

### MODE B / VIDEO CONTINUATION MODE

當單次生成時長不足但支援影片續寫時，持續擴展同一個影片資產，不分別生成多個成品再合成。

```text
CONTINUATION SEGMENT
- Source Video Asset ID
- Existing Timeline End
- Current Continuity Ledger
- Next Narrative Keyframe
- Transition Path
- Motion Handoff
- Extended Video Asset ID
```

- 每次續寫必須以上一次已接受的影片資產為源，不能新建無關影片後再拼接。
- 續寫只讀取固定 Master State、當前實際狀態、下一關鍵幀和到達它所需的連續路徑，不重複全部歷史提示詞。
- 續寫後檢查原影片邊界附近是否發生凍結、跳切、重繪、動作重啟、音畫斷裂或場景狀態漂移。
- 只有續寫結果透過檢查，才把擴展後的影片資產作為下一次續寫來源。

MODE A 和 MODE B 都不可用時停止執行並報告能力限制。不得建立多個獨立影片、不得退回尾幀圖片接力，也不得提出片段拼接方案。

## 固定工作流

嚴格按以下順序推進。

 1. 從使用者創意建立 Master State、Visual Asset Bible 和初始 Continuity Ledger。
 2. 建立 `UNIFIED VIDEO TIMELINE`、連續空間路線、攝影機軌跡和 `NARRATIVE KEYFRAME PLAN`。
 3. 檢查當前模型能力，只在 MODE A 和 MODE B 中選擇生成模式。
 4. 把時間軸拆成內部規劃單元，為每個單元定義 START STATE、ACTION、目標 END STATE、HANDOFF、MOTION HANDOFF、SCENE REALISM LAYER 和 REFERENCE MANIFEST。
 5. 在當前生成範圍開始前執行 Current-range Failure Analysis。
 6. 展示完整規劃、模式選擇及其能力依據，然後停止並等待使用者明確確認。
 7. 獲得確認後，準備當前生成範圍所需參考並完成 REFERENCE PREFLIGHT。
 8. MODE A 生成完整長影片；MODE B 生成初始影片或只執行下一次續寫。
 9. 檢查實際結果，並用真實畫面更新 Continuity Ledger 和時間軸完成狀態。
10. MODE B 只在續寫結果透過後繼續擴展同一影片資產。
11. 發現阻斷錯誤時停止後續生成，重做當前失敗範圍，不用修改後續文字掩蓋錯誤。
12. 當前生成範圍透過後展示檢查結果，並按確認規則決定是否繼續。
13. 完成目標時長後複核整條時間軸並輸出統一長影片資產。

規劃狀態不能覆蓋實際影片。只把已經生成、檢查並接受的結果寫入最新 Continuity Ledger。

## 兩道確認門檻

### 規劃確認門檻

完成 Master State、Visual Asset Bible、初始 Continuity Ledger、統一時間軸、關鍵幀計劃、模式選擇、全部規劃單元、REFERENCE MANIFEST 和首次生成範圍的 Failure Analysis 後，立即停止輸出並等待使用者確認。

使用者明確回覆“確認規劃並開始生成”或表達同等明確意圖之前，必須遵守以下限制。

- 不得建立影片節點
- 不得生成參考圖
- 不得呼叫影片生成能力
- 不得進入批次生成階段
- 不得消耗影片生成積分
- 不得把使用者最初提交創意的行為視為生成授權

使用者要求“先規劃”“看看分鏡”“檢查方案”時，只能停留在規劃階段。

### 逐次續寫確認門檻

獲得規劃確認後，MODE A 只執行一次完整長影片生成；MODE B 一次只執行初始生成或一次影片續寫。每次完成後先輸出實際 END STATE、連續性檢查、更新後的 Continuity Ledger 和當前影片資產狀態，然後停止並等待使用者確認繼續。

使用者明確要求自動續寫到目標時長時，可以免除逐次續寫確認，但規劃確認門檻仍然有效。自動模式中任何阻斷錯誤都會立即終止後續生成。

## Master State

Master State 儲存跨片段長期固定的資訊。不要把當前姿勢、臨時表情或正在發生的動作寫進角色鎖定。

使用下面的結構。

```text
MASTER STATE

CHARACTER LOCK
- ID / 名稱
- 穩定外貌與體型
- 臉部、髮型和膚色
- 固定服裝、配飾和識別標記
- 角色參考

PROP DEFINITIONS
- 道具 ID / 名稱
- 穩定外觀、材質、尺寸和功能
- 初始擁有者與位置
- 是否為核心道具

ENVIRONMENT MAP
- 場景區域
- 區域之間的連線關係
- 門、走廊、樓梯和關鍵傢俱位置
- 穩定光源與空間標誌

STYLE LOCK
- 影像類型與視覺風格
- 色彩、光線與質感
- 畫幅
- 基本攝影機風格
```

### Subject Lock / Character Lock 規則

- 鎖定可見的身份特徵、服裝和配飾。
- 穩定描述保持同一語義，不要在不同 Clip 中隨意改寫。
- 身份描述和動作分離。走路、奔跑、揮刀、哭泣、緊張等進入當前狀態或 ACTION。
- 角色在畫面中發生永久變化時，保留原始身份，並把傷勢、汙漬、衣物損傷等變化寫入 Continuity Ledger。
- 有角色參考能力時，相關 Clip 持續使用同一角色參考。

### Prop Lock 規則

- 每件核心道具只對應一個 ID 和一個當前狀態。
- 持有者、左右手、位置、朝向、可見性和損壞狀態必須明確。
- 道具狀態只有在畫面中發生交接、放置、損壞、消耗或離場後才能改變。
- 不允許核心道具靜默複製、替換、換手、瞬移或消失。

### Spatial Continuity / Environment Map 規則

- 只記錄會影響後續動作和鏡頭的空間事實。
- 明確門通向哪裡、走廊方向、房間相鄰關係和關鍵物件位置。
- 人物移動必須符合已建立的連線關係。
- 場景有意變化時，變化應在畫面中發生並進入 Environment State。

## Continuity Ledger

Continuity Ledger 儲存當前世界狀態。每接受一個 Clip 後更新一次。

```text
CONTINUITY LEDGER AFTER GENERATION RANGE [N]

CHARACTER STATE
- 角色所在區域與畫面位置
- 姿勢、朝向、視線和螢幕方向
- 正在進行的動作與完成程度
- 表情、受傷、汙漬和衣物損傷

PROP STATE
- 道具當前擁有者
- 道具所在位置或左右手
- 可見、遮擋、放置或離場狀態
- 完整、損壞、啟用或消耗狀態

ENVIRONMENT STATE
- 當前區域
- 門窗與可移動物件狀態
- 應持續存在的環境變化
- Directed Anomaly

CAMERA STATE
- 攝影機位置、高度和朝向
- 景別與主要構圖
- 運動方向與運動進度
- 動作軸線一側、視線關係和螢幕方向

MOTION STATE
- Motion Vector / 人物與關鍵道具的螢幕運動方向和速度趨勢
- Action Phase / 動作正處於準備、發力、騰空、接觸、落地或恢復的哪個階段
- Body Momentum / 身體重心、支撐腳與正在擺動的肢體
- Camera Motion / 攝影機正在平移、後退、推進、環繞或升降，以及是否仍在運動
- Environmental Motion / 衣物、頭髮、雨、煙、火焰和枝葉等可見動態的方向與趨勢

TIME STATE
- 故事內時刻
- 已經過的時間
- 持續動作、倒計時和因果事件進度
```

狀態帳本只寫當前真實狀態。不要把以前所有劇情重新敘述一遍。

## 劃分時間軸規劃單元

- 依據事件和動作階段劃分內部規劃單元，不把這些單元分別生成成影片。
- 使用 VARIABLE SHOT DURATION，讓規劃範圍服從事件負載，不要求所有單元等長。
- 每個規劃單元只承載一個主要動作或一個清晰動作階段。
- 動作過多時拆成準備、執行和結果等連續階段。
- 拆分點應落在容易交接的狀態上。優先選擇主體可見、動作方向明確、核心道具位置清楚的畫面。
- 下一規劃單元會用到的人物、肢體、道具或環境元素，應在當前 END STATE 中可見。
- 人物和道具在時間軸中可以自然遮擋或暫時離開畫面，不能為了狀態繼承擺出僵硬姿勢。

## 每個時間軸規劃單元的合同

規劃每個時間軸單元時使用以下結構；實際生成仍然只執行完整長影片或同一影片續寫。

```text
PLANNING UNIT [N] / [TOTAL]

VISIBLE SUBJECT SET
- 當前畫面可見的 Subject ID
- 當前畫面可見的核心 Prop ID

REFERENCE MANIFEST
- 按 Media Role 列出當前角色、服裝、場景、道具、風格和連線參考
- 缺失的連續性關鍵參考

START STATE
- 人物在哪裡
- 當前姿勢、朝向、視線和運動方向
- 當前速度趨勢、身體重心和動作階段
- 核心道具在哪裡，由誰持有，位於哪隻手
- 攝影機位置、朝向、景別和運動狀態
- 衣物、頭髮、雨、煙、火焰等可見環境動態
- 當前環境與時間狀態

ACTION
- 當前規劃單元唯一主要動作
- 動作的自然過程
- 本段允許發生的狀態變化

TARGET END STATE
- 人物最終位置、姿勢和朝向
- 核心道具最終狀態
- 動作完成程度
- 攝影機最終位置和方向
- 環境與時間變化
- 下一段需要可見的元素

HANDOFF
- 下一規劃單元必須繼承的狀態
- 必須繼續的未完成動作
- 人物、道具、攝影機和環境動態必須繼承的運動方向、速度趨勢與動作階段
- 不得改變的身份、道具、空間和方向
- 下一關鍵幀或規劃單元必須包含的可見資訊

CURRENT RANGE FAILURE ANALYSIS
- 當前動作最可能導致的連續性錯誤
- 針對這些錯誤的具體生成約束

CURRENT SHOT CAPTION
- 當前可見主體、動作、場景和攝影機的局部描述

SCENE REALISM LAYER
- 當前空間的物理環境與尺度
- 材質、重量、接觸和受力反饋
- 人物自然行為與即時反應
- 前景、中景、背景的深度與細微活動
- 光線如何作用於人物、物體和運動
- 當前鏡頭的導演意圖與視覺注意力

GENERATION PROMPT
- 當前模型可直接使用的本段提示詞
```

後續規劃單元的 START STATE 必須來自上一單元的 END STATE。影片續寫時，實際 START STATE 以當前已接受影片的真實結尾為準。HANDOFF 只傳遞下一範圍真正需要的資訊，不重複整段歷史。

## SCENE REALISM LAYER

連續性約束鎖定身份和世界狀態，不把人物、攝影機或環境凍結成僵硬擺拍。在寫最終生成提示詞前，為當前生成範圍補充以下可觀察資訊。

```text
SCENE REALISM LAYER

PHYSICAL ENVIRONMENT
- 空間尺度、地面與空氣狀態
- 當前天氣、光源和可見環境運動
- 與動作真正發生接觸的物體

MATERIAL RESPONSE
- 腳步、碰撞、重量、震動和表面反饋
- 衣物、頭髮、煙、火焰、雨水或塵土如何響應運動

HUMAN BEHAVIOUR
- 呼吸、視線、重心轉移和自然的小幅動作修正
- 人物對地形、阻力、聲音和事件的即時反應

DEPTH AND ACTIVITY
- 前景、中景和背景各自承擔的視覺資訊
- 不搶奪主要動作的細微環境活動

LIGHT INTERACTION
- 光線、陰影、反射和遮擋如何隨人物與攝影機運動變化

DIRECTORIAL INTENT
- 當前畫面希望觀眾感受到什麼
- 攝影機為何這樣移動，視覺注意力落在哪裡
```

- 只補充既定故事和場景能夠容納的細節，不能增加重要人物、重大事件、改變結局或改寫因果。
- 使用具體可見的動作、材質和環境反饋，避免只堆疊“電影級、史詩感、真實感”等抽象形容詞。
- 允許自然步態、呼吸、衣物擺動、重心調整和微小的不完全同步。不要要求人物以完美勻速移動或在狀態點擺出靜止姿勢。
- 環境細節必須服從 LOCATION CONDITION ID、TEMPORAL ENVIRONMENT LOCK 和 ENVIRONMENT ELEMENT INVENTORY，不能為了豐富畫面改變時間、季節、植物或關鍵物件。
- 細節數量服從當前動作。不要讓背景活動、粒子效果或複雜物理反饋搶奪主體動作。

## Current-range Failure Analysis

在寫當前生成提示詞前，結合 START STATE、ACTION、目標 END STATE 和 HANDOFF，找出當前段最容易失敗的問題。

優先考慮以下風險。

- 角色在當前角度或動作中變臉
- 服裝、髮型、配飾或傷勢漂移
- 核心道具複製、換手、變形或消失
- 動作起點不繼承，運動方向突然反轉
- 起跳、落地、打擊或交接動作提前完成或缺失
- 門、走廊、房間和傢俱關係變化
- 攝影機跳位、跨軸或視線關係錯誤
- 下一段所需元素沒有進入 END STATE
- 當前影片結尾無法自然支援下一次續寫

把最可能發生的少量風險轉換成當前生成範圍的正向約束和必要的負面提示。不要為全部範圍複用一套泛化 Negative Prompt，也不要把此前所有失敗項不斷累積。

## 生成與實際狀態回寫

1. 使用統一時間軸、當前生成範圍的 START STATE、ACTION、目標 END STATE、HANDOFF 和失敗約束生成或續寫影片。
2. 檢查真實影片，不以提示詞中的計劃代替畫面事實。
3. 記錄實際 END STATE。實際結果可接受但與計劃略有差異時，以實際結果更新 Continuity Ledger。
4. 實際結果命中阻斷錯誤時，不更新後續計劃，先重做當前失敗範圍。
5. MODE B 的續寫結果被接受後，把擴展後的影片 Asset ID 設為下一次續寫的唯一來源。

### MOTION HANDOFF CONTRACT

Motion Handoff 用於統一時間軸的相鄰規劃單元以及 MODE B 的續寫邊界，確保動作和運鏡不會因續寫呼叫而重啟。

```text
MOTION HANDOFF
- Motion Vector / 主體和關鍵道具的運動方向與速度趨勢
- Action Phase / 未完成動作所處階段
- Body Momentum / 重心、支撐點和肢體擺動趨勢
- Camera Motion / 運鏡類型、方向與速度趨勢
- Environmental Motion / 衣物、頭髮、雨、煙、火焰和枝葉等動態趨勢
- First-beat Continuation / 下一續寫範圍第一個動作節拍必須發生的延續動作
- Motion Binding Status / CONTINUOUS or BLOCKED
```

- 當前影片應優先結束在動作方向清楚且可自然續寫的時刻，不為交接強迫人物僵硬定格。
- 下一次續寫必須直接擴展同一個影片資產並立即延續 Motion Handoff，禁止靜止展示邊界畫面、重新擺姿勢、重新起步、再次蓄力或重複上一動作。
- 人物動作、道具運動、攝影機運動和環境動態不得在邊界無理由歸零、反向或重新加速。
- 提示詞使用可觀察的方向、動作階段和速度趨勢，不要求模型執行精確速度、加速度或慣性數值。
- 若當前影片結尾無法表達下一動作方向，應重做當前生成範圍的結尾排程，而不是讓下一次續寫猜測運動。
- 續寫後檢查邊界附近的最初動作節拍。出現明顯停頓、動作重啟、動作重複、攝影機先停後走或環境動態凍結時，當前續寫判定為阻斷錯誤。

## 連續性檢查

按以下優先順序檢查當前生成範圍和影片續寫邊界。

1. 人物身份
2. 核心道具
3. 動作
4. 空間
5. 攝影機方向
6. 風格
7. 普通背景細節

### 必須停止並重做當前生成範圍

- 主角明顯變臉或身份無法確認
- 核心道具複製、靜默替換或無理由消失
- 道具持有者或左右手狀態無法銜接
- 上一段動作結果沒有被繼承
- 人物位置與已建立空間關係完全衝突
- 門、走廊或房間連線關係完全錯誤
- 攝影機嚴重跳位、無理由跨越 180 度軸線或運動方向突變
- 人物、道具、攝影機或環境運動在邊界明顯停頓、重啟、重複或無理由歸零
- 當前 END STATE 無法自然成為下一 START STATE
- 同一 LOCATION CONDITION ID 從夕陽、白天或其他已鎖定時間無理由變成夜景
- 植物種類、季節、密度或顏色發生未經劇情授權的明顯變化
- 關鍵樹木、岩石、門、路牌、傢俱或其他環境錨點無理由消失、增加或換位
- 可移動環境物件沒有畫面動作卻改變位置或狀態

發現以上問題時停止後續生成或續寫。只重做當前失敗範圍，並保留此前已經接受的影片資產和狀態。

### 可以接受的輕微誤差

- 非關鍵背景紋理變化
- 群眾外觀和小動作變化
- 不影響劇情和空間理解的小型環境差異

輕微誤差可以記錄，但不單獨觸發重生成。

## 攝影機與動作方向

- Camera State 記錄攝影機所在動作軸線的一側。
- 雙人場景保持視線關係。一個角色看向畫面右側時，對方反打通常應看向畫面左側。
- 人物在連續動作中保持螢幕運動方向。方向改變時，把轉身或攝影機越軸過程展示在畫面中。
- 攝影機位置從上一 END STATE 繼承。沒有明確運動時，保持當前機位和基本構圖。
- 上一段動作結果必須進入下一段。起跳、落地、揮擊、開門、遞交道具和跌倒等動作不能在片段邊界重置。
- 不使用精確速度、加速度、慣性或阻尼數值，除非使用者明確提供且當前模型確實能夠執行。

## 時長模式

### 30 秒以內

優先檢查是否能使用 MODE A 一次生成完整影片。允許向模型提供相對完整的 Master State、Continuity Ledger、統一時間軸和適量關鍵幀。單次能力不滿足時只允許切換到 MODE B。

### 30 秒至 2 分鐘

優先使用 MODE A；單次時長不足時使用 MODE B 對同一影片分階段續寫。每次續寫只讀取 Master State、最新 Continuity Ledger、下一關鍵幀和 Transition Path。以前的劇情透過當前狀態和必要因果保留，不逐字重複。

### 2 至 5 分鐘

必須採用狀態化生成，並使用 MODE B 持續擴展同一影片。每個續寫範圍只讀取以下內容。

- 固定 Master State
- 當前 Continuity Ledger
- Current Planning Unit
- 下一段所需 HANDOFF
- 下一 Narrative Keyframe 與 Transition Path

不要在後續生成範圍中重複此前全部劇情、全部提示詞或每個舊規劃單元的詳細記錄。

## 類型規則

### 恐怖與 Cult

區分 Directed Anomaly 與 Generation Error。劇情明確要求的異常進入 Environment State，並在後續繼承。照片裡按劇情多出一個人屬於 Directed Anomaly。床的位置隨機改變、門無理由換牆或核心道具複製屬於 Generation Error。

### 動作片

額外追蹤人物位置、武器、左右手持物、運動方向、起跳和落地階段、衣物損傷與受傷狀態。高速動作和運鏡不能掩蓋道具唯一性或動作因果錯誤。

### 動漫

允許誇張動作、形變、速度效果和激烈運鏡。角色身份、武器唯一性、空間方向和動作因果保持為硬約束。

## 最終輸出

開始生成前，先向使用者展示以下規劃內容。

1. Master State
2. Visual Asset Bible 和需要準備的參考資產
3. 初始 Continuity Ledger
4. UNIFIED VIDEO TIMELINE、連續空間路線和攝影機軌跡
5. Narrative Keyframe Plan 及各關鍵幀之間的 Transition Path
6. MODE A 或 MODE B 的選擇及當前能力依據
7. 規劃單元及其 START STATE、ACTION、目標 END STATE、HANDOFF、MOTION HANDOFF、SCENE REALISM LAYER 和 REFERENCE MANIFEST
8. 當前生成範圍及其 Failure Analysis

輸出以上規劃後必須立即停止，並明確詢問使用者是否“確認規劃並開始生成”。不要在同一次響應中建立節點、生成初始影片或執行續寫。

MODE B 每次續寫後輸出擴展後影片 Asset ID、實際 END STATE、關鍵幀到達情況、連續性檢查和更新後的 Continuity Ledger。隨後詢問使用者是否確認繼續；阻斷錯誤出現時立即停止。

達到目標時長後，輸出統一長影片 Asset ID 和全片連續性複核結果。不生成獨立 Clip，也不執行片段拼接。
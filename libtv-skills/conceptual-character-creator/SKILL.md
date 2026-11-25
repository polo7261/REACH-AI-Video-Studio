---
name: conceptual-character-creator
description: "輸入一個角色想法，自動生成原創概念角色、角色板和15秒影片"
---

## 2. Agent自動執行硬規則

### 2.1 預設執行模式

當 Agent 具備可用的影象 / 影片生成工具時，本 Skill 預設進入：

```text
Agent Auto-Run Mode / Agent自動執行模式
```

在該模式下，禁止只把提示詞交給使用者手動複製。

Agent 必須儘可能直接執行：

```text
MJ角色概念圖生成
Image模型角色板生成
影片前置檢查
SD2.0最終15秒影片生成
```

### 2.2 文字回退模式

僅噹噹前 Agent 沒有對應生成工具、工具不可用、使用者明確要求只要提示詞，才進入：

```text
Prompt Fallback Mode / 提示詞回退模式
```

回退模式必須明確說明：

```text
當前無法直接呼叫對應生成工具，因此輸出可複製提示詞。
```

不得偽裝成已經生成影象或影片。

### 2.3 不再預設 TEXT ONLY

V0.6 廢除舊版“預設只輸出文字”的規則。新規則為：

```text
有工具則執行，無工具才輸出提示詞。
```

涉及“角色板”“關鍵幀”“成功幀”“影片”時，如果工具可用，預設理解為需要生成資產，而不是隻寫提示詞。

---

## 3. 省積分硬規則：No Video Before Validation

雖然 V0.6 支援自動出影片，但最終15秒影片仍然不能作為初次測試工具。

最終影片生成前必須完成以下檢查：

```text
1. 角色錨點確認
2. MJ概念圖質量確認
3. Image模型角色板質量確認
4. 技能機制確認
5. 技能因果鏈確認
6. 武器 / 媒介主導性確認
7. 真實接觸與物理反饋確認
8. 3個成功畫面確認
9. 失敗風險預判
10. 角色性格、當前情緒、表演微指令與情緒弧線確認
11. 最終提示詞強化項確認
```

如果任一項不清楚，Agent 必須先做低成本修正，不得直接燒最終影片積分。

可執行策略：

```text
先修MJ概念圖
再修Image角色板
再修技能機制
最後才生成15秒SD2.0影片
```

---

## 4. 標準自動生產流程

### 4.1 無角色輸入時

當使用者沒有提供角色圖、角色設定或角色板：

```text
1. 呼叫角色庫，給出6個角色方向。
2. 如果使用者要求“自動 / 全自動 / 你自己選”，Agent 直接選擇最適合做SSS技能展示的角色。
3. 使用 MJ 8.1 + --preview 自動生成單人角色概念圖。
4. 對MJ概念圖做質量檢查。
5. 若出現多角色、半身、武器缺失、海報感、角色不清，自動返修MJ概念圖。
6. MJ概念圖合格後，使用 Image 模型生成角色板。
7. 角色板引數固定為：16:9 / 高畫質 / 2K。
8. 角色板合格後，角色板成為唯一角色錨點。
9. 自動進行角色理解、技能機制設計和Video Preflight Gate。
10. Preflight透過後，使用SD2.0影片模型一次性生成一條完整15秒影片。
```

### 4.2 有MJ角色概念圖時

```text
1. 不直接進入影片。
2. 先檢查MJ概念圖是否為單人、全身、武器清楚、服裝結構可讀。
3. 合格後，使用 Image 模型自動生成角色板。
4. 角色板引數固定：16:9 / 高畫質 / 2K。
5. 角色板透過後，再進入技能預演和最終影片。
```

### 4.3 有角色板時

```text
1. 把角色板作為唯一角色錨點。
2. 分析角色身份、武器媒介、視覺母題、技能動力學。
3. 自動輸出技能機制預演。
4. 自動執行 Video Preflight Gate。
5. 若透過，使用SD2.0自動生成一條完整15秒影片。
```

### 4.4 有失敗影片時

```text
1. 分析失敗影片。
2. 判斷失敗發生在：角色錨點、武器主導、技能因果、鏡頭、物理反饋、模型誤讀。
3. 優先返修前置提示詞或角色板，不優先繼續燒影片。
4. 必須輸出下一次影片生成前的阻塞點和修正策略。
```

---

## 5. Midjourney 角色概念生成規則

角色概念圖預設使用 Midjourney：

```text
--v 8.1 --preview
```

`--preview` 必須放在 MJ 提示詞引數末尾，用於呼叫 8.2 測試版本。

### 5.1 單角色控制規則

當目標是單個角色概念圖時，禁止使用容易生成多角色的並列結構：

```text
A warlord, a gunslinger, a blade-bearer
```

必須改寫為：

- `A single character ...`
- `A single lead character who combines ...`
- `A xxx-xxx-xxx hybrid character`

並追加：

```text
solo, one person only, single character, full body, centered composition, no group, no lineup, no multiple characters, no extra people
```

### 5.2 MJ概念圖質檢硬規則

角色概念圖進入角色板之前，必須檢查：

- 是否多個角色 / 角色陣列
- 是否半身 / 裁腳 / 頭像
- 主武器或核心媒介是否缺失
- 是否過度海報感
- 服裝結構是否可讀
- 身份是否被誤解
- 是否提前生成多檢視 / 多面板
- 是否有文字、logo、UI、亂碼干擾

如不合格，先呼叫 `references/mj-common-error-repair-library.md` 返修，不進入角色板。

---

## 6. Image模型角色板生成硬規則

V0.6 明確修正：

```text
角色板不是用 MJ 繼續生成，而是使用 Image 模型生成。
```

角色板生成引數固定為：

```text
模型：Image模型
比例：16:9
畫質：高畫質
解析度：2K
輸入參考：最終MJ角色概念圖作為 {{Image 1}}
輸出目標：專業角色轉視角圖表 / 角色參考模型圖表
```

角色板必須包含：

- 面部特寫
- 正檢視
- 背檢視
- 左側輪廓
- 右側輪廓
- 全身視角旁的垂直高度測量刻度
- 左下角資訊面板
- 白色攝影棚背景
- 柔和均勻攝影棚光
- 全視角一致身份、比例、服裝、武器、材質

角色板生成後必須質檢：

- 是否同一角色
- 是否五個視角齊全
- 是否全身清楚
- 是否武器 / 媒介出現
- 是否服裝結構可讀
- 是否沒有多餘角色
- 是否沒有錯位 / 畸變 / 多手多腳
- 是否適合作為唯一影片參考錨點

模板見：

```text
templates/image-model-character-board-template.md
templates/character-board-from-mj-template.md
```

---

## 7. 角色板唯一錨點規則

角色板生成後，成為後續所有技能與影片的 **唯一角色錨點**。

禁止：

- 回退混用MJ概念圖
- 混用其他無關參考圖
- 重新設計臉、服裝、武器、體型
- 根據技能需要擅自換身份

影片提示詞必須保留角色板中的：

- 面部結構
- 髮型與髮色
- 年齡感
- 膚色
- 體型與比例
- 服裝輪廓與材質
- 武器 / 道具 / 配飾
- 核心氣質與身份感

---

## 8. 角色性格與情緒表演硬規則

V0.6.2 新增硬規則：最終影片不能只鎖定外形、武器和技能，還必須鎖定角色的性格、當前情緒和表演驅動力。

任何角色進入最終 SD2.0 15 秒影片生成前，必須完成：

```text
【角色性格錨點】
性格主軸：
氣質關鍵詞：
行為方式：
壓迫方式：
情緒表達方式：
禁用表演：

【當前情緒狀態】
當前情緒：
情緒強度：/10
觸發原因：
爆發方式：
收尾餘韻：

【表演微指令】
眼神：
嘴部表情：
呼吸狀態：
頭部動作：
肩頸狀態：
手部狀態：
爆發前停頓：
爆發後反應：
收尾狀態：

【15秒情緒弧線】
0-3秒：情緒建立
3-7秒：壓迫上升
7-11秒：爆發
11-15秒：餘震 / 收束 / 性格態度顯現
```

如果缺少以上任一部分，Agent 不得直接生成最終影片。

### 8.1 角色不能只是“會放技能的殼子”

錯誤方向：

```text
角色站著，釋放技能，最後擺 pose。
```

正確方向：

```text
角色以符合自身性格和當前情緒的方式執行技能，動作節奏、眼神、呼吸、停頓、爆發和收尾都服務於角色性格。
```

### 8.2 最終影片提示詞必須新增欄位

最終 SD2.0 影片提示詞必須包含：

```text
【角色性格錨點】
【當前情緒狀態】
【表演微指令】
【15秒情緒弧線】
【收尾情緒餘韻】
```

這些欄位不得被壓縮成一句話，也不得只寫“冷酷”“憤怒”等單詞。

詳見：

```text
references/character-personality-and-emotion-system.md
templates/personality-emotion-preflight-template.md
```

---

## 9. Video Preflight Gate 影片前置檢查

最終影片生成前，必須自動完成：

```text
【角色性格與情緒】
性格主軸：
當前情緒：
表演微指令：
15秒情緒弧線：

【技能因果鏈】
角色動作：
武器 / 媒介動作：
真實接觸：
第一視覺結果：
環境反應：
終局收束：

【武器 / 媒介主導性檢查】
主導動作是否來自武器 / 媒介：
特效是否由武器 / 媒介觸發：
是否有真實接觸與物理反饋：
觀眾能否一眼看出結果由該武器造成：

【必須出現的3個成功畫面】
1.
2.
3.

【失敗風險】
1.
2.
3.

【預演結論】
透過 / 阻塞
```

若結論為“阻塞”，Agent 不得生成最終15秒影片，只能自動修正前置資產或提示詞。

---

## 10. 技能動力學優先規則

禁止所有角色預設使用“站立蓄力 + 圓形法陣 + 大招爆發”的同質化結構。

必須先判斷角色動力學：

- 速度型
- 重擊型
- 武器軌跡型
- 槍械觸發型
- 儀式權杖型
- 召喚型
- 侵蝕型
- 環境改寫型
- 幻術錯位型
- 近身壓制型
- 一擊終局型
- 領域展開型
- 披風載體型
- 槍聲審判型
- 路徑延遲爆發型
- 現實裁剪型
- 命運縫合型
- 凋零終局型

詳見：`references/skill-dynamics-library.md`

---

## 11. 反模板檢查器

輸出 / 執行前必須檢查：

- 是否又寫成普通法陣？
- 是否又是火球 / 雷電 / 黑霧 / 光柱 / 鐳射？
- 是否所有角色都在揮劍或舉手大招？
- 是否特效沒有媒介來源？
- 是否角色特徵在大招中消失？
- 是否面部特寫超過0.5秒？
- 是否鏡頭全程單一中景？
- 是否沒有英雄收尾？
- 是否影片被拆成分段？
- 是否把影片作為初次測試？
- 是否只輸出提示詞而沒有呼叫可用生成工具？

硬規則：

```text
面部特寫只保留0.5秒以內，用於確認角色身份。不要長時間凝視。角色識別應透過服裝輪廓、武器、動作方式和英雄收尾持續體現。
```

---

## 12. SD2.0 影片生成硬規則

所有最終技能展示影片預設使用 **SD2.0 影片模型**。

硬性要求：

```text
模型：SD2.0影片模型
時長：15秒
生成方式：一次性直接生成完整15秒
禁止：分段生成 / 多段拼接 / 分鏡圖自動生成
比例：16:9 或 21:9
輸出畫質：720p固定，不要1080p
聲音：必須有聲音
參考圖：只使用角色板作為唯一角色參考錨點
前提：必須透過 Video Preflight Gate
```

Agent 具備影片工具時，必須直接生成影片。無影片工具時，才輸出最終提示詞作為回退。

最終影片提示詞必須明確：

- one continuous 15-second video
- no segmented generation
- SD2.0 video model
- 16:9 or 21:9
- fixed 720p output, not 1080p
- with sound
- character board as the only reference anchor

---

## 13. 最終預設輸出格式

### 12.1 Agent自動執行時

```text
【執行狀態】
當前階段：
已生成資產：
下一步動作：
阻塞點：無 / 有

【角色資產】
MJ角色概念圖：已生成 / 待生成 / 已返修
Image模型角色板：已生成 / 待生成 / 已返修

【Preflight結果】
透過 / 阻塞

【最終影片】
SD2.0 15秒影片：已生成 / 未生成
影片設定：15s / 16:9或21:9 / 720p固定 / with sound / one pass

【失敗風險與返修】
```

### 12.2 工具不可用回退時

```text
【當前限制】
當前Agent無法直接呼叫對應生成工具，因此輸出可複製提示詞。

【MJ角色概念提示詞】
【Image模型角色板提示詞】
【Video Preflight Gate】
【SD2.0影片提示詞】
```

---

## 14. 關鍵文件索引

```text
references/agent-auto-run-workflow.md
references/tool-execution-policy.md
references/image-model-character-board-generation.md
references/auto-run-asset-handoff.md
references/role-archetype-library.md
references/role-understanding-engine.md
references/skill-dynamics-library.md
references/weapon-medium-binding-library.md
references/anti-template-checker.md
references/mj-common-error-repair-library.md
references/video-preflight-gate.md
references/skill-causality-chain.md
references/weapon-dominance-check.md
references/three-success-frames.md
references/failure-risk-prediction.md
references/sd2-video-production-workflow.md
references/low-cost-validation-workflow.md

templates/mj-character-concept-template.md
templates/image-model-character-board-template.md
templates/character-board-from-mj-template.md
templates/skill-preflight-template.md
templates/three-success-frames-template.md
templates/sss-skill-prompt-template.md
templates/sd2-video-final-template.md
templates/agent-auto-run-status-template.md
templates/full-auto-user-command.md
templates/repair-prompt-template.md

examples/agent-auto-run-example.md
examples/no-character-to-sd2-video-example.md
examples/tailor-preflight-example.md
examples/tailor-final-video-example.md

evals/qa-scorecard.md
```

---

## 4. 影片提示詞語言與密度硬規則

V0.6.2 新增硬規則：Agent 自動執行時，最終影片提示詞不能被壓縮成英文短句。

### 4.1 預設語言

最終 SD2.0 影片提示詞預設使用 **中文完整結構提示詞**。

允許保留少量英文技術詞，例如：

```text
cinematic realism, PBR, 0.25x slow motion, one continuous 15-second video, no segmented generation
```

但不得把完整影片提示詞改寫成簡短英文 caption。

### 4.2 當工具偏好英文時

如果某個影片工具強制或明顯偏好英文，Agent 必須做 **完整結構翻譯**，而不是摘要壓縮。

錯誤做法：

```text
A powerful warrior strikes the ground with a hammer, cinematic, epic, 15 seconds.
```

正確做法：

```text
完整保留角色錨點、武器鎖定、技能因果鏈、15秒時間軸、鏡頭、物理反饋、聲音和負面約束，然後整體翻譯為英文。
```

### 4.3 最終影片提示詞最低密度

最終 SD2.0 影片提示詞不得少於以下結構：

```text
【角色板唯一錨點】
【影片目標】
【角色與武器鎖定】
【角色性格錨點】
【當前情緒狀態】
【表演微指令】
【15秒情緒弧線】
【技能核心】
【技能因果鏈】
【必須出現的3個成功畫面】
【15秒時間軸】
【鏡頭語言】
【物理反饋】
【聲音設計】
【影片引數】
【負面約束】
```

如果 Agent 在自動執行模式下呼叫影片工具，傳給工具的 prompt 必須是完整生產提示詞，不是狀態摘要、不是一句話提示詞。

### 4.4 短提示詞使用限制

短提示詞只能用於：

- 使用者明確要求“給我短版”
- 快速方向預覽
- Agent 狀態列摘要
- 檔案命名 / 任務名

短提示詞不得用於最終15秒影片生成。

### 4.5 使用者可見輸出與工具執行輸出

Agent 可以在聊天裡給使用者簡短狀態，例如：

```text
已透過 Preflight，正在用完整中文結構提示詞生成15秒影片。
```

但傳給 SD2.0 的內部影片提示詞必須完整、結構化、包含時間軸和約束。

完整模板見：

```text
templates/sd2-full-video-prompt-template.md
references/prompt-language-density-control.md
references/video-resolution-lock.md
```

### V0.7 新增 / 合併文件

```text
references/prompt-language-density-control.md
references/character-personality-and-emotion-system.md
references/video-resolution-lock.md
templates/personality-emotion-preflight-template.md
templates/sd2-full-video-prompt-template.md
```
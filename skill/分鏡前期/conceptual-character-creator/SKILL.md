## 2. Agent自动执行硬规则

### 2.1 默认执行模式

当 Agent 具备可用的图像 / 视频生成工具时，本 Skill 默认进入：

```text
Agent Auto-Run Mode / Agent自动执行模式
```

在该模式下，禁止只把提示词交给用户手动复制。

Agent 必须尽可能直接执行：

```text
MJ角色概念图生成
Image模型角色板生成
视频前置检查
SD2.0最终15秒视频生成
```

### 2.2 文本回退模式

仅当当前 Agent 没有对应生成工具、工具不可用、用户明确要求只要提示词，才进入：

```text
Prompt Fallback Mode / 提示词回退模式
```

回退模式必须明确说明：

```text
当前无法直接调用对应生成工具，因此输出可复制提示词。
```

不得伪装成已经生成图像或视频。

### 2.3 不再默认 TEXT ONLY

V0.6 废除旧版“默认只输出文本”的规则。新规则为：

```text
有工具则执行，无工具才输出提示词。
```

涉及“角色板”“关键帧”“成功帧”“视频”时，如果工具可用，默认理解为需要生成资产，而不是只写提示词。

---

## 3. 省积分硬规则：No Video Before Validation

虽然 V0.6 支持自动出视频，但最终15秒视频仍然不能作为初次测试工具。

最终视频生成前必须完成以下检查：

```text
1. 角色锚点确认
2. MJ概念图质量确认
3. Image模型角色板质量确认
4. 技能机制确认
5. 技能因果链确认
6. 武器 / 媒介主导性确认
7. 真实接触与物理反馈确认
8. 3个成功画面确认
9. 失败风险预判
10. 角色性格、当前情绪、表演微指令与情绪弧线确认
11. 最终提示词强化项确认
```

如果任一项不清楚，Agent 必须先做低成本修正，不得直接烧最终视频积分。

可执行策略：

```text
先修MJ概念图
再修Image角色板
再修技能机制
最后才生成15秒SD2.0视频
```

---

## 4. 标准自动生产流程

### 4.1 无角色输入时

当用户没有提供角色图、角色设定或角色板：

```text
1. 调用角色库，给出6个角色方向。
2. 如果用户要求“自动 / 全自动 / 你自己选”，Agent 直接选择最适合做SSS技能展示的角色。
3. 使用 MJ 8.1 + --preview 自动生成单人角色概念图。
4. 对MJ概念图做质量检查。
5. 若出现多角色、半身、武器缺失、海报感、角色不清，自动返修MJ概念图。
6. MJ概念图合格后，使用 Image 模型生成角色板。
7. 角色板参数固定为：16:9 / 高画质 / 2K。
8. 角色板合格后，角色板成为唯一角色锚点。
9. 自动进行角色理解、技能机制设计和Video Preflight Gate。
10. Preflight通过后，使用SD2.0视频模型一次性生成一条完整15秒视频。
```

### 4.2 有MJ角色概念图时

```text
1. 不直接进入视频。
2. 先检查MJ概念图是否为单人、全身、武器清楚、服装结构可读。
3. 合格后，使用 Image 模型自动生成角色板。
4. 角色板参数固定：16:9 / 高画质 / 2K。
5. 角色板通过后，再进入技能预演和最终视频。
```

### 4.3 有角色板时

```text
1. 把角色板作为唯一角色锚点。
2. 分析角色身份、武器媒介、视觉母题、技能动力学。
3. 自动输出技能机制预演。
4. 自动执行 Video Preflight Gate。
5. 若通过，使用SD2.0自动生成一条完整15秒视频。
```

### 4.4 有失败视频时

```text
1. 分析失败视频。
2. 判断失败发生在：角色锚点、武器主导、技能因果、镜头、物理反馈、模型误读。
3. 优先返修前置提示词或角色板，不优先继续烧视频。
4. 必须输出下一次视频生成前的阻塞点和修正策略。
```

---

## 5. Midjourney 角色概念生成规则

角色概念图默认使用 Midjourney：

```text
--v 8.1 --preview
```

`--preview` 必须放在 MJ 提示词参数末尾，用于调用 8.2 测试版本。

### 5.1 单角色控制规则

当目标是单个角色概念图时，禁止使用容易生成多角色的并列结构：

```text
A warlord, a gunslinger, a blade-bearer
```

必须改写为：

- `A single character ...`
- `A single lead character who combines ...`
- `A xxx-xxx-xxx hybrid character`

并追加：

```text
solo, one person only, single character, full body, centered composition, no group, no lineup, no multiple characters, no extra people
```

### 5.2 MJ概念图质检硬规则

角色概念图进入角色板之前，必须检查：

- 是否多个角色 / 角色阵列
- 是否半身 / 裁脚 / 头像
- 主武器或核心媒介是否缺失
- 是否过度海报感
- 服装结构是否可读
- 身份是否被误解
- 是否提前生成多视图 / 多面板
- 是否有文字、logo、UI、乱码干扰

如不合格，先调用 `references/mj-common-error-repair-library.md` 返修，不进入角色板。

---

## 6. Image模型角色板生成硬规则

V0.6 明确修正：

```text
角色板不是用 MJ 继续生成，而是使用 Image 模型生成。
```

角色板生成参数固定为：

```text
模型：Image模型
比例：16:9
画质：高画质
分辨率：2K
输入参考：最终MJ角色概念图作为 {{Image 1}}
输出目标：专业角色转视角图表 / 角色参考模型图表
```

角色板必须包含：

- 面部特写
- 正视图
- 背视图
- 左侧轮廓
- 右侧轮廓
- 全身视角旁的垂直高度测量刻度
- 左下角信息面板
- 白色摄影棚背景
- 柔和均匀摄影棚光
- 全视角一致身份、比例、服装、武器、材质

角色板生成后必须质检：

- 是否同一角色
- 是否五个视角齐全
- 是否全身清楚
- 是否武器 / 媒介出现
- 是否服装结构可读
- 是否没有多余角色
- 是否没有错位 / 畸变 / 多手多脚
- 是否适合作为唯一视频参考锚点

模板见：

```text
templates/image-model-character-board-template.md
templates/character-board-from-mj-template.md
```

---

## 7. 角色板唯一锚点规则

角色板生成后，成为后续所有技能与视频的 **唯一角色锚点**。

禁止：

- 回退混用MJ概念图
- 混用其他无关参考图
- 重新设计脸、服装、武器、体型
- 根据技能需要擅自换身份

视频提示词必须保留角色板中的：

- 面部结构
- 发型与发色
- 年龄感
- 肤色
- 体型与比例
- 服装轮廓与材质
- 武器 / 道具 / 配饰
- 核心气质与身份感

---

## 8. 角色性格与情绪表演硬规则

V0.6.2 新增硬规则：最终视频不能只锁定外形、武器和技能，还必须锁定角色的性格、当前情绪和表演驱动力。

任何角色进入最终 SD2.0 15 秒视频生成前，必须完成：

```text
【角色性格锚点】
性格主轴：
气质关键词：
行为方式：
压迫方式：
情绪表达方式：
禁用表演：

【当前情绪状态】
当前情绪：
情绪强度：/10
触发原因：
爆发方式：
收尾余韵：

【表演微指令】
眼神：
嘴部表情：
呼吸状态：
头部动作：
肩颈状态：
手部状态：
爆发前停顿：
爆发后反应：
收尾状态：

【15秒情绪弧线】
0-3秒：情绪建立
3-7秒：压迫上升
7-11秒：爆发
11-15秒：余震 / 收束 / 性格态度显现
```

如果缺少以上任一部分，Agent 不得直接生成最终视频。

### 8.1 角色不能只是“会放技能的壳子”

错误方向：

```text
角色站着，释放技能，最后摆 pose。
```

正确方向：

```text
角色以符合自身性格和当前情绪的方式执行技能，动作节奏、眼神、呼吸、停顿、爆发和收尾都服务于角色性格。
```

### 8.2 最终视频提示词必须新增字段

最终 SD2.0 视频提示词必须包含：

```text
【角色性格锚点】
【当前情绪状态】
【表演微指令】
【15秒情绪弧线】
【收尾情绪余韵】
```

这些字段不得被压缩成一句话，也不得只写“冷酷”“愤怒”等单词。

详见：

```text
references/character-personality-and-emotion-system.md
templates/personality-emotion-preflight-template.md
```

---

## 9. Video Preflight Gate 视频前置检查

最终视频生成前，必须自动完成：

```text
【角色性格与情绪】
性格主轴：
当前情绪：
表演微指令：
15秒情绪弧线：

【技能因果链】
角色动作：
武器 / 媒介动作：
真实接触：
第一视觉结果：
环境反应：
终局收束：

【武器 / 媒介主导性检查】
主导动作是否来自武器 / 媒介：
特效是否由武器 / 媒介触发：
是否有真实接触与物理反馈：
观众能否一眼看出结果由该武器造成：

【必须出现的3个成功画面】
1.
2.
3.

【失败风险】
1.
2.
3.

【预演结论】
通过 / 阻塞
```

若结论为“阻塞”，Agent 不得生成最终15秒视频，只能自动修正前置资产或提示词。

---

## 10. 技能动力学优先规则

禁止所有角色默认使用“站立蓄力 + 圆形法阵 + 大招爆发”的同质化结构。

必须先判断角色动力学：

- 速度型
- 重击型
- 武器轨迹型
- 枪械触发型
- 仪式权杖型
- 召唤型
- 侵蚀型
- 环境改写型
- 幻术错位型
- 近身压制型
- 一击终局型
- 领域展开型
- 披风载体型
- 枪声审判型
- 路径延迟爆发型
- 现实裁剪型
- 命运缝合型
- 凋零终局型

详见：`references/skill-dynamics-library.md`

---

## 11. 反模板检查器

输出 / 执行前必须检查：

- 是否又写成普通法阵？
- 是否又是火球 / 雷电 / 黑雾 / 光柱 / 激光？
- 是否所有角色都在挥剑或举手大招？
- 是否特效没有媒介来源？
- 是否角色特征在大招中消失？
- 是否面部特写超过0.5秒？
- 是否镜头全程单一中景？
- 是否没有英雄收尾？
- 是否视频被拆成分段？
- 是否把视频作为初次测试？
- 是否只输出提示词而没有调用可用生成工具？

硬规则：

```text
面部特写只保留0.5秒以内，用于确认角色身份。不要长时间凝视。角色识别应通过服装轮廓、武器、动作方式和英雄收尾持续体现。
```

---

## 12. SD2.0 视频生成硬规则

所有最终技能展示视频默认使用 **SD2.0 视频模型**。

硬性要求：

```text
模型：SD2.0视频模型
时长：15秒
生成方式：一次性直接生成完整15秒
禁止：分段生成 / 多段拼接 / 分镜图自动生成
比例：16:9 或 21:9
输出画质：720p固定，不要1080p
声音：必须有声音
参考图：只使用角色板作为唯一角色参考锚点
前提：必须通过 Video Preflight Gate
```

Agent 具备视频工具时，必须直接生成视频。无视频工具时，才输出最终提示词作为回退。

最终视频提示词必须明确：

- one continuous 15-second video
- no segmented generation
- SD2.0 video model
- 16:9 or 21:9
- fixed 720p output, not 1080p
- with sound
- character board as the only reference anchor

---

## 13. 最终默认输出格式

### 12.1 Agent自动执行时

```text
【执行状态】
当前阶段：
已生成资产：
下一步动作：
阻塞点：无 / 有

【角色资产】
MJ角色概念图：已生成 / 待生成 / 已返修
Image模型角色板：已生成 / 待生成 / 已返修

【Preflight结果】
通过 / 阻塞

【最终视频】
SD2.0 15秒视频：已生成 / 未生成
视频设置：15s / 16:9或21:9 / 720p固定 / with sound / one pass

【失败风险与返修】
```

### 12.2 工具不可用回退时

```text
【当前限制】
当前Agent无法直接调用对应生成工具，因此输出可复制提示词。

【MJ角色概念提示词】
【Image模型角色板提示词】
【Video Preflight Gate】
【SD2.0视频提示词】
```

---

## 14. 关键文档索引

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

## 4. 视频提示词语言与密度硬规则

V0.6.2 新增硬规则：Agent 自动执行时，最终视频提示词不能被压缩成英文短句。

### 4.1 默认语言

最终 SD2.0 视频提示词默认使用 **中文完整结构提示词**。

允许保留少量英文技术词，例如：

```text
cinematic realism, PBR, 0.25x slow motion, one continuous 15-second video, no segmented generation
```

但不得把完整视频提示词改写成简短英文 caption。

### 4.2 当工具偏好英文时

如果某个视频工具强制或明显偏好英文，Agent 必须做 **完整结构翻译**，而不是摘要压缩。

错误做法：

```text
A powerful warrior strikes the ground with a hammer, cinematic, epic, 15 seconds.
```

正确做法：

```text
完整保留角色锚点、武器锁定、技能因果链、15秒时间轴、镜头、物理反馈、声音和负面约束，然后整体翻译为英文。
```

### 4.3 最终视频提示词最低密度

最终 SD2.0 视频提示词不得少于以下结构：

```text
【角色板唯一锚点】
【视频目标】
【角色与武器锁定】
【角色性格锚点】
【当前情绪状态】
【表演微指令】
【15秒情绪弧线】
【技能核心】
【技能因果链】
【必须出现的3个成功画面】
【15秒时间轴】
【镜头语言】
【物理反馈】
【声音设计】
【视频参数】
【负面约束】
```

如果 Agent 在自动执行模式下调用视频工具，传给工具的 prompt 必须是完整生产提示词，不是状态摘要、不是一句话提示词。

### 4.4 短提示词使用限制

短提示词只能用于：

- 用户明确要求“给我短版”
- 快速方向预览
- Agent 状态栏摘要
- 文件命名 / 任务名

短提示词不得用于最终15秒视频生成。

### 4.5 用户可见输出与工具执行输出

Agent 可以在聊天里给用户简短状态，例如：

```text
已通过 Preflight，正在用完整中文结构提示词生成15秒视频。
```

但传给 SD2.0 的内部视频提示词必须完整、结构化、包含时间轴和约束。

完整模板见：

```text
templates/sd2-full-video-prompt-template.md
references/prompt-language-density-control.md
references/video-resolution-lock.md
```

### V0.7 新增 / 合并文档

```text
references/prompt-language-density-control.md
references/character-personality-and-emotion-system.md
references/video-resolution-lock.md
templates/personality-emotion-preflight-template.md
templates/sd2-full-video-prompt-template.md
```
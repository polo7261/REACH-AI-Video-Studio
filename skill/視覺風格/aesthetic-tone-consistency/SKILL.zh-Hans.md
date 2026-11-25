---
name: aesthetic-tone-consistency
description: "sref 一码锁定全片影调,美学不跑偏,逐镜成片调性如一"
---

---

## name: aesthetic-film\\

namespace: industry\
title: "美学定调短片"\
description: "以 Midjourney 美学风格（sref 定调）为核心的艺术短片：先用 MJ 锁定全片视觉调性，再由 Seedance 逐镜成片。适用于「用一套统一的电影级美学基调把一个短故事/氛围片做成成片」。两种模式——A：每镜 MJ 直出关键帧 → Seedance；B：MJ 出元素基准画板 → Nano Banana 轻改合成 key_frame → Seedance。纯图片美学（不成片）→ image-generation；通用多镜叙事（非 MJ 美学定调）→ cinematic-flow。"\
version: 3

# aesthetic-film

做**以 Midjourney 美学风格（sref 定调）为核心的艺术短片**时用本 skill：先用 MJ 把全片视觉调性锁死成一个统一基准，再由 Seedance 逐镜生成成片。核心不是叙事复杂度，而是**美学一致性**——整片靠一套 sref / 风格描述维持同一影调。本 skill 自足：sref 定调机制、镜头设计、电影化提示词、Seedance 序列、音频与合成规则全部内联，不外包给别的 skill。

## 两种模式

- **模式 A（MJ 直出关键帧，源 #16）**：每镜用 MJ 直接生成关键帧图 → Seedance 成片。适合以 MJ 出图质感直接驱动画面的场景。
- **模式 B（MJ 基准画板 → Nano 精修，源 #17）**：MJ 出**元素基准画板**（外观由 sref 锚定），再用 Nano Banana 在 MJ 参考图上做**轻量合成/微调**得到每镜 key_frame → Seedance 成片。适合叙事化、需要按分镜精确排布主体位置/姿态、但要严守 MJ 风格锁的场景。

模式选择在规范定稿阶段与用户确认；两模式共用下面的 sref 定调、镜头设计、提示词与合成规则。

## 阶段（按 SP 全流程）

不要一次跑完全部阶段。在每个关键阶段（规范定稿 / 风格路径确认 / 故事板确认 / 元素图完成 / 关键帧完成 / 逐镜视频后 / 音频后）暂停，用 `ask_human` 或卡片邀请用户确认后再进下一步。继续前用卡片或回复邀请用户审阅。

1. **规范定稿**：写 `Final_Video_Spec.md`（标题、类型、比例、时长、视觉风格、语言、模型偏好）→ `write_file_v2`。同时**确认美学风格路径**（见「风格路径与 sref 定调」）与模式 A/B。
2. **故事板**：生成 shot_list + audio_layers（模式 B 另含关键元素设计）→ 见「故事板设计」。
3. **元素/关键帧图**：模式 A 每镜出一张关键帧图；模式 B 先出 MJ 元素基准画板，再 Nano 精修出各镜 key_frame → `generate_image_v3`（见「元素与关键帧生成」）。已有用户素材先 `get_node_info` 绑定到对应故事板位置，不重复生成。
4. **逐镜视频**：`generate_video_v3` 逐镜，`reference_nodes` 引关键帧 / 元素图、`{{NodeKey}}` 绑定；单镜 ≤15s（引擎单次上限）。提示词按「逐镜视频提示词」内联规则写。
5. **音频层**：`generate_audio` 生成所有独立音频层（≥1 全局 BGM；长片可多段 BGM 各带 `audio_id` 与范围；有解说 / 旁白设 narration 层）。
6. **合成**：`composite_video` 按故事板与时间轴顺序拼成成片，引导用户导出。

**阶段依赖**（源 Flova #16/#17）：2→1；3→2；4→3；5→2；6→2,3,4,5。

**用户已有素材**（主要影响步骤 3–5）：在填充生成内容前，先用 `get_node_info` 把用户提供 / 现有素材绑定并分配到对应故事板位置；避免重复生成用户已给的素材。

## 风格路径与 sref 定调（核心工艺）

规范定稿与素材生成前，**先与用户确认用 MJ 生成美学风格图的路径**（两选一）：

- **路径一（风格描述词）**：用提示词描述确定风格。用户明确了风格专有名词或偏好时，把风格描述记入 `Final_Video_Spec`，并在**后续所有元素生成中始终复用**这套风格描述词。
- **路径二（sref code 定调）**：用 `--sref` 代码作为风格标杆来构建故事板内容，而**不是**把 `Final_Video_Spec` 的风格重写进每一条 MJ 提示词。

`--sref` **选择规则（路径二）**：

- 先问用户是否有 Midjourney `--sref` 风格代码。没有则由代理自选一个代码（通常取 **0–4294967295** 的整数，随机 / 贴合内容均可）；**记录所用代码，并在项目内后续所有 MJ 调用中复用**，除非用户更改。
- 语法 `--sref <code1> <code2> …`，token 之间**空格分隔**（如 `--sref 5877700996 4815442863`）。每个值必须是 0–4294967295 的整数。**多个代码可堆叠**；用户给了多个就记录完整列表并全程复用。无用户偏好而自行发明代码时，除非用户明确要求堆叠，**优先单个自动整数以保简洁**。

**工具适配**：MJ 图由 `generate_image_v3`（`ai_model` 指定 `Midjourney V8.1`）生成。**若当前引擎不支持** `--sref` **参数**：降级到路径一（风格描述词复用）+ 把风格基准图作 `reference_nodes` 的风格参考传入——机制（全片一套风格锁、跨镜复用）保留，落点适配。

## 故事板设计

### 关键元素设计（模式 B / 有复现元素时）

- 覆盖**关键主体**（角色、物体）、**关键地点 / 场景**、**关键道具**（如有）。
- **角色多状态显式分列**：角色在项目中有多个造型 / 外观（不同服装、年龄）时，在描述里明确写出（造型 1：…；造型 2：…）。
- **场景内物体位置朝向**：描述重要物体（尤其道具、发生主要动作 / 表演的区域）的位置和朝向。
- **用户素材必须匹配**：用户提供并指定为关键元素的素材，描述**必须与之匹配**，不得与所见 / 所听矛盾。

### 镜头设计（每镜三要素）

每个镜头描述必须含：

- **场景**：引用地点 / 布景，用场景元素 ID（如 `[Element_Office_Noir]`）。
- **叙事内容**：角色与关键物体的动作 / 动态、台词与表演，写出**确切台词**（口述对白或内心独白 / OS），用元素 ID 引用角色。
- **镜头语言（摄影）**：景别（全景 / 中景 / 特写）、机位角度（仰拍 / 俯拍）、运镜（固定 / 摇摄 / 推轨）。

### 独立音频设计

- **背景音乐**：至少设计一段全局 BGM。视频较长（如 ≥3 分钟）且有明显幕间 / 转折点时，可规划多段音乐（每段带自己的 `audio_id` 与作用范围）。
- **旁白**：用画外音 / 旁白推进故事时在此设计（类型 `narration`）：定义声音特征、语气、确切脚本；用 `layout_instruction` 把它限定在相关镜头范围内。

## 元素与关键帧生成

### 关键元素图（MJ 基准，两模式共用）

加载用户选定的风格路径（路径一：用 `Final_Video_Spec` 记录的风格描述；路径二：用 `--sref` 定调）。

- 用 `generate_image_v3`（`Midjourney` 系引擎）出**风格 / 场景、角色 / 道具基底、大场景**。
- **提示词规则**：描述内容（人物 / 事物 / 地点、可辨识轮廓、环境），按上文规则附加 `--sref`。**不要**把规范里"预想视频 / 图像风格"的长篇文案塞进 MJ，也不要把 MJ 步骤当成必须执行该文档的环节——**sref + 主体 / 场景描述就足够**。

### MJ 基准画板定位（模式 B）

- MJ 画板是**外观的事实来源**（source of truth）：外观由 `--sref` 锚定。
- MJ 在模式 B 里是后续 Nano 工作的**基准工厂（reference board）**，**不是最终装配时的调色步骤**——不要指望 MJ 一步出成品帧。

### Nano Banana key_frame 精修（模式 B 核心·反模式）

- 用 `generate_image_v3` 图生图（`Nano Banana Pro` 系引擎），出**每镜第一帧**，与故事板中的镜头描述对齐；分辨率按项目规范设 **2K–4K**。
- **输入**：按镜路由的场景 / 风格 / 角色 / 道具元素参考（`reference_nodes`）。
- **提示词必须简洁**：指定**哪张参考图提供环境 / 纹理**、**哪张提供风格 / 光照词汇**，**只**关联故事板脚本所要求的内容（姿势、布局、谁拿着什么）。**禁止**粘贴重新描述调色 / 光照 / 电影参考 / 情绪的段落——**那会强制模型完全重绘、削弱对 MJ 参考图的依从**。Nano 只做在 MJ 参考图之上的**轻量合成 / 微调**，不是从长提示词重建整张图。

## 逐镜视频提示词（全量内联，不外包）

### 语言规则（最高优先）

用户用中文输入或加载中文语言环境时，提示词用**中文书写**；但提示词里的旁白 / 对话内容严格遵循 `Final_Video_Spec` 的 Output Language。

### 图像提示词 6 大核心规则（写 MJ `key_element` 元素图时全局套用）

提示词不只是描述"图里有什么"，而是像专业电影导演 + 调色师给团队下指令。把这 6 条写成**流畅自然的英文段落**、**编织在一起**，不要输出为带标签分节：

1. **专业风格锚点**：结合专业艺术 / 电影术语与风格词；引入"作者"与具体电影视觉锚点（如 `Neo-Noir style, David Fincher Style, inspired by Se7en`），不要泛泛只说 `Neo-Noir`。
2. **构图与镜头**：明确电影化构图（`Over-the-shoulder shot` / `Dutch angle`）与景别（`Close-up` / `Medium shot`）。
3. **光影（含负光）**：详述主光并重点强调"负光"以产生对比与戏剧性（`Strong chiaroscuro contrast` / `dramatic interplay of light and shadow` / `deep facial shadows emphasizing facial structure`）。
4. **调色（90% 单主色·禁红蓝霓虹）**：高端好莱坞克制调色（`deep teal-cyan shadows dominating 90%, zero warm fill` / `muted watercolor wash`）；除非用户明确要求，**永不用红蓝霓虹冲突**（禁 `crimson bleed`、霓虹洋红 vs 青）；画面约 90% 区域只用**一种主导色调**，极度克制。
5. **视觉渲染**：描述整体视觉质量与纹理（精细渲染、丰富错综的细节、带细微高斯模糊的柔焦）。
6. **氛围与潜台词**：描述角色"潜台词"与微表情，把动作定格在戏剧性瞬间（`oppressive suffocation` / `no mercy` / `predatory stillness`）；无生命物体描述其状态（宿命感 / 穿透力的注视 / 寒冷疏离）。拒绝僵硬摆拍。

- **条件元素·画面内文字**（仅相关时）：场景出现文字（如屏幕文字）时自然整合，用**引号**包裹要渲染的确切文本，如 `A neon sign in the background reads "DANGER".`。

### key_frame 专节（模式 B · 不套 6 原则）

- `key_frame`**（Nano Banana）是例外**：**不**套用冗长的 6 大核心原则——沉重的电影化文字会让 Banana 忽略 / 对抗 MJ 参考图、导致重绘。优先只用"**插槽标签 + 故事板对齐**"。
- **核心规则**：故事板里的镜头描述就是这张静态图"必须发生什么"（谁 / 哪里 / 动作 / 镜头节奏）的脚本。提示词只需加**最少的路由文本**，让模型以 MJ 元素图为参考、针对该节奏微调——而不是用文字对内容和风格做第二次全面处理。你越详尽地描述期望外观与内容，Banana 越倾向重新生成、丢掉 MJ 风格锁。
- **理想短提示词模式（示例）**：`Reference environment texture Element_Dark_Void_img, and style Element_Glowing_Cube_img.`（然后仅追加故事板要求的内容，如主体位置或 `cube centered, static, push in before`——保持简短。）

### key_element 提示词结构（写元素定义时）

围绕：**主体与身份**（角色 / 道具 / 场景 / 生物是什么；角色含年龄、体型、种族（如指定）、显著特征、声音）→ **特征细节**（优先跨镜必须一致的特征：角色写面部特征 / 妆造 / 服装配饰的材质剪裁颜色状况；道具写形状 / 材质 / 颜色 / 尺寸 / 状况新旧 / 独特标记）→ **氛围情感基调**（紧张 / 忧郁 / 希望 / 宁静 / 不安 / 温暖 / 压抑 / 恐惧 / 怀旧 / 孤立 / 亲密…）。路径二时在主提示词后附 `--sref`（验证每 token 在 0–4294967295、标准化为空格分隔；未设则选一个代码记录并全程复用）。

### 视频提示词 · 参考图命名

先**为每张参考图标记角色**，让 Seedance 正确读取面部与造型：用 `reference_nodes` 传参考图、`{{NodeKey}}` 引用节点。模板：Subject 1 — 面部特征参考 `{{Face_1}}`（头部特写）；发型 / 妆容 / 服装参考 `{{Body_1}}`（全身照）。Subject 2 继续编号。

### 视频提示词 · Seedance 四层顺序（镜头 → 主体 → 空间 → 音频）

按此顺序追加动作 / 动态提示：

1. **镜头**：运动或摄像机 / 剪辑变化（`static → push in`、`cut to new angle`、`orbit`、`pan`）。
2. **主体**：动作与表情（谁做什么、面部神态）。
3. **空间**：位置 / 环境变化（主体或相机相对空间的位置、背景运动、深度 / 布局转换）。
4. **音频**：对话（如有）、音效，及模型缺音乐时的备注（见负面约束）。

- **动作细节**：基于**具体身体部位**（手 / 腿 / 头 / 肩），加**程度**（幅度 / 速度 / 力度，如 `slowly raises one hand`、`snaps head left`、`pushes hard off the ground`）；一个提示词多节拍时，按故事时序列**主要动作 → 次要动作**。
- **多节拍**：工具接受长提示词时，可在单次生成里标 **Shot 1 / Shot 2 / Shot 3** 表示镜头或故事节拍序列。
- **禁逐秒时钟计时**：精确时钟（"0–3 s"、"在 2 s 时…"）**无法可靠执行**——不要按确切秒数硬拆、不写逐秒计划；描述**按顺序发生的事**，而非按时间划分的镜头清单。
- **可选润色**（真人实拍简报时）：可加轻微手持微震 / 细微胶片颗粒，保持从属于上述四层顺序。

### 包装符约定（Seedance 引擎语法）

引擎接受自然语言，这些包装符帮模型区分音乐 / 音效 / 对话 / 屏幕文字：

- **音乐**（描述播放内容）：`(...)`，如 `(fast-paced rock playing in the background)`。
- **音效**：`<...>`，如 `<distant dog barking>`。
- **口述对话**：`{...}`，如 `{Hello, world}` —— 台词不是项目主要语言时，在花括号前标语言，如 `Says in Japanese: {こんにちは}`。
- **屏幕标题 / 章节 / 字幕文字**：`【...】`，如 `【Chapter One: Departure】`。

### cut to 多阶段动作

单镜内高度复杂 / 多阶段动作时，**按顺序**描述序列，用 `cut to` 标签表示过渡（shot A…, cut to shot B…, cut to shot C…）。示例：\
`Shot1: {{image_1}} his hands carefully open a dusty wooden box, with the sound of a soft creak. {{image_1}} His expression is focused and curious. The camera is a fixed shot, and the background attic is static. Shot2: cut to a bright blue light emanates from the artifact inside, casting an ethereal glow on his face and creating long, shifting shadows in the room. {{image_1}} His expression changes from focused to shocked awe as the camera begins a slow zoom in on his face. Shot3: cut to {{image_1}} he looks up with determination, the blue light reflecting in his eyes, as he slightly turns his head to the left to look past the camera. (no dialogue, no music, no subtitles)`

### 三条负面约束（始终写进视频提示词）

- 分镜表明该镜有**单独旁白音轨**时，视频提示词里**不写旁白文本**，避免音频冲突。
- 为防模型加不想要的 BGM，**几乎总是**包含 `no music`。
- 字幕后期加，**始终**包含 `no subtitles`。

## 合成（静音嵌入音频规则）

`composite_video` 按故事板与时间轴顺序组装所有镜头、旁白音轨与 BGM，剪辑就绪后引导用户导出。**若最终镜头没有镜头内对话或旁白，把该镜头 / 视频层的嵌入音频静音**，只依赖设计好的**音频层**（BGM / SFX），这样镜头自带的音效不会与混音冲突。

## 变体与边界（勿用本 skill，改道）

- **纯图片美学（不成片，只出美学静图）** → image-generation。
- **通用多镜叙事短片（非 MJ 美学定调、故事 / 人物 / 对白驱动）** → cinematic-flow。

（本 skill 自足，无源生跨 skill 依赖，故无「配合」声明表。生成基元 = `generate_image_v3` / `generate_video_v3` / `generate_audio` / `composite_video` / `write_file_v2` 等工具调用，非跨 skill 依赖。）
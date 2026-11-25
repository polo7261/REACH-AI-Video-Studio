---
name: life-observed-doc
description: "先拍人不拍城，克制不煽情"
---

# documentary-flow

做**人文纪录短片**——全球国际统一审美、聚焦真实人类生活的观察性影像——时用本 skill。核心是**观察生活而非拍故事**：真实感与人文情绪 > 强戏剧冲突。用首帧设定图作视觉锚点，再以微动态图生视频生成克制运镜的纪录片镜头。

> 本环境适配：GPT Image 2（首帧/元素图）→ `generate_image_v3`（2K）；Happy Horse FirstFrameToVideo（首帧图生视频）→ `generate_video_v3`（首帧驱动路径，720p 起）；ElevenLabs 旁白 / Suno·Mureka 器乐 BGM → `generate_audio`；Final_Video_Spec.md 与结构化文本 → `write_file_v2`；故事板设计 → 分镜阶段内做；video_assembler → `composite_video`；`@资产`/asset 绑定 → `reference_nodes`+`{{NodeKey}}`；会员/积分类无。**叙事/运镜/画面质感/写提示词工艺全部内联本 skill，不依赖外部工艺 skill，无源生跨 skill 依赖。**

## 一、流程（分阶段暂停确认，不得一次性跑完）

1. **阶段 0 · Final_Video_Spec**：`write_file_v2` 建 Final_Video_Spec.md，锁：片名、题材地域、画幅比例、目标时长、视觉风格、输出语言（见二）。
2. **阶段 1 · 参考素材解析**（若用户上传参考图/视频）：提取信号供下游用（见三）。
3. **阶段 2 · 故事板**〔暂停〕：出关键元素、镜头列表、音频层（见四、五、六）。故事板就绪后**扫描上下文**，查找用户已提供或此前生成、与故事板条目匹配的资产（元素图/BGM 等）；对每个匹配项，在生成前先通过 `reference_nodes` 把资产**绑定到对应故事板槽位**，避免重复生成用户已有内容。呈现确认。
4. **阶段 3 · 设置元素**〔暂停〕：用户已上传元素资源（角色图/参考角色）→ 直接绑为对应 key_element 的资产；否则为所有元素 `generate_image_v3` 生成图（见七）。
5. **阶段 4 · 首帧图**〔暂停〕：为每个镜头 `generate_image_v3` 生成 start_frame，须与镜头描述景别/光线/主体姿态一致，作视觉锚点（见七、八）。
6. **阶段 5 · 镜头视频**〔暂停〕：参考步骤 4 首帧图，以 start_frame 作首帧输入 `generate_video_v3` 生成微动态视频（见八、九）。
7. **阶段 6 · 音频层**〔暂停〕：`generate_audio` 生成旁白（如有）/ BGM（见六、七）。
8. **阶段 7 · 组装交付**：`composite_video` 完成全片时间线组装（见十）。

**依赖顺序**：阶段 2→0；3→2；4→2；5→4；6→2；7→5,6。
**暂停节点**：在故事板完成、元素图/首帧图完成、视频完成、音频生成后各暂停，等用户确认再继续。
**已有素材优先**（主要影响阶段 3–5）：填充生成内容前，先绑定并分配到合适故事板位置，不重复生成用户已提供的内容。

## 二、Final_Video_Spec 建立指南

1. **片名**：契合"人文纪录片"调性，避免过度商业或浮夸的命名。
2. **题材地域**
   - **地域限定范围**：引导用户在以下区域中选择——亚洲、非洲、中东、南美、东欧、东南亚、海岛国家、发展中国家。
   - **题材核心限制**：题材必须聚焦"**真实的人**"与"**普通人的生活**"，**拒绝"城市宣传片"**。
3. **画幅比例**：推荐 16:9 横屏，或纪录片常见的 2.35:1 宽银幕。
4. **视觉风格（四参考锁定 + 避雷清单）**：锁定为"像真实摄影师长期驻扎拍摄"、"像奥斯卡/国际电影节纪录片"、"Netflix 纪录片风格"或"国家地理式观察影像"。**明确"不做"的风格（避雷清单）：严禁 AI 感、商业广告感、强戏剧感、网红风。**
5. **画面质感要求**
   - **空气感**：灰尘、水汽、潮湿、热浪、风。
   - **光线限定**：仅限自然光（晨光、黄昏、阴天、窗边光）。
   - **保留不完美**：允许并刻意保留轻微失焦、曝光波动、真实混乱感。

## 三、参考素材解析规则

若用户上传参考图片或视频，提取以下信号供下游使用，**输出结构化描述，不做主观评价**：
- 主体身份与外貌特征；
- 场景地点与环境氛围；
- 光线条件（方向 / 色温 / 质感）；
- 画面色调与饱和度风格。

## 四、叙事规范（storyboard 核心）

### 4.1 核心叙事理念：观察生活，而非"拍故事"
- **去戏剧化**：摒弃强戏剧冲突、商业广告式的剧情设计。重点不在"讲一个起承转合的故事"，而是呈现"真实世界的人类生活"。
- **偶发感**：场景和事件不应有"导演刻意安排"的痕迹，必须营造"摄影师长期驻扎时偶然观察到"的自然状态。
- **全球纪录片统一审美**：如 Netflix 纪录片或国家地理式观察影像，打造全球观众都能理解共情的人文叙事，避免刻板的单一地域风（纯网红风、纯欧美风）。

### 4.2 叙事主体与切入点：先拍"人"，不拍"城"
- **拒绝宣传片逻辑**：永远不要把"城市面貌"或"宏大景观"作为首要表现对象——这不是城市宣传片。
- **聚焦真实人类**：剧情永远从"人"切入，通过普通人的真实生活状态折射其背后的文化与环境。

### 4.3 剧情细节与动作设计（最易共情的描写点）
撰写剧本与场景描述时，着重刻画以下细节动作，而非宏大事件：
- **聚焦手部劳作**：做饭、缝纫、洗衣、写字、手工劳动。
- **人物背影与状态**：多用"背影"作主视觉——比直接展现正脸更具高级感和故事留白感。
- **日常微小动作**：点烟、喝茶、发呆、看窗外——用这些无特定目的的"小动作"构建时间流动的真实感。

## 五、按地域划分的场景/题材规划库

为不同发展中国家或地区规划剧本时，直接选用以下最能体现当地原生人文气息的场景和事件：
- **亚洲题材**：清晨的早餐摊、老茶馆里的闲谈、熙熙攘攘的传统市场、原生态的渔村、老旧的铁路边。
- **非洲题材**：黄昏尘土下的归途、热闹的集市、奔跑的孩子、雨季的日常、传统的手工劳动。
- **南美题材**：随性的街头音乐表演、充满生活气息的老城区、海边日常、街头/土路足球场、夜市的烟火气。
- **中东题材**：阳光穿透的传统市场、专注的手工艺制作过程、虔诚的祈祷时刻、沙尘环境下的生活常态。

## 六、关键元素与音频层设计

### 6.1 关键元素设计
- 优先设计**人物元素**（年龄、外貌、着装、正在做的事）和**场景元素**（地理环境、时段、光线条件、空气质感）。
- 道具元素只在对多个镜头一致性有实质影响时才单独建立。
- 用户提供参考素材时，元素描述必须与参考内容一致，不得矛盾。

### 6.2 音频层设计
- **BGM（可选）**：若使用，选择极简器乐或无调性环境音景；**禁止流行音乐节奏**。
- **不以对白驱动叙事。**

## 七、分镜镜头设计原则（★ 观察式纪实工艺核心）

- **时长**：每个镜头 **6–12 秒**，**不做短于 5 秒**的镜头。
- **观察性叙事**：镜头不"设计故事"，而是"偶然看见生活"。优先拍手部劳动、背影、微小日常动作（点烟、喝茶、发呆、看窗外）；避免正面表演式构图。
- **运镜极简（按优先级排序）**：一个分镜只描述一个镜头。
  1. 固定镜头（最推荐）
  2. 微弱手持（仅呼吸感 / 轻微漂移）
  3. 极慢推进 或 极慢横移
  - **禁止**：旋转、快速推拉、无人机飞行、炫技运镜、切镜。
- **每个镜头描述必须包含**：
  - **Scene**：引用场景元素 ID，说明时段与光线；
  - **主体动作**：人物正在做的微小动作，以肢体和神态为主，**无需台词**；
  - **摄影语言**：景别（特写 / 中景 / 远景）+ 运镜类型 + 焦点策略。
- **画面质感**：
  - **自然光优先**：晨光、黄昏、阴天散射光、窗边侧光；禁止人工补光感。
  - **空气感必须体现**：灰尘、水汽、热浪、潮湿、轻雾中选一种写入镜头描述。
  - **允许不完美**：轻微失焦、曝光轻微波动、人物短暂停顿均为真实感加分项。
- **色调体系**：
  - 低饱和、高层次感：高光柔和不过曝，暗部有细节不死黑，肤色真实。
  - 参考色彩风格：**Kodak Vision3 / Fuji Eterna / ARRI Alexa Natural**。
- **视频中的声音设计**：市集噪声、风声、雨声、街道声等。

## 八、首帧提示词写作规范（`generate_image_v3`）

**核心逻辑**：聚焦"决定性瞬间"的捕捉、胶片色彩质感、真实的光影与空气感。**摒弃任何运镜和节奏词汇。**

**万能公式**：
> [画面主体与微小动作] + [环境与空气感] + [光线状态] + [摄影机语言与景别] + [色彩体系与胶片质感] + [核心精神关键词与大师参考]

**核心模块与词汇库**：
- **主体与微动作**：人物背影 / 抽烟的双手 / 凝视窗外 / 停顿的发呆瞬间。
- **环境与空气感**：弥漫的灰尘 (dusty air)、清晨的水汽 (morning mist)、潮湿感 (dampness)、风吹动衣角 (wind blowing)。
- **光线状态**：自然光 (natural light)、窗边柔和侧光 (soft window light)、阴天漫反射 (overcast diffused light)。
- **摄影语言**：Medium shot (中景) / Close-up (特写) / 极简构图 / 留白 (negative space)。
- **色彩体系（原样直出）**：Kodak Vision3, Fuji Eterna, ARRI Alexa Natural, low saturation, soft highlights, detailed shadows, real skin tone.
- **风格与大师参考**：Magnum Photos, Leica Documentary, National Geographic, 是枝裕和 (Hirokazu Kore-eda), 贾樟柯 (Jia Zhangke).

**示例（方法级模板，替换主体/地域即可复用）**：
> (EN) A medium shot of an old man's weathered hands rolling a cigarette, sitting in a dimly lit traditional tea house. Morning mist and dust particles floating in the soft window light. Kodak Vision3 film stock, low saturation, soft highlights, real skin tone. Magnum Photos style, Leica Documentary, observational, honest, real, quiet, timeless. Hirokazu Kore-eda aesthetic.
> (ZH) 中景，一位老人在昏暗的老茶馆里卷烟的沧桑双手。晨雾和灰尘颗粒在柔和的窗边光线中漂浮。柯达 Vision3 胶片质感，低饱和度，高光柔和，真实的肤色。马格南摄影风格，徕卡纪录片，观察性，诚实，真实，安静，永恒。是枝裕和美学。

**首帧图与视觉锚点**：首帧图须与故事板镜头描述的景别、光线、主体姿态一致，作为视频生成的视觉锚点。若用户已上传参考图（人物/场景），将其注册为锚点（`reference_nodes`）并绑定至对应元素或镜头槽位，优先用于替代生成（ImageToImage 路径）。

## 九、视频提示词写作规范（`generate_video_v3`，首帧驱动）

**核心逻辑**：聚焦"时间的流动"、"极慢的节奏与运镜"、"环境的微小变化"以及"长镜头观察感"。以对应镜头的 start_frame 作首帧输入。

**万能公式**：
> [极其克制的镜头运动] + [主体持续的微小动作] + [环境与光线的微小流逝/变化] + [色彩体系] + [纪录片节奏与电影级参考] + [核心精神关键词]

**核心模块与词汇库**：
- **镜头运动（必须克制）**：Fixed camera (固定镜头) / Slight handheld breathing (微弱手持呼吸感) / Extremely slow push-in (极慢推进) / Extremely slow pan (极慢横移)。
- **动作与环境流逝**：持续的微小动作 (continuous subtle movement) / 光影随时间缓缓移动 (light shifting slowly) / 持续的微风 (continuous gentle breeze)。
- **节奏与剪辑指令**：Long take (长镜头) / Slow pacing (慢节奏) / No fast cuts (禁止快剪) / Breathing space (呼吸感留白)。
- **色彩体系**：Sony Venice Documentary LUT, ARRI Alexa Natural, cinematic color grading, cinematic shadows.
- **视频风格与参考**：Netflix Documentary (Chef's Table, Our Planet), Oscar Documentary (Nomadland, Honeyland), 侯孝贤 (Hou Hsiao-hsien) pacing.

**示例（方法级模板）**：
> (EN) Fixed camera with slight handheld breathing. A slow long take of a South American woman washing clothes by the river. Her back is to the camera. The damp morning air slowly blows her hair. Natural overcast light with subtle environmental shifts. ARRI Alexa Natural, Sony Venice Documentary LUT, low saturation, soft highlights. Cinematic pacing, breathing space, no fast cuts. Nomadland and Honeyland style, Netflix documentary vibe, observational, slow, human, quiet, timeless.
> (ZH) 固定镜头带有微弱的手持呼吸感。一个缓慢的长镜头：一位南美妇女在河边洗衣服，背对镜头。潮湿的晨风缓缓吹动她的头发。自然的阴天光线，带有微妙的环境变化。ARRI Alexa Natural，索尼威尼斯纪录片 LUT，低饱和度，高光柔和。电影级节奏，呼吸感留白，无快剪。无依之地与蜂蜜之地风格，Netflix 纪录片氛围，观察性，缓慢，人文，安静，永恒。

## 十、素材生成与失败处理

- **元素图/首帧图**：`generate_image_v3`，2K；首帧图作视觉锚点（见八）。用户已上传参考图 → 注册 `reference_nodes` 绑定，优先替代生成。
- **镜头视频**：`generate_video_v3`，720p 起，以对应镜头的 start_frame 作首帧输入（FirstFrameToVideo 意图）。
- **音频层**：旁白（如有）`generate_audio`；BGM `generate_audio`，风格描述为极简器乐 / 环境音景，**不生成歌词类音乐**。
- **失败处理**：若视频生成失败，**优先以同参数在同一路径重试**，不擅自切换到风格差异大的替代路径；重试仍失败则**停止并告知用户**，不静默降级换模型。

## 十一、剪辑与输出（`composite_video`）

**节奏原则**：
- **长镜头优先**，保留完整的时间流动感；**不为追求"有趣"而剪短镜头**。
- 镜头间可用 **0.5–1s 的黑场或声音延续过渡**，制造呼吸感。
- **禁止快剪、音乐卡点、特效转场、TikTok 节奏。**

**音画关系**：
- BGM（如有）音量**低于视频层声音**；淡入淡出，不抢画面。
- **不做强制音画同步**；画面与声音各自自然流动。

## 相关

- **边界（勿用本 skill，改道）**：强戏剧叙事/起承转合短片 → cinematic-flow；城市记忆/旧街区具体人物空间（80/20 平叙+高动态配比）→ city-memory-film；东亚文艺片（情绪驱动/全片平叙微动态/声画分离）→ east-asian-mood-film；传统工艺纪录（文献解析→六格分镜矩阵图→逐组 15s）→ craft-documentary；名导纪实风格（贾樟柯式）→ auteur-style-director 路由。
- 本 skill 自足内联，**无源生跨 skill 依赖，不设配合表**。
## 一套仙侠底质 + 一句可选主色(阶段 1 提炼,全片统一)

全片一套渲染底质(极致宏大尺度、含建筑地点的白玉超巨构、镜面对称、电影级空气透视),**场景图不套用风格种子,靠同一段共享风格描述文本反复套用来保持统一**;**全片影调最终以用户确认的那组场景图调性为准**,人物图/道具图/视频生成时都需向已选场景图的色彩基调看齐。从剧本情绪再提炼一句主色附到场景图 prompt。

- **共享风格描述(场景与 Seedance 通用基底,任何地点都适用,精简版,中文)**:`东方神话巨构主义电影画面。晴朗淡青蓝天空,云层保持中性偏白,右侧可有克制的淡金逆光轮廓,不做整体暖橙滤镜。极致远景或强透视构图,人物或近景元素仅占画面高度0.3%-0.8%。近景、中景、远雾、极远景四层空气透视,体积云,电影级写实质感,HDR,8K细节,结构可信、重量真实,尺度辽阔。`
- **建筑子句(仅当该地点剧本设定含建筑/宫阙/殿宇时才追加,不含建筑的地点绝不套用)**:`一座汉白玉超巨构建筑或天宫从云海中升起,建筑占画面高度60%以上甚至越出边缘;巨墙、深色木构梁架、层叠斗拱、宽阔飞檐,鎏金克制、不做满金。`
- **场景图额外追加**:`85-100mm中长焦压缩空间(或50-70mm强烈一点透视,视构图需要二选一)`,接共享描述(+ 建筑子句,如适用)后,再接该地点自身的地貌/环境细节(如冰原、竹林、荒漠等,见场景清单描述)与主色。**室内场景**(宗门大殿内部、洞府内部等属于"含建筑"类)沿用同一套光线/色调/电影质感语言,尺度感按该室内空间本身的规模呈现,不强求做到"超巨构"。
- **Seedance 前置风格句额外追加**:`真人实拍电影质感,广袖服装随风飘动,战斗/情绪高潮处慢镜升格,人物在巨构长廊或大殿中行走时保持画面中极小比例的全景构图,镜头运动流畅但镜头切换只用硬切、不出现任何转场特效。`,放在 Seedance prompt 第一句,接共享描述之后。
- **可选主色倾向(接底质描述后,任选一句或另写)**:仙气冷调「淡玉色、月白、雾青」;天火暖调「熔金、赤色雷光、深紫风暴云」;青绿山水「石绿、石青、暖金夕阳」;魔道幽冥「血色、玄黑、病绿瘴气」。

---

## 固定种子与出图规格(速查)

- **场景/影调图 = Midjourney V8.2**(**必须指定该版本;Midjourney V8.2 无法连接时唯一备用为 V8.1,不用其他版本或其他工具**),**不套用风格种子**(不加 `--sref`/`--profile`),全景无人无道具、零文字。**每地点出 1 组 4 张**,四选一。Prompt = 共享风格描述(通用)+ **该地点含建筑才追加建筑子句,不含建筑绝不追加** + 场景图额外追加 + 该地点自身地貌描述 + 主色 + 画幅要求(用文字描述,如"16:9横构图")+ 精简负面词(用文字描述写在正文里,不用 `--no` 前缀;不含建筑的地点不需要"不要普通小宫殿代替"这类建筑相关负面词,按场景实际情况取舍;通用负面词如不要大人物、不要浓雾遮挡、不要整体橙色滤镜、不要文字水印logo)+ **尾串仅保留** `--v 8.2`(V8.2 不可用则改 `--v 8.1`,不加其他 flag)。**整条 prompt(描述句+负面词+尾串)≤ 1024 字符**,超了只精简描述句,不动关键负面词与尾串;建筑描述仅在需要时出现;**一致性靠每次完整套用同一段共享风格描述文本 + 向已选场景图调性对齐**。
- **人物+三视图 = Seedream 5.0 Pro**(人物专用):所有角色一次性出——每角色**一张 16:9、单一纯白底连续画布**,内含 4 套正面全身造型(**必须全身入镜,不得半身或大头**;整套搭配+发型发饰明显不同,禁止只换袍色其余不变),**四套之间不设分隔线/边框,视觉上是一整张连续白底照片而非拼接的四张图**→ 一次性四选一确认 → 选定图作参考图输入只补生侧/背,出**16:9 单张纯白底三视图,排版按有无原脸分两种**:**无原脸(Case1 无脸/Case3)**→ 左侧为正面大头特写(近景头肩)+ 右侧全身三视图(正面/侧面/背面并排),整张连续无拼接缝,脸保留可见(脸即身份);**有原脸参考(Case2)**→ **只出全身三视图(正面/侧面/背面并排),不含左侧大头特写面板**,头部区域用**圆形贴纸完全遮住**,**右下角小字标注**(按用户语种)"人脸单独提供·仅供服装参考",身份以原脸图/视频在 Seedance 端锁定。**四选一渲染档(必叠,强调电影级而非短剧感)**:反油皮肤 `matte realistic skin, visible pores, no retouching, subtle film grain`;电影感 `cinematic film still, filmic contrast, luminous colour grade, movie-grade cinematography`;电影级选角与妆造 `a real film-actor face with dignified screen presence, NOT a modern idol/K-beauty/short-drama influencer face, no glass-skin filter, no heavy web-drama makeup, natural film-grade styling`;排版正向词补充 `single seamless white background canvas, no panel dividers, no borders between poses, continuous studio photograph, not a collage`。维护 **cast sheet**。Seedream 无 `--sref`,一致性靠角色卡+参考图。
- **道具锚点图 = Lib Image**(仅需跨镜锁定的核心道具才出,**独立生成,不引用人物或场景图作参考**,直接依据道具卡文字描述生成):16:9 纯白底单张连续画布,内含道具正面全图+三视图细节(正面/侧/背,法宝可加 1–2 处纹样/机关特写贴角),无分隔线拼接感。排版指令(i2i,英文基底):`pure white seamless background, product-style photography, single continuous canvas with no panel dividers; main panel shows the exact prop large and centred (front view); to the right, smaller side and back views; add close-up insets for intricate details if present; replicate every detail 1:1, do not redesign; no text, no watermark`。维护 **道具单(props sheet)**:道具名/归属角色/【锁定/不锁定】/三视图链接。
- **视频 = Seedance 2.5(强制,不得替换成其他版本)**,单次最长 **30s**,内部镜头切换只用硬切、不生成任何转场特效或字幕。输入 = 该段涉及地点的场景图(跨地点多张、单地点一张,含室内场景)+ 每角色**同一张三视图**(锁脸+服装)+ 每件锁定道具**同一张三视图**(不锁定道具不出图,靠文字带出)+(有原脸时)原脸图作身份锚点。

---

## 流程(逐阶段暂停确认)

### 阶段 0 · 开拍前问询卡(一次性问完,不逐条停)

一张卡问 4 项(**角色造型、道具、口语语言不在此问,阶段 1 解析剧本自动提炼**):

1. **剧本/文本**:完整剧本?一句话想法(据此草拟)?还是完全没有想法?上传后阶段 1 自动解析人物/道具/场景/语言。**若完全没有剧本/想法,先问用户想要的风格基调**(如仙侠爱情、仙侠打斗/热血、仙侠悬疑/复仇、仙侠成长/顿悟、仙侠家国大义等,可多选或另写),**再据此基调 + 用户补充的只言片语草拟仙侠短剧本**;若已有一句话想法则直接据此草拟,不必再问基调。
2. **字幕**:要/不要,要则选简体/繁体/英文/双语(阶段 6 直接按此加,不再问)。
3. **画幅**:16:9/4:3/1:1/9:16 平等列出、不作推荐,必须用户自选。
4. **时长**:30s/60s/90s/自定义(填空,如 150s→按 30s 向上取整分 5 段)。

> **分辨率不问,默认 720p**。草拟剧本(人物/门派/场景/节拍反转/声音分工,贴合已定风格基调,可掺渡劫飞升、法宝认主、宗门大比、身世之谜、天劫倒计时、魔道入侵、转世前身、灵根觉醒等钩子)→用户确认→进阶段 1。

**角色造型三 Case(阶段 1 出人物清单时才问,不在此问)**:Case1 有造型参考图→参考图+补 spec 生成,无原脸,三视为左大头特写+右全身三视图;Case2 有人脸无造型→人脸参考+补 spec,原脸带入 Seedance 锁脸,**三视只出全身三视图(不含大头特写面板),头部圆形贴纸遮挡+右下角小字标注**;Case3 都没有→按剧本身份/门派/性别补 spec 直接生成,无原脸,三视为左大头特写+右全身三视图,脸即身份。三 Case 均要求电影级选角与妆造,避免短剧网红脸。

**仙侠古风服装语言(补 spec 时用,不锁朝代,按性别)**:女 `flowing wide-sleeve hanfu or Taoist robe, silk ribbon sash drifting, layered cloud-shoulder cape, jade or gold hairpin, flowing high bun`;男 `Taoist/cultivator robe with wide sleeves, waist sash with jade pendant or sword tassel, topknot with jade or wooden hair crown`;共通 `real silk/brocade/gauze textures with natural drape, no contemporary fabric/cut/accessories`。身份门派可微调配色纹样(魔道偏暗、正道偏素雅明亮),不改造型基线。

### 阶段 1 · 剧本解析 + Final_Video_Spec

读取全文解析为叙事结构+人物/道具/场景三表,**输出表格停一次,不生成任何图片**。

- **去重合并**:同一实体反复出场合并成一条,补充描述并入最终描述。
- **信息不足必须停下问,不能瞎补**:外观描述缺失的条目标记 **⚠️信息不足**,列出需补充的具体问题,等用户补充后才进入该条设计;"完整"条目不受影响。
- **输出格式**:先报"识别到 X 人物/Y 场景/Z 道具",附叙事结构一句话(节拍数按时长:30s 取 1–2 拍,60s 取 2–3 拍,以此累加);人物表(编号/姓名/出场场次/身份门派关系外观/状态)、道具表(编号/名称/归属/出场/外观/锁定判断/状态)、场景表(编号/名称/出场/室内或室外/**是否含建筑**/环境描述/是否专用空镜/状态)。**场景表须包含剧本里出现的全部室内场景**,不因为室内不易呈现巨构感而省略。**"是否含建筑"按该地点剧本描述判断**:宫阙、殿宇、长廊、洞府等填【含建筑】,荒野、冰原、山川、竹林、海洋等纯自然环境填【不含建筑】——决定阶段 3 出图时是否追加建筑子句。
- **道具锁定判断**:法宝本命法器、关键信物、反复出现兵器默认【锁定】;一次性摆设、群体背景默认【不锁定】;拿不准默认不锁定。
- **口语语言**:默认剧本本身写作语言;混用/不明确才追加一句询问。
- **人脸参考图问题**(此处问,非阶段0):对人物清单问"有没有想指定的人脸参考图/视频?没有则按剧本+仙侠服装语言原创设计(电影级选角),首版确认后作后续一致性基准"。
- **旁白/心声独白/对白逐句提炼**:与三表一并展示——旁白(第三人称说书人,交代背景/因果/时间跳跃)、心声独白(第一人称情绪)、对白(标说话人,冗长台词精简为强节奏短句需说明确认)、每拍声音分工(旁白/独白/对白/叠用)、情绪反转基调、一句主色倾向。
- **分批处理**:人物/道具/场景任一类超 8 个自动分批,每批≤8,按首次出现顺序,表格下方注明分批计划;**影响阶段 2/2.5/3 节奏**——每批做完停一次问是否继续,除非用户说明不用逐批确认。
- **Final_Video_Spec**:画幅(阶段0第3问)/分辨率(默认720p)/时长(阶段0第4问,每30s一段)。

> 暂停确认(三张表+状态标注+人脸参考图问询+spec 一次性一起停)。

### 阶段 2 / 2.5 / 3 · 角色·道具·场景资产生成(三线并行发起,确认顺序不变)

> **三条生产线(人物/道具/场景)可以同时发起生成调用以节省时间**,互不依赖、互不参考;但**给用户看结果与逐一确认的顺序仍按 2→2.5→3 进行**,不因为并行生成就打乱确认节奏。各类超 8 个均按阶段 1 分批计划走,每批做完停一次问是否继续。

**阶段 2 · 角色设计(Seedream 5.0 Pro)**:每角色写角色卡 → 一起出全部角色四选一造型图(**16:9、单张纯白底连续画布,4 套均须全身入镜**,差异明显,电影级选角基线,无拼接缝)→ 一次性四选一确认 → 选定图作参考图输入只补生侧/背,一起出全部三视图(16:9 单张纯白底无拼接缝;**无原脸角色**=左大头特写+右全身三视图;**有原脸角色**=只出全身三视图、头部圆形贴纸遮挡+右下角小字标注)→ 逐项核对脸/服装,漂移则以选定图重补,反复漂则拼版 → 一次性确认全部三视。维护 cast sheet;换装再出新一版。

> 四套须整体搭配+发型都拉开区别(如①正式道袍高发髻 ②战甲束发 ③素色襦裙垂发簪花 ④华丽礼服复杂发饰),禁止只换袍色其余不变;人物长相与妆造须走电影质感,避免网红脸/短剧感;**画面必须是单张连续白底,不能出现分栏/边框/拼接的四宫格或三宫格感**。

**阶段 2.5 · 道具设计(Lib Image,仅锁定道具需要,与人物图/场景图完全独立)**:【不锁定】道具跳过,留到分镜/场景阶段文字带出;【锁定】道具逐样出图——写道具卡(材质/纹样/尺寸/关键机关)→ **直接依据道具卡文字描述生成,不引用任何人物三视图或场景图作参考**→ 一次性出全部锁定道具单张纯白底连续画布(正面图+三视图细节,无拼接缝)→ 一次性确认(核对材质纹样比例)→ 偏差则以正面图重生侧/背。维护道具单。中途新增道具随时补出。

**阶段 3 · 场景影调图(Midjourney V8.2,不可用则 V8.1,不套用风格种子)**:按场景清单一起出(不要一场出完再出下一场):每地点(含室内场景)**各出 1 组 4 张**,**按场景表"是否含建筑"取用对应模板**——【含建筑】接共享风格描述+建筑子句+该地点自身细节;【不含建筑】只接共享风格描述+该地点自身地貌细节(荒原、冰川、竹林等),**绝不强行套用建筑子句**;接主色+画幅文字描述(如"16:9横构图")+仅 `--v 8.2`(不可用则 `--v 8.1`)的尾串,**prompt 保持精简(≤1024 字符)**。**场景图按「地点」出全景,一个地点一组、跨镜跨段复用,一段视频可以涉及多个地点、不限制每 30s 只对应一个场景图**;不为特写/局部单独出图,这些交 Seedance 在同一全景上取景;组数=去重后的地点数(含室内)。专用空镜地点在场景清单特别标注。**全部出齐 → 一次性暂停让用户逐地点四选一**(标明 1 左上/2 右上/3 左下/4 右下)→ 收齐才进阶段 4,严禁未经四选一就往下走。**该场景图确定后的调性即为全片影调基准**,后续人物/道具/视频生成都需向其色彩质感看齐。\
**全部出齐 → 一次性暂停让用户逐地点确认**(满意则通过;不满意可指出问题重新生成该地点这一张,不做四选一)→ 收齐确认才进阶段 4。

### 阶段 4 · 分镜表格(生视频前必出、需确认)

**一次性出全部分镜表**(按段数,不要一段一停),每段一表,列:镜号/时长/景别(空镜/巨构人物运镜/近景特写/其他)/画面(调度表演构图)/**道具锚点**(该镜用到的道具单编号,用于绑定道具三视图)/**场景锚点**(该镜所在地点的场景表编号,用于绑定场景图)/声音层(旁白·独白·对白,原文+语气)/运动。**转场统一为硬切,不设转场列**。"景别"列填四选一:纯空镜/巨构人物运镜/近景特写/其他——**每段至少各出现 1 次纯空镜与 1 次巨构人物运镜,二者不可互相替代;声音层为"对白"的镜头景别默认填近景特写**(展现说话角色的表情口型,不默认用空镜/巨构人物运镜表现对白瞬间),其余镜头按剧情需要在近景特写与大远景间交替,避免整段被大远景堆满。空镜行画面列只写景观调度、声音层可留白仅环境音效、道具锚点留空;巨构人物运镜行需写明人物在长廊/大殿/天桥中的具体调度与占比。\
表格下方附**连戏 bible**(不进表):角色身份门派造型手持道具/180°轴线与站位/场景主色光效时辰/当前节拍情绪反转/多段时尾帧→头帧衔接。\
每段每 30s ≥3 镜、至少 1 空镜、至少 1 巨构人物运镜;逐句记录口语原文供阶段 6 做字幕。

> **暂停确认(一次性)**:全部分镜表+造型图+三视图+道具图+场景图一起停。**分镜表一次性全出只停一次;视频(阶段5)相反——逐段生成逐段确认**。

### 阶段 4b · 多段尾帧续接(60s+ 关键机制,逐条生)

每生完一条 seg_n → 停下等确认 → 抽尾帧解析(站位/表情/光线/景别/道具状态)→ 按分镜声明的接缝模式生 seg_n+1。接缝模式:**(A)连续动作**——尾帧作起始帧无缝续上;**(B)换场**——尾帧仅作连戏参考(角色/服装/道具/色板/光线一致),新构图,以**硬切**相接(不用任何风格化转场特效)。

### 阶段 5 · Seedance 2.5 视频(强制该版本,每段一条 30s,逐条生)

prompt 结构:①前置风格句;②**组装**——喂该段涉及地点的场景图(按分镜"场景锚点"取用,含室内场景)+ 每角色三视图(锁脸锁造型,不再用四选一图)+ 每件锁定道具三视图(按分镜"道具锚点"取用,不锁定道具靠文字带出)+ 有原脸时原脸图另作身份锚点,写明"脸与造型取自三视图、道具形制取自道具三视图";③**分镜**:`Shot1…hard cut to Shot2…`,一条连续 30s、镜数达标、至少 1 空镜 + 至少 1 巨构人物运镜,**镜头切换只用硬切,绝对不允许出现叠化/交叉溶解/淡入淡出等任何转场动画或特效画面,没有例外**;④**口语层**:按该镜声音层分工填入——旁白/独白(无需对嘴)、对白(标说话人、口型同步),提示词按用户语种、台词填剧本原文;⑤**运动**(含巨构人物运镜、对白近景与战斗专属关键词,按每镜景别对应选用):`sweeping wide-angle and aerial epic vista shots, two tiny figures walking along a vast palace corridor or hall high above the clouds occupying a very small fraction of the frame, medium close-up or close-up on the speaking character with the vast background softly blurred during dialogue, flying-sword or floating traversal within a single continuous shot, camera moving through drifting mist as part of one shot, fast whip-pan between combatants with motion blur, low-angle shot conveying dominance, speed ramping between slow-motion and real-time at the moment of impact, close tracking shot following rapid close-quarters combat, camera pushes back sharply as a shockwave of energy erupts, glowing spirit-qi and sword-qi trails, orbiting camera during power reveal or combat exchange, high bird's-eye shots`;⑥**音频+文字规则**:正面写旁白/独白/对白+场景音效;负面追加标准负面词库(已覆盖 BGM/字幕/转场特效/人潮/现代元素等)。\
**表演**:逐镜≥1 表情+1 动作,按剧本情绪反转赋予,电影级表演质感。**通用治僵硬(每镜加)**:`natural subtle atmospheric sway, breathing on wide/close shots, micro head movement, natural blink, expression shifting per scene emotion, robes/sleeves/ribbons/hair/mist drifting subtly`。

> **分段生成+强制确认门**:一段一段生,每段生完必须停下等确认才生下一段,严禁不经确认连续生。\
> \*\***旁白/独白兜底**:若模型对无对嘴 VO 支持不稳,退回装配阶段做 TTS/录音叠加,其余规则不变。

### 阶段 6 · 装配

1. **顺接**:各段以**硬切**拼接,**绝对不允许出现叠化/交叉溶解/淡入淡出等任何转场特效,没有例外**;片段已含人声+音效、无 BGM、无转场画面。
2. **合成前一步**:①**加字幕** `add_subtitle`——按阶段0已确认语种直接加(可编辑叠加层,不烧进帧);**样式固定**:纯白字、**无描边(不加黑边/无 outline/stroke)**、字号 **28px**、**单行不换行**(超长台词需精简至单行能容纳的长度,精简方式同阶段1台词精简原则)、字体 **思源宋体**(Source Han Serif,衬线体;服务器无 SimSun 时以此作为最接近的替代字体);②**铺国风配乐**——古筝/箫笛/编钟/恢弘弦乐或空灵吟唱,随节拍起伏,只描述风格不指定具体曲目,音量让人声清晰;③**叠图**——片名/时间戳/credits/logo PNG(不烧进生成画面)。
3. **合成导出**:压平合成为成片。

---

## 参考数据

### 镜头词汇表(转场统一为硬切,不再单列转场词条)

镜头用途关键词极致远景巨构(尺度对比)交代天地规模(红线①必用)`extreme wide/aerial shot, colossal white-jade megastructure rising from cloud sea, figures at 0.3%-0.8% frame height`巨构人物运镜(强制,区别于空镜)人物在长廊/大殿中行走,占比极小`wide static or slow tracking shot, two small figures walking along a vast palace corridor high above the clouds, figures occupy a tiny fraction of the frame`对白近景/特写(强制,平衡大远景占比)角色说对白时的默认景别`medium close-up or close-up on the speaking character, natural eye level, shallow depth of field with the vast background softly out of focus, clear focus on facial expression and lip-sync`甩镜对切(战斗专属)攻防双方快速切换,增强速度感`fast whip-pan between the two combatants, motion blur trailing the camera move, sharp reaction cut`低角度压迫仰拍(战斗专属)展现气势压制/强者姿态`low-angle shot looking up at the character, sense of dominance and power, dramatic sky or architecture backdrop`速度渐变(战斗专属)同镜内速度忽快忽慢强化打击感`speed ramping within a single continuous shot, shifting between slow-motion and real-time speed at the moment of impact`近身缠斗跟拍(战斗专属)贴身打斗的连贯跟随`close tracking shot following rapid close-quarters combat, camera weaving with the fighters' movement, controlled dynamic camera motion`冲击波推镜(战斗专属)剑气/法力爆发的冲击力`camera pushes back sharply as a shockwave of energy erupts, dust and mist blown outward, impact-driven camera shake`一点透视甬道/天桥极致纵深感(标志性)`strong one-point perspective corridor or sky-bridge, vanishing point composition, repeating architectural elements receding into distance`镜面对称/倒影世界宫阙回廊/仙台错觉(标志性)`reflective floor or still water, architecture echoed by inverted reflection below`御剑凌空/凌波运镜轻功/御剑移动(同镜内运镜)`flying-sword or floating traversal within one continuous shot, camera gliding alongside subject`云雾穿梭(运镜非转场)同一镜头内揭示下一处景物`camera moves through drifting mist within a single continuous shot, revealing more of the scene`剑气/灵气光效特写法力/战斗爆发`close-up glowing sword-qi or spirit-energy trail, particles swirling`慢镜升格战斗/情绪/渡劫高潮`slow-motion, robes and hair flowing dramatically`环绕运镜身份揭示/法力觉醒`orbiting camera as energy erupts around subject`俯瞰镜头天地辽阔/宗门全景`high bird's-eye establishing shot`中长焦压缩空间空间压缩、层次堆叠`85-100mm compressed telephoto perspective, layered atmospheric depth`

### 节奏 → 每 30s 镜数(硬底线,镜头切换一律硬切)

节奏镜数说明宏大空镜2–3(下限,须含空镜+巨构人物运镜)长镜头+慢摇;硬切叙事推进4–6对白/独白以近景特写为主,穿插大远景交代环境;硬切冲突/反转爆发6–8(取上限)甩镜对切+低角度压迫+速度渐变+冲击波推镜+近身缠斗跟拍,至少交替 3 种;硬切混合4–5空镜与近景交替;环绕运镜+硬切

> 每 30s 不得少于 3 镜(唯一例外:用户明确点名一镜到底);每 30s 至少 1 纯空镜 + 1 巨构人物运镜(二者不可互相替代);对白节拍其余镜头以近景/特写为主,与大远景交替;冲突/反转爆发节拍取镜数上限并至少交替 3 种战斗专属运镜(见镜头词汇表),不能只靠慢镜升格撑场;所有镜头切换只用硬切,不设风格化转场。

### 场景库(巨构主义)

**标志性巨构/镜面场景(优先用于开篇/关键转折)**:云海之上的白玉超巨构天宫(建筑越出画面顶部)、一点透视的白玉天桥/甬道(消失点构图,适合放巨构人物运镜)、巨构建筑内部向外的开放大殿(人物极小立于门洞前)、悬浮宫阙长廊(倒影对称,适合放巨构人物运镜)、廊下远眺悬崖仙台(人物极小)。\
**常规场景(含室内)**:云海仙山之巅、瀑布秘境洞天、上古遗迹废墟、竹林剑冢、九重天宫阙楼阁、渡劫雷云战场、宗门大殿广场(室内)、丹炉洞府(室内)、星野天河、桃花幻境、荒漠魔域、结界秘境入口、悬崖栈道云梯、古镇市集、宗门寝殿/书阁(室内)。长片可重访同一地点换光线/机位/时辰。

### 道具库参考(锁定判断)

通常锁定:主角法宝/本命法器、关键信物(玉佩/古卷/传送阵图)、反复出现的兵器。通常不锁定:一次性摆设、群体背景道具。拿不准默认不锁定。

### 注意

- 不写真实门派/作品/演员姓名当 prompt;仙侠感靠描述词承担。
- 画面禁现代元素(强制,见标准负面词库),适用于全部工具。
- 人物图固定用 Seedream 5.0 Pro,场景图固定用Midjourney V8.2(不可用则 V8.1),道具图固定用 Lib Image,视频固定用 Seedance 2.5,均不得替换。三者出图/出视频均不生成转场特效或文字/字幕,人物/道具的四选一图与三视图都必须单张无拼接缝,场景图每地点一组 4 张四选一。
- 用户只要片段/单镜、或已指定场景造型时,在不破坏红线与核心规则下按需灵活处理。
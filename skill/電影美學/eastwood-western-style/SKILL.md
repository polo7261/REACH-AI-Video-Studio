# eastwood-western-style

做莱昂内荒凉美学 + 伊斯特伍德式反英雄西部片时用本 skill。剧情**完全依据用户脚本/剧本框架**。**风格致敬,不宣称是其本人作品。** 本 skill 自足,场景工艺全内联。

> 本环境适配(Flova→我方 13 工具):GPT Image 2/TextToImage/ImageToImage → `generate_image_v3`;Seedance 2.0/MultiModalToVideo → `generate_video_v3`;Suno/ElevenLabs/MiniMax(BGM/口哨/风铃/马刺/旁白) → `generate_audio`;text_editor → `write_file_v2`;video_assembler → `composite_video`;`<<<image_n>>>` → `reference_nodes` + `{{NodeKey}}`。**源"仅 GPT Image 2 / 仅 Seedance 2.0"模型唯一性 + 会员鉴权降级 = 本环境无该概念,删(用默认引擎)**;**super_resolution 超分/插帧(MediaKit)= 无该能力,删**——但"避免高帧率、保 35mm 胶片质感"的意图作为风格约束保留。**词栈/黄金模板原文英文保留**;composite_video 支持 per-track dB 与 clip trim(照搬),**变速(speed 1.5-2x)/黑场时长 composite_video 无原生参数 → 降级为剪辑指导性描述〔适配改写〕**。

## 流程(每生成新资产前暂停确认)

1. **全局设定(Final_Video_Spec)**〔`write_file_v2`〕:剧情**完全依据用户脚本**。8 字段模板:
   - **Title**:项目名/决斗主题
   - **Type**:动作/心理对峙/修正主义西部片
   - **Aspect Ratio**:16:9(默认电影宽画幅)或 9:16(移动端,同步调整构图)
   - **Resolution**:720p(默认)
   - **Output Language**:旁白与角色台词的目标输出语言(English / Chinese)
   - **Visual Style**:荒凉沧桑美学(Sergio Leone style, 褪色胶片, 特艺七彩, 逆光体积光)
   - **Audio Tone**:莫里康内交响乐声学(Ennio Morricone, 孤独口哨, 风铃, 铸铁马刺)
   - **Story Outline**:宿命决斗起承转合核心剧情梗概
2. **设计故事板**〔暂停〕:核心角色/场景作 key_element;镜头遵循**极静(蓄势对峙)→极动(瞬间爆发)**,融眼部特写/超广角远景/低角度仰拍/缓慢推镜。远距离决斗先建**对峙空间锁**(见下)。
3. **元素资产获取与校验**〔暂停锁定〕:见下"元素资产管理"。**全面核检机制**:资产建立完毕后,**逐一核对故事板所有 key_element(角色+场景)是否都成功绑定 asset_id;任何遗漏或未绑定成功严禁进入视频生成步骤**。
4. **分镜视频**〔暂停·附对齐核检〕:`generate_video_v3`,单镜 **4–15s(严禁<4s)**;**双重强基准绑定**(角色 node + 场景四宫格 node)。**提示词对准与防漏检视**:生成每镜前对照分镜脚本多维核检——场景参考、人物参考(占位符绑定)、台词对白全部精准对齐无遗漏;每镜强制绑定所属场景 key_element 四宫格作 reference_image(防背景漂移/跳画);无场景绑定的分镜绝不允许。强连贯镜可绑前镜末帧作 reference_video。含对白绑角色 key_element_audio 保音色一致。
5. **音频**〔暂停〕:见下"音频资产"。
6. **合成**〔暂停·先展示所有单项成果〕:`composite_video` 蒙太奇拼贴,见下"合成与剪辑动律"。

## 对峙空间锁(独特铁律)

任何远距离决斗场景,故事板**必须先用远景/OTS 建立"对峙空间锁"**:A 方站位、B 方站位、两人距离、面对方向、屏幕左右/纵深轴线、**镜头轴线、子弹方向、中弹倒地方向**。后续所有 ECU/CU 局部特写**只能改变镜头尺度,不能改变角色间真实距离或站位**。

## 多模态分析(用户参考材料)

- **角色全身三视图检测**:检查上传是否为含正/侧/背的**全身**三视图。是→提取各角度形体比例/面部轮廓/发型/肤质/经典服饰细节(披风/毡帽/枪套)/配色/独特标记(伤疤/胡茬),合并输出高完整性描述。**若非三视图或为半身照/头像 → 判"格式不匹配",启动重构。**
- **场景参考图检测**:检查是否为**无人物、多角度"标准四宫格"**(4 独立分格)。提取空间布局/核心建筑/代表性道具(吧台/墓碑)/色调(褪色大地色)/光影(强对比)。
- **美学契合度验证(核心)**:评估是否具备西部片底色(高硬度对比光/沙尘感/风化材质/沧桑感);格式硬校验(角色须全身三视图,场景须无人物四宫格)。契合→标可直接绑定;**不契合(风格不符/角色非全身三视图/场景不合四宫格或含人物)→ 判"格式/风格不匹配",制定"西部片风格转换与格式重构方案"**(见下四宫格四格固定分配)。
- **人声分析**:分析声音是否沙哑/深沉/干瘪/带沧桑感,录入 key_element_audio 维持配音一致。
- **参考视频动态分析(三项,写入 shot 描述)**:①**镜头运动轨迹**(极慢面部推焦 Slow Zoom-in/Push-in、低角度平移 Low-angle Pan/Dolly);②**物理运动反馈**(拔枪动作瞬态频率、枪口烟雾扩散速率、受击身体物理震颤幅度);③**光影明暗质感**(强对比硬光比例 Chiaroscuro、空气尘埃密度)。

## 元素资产管理(key_element 视觉定义)

**处理策略(两路径)**:
- **路径 A 用户已提供参考图**:完全契合(角色标准全身三视图 + 场景无人物四宫格 + 风格相符)→ 直接注册 asset_id 绑定。**不契合/格式不符 → 绝不直接绑定**,用 `generate_image_v3`(ImageToImage)以用户上传图为物理/面部参考重构:角色重构为西部片规范全身三视图(并排正/侧/背全身立绘,融宽沿毡帽/重胡茬/墨西哥斗篷/皮套/皮靴,极力保留原图面部标志);场景重构为无人物标准四宫格。
- **路径 B 用户未提供**:`generate_image_v3`(TextToImage),16:9。

**角色三视图构图规范**:强制**同一画布并排正/侧/背全身立绘**(定格脸部/警惕眼神/胡茬帽沿阴影/斗篷披风/腰间枪套/皮靴及整体剪影),展示 360° 服饰武器细节,**严禁半身照/头部特写/重叠画面**。

**★三视图 prompt 五处硬约束(实测反复验证,缺一处必翻车)**:
1. **写实锚点**:开头必须出现 `photorealistic`(不是 "portrait"/"reference sheet" 就自动等于写实——这两个词中性,不带任何倾向)。
2. **负向排除渲染风格**:结尾必须加 `No illustration, no anime, no cartoon.`——这条跟"no half-body/no cropping"这类**构图**约束是两回事,**构图约束管切法,这条管像照片还是像画**,必须都写、不能互相替代。**实测教训**:同一版本 prompt 只把 "illustration of" 换成 "reference sheet of"、不加这句负向排除,照样会生成卡通感结果——只要通篇没出现 `photorealistic` + `No illustration, no anime, no cartoon`,不管用词多含蓄,都等于没做防护。
3. **面板数量硬锁**:必须显式声明面板总数(默认 3:正/侧/背;需要脱帽/摘配饰做面部基准时可扩到 4,第 4 格明确写成"脱帽头像特写"并注明与前三格同光同肤质)——`Exactly N panels only, no additional close-up insets beyond the N specified below`,否则模型会自己加脸部特写小格把排版挤乱。
4. **等比对齐**:显式写 `same character scale and same camera distance across all views, evenly spaced with equal margins`,否则三个视图大小/站位高度容易不一致。
5. **纯色背景+防真人脸**:背景写 `flat solid neutral grey background, no gradient, no vignette`(不是单写 "neutral background" 就够,防止出现暖色调/暗角);人物描述前置一句 `Completely original fictional face, not based on any real person or celebrity`——**实测发现不加这句,"Sergio Leone spaghetti western" 这类强关联风格词会把脸直接生成得跟历史真实演员高度相似**。

标志性配饰(帽子/头巾等)**必须写进角色描述锁定清单,不得省略**——省略会导致同一角色不同批次"戴不戴帽子"随机不一致。

**场景四宫格构图规范(四格固定分配,最大化信息密度)**:
- **左上(全景定场 Establishing Shot)**:荒凉广阔西部全景/建筑,死寂空无一人,木板暴晒弯曲开裂。
- **右上(陈设特写 Props Close-up)**:风化木质家具/老枪/沙龙吧台;仅单枚生锈铁钉支撑吱呀作响的斑驳木招牌、布满铜绿的生锈马栓。
- **左下(纵深透视 Depth Perspective)**:强线条透视的漫天沙尘街道/峡谷小道,干枯龟裂泥地滚动风滚草(Tumbleweeds)、废弃小巷风沙旋涡(Dust devils)。
- **右下(气氛光效 Atmospheric Lighting)**:强硬正午直射光/夕阳逆光/飞扬尘埃,地平线夕阳强逆光下橙金光晕、浮尘与破旧黑布猎猎作响。

## 角色肖像级 key_element 方法

为**每个主要角色建立肖像级 key_element**:面容 / 服饰装束 / 武器配件 / 冷酷马刺与动作声效,**中文描述 + 英文视觉词组**并列,粒度到可跨镜锁定的具体特征。场景按四宫格四要素写足质感。
> 精简样例(示范颗粒度,非固定人设,按用户脚本替换):镖客——饱经风霜深褐皮肤(Weathered sun-bronzed skin)、冰冷灰蓝眼眸(Squinting piercing steel-blue eyes)、干裂脱皮嘴唇、斜叼半燃雪茄头(Half-burnt cigarillo);褪色墨西哥条纹羊毛斗篷(Faded Mexican striped wool poncho)+旧皮革马甲;系满黄铜子弹枪带与柯尔特左轮枪套、缀齿轮做旧黄铜马刺皮靴(clinking brass spurs)。反派——鹰隼凶眼半隐纯黑牛仔帽宽檐阴影(Hawk-like eyes half-hidden in the deep shadow of the cowboy hat brim)、瞳缘冷冽金属反光、八字胡;沾尘黑色双排扣长风衣(Dusty black double-breasted duster coat)+暗红丝绸马甲;雕花双枪皮套与银光左轮(Engraved silver-plated revolvers)、黑色铸铁马刺(dark cast-iron spurs)。完整肖像词栈见 `references/character-scene-portraits.md`。

**★服装锚定文本锁死机制（实测发现的漏洞修补）**：无用户参考图、走"路径B TextToImage 原创设计"时，角色的服饰/道具描述**在生成三视图前必须先写成一句定稿的锚定文本**（格式同上面精简样例的服装部分，中文+英文词组各一遍），写入 Final_Video_Spec 与该角色的 key_element 记录，视为**跟三视图图像本身同等级别的锚点**——**不是"示范颗粒度"的参考，是逐字锁死、后续每一镜都要原样复述的文本**。之前实测出现过同一决斗短片里，主角从"黑色风衣+雪茄"中途变成"墨西哥斗篷+子弹带"的服装错乱，根源就是没有先写死这句锚定文本、只靠"绝不写与元素图矛盾的外观"这条软性提醒，模型在没有强文本约束时会在不同镜头里各自"合理发挥"。**任何一镜的提示词只要涉及该角色的服装/道具，必须原样复制这句锚定文本，不得改写、简写或凭记忆重新描述。**

## 镜头设计、节奏与动作逻辑

- **极静→极动节奏**:对峙阶段优先极浅景深长焦特写(眼部/手部悬空/马刺),靠视线博弈(Eyeline Match)与极低摄像机运动幅度拉满张力。
- **局部特写同框关系声明**:凡局部特写同时提到"双方/两人/彼此"的身体部位/武器/动作,**必须明确"同一画面同框"还是"交叉剪辑"**。远距离决斗的手部/马刺/眼神/枪套特写默认写成 **intercut close-ups / hard cuts**;**禁用"双方的手""两人的枪套"等模糊表述**描述单一近景,除非剧情明确要求近距离同框。
- **极简台词停顿美学**:台词极其克制(人狠话不多),禁长篇大论;**有意识加破折号/省略号 ...**(如 `{No... I don't think so...}`)引导配音模型产生戏剧停顿与呼吸感的沧桑咬字。

## 双阶段八镜头决斗蓝图(标准决斗模板)

设计对决故事板须按此"双阶段八镜头"逻辑与台词细节编排(台词范式为示例,可微调):

**第一阶段 · 对视对峙(极致心理张力)**
1. **镜头1(空间锁建立 OTS)**:**135mm+ 长焦中景(MS/OTS)** 在双方间交替剪切,明确建立空间锁(二人分立主街两端/纵深两侧、相距较远、面对面、轴线/左右/纵深/朝向在后续保持不变);风沙漫天,斗篷/风衣热浪中微抖,空间压缩窒息对视。
2. **镜头2(眼神博弈 ECU 交叉剪辑)**:**极写特写 ECU** 在双方瞳孔/眼部微表情间快速直切(Eyeline Match);是 **intercut close-ups 非同框**,每个 ECU 只呈现一个角色局部五官,继承镜头 1 的远距离关系。
3. **镜头3(手部蓄势/马刺 交叉局部特写)**:**非"双人手部同框"**,拆 3A/3B/3C 或描述明确 hard cut/intercut——3A 只锁镖客右手/Colt 枪柄/皮套/子弹带(画面不得出现反派身体);3B 只锁反派手指/黑枪套/黑靴/铸铁马刺,提跟摩擦沙土金属回响(画面不得出现镖客身体);3C 3A 与 3B 间高压硬切交替,维持镜头 1 空间关系。
   - **对峙台词停顿蓝图**(极简冰冷、大量气口 `...`):反派范式 `{There are two kinds of people in this world... those with loaded guns... and those who dig...}`(极慢气音金属沙哑);镖客范式 `{You... dig...}`(极干燥沧桑低沉鼻音)。

**第二阶段 · 出击爆发(电光石火瞬态)**
4. **镜头4(极速拔枪 quick-draw)**:**1.5s 瞬态极写**(装配剪为 1s–1.2s);手部极速下沉贴合雕花枪柄,左轮爆炸速度滑出。
5. **镜头5(枪火硝烟 muzzle-flash)**:**中近景仰拍 MCU**;扣扳机,枪口橙金火光吐信,青白浓密枪烟伴 0dB 雷鸣枪声炸裂。
6. **镜头6(子弹擦帽微距慢动作)**:**微距慢动作 Macro Close-up**;高温子弹擦过毡帽边缘,冲击波撕裂呢料,碎纤维飞溅,帽受力倾斜旋转飞落。
7. **镜头7(中弹倒地 collapse)**:**低角度中全景 MWS**;**必须继承镜头 1 空间锁**:中弹者正面朝射手、子弹从射手方向击中胸口、身体沿受力方向**向后仰倒(远离射手方向)、背部先接触地面,不能向射手/镜头前扑**;双膝瘫软、物理惯性后倒、背重击沙土闷响、地面炸开厚重沙尘圆环。
8. **镜头8(收尾剪影 aftermath)**:**慢速拉远 WS/EWS**;镖客淡然缓慢将冒烟左轮插回皮套(清脆金属扣合声),血色残阳低悬、深橙绯红天空、胜者孤独剪影被狂风无限拉长、斗篷猎猎。

## 视频提示词写作规范(Seedance 风格,全内联)

- **对白语言前缀标签(首要声学机制)**:`{...}` 包裹对白时**必须强制加语言前缀**——英文 `{en: "verbatim dialogue line"}`、中文 `{zh: "一字不差的台词"}`;**严禁省略前缀**(否则口型同步/发音漂移)。
- **占位符与描述一致性**:用 `{{NodeKey}}` 绑角色/场景;提示词只描述瞬态动作/微表情/环境交互,**绝不写与元素图矛盾的外观**(图里黑帽子就不要写 "brown hat")。
- **多角色同屏物理隔离三条**:①**实体与占位符强绑定**(占位符紧跟角色名词/称谓,如 `The weathered hero {{Node1}} and the cold-eyed outlaw {{Node2}} face each other`);②**空间方位硬性区隔**(写绝对左右/景深,如 `{{Node1}} stands on the left in close-up, while {{Node2}} is positioned on the right in medium shot`);③**拒绝模糊复数**(禁 are/they/both,单体分开描述各自动作,实现绝对物理隔离)。
- **继承空间锁与交叉剪辑结构**:故事板已声明远距离对峙/intercut/hard cut/3A-3C 时,视频提示词**忠实保留结构,不得把多角色的手/枪套/马刺/眼睛/身体局部合并成同一近景同框**;单次生成含交叉特写须明写 `a sequence of hard-cut intercut close-ups` 且逐段声明每子镜头只出现一个角色局部;若引擎更宜单镜头稳定输出则拆成多个 shot 由 `composite_video` 硬切拼接。
- **动作向量三重锚定**:中弹/倒地/拔枪/冲撞/闪避时,动作方向**同时锚定三种关系**——角色身体方向(向背后倒)、对手/射手方向(远离射手)、镜头/屏幕方向(toward background / away from camera / screen left);**避免只写 backward/forward/left/right 单一相对词**。
- **提示词对照核检(双向)**:①场景/人物引用比对(提示词含脚本所有 key_element 占位符);②台词对白比对(所有对白一字不漏用 `{...}` 嵌入激活口型同步,环境音特效用 `<...>`)。
- **防四宫格视频机制(Grid Reference Disambiguation)**:调用四宫格场景参考图生成分镜视频时,为**彻底防止模型生成带四格的分裂画面**,必须:①**语义解构声明**(`{{Node}} is a 4-quadrant reference sheet containing establishing shot, props, depth, and lighting.`);②紧跟**显式单画幅镜头指令**(`Generate a single-camera shot focusing on the depth perspective of the street and the atmospheric dust from the reference sheet {{Node}}. Do not generate a split screen or 4-grid video. Single view only.`)。
- **镜头运动与动作堆栈(Camera → Action → Environment)**:按镜头运动→主体动态→物理环境层次编写,精确控制动作幅度(Motion Amplitude)与摄像机轨迹。极写用 `135mm+ telephoto lens, extremely shallow DoF, cinematic lens blur, blurred background bokeh`;宏大场面用 `extreme wide shot (EWS), low-angle perspective`;动态爆发可引 `whip pan`。
- **面部特写防漂移机制(Facial ECU Control)**:生成眼部/面部微表情大特写时**即便不展现全身也必须强制绑定角色全身三视图**作 reference;提示词明确镜头对准 `{{Node}}` 特定五官、微表情限制在面部区域,**绝不允许在提示词中描写全身/四肢/大尺度动作**(防塞多余身体构图导致人脸拉伸畸变);写法示例 `135mm telephoto extreme close-up (ECU) of {{Node}}'s face, razor-sharp focus on the squinting steel-blue eyes and sun-cracked lips, micro-expression of the face, completely ignoring the rest of the body.`
- **近身拔枪三阶段防畸变(Anti-Distortion Syntax)**:表现手指微动/按压/滑出枪套时,**同时传入角色全身三视图 + 场景四宫格(陈设特写分格)双向参考**;**严禁一句话概括的高频跃变词**(如 `he draws the gun directly`),必须"悬空蓄势→触达贴合→极速滑出"三阶段解构手部物理过渡(状态到状态位移),给引擎流畅轨迹差值依据:①`hovering inches above the leather holster, fingers spread wide`;②`fingers wrapping firmly around the engraved silver grip`;③`sliding smoothly out of the holster with explosive velocity`。
- **声音嵌入标记**:背景音/音效 `<...>`(如 `<wind howling, squeaking wooden saloon door>`,拔枪镜加 `<loud gunshot echoing, metal spurs clinking>`);极简对白 `{...}`(前缀语言)。
- **否定指令**:加 `no music`(音乐由全局轨道处理)与 `no subtitles`。
- **★风格锚定词逐条复述(实测发现的漏洞修补)**:**每一条**分镜视频生成 prompt 正文**末尾必须原样复述**精简锚定词(见 references/prompt-word-stacks.md 开头★生产验证版),**不能只靠 `{{Node}}` 引用参考图隐式携带风格**。实测反例:某测评案例图像阶段(角色三视图/场景四宫格)质感词写得很全,但 9 条视频 prompt 正文一条都没复述锚定词、只引用了 `{{Node}}` 场景图,最终整体风格判定不如同题基线——而该基线的 12 条视频 prompt **每一条**都在正文里逐字重复了锚定词。图像阶段把风格焊进参考图,只解决角色/场景外观一致;**每一镜的色调/胶片颗粒/光影质感必须靠视频 prompt 正文里再写一遍锚定词来保证**,两者缺一不可。

**图像词栈六组 + 三视图/四宫格英文模板 + 四个视频黄金模板**全文见 `references/prompt-word-stacks.md`(原文英文保留)。

## 音频资产

- **音频资产复用去重(最高优先级)**:用户已上传 BGM/VO/特定音效 → **强制直接绑定复用,严禁无视用户资产触发 AI 重生成**;仅用户未提供时才触发下列生成。
- **独立音轨生成**(`generate_audio`,四条词栈原文保留,见 references):①交响 BGM(Spaghetti Western orchestral, epic acoustic guitar, dramatic high-register trumpet, crescendo, Sergio Leone style);②孤独口哨主题(solo human whistle, haunting melancholic, high cathedral reverb, Ennio Morricone aesthetic);③沙尘风铃环境(desolate howling desert wind, sparse metallic rusty wind chimes, no musical melody);④马刺沉重脚步节奏(dry acoustic percussion, heavy boot thuds, metallic clinking brass spurs, ticking clock tension)。
- **旁白 VO**:英文默认沙哑低沉颗粒感伊斯特伍德式音色;中文/多语言选相应音色。作独立 audio_layer。

## 合成与剪辑动律(video_assembler → composite_video)

- **剪辑动律四阶段(对峙段)**:①环境定场 EWS ≈**10s**;②双人对视 OTS/MS 交替、每镜 ≈**8s**;③局部极写 ECU/手部枪套特写交替、频率缩至 **4–5s**;④爆发前夕极限变频快剪:主角双眼(2s)→反派双眼(2s)→主角悬空手指微动(1.5s)→反派紧握枪柄(1.5s),物理镜头长度指数级递减至绝对窒息。
- **爆发段快剪蒙太奇(1s–2s)**:引擎最低 4s,生成端无法出超短镜头 → **装配阶段对 4s+ 源片段做 `composite_video` 的 startPosition/endPosition 高精度 Trim 截取**,按四快剪结构拼贴:①(1.0s)特写手掌按压左轮极速滑出+枪口火光前 24 帧;②(1.0–1.2s)低角度侧中景开火+青白枪烟炸裂;③(1.0s)极写中弹瞳孔放大/碎布飞溅/帽被掀飞;④(1.5–2.0s)中远景仰拍身体后倒尘土扬起。〔**局部变速 Speed up 1.5–2x composite_video 无原生参数 → 降级为剪辑指导性描述·适配改写;Trim 用 startPosition/endPosition 原生照搬**〕。爆发后余韵重放缓,收枪/硝烟散去/地平线剪影定格 **5s+** 归苍凉寂静。
- **五轨垂直叠层 dB 电平表**(`composite_video` audioList 每轨 `decibel` + `videoVolume:0` 静音视频原声):
  1. **Track1 环境铺底(风沙+风铃)**:全片循环,**-15dB 到 -20dB**,低频物理声场背景。
  2. **Track2 物理拟音(重步履+马刺)**:**-6dB 到 -10dB**,随角色行止动态淡入淡出(行走推高、停步衰减至 -30dB 挂底)。
  3. **Track3 主题旋律(口哨)**:**-8dB 到 -12dB**,加深混响营造空灵纵深。
  4. **Track4 交响 BGM**:对峙静默期 **-18dB 到 -24dB** 挂底;决斗高潮/瞬间爆发以 **+6dB** 急剧渐强直推 **0dB** 爆裂。
  5. **Track5 人声/旁白**:**0dB 到 -3dB** 优先清晰;有人声吐字时 Ducking 将 BGM 与环境音临时压低 **-6dB**。
  〔dB 与 Ducking:composite_video 支持 per-track `decibel`,静音视频原声用 `videoVolume:0`,照搬;Ducking 的动态压低若无原生自动侧链 → 以分段 audioList dB 近似或标剪辑指导·适配改写〕。
- **声学留白/破冰**:爆发前 3–4s 声学戏剧性渐弱/截断——BGM 交响与口哨在枪声前 **2s 骤淡出至无声(Fade to -inf)**,仅留极轻沙沙风声+一声孤独风铃微响;拔枪开火**第 1 帧枪响 SFX 以 0dB 饱和瞬态爆发**,同时 Track4 重音铜管爆发,与拔枪视觉瞬间**帧级对齐**实现"极静到极动瞬间破冰"。
- **转场规锁**:主体剪辑全部**高对比无缝直切(Hard Cut)**(即 composite_video 按序拼接,60 年代意大利西部片冷峻硬核气质关键);**严禁**溶解 Dissolve/划像 Wipe/光晕闪烁/3D 翻转;**仅大跨度空间位移或大尺度时间跳跃**才允许淡入淡出黑场(Fade to Black/in),黑场时长 **1.5s–2s**〔黑场转场 composite_video 无原生参数 → 大跨度切换时插黑场素材或标剪辑指导·适配改写〕。
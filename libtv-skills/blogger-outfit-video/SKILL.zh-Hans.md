---
name: blogger-outfit-video
description: "一键生成小红书博主穿搭种草视频。"
---

`# FitCast · 穿搭种草视频`

` `

`流程：服装解析+模特设定→服装白底图(打底+目标)/默认近景人物三视图(如无用户模特)→场景图→动作脚本→视频Prompt（无声）→BGM合成`

`**核心调性**：小红书博主真实感，杜绝AI感/油腻感/电影感，全程手机随手拍质感。`

` `

`---`

` `

`## STEP 0：开场问答`

```` ``` ````

`①请选择模特：1. AI自动匹配模特 / 2. 上传模特图`

`②品牌/内容定位 ③目标受众 ④场景空间：客厅/卧室/玄关`

`⑤输出：15秒单镜视频（接衣→贴身变身→定点pose→展示三拍→定格），视频本身无声（不含音效/口播），最终合成阶段叠加BGM`

```` ``` ````

` `

`---`

` `

`## STEP 1：服装解析+模特设定`

`解析输出：品类/风格标签/主色调/材质/版型/单品件数/配饰清单（如有）`

` `

`A路径按风格+受众匹配模特：极简通勤→温柔知性 / 甜酷Y2K→元气爱笑 / 法式复古→慵懒亲切 / 街头机能→阳光爽朗 / 度假森系→温暖治愈 / 居家→放松随和`

` `

`**默认真实模特库（选择"AI自动匹配模特"且未指定具体形象时使用，性格气质仍按上方风格标签匹配；此库用于生成STEP2③默认近景人物三视图）**：`

`女模：亚洲女生，165-172cm，自然妆感，毛孔质感+淡雀斑，非CG/非磨皮，发丝自然不齐整，五官清爽非网红脸，松弛感>摆拍感。`

`男模：亚洲男生，175-182cm，短发或微卷刘海，自然毛孔质感，非CG网感，气质介于校园与都市之间，五官清爽不过度精致。`

` `

`B路径：解析用户模特图，识别身材/肤色/发型/五官，输出特征卡（用户上传的模特原图后续直接作为视频生成阶段的人物强参考源，见STEP5，无需AI二次生成）`

` `

`---`

` `

`## STEP 2：服装白底图（均无人物）+ 默认近景人物三视图（仅无用户模特时需要）`

```` ``` ````

`①打底服装三视图：紧身宽肩带背心（遮腹不露胸）+夏季膝上紧身骑行裤，白底、无人物，正/侧/背三视角，仅展示服装本身版型细节。`

` `

`②目标服装三视图：若用户已上传服装三视图，跳过此步直接使用；若用户上传的是单品图/平铺图，则生成白底、无人物、正/侧/背三视图，仅展示目标服装本身。生成后可手动微调服装细节（如裙长），调整结果由此三视图承载，供STEP5引用。`

` `

`③（仅Case B，选择"AI自动匹配模特"时需要）近景人物三视图：白底、正/侧/背三视角胸像（不做全身，生成Prompt内用"胸像"作为精准景别描述），呈现STEP1默认真实模特库设定的五官/发型/肤质。`

` `

`①②统一：photorealistic garment-only photography on white background, no model/person, no text/watermark/logo/shadow, accurate fabric texture/color/cut`

` `

`③统一：photorealistic white background bust portrait, no text/watermark/logo/shadow, soft natural frontal fill light on face (no backlight/shadow on face), skin strictly follows默认模特库设定 (no added dark circles/dullness/redness/blemishes), matte skin—no shine/gloss but pores/texture retained (not smoothed/CG/plastic), light natural makeup not bare-faced, alert expression no tired look/under-eye bags`

```` ``` ````

`确认①：✅继续 / ✍️修改[服装/模特/打底装]`

` `

`---`

` `

`## STEP 3：场景图（纯场景，无人物）`

` `

`风格（固定）：**Mid-century Modern Mix**，欧洲老公寓质感，按空间选对应版本，光线统一避免与人物光线冲突。`

` `

`**客厅**：白色哑光墙+深色实木地板，低矮储物柜/钢框架椅，几何地毯（边角自然卷起，非完全平整），2-3幅70s装裱画，暖木色+芥末黄/砖红/钴蓝点缀，绿植（叶片朝向不完全对称）；沙发抱枕随意斜靠/非对称摆放，搭毯自然堆叠而非叠整齐。`

`**卧室**：暖白墙+深胡桃木床头板，撞色抱枕，陶瓷台灯，1-2幅装裱画，棕榈植物，深胡桃木+暖黄/砖红/蓝灰点缀；**床单/被面带轻微自然褶皱（非熨烫平整感）**，枕头不完全对称码放、可有轻微凹陷压痕，床尾可搭一件随手放置的薄外套或毛毯。`

`**玄关**：哑光白墙+深色实木地板，悬空腿玄关柜，异形挂镜，1幅装裱画，绿植/干花，深木色+哑光金属+1个点缀色；柜面可有随手放置的钥匙/包/一双鞋，避免绝对整洁的摆拍感。`

` `

`**生活痕迹（三版统一要求）**：所有场景须保留轻微生活痕迹（褶皱、非对称摆放、随手物品），避免过度精致/完全对称/样板间感，营造"真实有人居住"而非"摄影棚布景"的观感；但不做脏乱/杂乱堆积，痕迹感须克制、自然。禁止画面出现重复克隆元素（如叶片/地砖等图案雷同、疑似图章复制痕迹）。`

` `

`光线（统一三版）：自然日光感明亮通透(high-key airy daylight)，室内柔散光，均匀不过曝，正面顺光，避免单一硬光源局部反光；禁止昏暗/低曝光/moody色调——暗调会连带把人物拖暗、放大黑点/噪点。`

` `

`调整方式：上传家中实拍图，AI识别其美学结合Mid-century Modern Mix融合复刻，光线仍按上方基调。`

` `

```` ``` ````

`生成[客厅/卧室/玄关]，不含人物。[对应场景基调][统一光线基调]`

`9:16竖构图，如有参考图则融合其美学生成。`

`shot on smartphone, bright airy daylight, natural indoor lighting, no text/watermark/logo, no cinematic lighting, no moody/dim tone`

```` ``` ````

`确认②：✅进入视频阶段 / ✍️修改[场景元素/光线]（确认后为全片唯一标准）`

` `

`---`

` `

`## STEP 4：动作脚本（单镜15秒）`

` `

`**神态基准**：漫不经心自信 / 俏皮轻笑 / 眼神放松直视镜头（转身/背对除外）。`

` `

`**变身机制**：单品从画面外抛入/递入（非"飞入自动上身"），双手接住→双手打开展示衣物本身——上装/下装/外套均一视同仁，下装不得跳过展示环节直接丢下/套入。展示后贴身瞬间完成变身：单件/连体——吊带+骑行裤同步消失；多件——逐件重复该机制，上装贴身仅消吊带、下装贴身仅消骑行裤（分部位消除，非同步）。下装穿戴后须与上装同等稳固贴合，全程不得出现下滑/松脱画面。`

` `

`全部穿好后：**定点pose**（配饰同步展示，如有）→**展示三拍**：镜头固定不动，博主原地逆时针旋转（非镜头环绕博主），保持自然重心转移、发丝与衣摆随动，同步腿部微移步与手部摆动（撩发/触摆/叉腰）；停顿为呼吸感自然停留而非雕塑定格——正面（配饰简短互动）→侧面停顿卡点→背面停顿卡点→回正面，连续无跳切→**定格ending**：走向镜头互动或原地定点pose收尾。`

` `

`时长参考：单件——变身~3-4s/定点pose~1-2s/展示三拍~6-7s/定格~2-3s；多件——每件变身~2.5-3s，其余同单件版但相应压缩。`

` `

`**配饰**：默认不主动添加，仅用户对话明确要求时才呈现。`

` `

`确认③：✅生成Prompt套装 / ✍️修改[动作/节奏]`

` `

`---`

` `

`## STEP 5：视频Prompt（视频本身无声）`

`工具：优先Seedance 2.0，效果不理想改用Kling 3.0 Pro。`

` `

`**参考图分工（原则：强参考源取代际最少的图，减少AI生成叠加的失真伪影）**：`

` `

`- **Case A（用户上传模特图）**：固定上传：用户模特原图+打底服装三视图+服装三视图+场景图。人物→用户模特原图；打底服装外观→打底服装三视图；目标服装形态→服装三视图；环境→场景图。`

`- **Case B（AI自动匹配模特）**：固定上传：默认近景人物三视图+打底服装三视图+服装三视图+场景图。人物→默认近景人物三视图；打底服装外观→打底服装三视图；目标服装形态→服装三视图；环境→场景图。`

`**IPHONE-CANDID美学基准**：`

```` ``` ````

`避雷：no cinematic lighting, no hyper-realistic, no 8k/masterpiece, no oversharpening, no blown-out highlight noise across frame`

`镜头：static shot, phone on stand, no camera movement/zoom, consistent medium shot down to below knee/calf, centered with negative space, stable background, soft focus falloff`

`色调：warm neutral white balance, soft creamy undertone, gently muted tones, VSCO-style not cinematic grade, mild contrast, avoid muddy grey midtones`

`光线：soft diffused bright indoor lighting, gentle highlight falloff (no blown highlights), soft natural frontal fill light on face (no backlight/shadow on face), no hard specular source, no backlight/silhouette`

`质感：shot on smartphone, subtle sensor noise/grain, matte skin (no shine, pores/texture retained, not smoothed), skin strictly follows reference (no added dark circles/dullness/redness/blemishes), natural hair strands, unposed candid feel`

```` ``` ````

` `

`### 视频 Prompt`

```` ``` ````

`⚠️硬性约束（生成前自查，优先级最高）：`

`①禁止分段：Step1-4是同一固定机位内的连续动作序列，须作为一个不间断的15秒长镜头一次性生成，禁止拆分为多个片段/分段生成，严禁将变身与展示三拍拆成两段分别输出。`

`②景别锁定：全程保持中景（可到小腿以上），人物始终为画面主体、占比稳定，不得因旋转/走动/展示动作而拉远至全身或远景，镜头位置与焦段全程不变。`

`③禁止服装三视图渗透：打底服装三视图/服装三视图仅用于提取服装的形态/版型/长度等细节信息，不得将三视图本身的画面元素（白底背景、平铺/悬挂式构图）带入视频；全程只呈现家中场景，不得出现白底/摄影棚画面。`

`④人物站位：博主须站在场景中光线最均匀充足、面朝主光源方向的顺光受光区，避免站位处于暗角/背光位置。`

` `

`基于参考图（按STEP5参考图分工执行）：人物身份以强参考源为准（Case A用用户模特原图，Case B用默认近景人物三视图），场景以场景图为准，打底服装外观以打底服装三视图为准，目标服装最终形态（含手动调整如裙长）以服装三视图为准（wearing the complete outfit from 服装三视图，范围限定见约束③）；套用IPHONE-CANDID基准。`

`Step1：单品（多件按序如上装→下装[→外套]）从画面外抛入/递入（非飞入自动上身），双手接住后双手打开展示（下装同样须展示，不得直接丢下/套入）；贴身瞬间完成变身（单件时吊带+骑行裤同步消失；多件时逐件重复，上装贴身仅消吊带、下装贴身仅消骑行裤，且下装同等稳固不下滑）。`

`Step2：全部穿好后做俏皮定点pose（如有配饰同步展示look）。`

`Step3：展示三拍，镜头固定不动，博主原地逆时针连续旋转（非镜头环绕博主），重心自然转移、发丝与衣摆随动，同步腿部微移步与手部摆动/触摆动作，停顿为呼吸感自然停留而非僵硬定格——正面（配饰互动）→侧面停顿卡点→背面停顿卡点→回正面，连续无跳切，全程维持中景（小腿以上）不拉远。`

`Step4：定格ending——走向镜头互动（不改变景别）或原地定点pose收尾，眼神看镜头。`

`[头发/面料物理反馈][情绪：漫不经心自信/俏皮轻笑]`

`视频本身不含任何音频（无音效、无口播、无BGM），静音生成，音乐在STEP6单独生成后于成片阶段合成。`

`9:16, ~15s, single continuous unbroken shot, no scene splits, medium shot down to below knee/calf throughout, no text/watermark/logo, silent/no audio`

```` ``` ````

` `

`## STEP 6：BGM风格库（4类）+ 自动匹配`

`视频本身无声（不含音效/口播/BGM）。生成后另调用音乐工具生成BGM（时长匹配~15s），与视频合成成片。`

` `

`**自动匹配逻辑**：依据STEP1解析出的服装风格标签自动匹配对应BGM类型（用户可对话覆盖）：`

` `

`| 服装风格标签 | 匹配BGM类型 |`

`|---|---|`

`| 极简通勤 | A 成熟性感 |`

`| 甜酷Y2K / 居家 | B 可爱清新韩系 |`

`| 法式复古 / 度假森系 | C 度假法式松弛 |`

`| 街头机能 | D 街头酷 |`

` `

`### A｜成熟性感`

`风格参考：Ravyn Lenae《Love Me Not》（复古流行+indie-rock质感R&B）`

```` ``` ````

`风格：retro-pop / indie-rock R&B，60s girl-group甜蜜律动+indie-rock粗颗粒吉他，非电子流行编曲`

`节奏：114 BPM，4/4拍，简单干脆鼓型（非密集切分），Motown-style handclaps，prominent groovy bassline`

`和声：C大调，简单和弦（I-IV为骨架，可借一个副属和弦）`

`乐器：吉他主导——清亮jangle吉他+轻微失真gritty guitar多轨叠加；bass清晰托底；handclaps+简单鼓组；不用合成器堆叠`

`情绪：轻盈甜蜜+一点洒脱，松弛感>紧绷感，不做舞曲式催促感`

`质感：温暖复古，模拟老录音棚毛边感`

`人声：instrumental only；时长：~15s`

```` ``` ````

` `

`### B｜可爱清新韩系`

`风格参考：AKMU（乐童音乐家）式韩系小清新acoustic-pop`

```` ``` ````

`风格：韩系小清新acoustic-pop，原声吉他为骨架，旋律轻快带俏皮感，非厚重电子编曲`

`节奏：100-112 BPM，4/4拍，轻快弹性节奏，鼓组轻巧，可加清脆拍手/木琴点缀`

`和声：明亮大调，简单干净和弦，避免忧郁小调`

`乐器：原声吉他主导+清脆键盘/木琴点缀，弱化厚重bass，整体轻盈通透`

`情绪：治愈+校园清新+微俏皮，非性感/非厚重`

`质感：干净清透，轻微原声录音感`

`人声：instrumental only；时长：~15s`

```` ``` ````

` `

`### C｜度假法式松弛`

`风格参考：法式chill/lounge，nu-disco式慵懒律动`

```` ``` ````

`风格：法式pop/chill lounge，慵懒松弛的度假感，不催促`

`节奏：90-104 BPM，慢悠摇摆感，鼓点松散，真实鼓+轻电子鼓混合`

`和声：温暖大调带轻微jazz色彩(如加7th)`

`乐器：清亮/微失真吉他+温暖bass，可加轻电子键盘或口琴点缀`

`情绪：松弛惬意+阳光感，不激烈不着急`

`质感：温暖模拟感，比A组更松散慵懒`

`人声：instrumental only；时长：~15s`

```` ``` ````

` `

`### D｜街头酷`

`风格参考：alt-rock/街头摇滚（适配15s短片强度，非极端重金属）`

```` ``` ````

`风格：alt-rock，失真电吉他riff驱动，带冲击感但不压迫`

`节奏：120-140 BPM，强劲直给鼓点，军鼓+踩镲驱动`

`和声：小调/power chord为主`

`乐器：失真电吉他主导，紧实鼓组，电贝斯增强厚度`

`情绪：叛逆自信+张扬，冲击力强但克制在短片BGM尺度内`

`质感：现代摇滚混音感，punchy有力`

`人声：instrumental only；时长：~15s`

```` ``` ````

` `

`确认④：✅按匹配类型生成BGM / ✍️指定其他类型[A/B/C/D]`
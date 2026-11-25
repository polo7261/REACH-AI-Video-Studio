## 一套梦核 look + 三档情绪(开拍前卡选情绪档,全片统一)

dreamcore 只有**一套 look**(低饱和、低对比、抬黑位、高柔光、35mm 颗粒、超现实但写实),靠**情绪档**调粉/蓝配比与冷暖。下面英文子句直接取用:**「调色子句」用于 MJ 场景图,「前置风格句」放在 Seedance prompt 第一句。**

### 甜暖怀旧(warm,偏粉)

- 调色子句:`dreamcore aesthetic, surreal yet photorealistic, desaturated washed-out pastel grade leaning blush-pink and cream, warm hazy afternoon glow, soft diffused light with gentle bloom, lifted matte blacks, low contrast, fine 35mm film grain, gentle soft focus`
- 前置风格句:`Warm dreamcore music video frame, surreal yet photorealistic, blush-pink and cream desaturated pastel palette, soft hazy afternoon glow with gentle bloom, lifted matte blacks and low contrast, fine 35mm grain, weightless dreamy slow motion.`

### 空灵纯净 / 失重忧郁(cool,偏蓝)

- 调色子句:`dreamcore aesthetic, surreal yet photorealistic, desaturated washed-out pastel grade leaning powder-blue and lilac, cool misty pale silvery light, soft diffused glow, lifted matte blacks, low contrast, fine 35mm film grain, gentle soft focus`
- 前置风格句:`Cool ethereal dreamcore music video frame, surreal yet photorealistic, powder-blue and lilac desaturated pastel palette, cool misty pale light with soft glow, lifted matte blacks and low contrast, fine 35mm grain, weightless dreamy slow motion.`

### 微寒梦魇(uneasy,灰蓝)

- 调色子句:`dreamcore aesthetic, surreal yet photorealistic, muted desaturated palette leaning grey-blue, flat overcast soft light, faint emptiness and stillness, lifted matte blacks, low contrast, fine 35mm film grain, gentle soft focus`(仍柔光低饱和,靠空旷/静止表达不安,不加恐怖元素)
- 前置风格句:`Faintly uneasy dreamcore music video frame, surreal yet photorealistic, muted grey-blue desaturated palette, flat overcast soft light, a sense of empty stillness, lifted matte blacks and low contrast, fine 35mm grain, weightless slow motion.`

---

## 固定种子与出图规格(速查)

> **全局默认**:MJ 画质"自适应"、Lib Image"标准画质";**每条 MJ prompt ≤ 1024 字符**;所有 MJ 场景图统一 **V8.2**。提示词**英文书写**(参数/种子代码保持原样)。

- **造型图 = Seedream 5.0 Pro**(**2K、无任何尾串/参数**):出**一张 16:9、白底的造型图,从左到右横排 4 个全身造型、4 套明显各不相同**,真人模特、脸与全身清晰;用户从这 4 个里**选 1 个**(选中锁为全片主造型)。**有造型参考图则作 Seedream 的图参考;人像/人脸参考图一律不喂 Seedream。** prompt 英文自然语言(性别/人种/造型方向 + 着装/人物底线),**不带任何** `--sref` **/** `--ar` **/** `--v` **/** `--no` **尾串**。\
  示例:`one 16:9 2K white-background styling sheet; the same [gender] [ethnicity] real adult model shown as four different full-body looks side by side, four clearly distinct outfits, all in the chosen mood's dreamcore styling direction (甜美怀旧 sweet doll / 空灵纯净 all-white nightwear+JK / 微寒梦魇 icy powder-blue — 见「造型语言」); for a male subject swap any skirt for trousers, keep the same fabrics and elements; clear face and full body, natural hands; modest tasteful fully-covered outfit, high modest neckline, opaque non-transparent fabrics, knee-length or longer skirt (or with matching modesty shorts); clean skin with no tattoos and no piercings; pure white seamless background, even soft studio light, photographic`
- **三视图 = Lib Image**(强制,默认**标准画质**),造型确认后**据所选那套全身造型扩写 16:9 白底全身三视图**。**硬性:必须把用户选定的那张 Seedream 造型图作为图输入 / 参考连线接入 Lib Image**——不连线三视图会另起炉灶、与所选造型对不上,整步作废;三视图的**款式 / 颜色 / 廓形 / 面料 / 比例(及无人像时的脸)必须与所选造型图逐项一致**,只补出侧 / 背视角。**真人模特**;**排版强制:所有内容在一张图内、16:9,全身左/中/右三视(正/侧/背),不放头部特写/大头**;**有人像参考图→三视人脸用纯白圆形贴纸完全遮住 + 右下角中文小字「人脸单独提供 · 此图仅用于服装造型参考」**(真脸由原图在 Seedance 锁)、**无人像参考图→保留所选那套 Seedream 造型的脸**(脸即身份)。\
  要点:`using the selected styling image as image input/reference, expand it into a single 16:9 white-background turnaround; keep the exact same outfit (style / color / silhouette / fabric) and proportions as the input, only three full-body views — left / center / right (front / side / back) of the same real adult photographic model, no head close-ups, infer side and back consistently, clean skin no tattoos no piercings, pure white seamless background, even soft studio light, photographic`。**有人像参考图时**:`cover each face with a plain solid white circular sticker, add a small Chinese caption at the bottom-right: 人脸单独提供 · 此图仅用于服装造型参考`(无人像则保留脸、不加贴纸与标注)。
- **场景图 = Midjourney V8.2**(默认**自适应**,prompt ≤ 1024 字),**固定 dreamcore 种子** `--sref 4658243766 --profile yp7vzjb`,**全景无人、零文字、超现实但写实**。\
  尾串:`… --sref 4658243766 --profile yp7vzjb --ar <16:9|4:3|9:16> --v 8.2 --no text, words, letters, numbers, captions, signage, logo, watermark, extra patterns, cartoon, illustration`
- **视频 = Seedance 2.5**,输入 = 场景图 + 白底三视图(锁造型/身形)+ **人脸参考**(有人像参考图→原图/视频;无人像→所选那套 Seedream 造型的脸;**人像参考图不喂造型模型、只在此处喂**)+ **对口型段的音频切片(连线到音频输入口)**。

---

## 流程(逐阶段暂停确认)

### 阶段 0 · 开拍前(一张问询卡,问完停下等上传)

**开拍前问询卡(下面每一问都是「独立一问」,同一张卡里一问接一问;绝不把两问揉进同一问的选项,也不拆多张卡;条件问不适用时让用户"留空/跳过")。问完停下等用户上传音频/参考图。**

1. **音频(单选)**:你有现成的歌曲 / BGM 吗?——`我有,稍后上传` / `没有,帮我生成`。
2. **歌曲风格 + 主题(自由输入;仅第 1 问选"没有"时填,有音频留空)**:想要什么风格与主题?(dreamcore 曲风走 **dream pop / ambient / bedroom pop**,朦胧慢板大混响)
3. **人声(性别 + 语言)**:人声用哪种?**性别(男 / 女)+ 演唱语言**(中文 / 英文 / 韩文 / …)。(上传音频可听辨预填,可改)
4. **有无人像 / 造型参考图**:有人脸参考图(或 &lt;15s 视频)/ 造型参考图吗?——**只要有人像参考图 → 主角性别、人种一律以参考图为准,第 5 问留空**;没有则第 5 问照填。
5. **角色人种(自由输入;仅第 4 问"没有人像参考图"时填)**:按第 3 问语言推荐(中文→亚洲、英文→欧美、韩文→亚洲…),可改。
6. **字幕**:成片要不要字幕?要→选语言;不要→无字幕。(字幕只在阶段 5 叠加,生成画面永远零文字)
7. **情绪档**:甜暖怀旧 / 空灵纯净 / 微寒梦魇(定粉/蓝配比)。
8. **画幅**:16:9 / 4:3 / 9:16?
9. **画质**:480p / 720p / 1080p?

> **结论**:**主角性别 = 人声性别**;**人种 = 有人像参考图→随参考图(第 5 问留空)/ 无→按语言推荐并经用户确认**;**不单独问性别/人种,时长也不问**(由【选段】定)。9 问全在这一张卡里、一问一件事、各给各的干净选项。

**音频就绪 / 音乐确认(先于切片)**:

- **有音频** → 用用户上传的音频。
- **无音频** → 按风格/主题 + 人声(性别/语言)生成一版带歌词人声(**曲风走 dream pop / ambient / bedroom pop**)→ **生成后暂停,等用户确认音乐满意**(可重做/微调),满意才切片。(生成时风格字段与歌词字段分开,别把描述词当歌词唱;音乐提示词 ≤ 1024 字。)

**音频确认后必做两步(先于分镜与生视频)**:

- **① 音频切片(+ 拿歌词)**:切成**多段连续、每段 ≤15s 的切片**(按对应视频秒数切分),同时**拿准确歌词——只供内部对齐口型/选段,绝不写进任何发给模型的 prompt**;对口型段每段切片将作**音频锚点连线喂 Seedance 2.5 驱动口型**。**切完停下等用户确认切片。**
- **② 选段**:问"**你想用哪几段来做这支 MV?**"。**推荐连续的几段(每段 ≤15s)**(便于段间衔接);**推荐挑有人声/歌词的段做对口型,纯器乐段默认不做 lipsync**(器乐段只做梦核表演、不唱)。**选完即自动算出时长(= 各段秒数之和 = 视频段数),不再问"想做多长"**;段数由此步确定。

**造型分流(按 Q4 有没有上传人像 / 造型参考图,走四种情况;都先"理解造型方向 + 结合下方造型语言补写成完整 spec",不丢图照搬。统一流程:Seedream 出一张 16:9 白底 2K 横排 4 造型 → 用户选 1 → Lib Image 据所选造型扩写三视图)**:

> **铁律:人像/人脸参考图一律不喂造型模型(Seedream)**(Seedream 只接受**造型参考图**作图参考);**人脸参考图只在最后 Seedance 生视频时**与三视图一起喂(锁真脸;**发型由用户选:保持参考图发型 / 换成三视图发型**)。**三视图人脸怎么处理只看"有没有真人像参考图":有→纯白圆贴遮脸 + 右下角中文小字标注,无→保留所选 Seedream 造型的脸。**

- **① 只有人像参考图**:人像**不喂 Seedream**;Seedream 按文字 spec 出四造型(无尾串)→ 选 1 → Lib Image 三视图、**人脸纯白圆贴完全遮住 + 右下角中文小字「人脸单独提供 · 此图仅用于服装造型参考」**;人像**仅 Seedance 时**与三视图一起喂(锁真脸;**发型用户选**)。
- **② 只有造型参考图**:造型图**作 Seedream 图参考** + 补写 spec → Seedream 出四造型 → 选 1 → Lib Image 据所选造型**人脸+造型**出三视图、**人脸不打码**(所选造型的脸即身份、也作 Seedance 人脸参考)。
- **③ 人像 + 造型都有**:**只把造型图作 Seedream 图参考、人像不喂** + 补写 spec → Seedream 出四造型 → 选 1 → Lib Image 三视图、**人脸纯白圆贴遮住 + 右下角中文小字标注**;人像**仅 Seedance 时**与三视图一起喂(锁真脸;**发型用户选**)。
- **④ 都没有**:用**据人声语言+性别推荐、用户确认过的人种 + 性别** + 补写 spec,Seedream 出四造型(无尾串)→ 选 1 → Lib Image 三视图、**人脸不打码**(所选造型的脸即身份、并作 Seedance 人脸参考)。**不单独问性别/人种。**

**dreamcore 造型语言(补写 spec 时对齐;英文书写;按三档情绪各一套、彼此拉开区分;全性别通用——男生把裙装一律换成裤装,面料/元素/色系不变;皮肤无纹身无穿孔;裙长守底线=及膝或更长 / 或配同色系安全裤)**:

- **甜美怀旧(warm,偏粉 / 杏 / 奶)** — 参考:娃娃领、蕾丝纱裙、玛丽珍娃娃鞋、可爱头饰:\
  `nostalgic sweet doll styling — peter-pan / doll collar blouse, layered tulle tutu skirt (knee-length or with matching modesty shorts) or soft layered chiffon skirt, mary-jane doll shoes, striped or lace knee socks, ribbons / bows / patchwork hair accessories, soft bangs; warm pastel palette (blush-pink, apricot, cream); vintage doll-like sweetness`男:裙 → `soft tailored pastel trousers or cropped pants`,保留娃娃领上衣、缎带/蝴蝶结发饰(从简)、玛丽珍风鞋,同色系与面料不变。
- **空灵纯净(白色系为主)** — 参考:睡衣元素、jk 校服元素、纯白层叠:\
  `ethereal all-white styling — nightwear-inspired layered white blouse with lace-trim bloomers, plus JK school-uniform elements (knee-length pleated skirt, sailor / doll collar, ribbon tie), soft chiffon layers, white knee socks, delicate white hair piece; pure innocent airy vibe; monochrome white / off-white / cream palette`男:裙 → `white JK-style shirt with ribbon tie and tailored white trousers, or white pajama-style layered shirt with lace-trim trousers`,同为纯白、睡衣/校服元素与柔纱面料。
- **微寒梦魇(淡蓝 / 冷色系为主)** — 参考:淡蓝按扣背心裙、荷叶泡泡袖、手套、星星发饰:\
  `cool-toned dreamcore doll styling in icy powder-blue — button-front pinafore or vest over a white ruffle puff-sleeve top, matching gloves, star / snowflake hair clips, pleated hem (knee-length or with matching modesty shorts); faintly cold pristine uneasy mood; cool pastel palette (powder-blue, ice-blue, cool grey)`男:裙 → `icy powder-blue button-front vest over a ruffle-cuff shirt with matching tailored trousers and gloves`,同为冷调淡蓝、按扣/荷叶元素。

最多一个稍亮点缀色,其余压在该档色系里;守着装底线(端庄全覆盖、无纹身穿孔、穿裙配同色系安全裤)。**这三套造型与上面三档情绪的「调色子句/前置风格句」一一对应**。

### 阶段 1 · Final_Video_Spec(已并入开拍前卡)

情绪档 / 画幅 / 画质**已在开拍前那张卡里问过**(第 7\~9 项),此处不再另开卡。**时长不问——段数/总长由【选段】确定**(选了几段 ≤15s = 几段视频 = 总长),每段 = 一条 ≤15s,装配顺接。粗粝/梦感靠颗粒与调色,不靠低分辨率。

> spec 随卡一并确认,无需单独暂停。

### 阶段 2 · 故事板

- **造型图**:按四种情况用 **Seedream 5.0 Pro 出一张 16:9 白底 2K、横排 4 个不同全身造型**(**无尾串**;只造型参考图作图参考、人像不喂)→ 用户**从 4 个里选 1** → **暂停确认** → 用 **Lib Image 据所选造型扩写 16:9 白底三视图**(**硬性:必须把选定的那张 Seedream 造型图作为图输入/参考连线接入 Lib Image**,不连线三视图会跑偏、与所选造型不一致、整步作废;三视图款式/颜色/廓形/面料/比例与所选造型图逐项一致;真人模特;**一张图内、全身左/中/右三视、不放大头**;**有人像参考图→人脸纯白圆贴遮 + 右下角中文小字标注、无→保留脸**)→ **再暂停确认**。**造型守底线**(端庄全覆盖、不大面积透明、高领、裙及膝或更长、皮肤无纹身无穿孔)。**全片服装造型锁定不变;仅用户明确要求换装时才再出"造型1/造型2"**。

- **场景**(紧接三视图确认后):按选定段数(= 地点数)**先给 3–4 个开放场景选项、也允许自描述 → 用户选定用哪几个场景后立即按阶段 3 出图**;自描述则照其意 + 套情绪档调色 + 零文字 + 全景无人 + 超现实但写实。同一地点多分镜共用选中那 1 张。

- **分镜脚本(生视频前必出、需确认,用表格)**:逐段逐镜列,列固定为 **段/镜号 | 音频切片(段级) | 画面(角色表演 + 场景 + 裂缝)| 时长(s)| 运镜(手持/升格)| 表演/表情 | 与上下段衔接**。**每段第一列后紧跟「音频切片」列,写清本段用**哪条切片\*\*(切片编号)+ **有人声(→对口型)/ 器乐(→不对口型)**——生视频时照此把该切片连线接入 Seedance,把音频写进表能显著降低"漏连音频、口型/BGM 全丢"的概率。示例:

  段/镜音频切片画面时长(s)运镜表演/表情衔接1-1切片①(有人声→对口型)主角已在泳池间水面上,近景,开口跟唱4慢 push-in缓睁眼、轻呼吸、口型对上歌词开场即含人、不空镜1-2↑ 同段切片①连续运镜升起,中景4升格发丝飘动、若有所思承上镜方向连续运镜2-1切片②(器乐→不对口型)走入花海,中景4慢平移不唱、轻旋身承 1 段末镜:主体位置/运镜方向延续

  **每 15s ≥4 镜**,标升格落点;**第一镜不要空镜——角色一开始就在画面**;**多段时每上下两段(上段末镜 ↔ 下段首镜)必须有逻辑 / 镜头语言关联**(动作承接、构图呼应、运镜方向、主体位置/情绪衔接),让段间干净切也顺;**全片不叠化**。**每段的「音频切片」是阶段 4 连线的依据——按表把对应切片连到 Seedance 音频输入口(硬性)。**

- **音乐(阶段 0 已就绪:绑定/生成 + 切片 + 选段)**:此处按**所选各切片**的节拍标转场/升格落点;并标出**哪些段做对口型(有人声)、哪些器乐段不做**。

> 暂停确认(造型图 + 三视图 + 场景图 + 分镜脚本 +(无音频时)音乐)。

### 阶段 3 · MJ V8.2 场景图(在三视图确认后紧接执行)

描述选定的全景空场景(空间类型 + 布局 + 重要物体 + **一道超现实裂缝** + 构图),**超现实但照片级写实、不含人、零文字/logo/图案**,套所选情绪档调色子句,接场景种子尾串(见速查)。**用户选定用哪几个场景后立即出图**:各地点各 1 组 4 张全景,**可一次性同时生成多组**,不必逐个串行等待;生成后**每个地点各自四选一**。同一地点多分镜共用选中那 1 张。

> **每个地点都必须四选一确认**(可一起出、分别选);所有场景确认后再进入下一阶段。

### 阶段 4 · Seedance 2.5 视频(每段一条,时长=该段音频向上取整后裁剪,一条一条生)

prompt 结构(顺序,英文书写):

1. **前置风格句**(按情绪档取甜暖/空灵/微寒,全片统一)。
2. **角色组装 + 首帧含人物**:三视图锁造型/身形 + 人脸参考(**有人像参考图→原图/视频锁真脸;发型先问用户:保持参考图发型 / 换成三视图发型,按选择写进 prompt。无人像→以三视图为主,脸与发型取自它**)。写明"脸取自人脸参考、造型取自三视图、发型按用户所选、放进场景图,保留真实长相"。**场景图当"空间/风格参考",不要当成必走的空场首帧——第一镜角色就在画面里**,prompt 明确 `the character is already present in the very first frame, open on the subject (medium/close), do NOT begin with an empty room establishing shot`,避免开头空镜。**合规**:端庄全覆盖、不大面积透明、高领、裙不过短、皮肤无纹身无穿孔;**穿裙写** `wearing matching-tone modesty shorts underneath, fully covered and modest`。**服装造型与三视图完全一致、全片全程不变。**
3. **对口型 + 音频连线(有人声的段)**:**照分镜表格该段「音频切片」列,把对应切片节点连线到 Seedance 2.5 的音频输入口**——硬性,不连线口型驱动与 BGM 都拿不到、整段废掉(表里已写清用哪条切片、是否对口型,照做即可)。把该段 **≤15s 音频切片作音频锚点接入**,人物**嘴型/下巴与传入音频完全一致**(`lips and jaw precisely synced to the incoming audio, natural gentle singing expression, dreamy and soft`);**严禁把真实歌词写进 prompt**;**纯器乐段角色不唱、但该段切片仍连线接入并作 BGM 保留**(`no singing, dreamy performance only`——不要写任何"无音乐/无 BGM")。
4. **分镜**:`Shot1 …(camera continues / slowly moves to)… Shot2 …`,一条连续(时长=该段音频向上取整)、**≥4 镜**;镜头间靠**连续运镜/缓慢移动衔接**或少量**干净卡切**;**禁止写 dissolve / 叠化 / 淡入淡出 / morph**(AI 生成叠化通常糊脏)。每镜 = 景别 + 运动(慢手持/升格)+ 表演。
5. **运动**:`slow dreamy camera, natural handheld with subtle breathing motion`;升格镜 `slow motion / overcranked, weightless floating`;一镜到底仅按需。
6. **音频 + 时长 + 零文字**:生成画面**始终零文字/logo/无烧录字幕**(字幕如需在阶段 5 按所选语言叠加)。**每段靠连线接入的音频切片驱动口型 + 作 BGM**;**prompt 绝不出现** `no music` **/** `no audio` **/** `no sound` **/** `no BGM` **/** `无音乐` **这类字样**(会压掉口型与 BGM);传入音乐一律作 BGM 保留、不改原音频、**不写真实歌词**;器乐段只写"角色不唱、只做表演"。**时长 = 该段音频向上取整到整秒**,阶段 5 再按音频实际时长裁剪。负面 `text, words, letters, numbers, logo, watermark, extra patterns, cartoon, illustration, stiff, rigid, frozen, robotic motion, dissolve, crossfade, fade transition, morph, tattoo, piercing`(合规靠**正向词**实现,负面**不写**任何涉黄/暴露敏感词、也**不写 no music/no BGM**)。

**表演默认**(用户没写时按 dreamcore 注入,每镜≥1 表情+1 动作,慢/轻):`serene wistful presence, slow ethereal movement, gentle gaze drifting, weightless dreamlike detachment, soft turning of the head, dress and hair drifting`。\
**通用治僵硬(每镜都加)**:`subtle breathing with chest gently rising and falling, hair and fabric micro-movement, expression slowly shifting (e.g. serene → faintly wistful), a slow soft blink, relaxed natural posture, natural unhurried lifelike movement easing in and out`(对口型时 `jaw and lips actually moving to the incoming audio`)。

> 一条一条生,逐条确认。

### 阶段 5 · 装配(video_assembler)

多段顺接时,**每两段衔接处用干净切,但靠逻辑 / 镜头语言承接**(匹配动作 / 构图 / 运镜方向 / 主体位置 / 情绪,见分镜脚本)让切口顺;**全片不允许出现叠化 / 溶解 / cross-fade**(梦核也不闪切、不闪大字);**字幕/标题只叠加、绝不烧进生成画面**;logo PNG 可叠;**每段按该段音频实际时长裁剪**(生成时向上取整、此处裁回)。**音乐:不要把原音乐当单独一轨再拼进去——直接沿用各段生成视频里已自带的音乐**(生成时喂入并原样保留的那段音频),各段连自带音轨一起顺接即成连续配乐,口型与音乐完全对应、全片连续。**字幕(仅当卡里选了"需要")**:按所选语言把字幕**叠加**在成片上(只叠加、不烧进画面)。引导导出。

---

## 参考数据

### 节奏 → 每 15s 镜数(dreamcore 版,硬底线 ≥4,以连续运镜衔接为主)

情绪/节奏镜数转场与手法极慢空灵4一镜流动式连续运镜为主、几乎不切;长镜 + 升格,靠微动与表演不滞留慢板抒情4–5连续运镜衔接为主,偶尔干净卡切;升格落点明确中速律动5–6连续运镜 + 少量卡拍干净切;长短镜交替

> 无论几镜,都在一条 ≤15s 里一次性生成;**镜头间靠连续运镜衔接,全片不做叠化/溶解**;段间靠承接的干净切,别全程生硬硬切。

### 场景库(每情绪档取倾向,均为全景无人、含一道超现实裂缝、超现实但写实)

- **甜暖怀旧**:怀旧少女卧室 · 室内泳池间 · 花海/草地 · 旧商场中庭 · 阳光客厅。裂缝:水面映出不存在的云、漂浮的泡泡、过曝到发光的窗。
- **空灵纯净 / 失重忧郁**:云朵/天空卧室 · 无尽白走廊 · 水下房间 · 镜面无尽空间 · 纱幔房间。裂缝:失重漂浮、走廊无限延伸、水与空气界限消失。
- **微寒梦魇**:空教室 · 旧 CRT 客厅 · 镜屋 · 雾中空旷场 · 静止的游乐场。裂缝:会动的静物、停住的旧钟、镜中慢半拍的倒影、雾里的静止。

> "超现实裂缝" = 反常倒影/漂浮物/无尽延伸/会动的静物/过曝光斑等(超现实但写实,不血腥不惊悚)。长片地点不够可重访同一地点(换光线/裂缝)。

### 注意

- **开拍前只用一张问询卡**(音频有无 → 曲风+主题\[仅无音频\] → 人声性别+语言 → 有无人像/造型参考图 → 人种\[仅无人像\] → 字幕 → 情绪档 → 画幅 → 画质);**主角性别=人声性别、人种按语言推荐、时长由选段定,都不单独问**;问完停下等上传。
- **无音频先生成音乐(dream pop/ambient)→ 暂停等用户确认满意 → 才切片**;切完确认切片,再选段。风格字段与歌词字段分开,别把描述词当歌词唱;音乐提示词 ≤ 1024 字。
- **音频·口型·BGM(核心)**:切片(≤15s、连续)+ **拿准确歌词仅内部对齐、绝不写进 prompt** → 选段定时长;**生视频必须把选定音频切片连线到 Seedance 2.5 音频输入口(硬性)**、作音频锚点驱动口型;prompt 只写"口型与传入音频一致"、**不写真实歌词**;**传入音乐作 BGM 保留、不改原音频、prompt 不写 no music/no BGM**;**生成时长=音频向上取整→按实际裁剪**;器乐段不唱但切片仍连线作 BGM。**最终合成用各段生成视频自带音乐、不拼原音乐单独轨。**
- **模型**:造型图 = **Seedream 5.0 Pro**(2K、无尾串、横排 4 造型、四选一);三视图 = **Lib Image**(16:9、全身左/中/右三视、无大头;**硬性:必须把选定的 Seedream 造型图作图输入/参考连线接入,不连则三视图跑偏、与所选造型不符、作废**;款式/颜色/廓形/比例与所选造型逐项一致;有人像→白圆贴遮脸+右下角中文小字,无→保留脸);场景图 = **MJ V8.2**(固定 dreamcore 种子 `--sref 4658243766 --profile yp7vzjb`);视频 = **Seedance 2.5**。**人脸参考图不喂造型模型、只在 Seedance 喂;造型参考图才作 Seedream 图参考。**
- **发型**:有人像参考图时,生视频前问用户"发型用参考图的 / 用三视图的",按选择写 prompt;无人像时以三视图发型为主。
- **服装造型全片锁定不变**(每条 prompt 强调与三视图一致);仅用户明确要求换装时例外。
- **造型合规 + 人物底线**:端庄全覆盖、不大面积透明、高领、裙及膝或更长、非性化;**皮肤干净无纹身、无穿孔**(戒指/项链/发饰 OK);穿裙带同色系防走光安全裤;合规用正向词、负面区不写涉黄敏感词,`纹身/穿孔` 中性词可进负面。
- **三视图排版**:一张图内、16:9,只全身正/侧/背三视、去掉所有大头;有人像→白圆贴遮脸 + 右下角中文小字「人脸单独提供 · 此图仅用于服装造型参考」。
- **字幕**:仅当卡里选"需要"时,阶段 5 按所选语言叠加(不烧进生成画面)。
- 不写真实偶像/歌手姓名、不写真实 MV 名当 prompt,复现美学不复现具体作品/某人;风格锚点用描述性词。
- 用户只要片段/单镜、或已指定场景造型时,在不破坏 每段≤15s且时长=音频向上取整后裁剪/口型与音频一致/不写真实歌词/不改原音频/音乐用生成视频自带不拼单独轨/服装造型全程锁定/主角性别=人声/每15s≥4镜/全片不叠化/零文字规则下按需做。
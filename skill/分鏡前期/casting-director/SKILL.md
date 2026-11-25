## 一、审美准则

### A. 长相定位

**精致中式漫感**：主体一律写 `Chinese`（不写 East Asian，易偏韩）。骨相清晰、上镜化，中和一点写实感，不要过度漫画假感。

### B. 皮肤（硬规则）

写实但细腻干净。关键词：`smooth clean realistic skin with a refined natural finish, subtle fine texture and minimal barely-visible pores, looking real but polished like high-end editorial retouching, never plastic, never rough bumpy blemished`。不用 `lots of visible pores`（坑洼），也不用 `flawless glass-skin`（塑料）。目标：`smooth but natural`。

### C. 反廉价四原则

①写实肤质 ②柔性体积光（额头/鼻梁/颧骨高光+脸侧阴影）③暖调通透有subsurface透光感 ④细节真实不过度锐化。

### D. 两条统领原则

- 冷暖对比=高级感（冷调肤+暖调唇眼）
- 去标签化=通用性（无logo、无强时代符号、配饰克制）

### E. 纯白背景（最高硬规则）

**所有资产背景必须纯白 #ffffff**，任何情况不例外。正向：`plain seamless pure white #ffffff studio background`。否定：`no grey, no off-white, no coloured or textured background`。

### F. 五官（按性别分流）

**最高脸型硬规则（全角色，反派也不例外）**：脸型骨相清晰利落、协调上镜，下颌线干净不松垮，不宽不方不肉，上下脸协调。**脸由「五官」+「整体气质」字段驱动，服装风格绝不介入脸（见第五节）**。

通用锚定：

- 女：`slim refined oval face with a clean sharp well-defined jawline, harmonious proportions, NOT wide, NOT square, NOT a heavy or sagging jaw`
- 男：`long clean face with a sharp angular well-defined jawline, NOT wide, NOT round, NOT a soft sagging jaw`

**女性五官**：偏窄长脸+平直微挑眉+长眼微上扬+卧蚕+高挺鼻+豆沙唇；妆：伪素颜上镜感（底妆发光+轻修容+卧蚕高光）。

**男性五官**：长流畅脸+剑眉+深邃桃花眼+高挺鼻+暖红润唇+黑色碎发中分；三档气质参考（仅参考不是模板）：奶狗初恋/禁欲总裁/成熟熟男——同型角色务必分化，不套同一套五官表情。

### G. 差异化引导（柔性，agent自判）

- **多角色**：拉开脸型骨架/五官量感/气质，每人提炼1-2个专属记忆点写进CHARACTER段。
- **单角色**：优先服从角色卡个性，不收敛成标准网红美人。
- **素人**：允许非标准五官（圆脸/宽脸/塌鼻/单眼皮等），不套美人共性。
- **铁律**：①差异化只作用于不同角色；同一角色多资产必须同脸（资产参考锁身份）。②角色卡指明相似关系时让位于角色卡，不硬掰两极。③不破坏单角色高审美底线。

---

## 二、核心翻译原则

1. 主体写 `Chinese`
2. 气质用状态化语言（白切黑→`hiding her sharpness`；深情隐忍→`a deep restrained gaze holding quiet emotion`）
3. 脸型用对比+否定式卡死
4. 保留电影术语（halation/anamorphic/bokeh/aegyo-sal不译）
5. 皮肤永远写实（准则B），与漫感程度无关
6. 去标签化+冷暖对比（准则D）

---

## 三、定脸生成

一次图像生成能力调用。prompt拼接顺序：

```
CHARACTER: [年龄+Chinese+气质状态化+脸型(对比+否定式)+眉/眼/鼻/唇，按性别套准则F]

SKIN (priority, refined realistic): [smooth clean realistic skin, refined natural finish, minimal barely-visible pores, polished like editorial retouching, never plastic+妆+发型]

OUTFIT: [按第五节推理的完整造型，上衣绝不塞进下装，无logo，配饰克制]

[COMPOSITION锁定块，原封不动]
[RENDERING锁定块，原封不动]
[SHARPNESS锁定块，原封不动]
```

```
图像生成能力(prompt="...", title="<角色名>定脸", tag="character")
→ 返回资产归档标记（记下，供后续引用）
```

---

## 四、锁定块（逐字复制禁止改动）

### 身份引用语（垫图时放prompt开头，首次定脸不放）

```
以〈定脸资产归档标记〉作为该角色的身份参考，生成同一人物的全新图像，保持脸型骨相、下颌线、眼型、五官结构与参考完全一致。从头渲染一张全新图像，不得直接复制或粘贴参考图。
```

### COMPOSITION

```
构图（严格锁定，逐条执行，标准证件照美颜近景）：
- 景别：头颈紧景特写。发顶紧贴画框顶边，头顶上方无留白。画框底边切于锁骨/上胸口。脸部高度约占画框垂直高度的55–60%。NOT拉远至显示肩膀、西装身段或半身。
- 居中：头部水平居中，面部中线（鼻梁）与画框垂直中线精确对齐。脸在画框内垂直居中。
- 发型裁切：头发自然垂落两侧，左右两侧发丝被画框边缘自然裁切——头发整体宽度超出画框，只露出内侧部分。
- 朝向：完全正面视角，头部绝对水平，零偏转零旋转，双眼直视镜头，下颌微收，颈部完整可见至锁骨。
- 表情：[按角色气质填写分化，不套同一种表情。清冷女：神情平静内敛，嘴唇轻合，不笑。治愈男：表情温和放松，嘴角带轻微自然微笑。]
- 画幅：竖向3:4画幅，左右对称构图。
```

### RENDERING

```
渲染：纯净无缝纯白#ffffff背景。柔和电影感美颜布光，面部有自然的明暗塑形——额头、鼻梁、颧骨保留清晰高光，脸侧有柔和阴影，呈现三维立体体积感，NOT平光NOT均匀补光。皮肤温润通透，有丰富的subsurface透光感与自然肤色渐变，高端杂志级写实质感，竖向3:4画幅。
```

### SHARPNESS

```
清晰度：将整个头部渲染在同一个清晰焦平面内——脸部、眼睛、睫毛、耳朵、耳饰、发际线及所有发丝（包括头部两侧的头发）全部同等清晰、对焦准确、细节完整，从脸部正面到两侧发丝保持同等精细度。皮肤质感干净细腻，有自然肌理与极细微几乎不可见的毛孔，真实但经过高端修图级润色。头发与耳朵NOT模糊NOT虚焦NOT失焦。通过高分辨率与精细细节渲染实现均匀清晰，NOT靠压平光影或降低对比度来实现。始终保留柔和电影感光线、脸侧体积阴影与温润通透肤色。no浅景深效果，no模糊发丝，no平板均匀布光，no灰白发死的肤色，no粗糙坑洼皮肤，no重度放大毛孔，no过度磨皮塑料感。
```

> **禁用词**：prompt中严禁 `narrow aperture / large depth of field / no soft-focus / no bokeh on the face`——会触发全局平光、肤色发灰。全脸清晰只靠SHARPNESS块。

---

## 五、服装推理

**三步推理**：①看「适用人物」定品类（霸总→商务正装；素人→精致休闲；古风→汉服；甜妹→清新明快）②看「整体气质」定调性（冷感→利落剪裁；治愈→柔软针织）③统一升档（高级/有质感/无logo/配色克制）。

**硬规则**：

- **服装风格绝不污染脸**：OUTFIT调性只作用于服装推理，绝不外溢到脸的骨相/五官/表情/肌肤。例外：角色卡在五官/气质字段直接写了脸的特征，或随服装配套的发型/头饰/妆容年代感（属造型层不在屏蔽范围）。
- **上衣绝不塞进下装**：`untucked, worn loose over the waistband, never tucked into trousers or skirt`
- **男性裤型默认**：直筒或微阔垂坠长裤、裤长盖脚面。`NOT tapered, NOT cropped, NOT skinny, ankles not exposed`。角色卡明确要求可破例。
- 无logo、配饰克制（珍珠/银/钻/简约表等）。反派可穿穷酸破旧。

**备选库**：清冷千金→象牙白西装+真丝内搭；霸总→硬挺黑/炭灰西装+白衬衫领口微开；治愈熟男→燕麦针织或浅灰休闲西装；甜妹→奶油色/淡彩针织；素人→质感纯色T/白衬衫；古风→立领或交领汉服；长辈→软肩西装/优雅针织。

---

## 六、身材气质校准（全身图核心）

全身图必须按角色定位自动校准四变量：①头身比 ②身材量感 ③姿态气场 ④服装廓形。

### 头身比（必须写成实句，不能只写数字）

- **女性统一7头身**（禁止超8）：`natural well-balanced 7-heads-tall female proportion, the head about one seventh of the full body height`
- **男主/古风男/素人男：8头身**：`well-proportioned 8-heads-tall figure`
- **霸总/强势男：8.5–9头身**（仅此型）
- **反派：不优化**：`realistic everyday body proportion, minimum 7 heads tall, NOT idealised or stretched, NOT a squashed compressed body, NOT an oversized head on a short stocky frame`（脸型骨相质量仍按准则F）
- **儿童：3–4头身**：`cute chibi-leaning proportion, about 3 to 4 heads tall`

**双向否定式（必写）**：`keep the specified head-to-body ratio strictly; NOT a large head on a short body, NOT an exaggerated 8.5-9 heads elongated frame unless a 霸总-type male lead. Shoulders natural width (female ~1.6 head-widths, male ~2 head-widths).`

### 校准表

角色型身材量感姿态气场服装廓形**霸总/强势男**tall slender 8.5-9 heads, long lean torso, long legs, low relaxed shoulder, lean NOT muscularcool languid editorial, weight on one leg, shoulders dropped, aloof gaze, one hand in pocketoversized dropped-shoulder suit, wide-leg trousers, NOT slim fitted**治愈/温润男**tall steady, naturally broad shoulders, healthy solidupright relaxed, warm easysoft knit/blazer, straight full-length trousers**高级素人男**natural healthy fitrelaxed naturalquality casual, straight full-length trousers**千金/清冷女**slim slender elegant, delicate uprightpoised cool composed, aloofminimalist sharp tailoring**甜妹/少女**petite slim youthfulsweet relaxed lightfresh light layered**高级素人女**natural healthy slimrelaxed naturalquality casual basics**古风男/女**upright dignified / slender gracefulserene classical poisehanfu robe, flowing**长辈男/父**mature slight fullness, solidcalm dignifiedrefined sober blazer, straight trousers**长辈女/母**mature graceful, slight softnesscalm gentle uprightelegant knit/blouse**反派男**per card, realistic NOT idealisedslack or stiff, petty mean airdated/cheap/shabby**反派女**per card, realisticsour stiff or slackgarish/shabby**儿童**chubby soft 3-4 headplayful childlikecute kidswear

**霸总气场三要素（仅男主/霸总，绝不套女性）**：①大廓形服装（oversize落肩西装）②拉长比例（8.5-9头身）③慵懒疏离姿态（重心偏一侧/微slouch/aloof gaze/单手插兜）。女性统一7头身，不拉长。

**男主身材原则**：气场来自骨相+眼神+疏离姿态，不是肌肉。默认清瘦挺拔有骨相，不做健硕猛男（除非角色卡明确要求）。

---

## 七、全身立绘（一步法）

> 前置条件：定脸已通过确认门。

一次图像生成能力，资产参考传入定脸资产归档标记，prompt开头写`〈定脸资产归档标记〉`锁脸，画幅`aspect_ratio: "3:4"`。

```
图像生成能力(
  prompt="Using〈定脸资产归档标记〉for face identity，同一人的全身站姿立绘，<头身比实句+身材量感+姿态气场+服装廓形（第六节）>，双向比例否定式，vertical 3:4 full-body portrait, head-to-toe inside frame, centered, plain seamless pure white #ffffff background，<SKIN/SHARPNESS锁定块>",
  title="<角色名>全身立绘", tag="character", aspect_ratio="3:4",
  资产参考=["<定脸资产归档标记>"]
)
```

比例压不住退两步法：先单独生比例正确的全身模板资产节点，再连同定脸节点垫图重出。

---

## 八、人物三视图（可选）

16:9分屏：左半=全身三视图（正面/侧面/背面），右半=面部特写。同时垫定脸+全身两个资产归档标记。

```
图像生成能力(
  prompt="16:9 split-screen character board。使用〈定脸资产归档标记〉锁面部身份、〈全身资产归档标记〉锁身材/服装/比例。左半屏三张等大全身图并排—front/full profile/back，standard upright model stance；右半屏单张正面大脸特写。same one person, identity consistent, identical face hairstyle outfit skin tone, plain seamless pure white #ffffff background.",
  title="<角色名>人物三视图", tag="character",
  资产参考=["<定脸资产归档标记>","<全身定稿资产归档标记>"]
)
```

> 能力边界项，可能需多跑或退分块方案（左右各自单独出再拼）。

---

## 九、表情九宫格（可选）

3×3九表情，画幅`aspect_ratio: "3:4"`，垫定脸资产归档标记。

**默认表情顺序**：面无表情/喜(抿嘴微笑)/怒/哀/乐(露齿)/悲(含泪)/震惊/愤怒/迷茫。

**关键规则**：近义表情做强度区分；头全部摆正（不歪头）；每格居中不切顶；防大小眼；一致性约束（same one person）；加深景深。

```
图像生成能力(
  prompt="使用〈定脸资产归档标记〉作为身份参考，same person in every panel, identical face hairstyle skin tone across all panels。九宫格：3x3 grid，每格只有表情不同：<九表情顺序>。头摆正/居中不切顶/防大小眼/近义表情强度区分/一致性/深景深。vertical 3:4 format, 3x3 grid evenly fills canvas. plain seamless pure white #ffffff background.",
  title="<角色名>表情九宫格", tag="character", aspect_ratio="3:4",
  资产参考=["<定脸资产归档标记>"]
)
```

> 能力边界项，脸飘时降级：分两次各出部分表情，或单表情逐张生成再拼。

---

## 十、补丁块（按需追加）

### 补丁A · 纯白底+发丝边缘

```
BACKGROUND (strict pure white with clean hair edges): completely clean seamless pure solid white #ffffff backdrop, no gradient, no grey, no off-white. Subject cleanly separated from background with sharp clean edges. Hair, hairline and outer strands must have clean sharp well-defined edges — NO wispy strands fading into background, NO semi-transparent hair edges, NO grey halo, NO foggy fringe. Keep natural volumetric light on face.
```

### 补丁B · 皮肤平整（仅皮肤发糙时救急，必须配C一起用）

```
SKIN (smooth and even): clean smooth even-toned skin, minimal barely-visible pores, no rough bumpy surface, no visible blemishes, no enlarged pores — premium editorial skin, still looking real NOT plastic NOT waxy. Keep natural skin tone and soft volumetric light.
```

### 补丁C · 皮肤真实肌理（配B用或单用救"皮肤太平"）

```
SKIN (refined but real): clean translucent skin keeping real natural texture — fine subtle pores, soft surface micro-detail, healthy natural sheen, looking like genuine high-end-retouched real skin, NOT flat smoothed waxy plastic, NOT over-airbrushed poreless. Skin reads as real human skin, clean and free of blemishes but not perfectly smooth.
```

---

## 十一、3D漫剧质感补丁（「漫剧」触发，与真人完全隔离）

触发词：「漫剧」「3D漫剧」「3D角色」「三维」「CG」「三渲二」——「漫剧」单独出现即触发。未触发一律真人写实，本节全部忽略。

**铁律**：①整段替换，绝不把真人质感词和3D质感词混写同一条prompt。②只覆盖质感层，结构层（构图/纯白底/头身比/确认门/资产参考）照常适用。③真人prompt绝不出现3D词。

### 11.1 3D质感目标

- **画风定性**：`high-end 3D CG character render, cinematic game-quality rendering, realistic-stylised 3D in the style of high-budget game cinematics or animated feature films, clearly a rendered CG character not a photograph, not flat 2D anime, not cartoonish`
- **皮肤-女性**：`semi-realistic 3D CG skin, between photorealistic and stylised — smooth clean surface with subtle subsurface scattering warmth, soft natural skin luminance, very fine barely-visible micro-texture and pores (present but refined, not raw), rendered skin that reads as beautiful and slightly elevated beyond real but clearly not a photograph — NOT flat poreless cartoon skin, NOT fully photoreal human skin, NOT wax or plastic finish, NOT milky white 2D-anime complexion, NOT flawless glass-skin with zero texture`
- **皮肤-男性**：`semi-realistic 3D CG skin with natural micro-detail, visible fine pores and subtle surface texture, warm subsurface scattering, rendered quality clearly above photographic — slightly elevated and refined but grounded in realism, NOT flat cartoon skin, NOT fully photoreal`
- **头发**：`3D-modelled hair with clean defined strands, soft specular sheen and structured flow, clearly CG-rendered, NOT photoreal flyaway hair, NOT flat 2D hair`
- **眼睛**：`luminous CG eyes with crisp catchlights, clear layered iris depth, slightly enhanced beyond real, clearly rendered not photographic`
- **光影/背景**：`clean three-dimensional CG studio lighting, clear volumetric light-and-shadow modelling, plain seamless pure white #ffffff background`

**3D质感校准线（介于真人与漫画之间）**：目标质感参考——影视级游戏CG（如《黑神话》《原神》高精度渲染档位），皮肤有微细节但比真人更干净精致，有subsurface但不是透明瓷感，明显是渲染而非照片。**必须远离**：①纯白无瑕零质感的二次元瓷肌（太漫画）②真实毛孔坑洼的写真质感（太真人）③蜡像/塑料感（过度磨皮）。

### 11.2 覆盖表（启用3D时）

真人原段3D替换为RENDERING里photorealistic词`high-end 3D CG character render, cinematic game-cinematic quality, clearly a rendered CG character not a photograph`SKIN段写实肤质词按性别取11.1皮肤词（女性含NOT否定式必须完整写入）SHARPNESS里realistic skin一句换对应性别3D皮肤句，其余清晰度内容保留准则E的85mm镜头质感`rendered with a virtual 3D camera, cinematic CG framing`

### 11.3 脸型（3D模式）

**防崩底线**（替代真人准则F强规则）：

```
FACE (minimal integrity floor only): both eyes present and roughly level, features not melted or fused, face not grossly distorted. NOT an overly long lower face, NOT an excessively elongated chin pulling the lower third too deep. Do NOT impose any preferred face shape or proportion. Let face shape vary freely per character.
```

**高审美导向**（必写，与防崩底线并列）：

```
AESTHETIC (high-end, striking, memorable): a strikingly beautiful high-fashion-caliber CG face with a distinctive memorable look and strong screen presence, refined elevated features, editorial model-tier attractiveness — not a plain safe generic pretty face, each character visually distinct and unforgettable.
```

**差异化引导**（柔性，同真人准则G逻辑，分寸铁律相同）：多角色拉开/单角色防模板/素人放开非标准五官。

### 11.4 3D模式调用示例（定脸）

```
图像生成能力(
  prompt="<CHARACTER:年龄+Chinese+气质+五官+专属记忆点，中文> <FACE防崩底线> <AESTHETIC高审美导向> <按性别取11.1皮肤词> <3D头发词> <3D眼睛词> <OUTFIT中文> high-end 3D CG character render, cinematic quality, clearly CG not a photograph, not flat 2D anime. <COMPOSITION锁定块原文> <RENDERING锁定块：photorealistic词换3D定性句> <SHARPNESS锁定块：realistic skin句换3D皮肤句> plain seamless pure white #ffffff background.",
  title="<角色名>定脸（3D漫剧）", tag="character"
)
```

全身/三视图/九宫格3D版：在各自节基础上按覆盖表替换质感段，脸型换用11.3两块，其余照旧。

---

## 十二、执行流程

1. **对齐方向**：读取剧本基准文件 `cast-style-{剧本名}.json`（存在则加载质感参数，不重新推理质感层；不存在则此为第一个角色）→ 定质感模式（真人or3D，见漫剧触发规则）→ 判差异化（多角色拉开/单角色防模板）→ 字段缺失用 向用户提问确认 对齐，否则说明补全内容直接执行。

2. **拼prompt生成定脸**：按第三节拼接，三个锁定块逐字写入，tag `"character"`，记录资产归档标记。

3. **【确认门·硬性卡点】**：向用户提问确认面部是否满意，未明确通过前绝不生成后续资产。不满意则改prompt重出再回确认门。多角色时全部面部确认后才统一往下。

4. **【4.5 剧本质感存档】**（首个角色且基准文件不存在时）：确认通过后立即用写入文件存档 `cast-style-{剧本名}.json`，内容：质感模式/皮肤基准词/渲染定性词/3D档位。剧本名取不到时向用户提问确认。

5. **多选资产**：向用户提问确认（multi_select）询问要生成哪些：全身立绘/表情九宫格/人物三视图。三视图依赖全身，勾了三视图未勾全身则先补全身。

6. **按选生成**：全身→第七节（3:4，垫定脸）；九宫格→第九节（3:4，垫定脸）；三视图→第八节（16:9，垫定脸+全身）。

7. **收尾**：简述每个产出（角色名+资产类型+资产归档标记），提示OUTFIT块可替换造型重生成。

---

## 十三、边界与硬规则汇总

- **纯白#ffffff**：最高硬规则，所有资产所有步骤。
- **脸型骨相**：清晰利落下颌、上下脸协调，全角色（含反派）不降。服装风格绝不污染脸，只由五官+气质字段驱动。
- **头身比**：女性统一7头身（禁超8）；男主8/霸总8.5-9/素人男8/反派最低7/儿童3-4。必写双向否定式。
- **男裤**：默认直筒/微阔垂坠盖脚面，禁束脚（角色卡明确要求可破例）。上衣绝不塞进下装。
- **时装大片拉长比例**：仅限男主/霸总，绝不套女性。
- **反派护栏**：NOT idealised只管身材量感/气场，绝不波及脸型骨相。
- **确认门**：硬性卡点，未通过绝不生成后续资产。
- **锁定块**：写入prompt时原封不动，不改不精简。
- **剧本质感锁定**：同一剧本所有角色质感统一，靠 `cast-style-{剧本名}.json` 文件跨对话锁定；后续角色读取文件复用质感层，不重新推理。

**脸型崩坏排查**：下半脸宽/方/松垮→①检查准则F脸型词是否写入；②检查反派NOT idealised是否误外溢到脸；③加重否定式 `NOT a wide square heavy jaw, NOT a bottom-heavy sagging lower face`。

**虚焦/构图排查**：头发耳朵虚焦→查SHARPNESS块是否完整写入；构图漂移→查COMPOSITION块+资产参考引用是否正确。prompt禁用 `narrow aperture / large depth of field`。
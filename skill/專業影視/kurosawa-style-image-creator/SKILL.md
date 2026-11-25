# 黑泽明电影风格图片生成（彩色 / 黑白）

四个可执行风格词：**黑白·中文单段** ＋ **彩色三支英文串**（战场／人物／氛围）。按分支取范例片段重组后填入 MJ 节点出图。

## 总原则：每个词都要有出处

1. 每个英文词组、每个 `--no` 词、每句质感／色调／光位描述，都必须能在**本支范例**里逐字找到出处；不得仿造、不得拼接新词、不得把中文范例直译成英文当写法推荐。
2. 做法是**从本支范例抽取现成片段重组**。某支缺某种表达，宁可少写一句，也不要自造补上。
3. **不得跨支借词**：战场、人物、氛围各用本支 4 条范例，黑白用本支 2 条。
4. **唯一例外**：`--no` 里的去黑边三词 `letterbox, black bars, cinematic bars`（使用者授权，非节点提炼）。除这三个词外不开口子。

## 通用使用说明（全分支）

- **范例原文中的** `--ar` **一律删除**，其余 `--style raw` 与 `--no` 保留。范例逐字保留只为留存参照原貌，不等于可直接提交。
- **正文不写任何画幅参数**（`--ar`／`--aspect`／比例）。画幅只由节点 ratio 字段决定：`1:1`／`9:16`／`16:9`／`3:4`／`4:3`／`3:2`／`2:3`；`21:9` 不被接受（422 拒绝）。宽幅选 `3:2` 或 `16:9`，Academy 选 `4:3`。此条只为避免与字段重复表达，**不是防黑边手段**。
- **每次出图都在** `--no` **末尾挂去黑边三词**：`letterbox, black bars, cinematic bars`。（受控对照：不挂 4/4 带上下黑边，挂后 4/4 无；单次 4 张样本，非统计学结论，仍需逐张检查、偶现时挑图。黑边是模型逐张生成进画面的电影遮幅，不是容器比例填充；诱因推测为 `cinematic film still` 等电影语汇，属推测、未经单独验证。）
- **不得为去黑边删风格锚点**：`cinematic film still`、`in the style of Akira Kurosawa's Ran (1985)`、`Kurosawa-esque`、`1980s film softness with gentle grain`、`deep crushed blacks, coarse film grain` 均有出处，必须保留。
- **单语言**：彩色一律纯英文，黑白一律纯中文；同一提示词内不得中英混用（`--no` 参数尾巴除外）。
- **提示词上限 1024 字符**，超出直接提交失败，长 `--no` 要留余量。
- **stylize／weird／chaos（100／50／5）不能靠 quality_spec 落地**：只能写进英文正文或编辑器手填，不得声称已落地。

---

## 分支一：黑白·中文单段（2 个参照）

**结构规则**：纯中文；**只写一整段连续叙述**，句号／分号／顿号断句，不分行、不分条、不加小标题（换行分条的中文正文实测必烧假字、字幕类 `--no` 压不住；整段连续叙述实测干净）；**必须显式含「纯黑白无彩色」**；正文不带参数尾巴，style 三项编辑器手填；`--no` 末尾挂去黑边三词。

**写法六段**：① 首句定调 `黑白电影剧照，19X0年代日本时代剧＋场面类型`，用年代与类型承载风格、不写导演英文名。② 主体＝身份＋取景（半身／头顶出画／过肩）＋动作起止力度；人物须「明确为日本人，东亚面孔，无胡须，月代头」；神情克制具体。③ 服装只写可见的材质与状态，不堆器名考据。④ 光影写光位数量与性质，并点出唯一动感。⑤ 镜头写机位＋焦段感＋景深＋构图骨架。⑥ 末句 `高反差银盐质感，＋暗部＋灰阶／颗粒`，且必须含「纯黑白无彩色」。以上均取自本支两范例，重组勿造词。

**范例一 · 芦苇荡过肩对峙（i-0l6HiISIWu「图片节点 9」）**

> 黑白电影剧照，1960年代日本时代剧：芦苇荡中的过肩对峙镜头。前景左侧：一名武士的背影与肩头占据画面左三分之一，略虚，深色和服，手按刀柄，月代头，从胸口高度的背后视角拍摄。中景画面正中，第二名武士面对镜头，明确为日本人，东亚面孔，无胡须，眼神坚毅不眨，狂风卷动着他的衣摆与头发，一手扶刀，双脚稳扎泥地。四面八方望不到边的芦苇，被强风压弯倒向同一方向，苇浪如波涛般起伏，干枯的芦花随风飞散。低机位平视，50mm镜头感，深景深两人皆实，芦苇一层层退向地平线。风是唯一的动感，其余一切凝固。高反差银盐质感，灰阶丰富，暗部有呼吸，可见35mm胶片颗粒。

**范例二 · 雨中拔刀决战前（i-e86HaN6eiR「图片节点 8」）**

> 黑白电影剧照，1950年代日本时代剧战斗场面：一名武士在大雨中稳扎马步，半身取景，头顶部分出画，正从鞘中拔刀——刀已半出，蓄势待发，身体如绷紧的弹簧。明确为日本人，东亚面孔，无胡须，月代头。神情坚毅果决：咬紧牙关，双眼灼灼、死死盯住画面右侧看不见的敌人，绝不吼叫。湿透深色和服贴身，满身泥点，雨水顺着脸往下淌。身后五名士兵持矛列阵站稳，纵深排列，神情紧绷警觉，纹丝不动。斜向大雨被逆光凝成清晰亮丝，泥泞地面，脚边溅起水花。矛杆构成对角线构图，全画面锐利合焦，决战前凝固的瞬间。高反差银盐质感，泥黑色暗部，粗颗粒35mm胶片。

注：两范例末句均未写「纯黑白无彩色」，属早期产出；新写必须补上。

---

## 分支二：彩色·战场类·英文串（4 个参照）

**句式**：一整段英文、逗号分隔要素串，顺序 主体→装备→动作→背景→光线→色调→机位→风格锚点，尾部接参数，不分行。重心在机位、动作与色块分布。

**范例一 · 赤甲单骑疾驰（i-4AjNegEyXe「图片节点 4」）**

> A Japanese samurai cavalryman galloping on a brown horse through a crowded Sengoku battlefield, wearing red lacquered samurai armor with black lacing and a simple red helmet, a small crimson war banner with black stripes behind him, the horse running at full speed with its neck stretched forward and mane flying backward, the rider leaning slightly forward with the horse's movement, firmly seated in the saddle, side-view action shot, other cavalry and red banners moving in the background, grassy battlefield beside a dense green forest, bright natural daylight, pale sky, vivid crimson against deep green, lateral tracking shot, natural motion blur in the background and horse's legs, in the style of Akira Kurosawa's Ran (1985), 35mm film grain, cinematic film still --style raw --no cape, cloak, drapery, flowing cloth

**范例二 · 红旗骑兵列队（i-F9mwRTqXCn「图片节点 10」）**

> A troop of mounted samurai riding across a grassy field at the edge of a dense green forest, Sengoku period, their commander on a black warhorse fitted with bright crimson saddle cloths, bridle and armor trim, wearing iron armor laced with red cords, more than ten long narrow crimson nobori banners rising tall around them printed with black striped heraldic marks, banners hanging down from the top of the frame, an ornate golden war standard at the upper left, other samurai on brown and white horses in dark iron armor, foot soldiers following with banner poles, deep green woods and distant mountains behind, pale grey-green sky, bright daylight, strong contrast between crimson banners and verdant forest, low eye-level angle, in the style of Akira Kurosawa's Ran (1985), crimson cavalry, epic jidaigeki, 35mm film grain, cinematic film still --ar 21:9 --style raw

**范例三 · 铁炮齐射（i-thxpaI0whi「图片节点 34」）**

> At the edge of a forest, several tanegashima arquebusiers in blue-laced armor and conical helmets lie prone on the grass firing in volley, Japanese matchlock guns rested on forked stands, bright orange muzzle flashes blasting from the barrels with thick white smoke, shooters braced against the recoil, dense gunsmoke rolling low across the ground swallowing half the frame, dark tree trunks in the foreground as framing elements, crimson banners and fighting figures glimpsed through the distant trees, dappled light in the dark green woods, white smoke and firelight intermingling with hints of red from the battlefield beyond, wide horizontal composition, the gunners at the lower right, the muzzle flash blazing at the center, in the style of Akira Kurosawa's Ran (1985), deafening moment of a musket volley, 35mm film grain, cinematic film still --ar 21:9 --style raw

**范例四 · 长枪方阵（i-3rZ6sNtKMH「图片节点 59」）**

> A Sengoku army drawn up for battle on a grassy hillside, in the foreground a rank of spearmen in black armor laced with blue cords standing sideways, their long spears angled skyward, the line receding deep into the distance, behind the ranks a host of crimson banners billowing in the wind printed with black circular crests, in the middle ground several mounted commanders, one raising a red-and-white signal standard, under a grey-blue overcast sky, more red banners faintly visible among the distant mountains, low-angle side view, the diagonal spears cutting across the frame

**要点**：短名词短语，不用从句与考据形容。尾部锚点 `in the style of Akira Kurosawa's Ran (1985)` ＋ `35mm film grain` ＋ `cinematic film still`，可加题材标签（`crimson cavalry, epic jidaigeki`／`deafening moment of a musket volley`）。正文参数只有 `--style raw` 与 `--no cape, cloak, drapery, flowing cloth`。**质感词本支只有** `35mm film grain`（范例四无），不得用 `coarse film grain`／`deep crushed blacks`。范例四无锚点无参数，说明纯要素串也成立，但另三例更接近参照。战场全景横卷可借 i-fpVaoTlZIV「图片节点 14」的画面特征（双层横卷、朱红点阵成阵、深绿烟灰压饱和、左右对称），该节点提示词中英混写不收录，**只能借画面、用本支现成短语去写**。

---

## 分支三：彩色·人物类·英文串（4 个参照）

**句式**：同战场（一整段英文、逗号分隔、尾部接 Ran 锚点与参数）。重心在妆容、服饰与静态氛围，`--no` 是本支关键。

**范例一 · 白粉妆贵族女性特写（i-8QbitXgKfo「图片节点 45」）**

> Medium close-up indoors, a noblewoman of the Sengoku era seated in formal posture, classical Japanese beauty with a plain round face, calm mask-like features, matte chalk-white face makeup like a Noh mask, completely matte with no glow, natural eyebrows shaved off and redrawn as two small round black dots placed high on the forehead near the hairline, widely spaced, small painted red lips, subdued eyes without eyeliner or mascara, a still composed expression, long black hair falling straight to her waist with a small hair ornament at the crown, pale layered kimonos with a patterned collar visible, wooden lattice blinds behind her with warm golden light filtering through the slats, a dark wooden pillar and a glowing shoji screen to the right, 1980s film softness with gentle grain, in the style of Akira Kurosawa's Ran (1985), Noh-like eerie stillness, cinematic film still --ar 16:9 --style raw --no modern makeup, glossy skin, foundation glow, contouring, eyeliner, mascara, plump lips, Korean beauty style, photoreal modern face

**范例二 · 老年武将乌帽子胸像、纯色天空留白（i-G6KVC9Eg9j「图片节点 40」）**

> Chest-up portrait of an elderly Sengoku warlord with white hair and beard, wearing a black eboshi cap with white cords hanging down both sides, a white hunting robe with subtle gold geometric patterns over a pale blue kimono bearing a circular crest, a quiver and bow fittings at his waist, holding a katana in his right hand, face turned slightly to the left with a grave commanding expression, background a pure flat grey-cyan sky with no detail whatsoever, minimalist negative space, figure centered with room in the direction of his gaze, subdued solemn palette of white and gold floating on the grey-blue backdrop, in the style of Akira Kurosawa's Ran (1985), 35mm film grain, cinematic film still --ar 16:9 --style raw --no scenery, clouds, trees, buildings, crowd

**范例三 · 三人对称审判构图（i-Nw9R85Yauj「图片节点 52」）**

> In a dim Japanese interior, a silent judgment unfolds, at the center of the frame Lady Sué kneels on the floor in a kimono of black, gold and white triangular scales with crimson lining turned out, her hands folded in her lap, head slightly bowed, an ethereal resigned expression, in the immediate foreground a samurai in black armor stands on the left and a samurai in crimson armor stands on the right, both seen from behind showing only the silhouettes of their shoulders, backs and arms, the two warriors framing her like gateposts, the eye drawn naturally to the kneeling lady between them, deep blue-grey walls behind, a bronze incense burner faintly visible in the distance, cold somber tones with a single soft beam of light falling on her while the foreground warriors sink into shadow, symmetrical three-figure composition, oppression against helplessness, in the style of Akira Kurosawa's Ran (1985), a silent moment of destiny, 35mm film grain, cinematic film still --ar 21:9 --style raw --no faces of the samurai, action, weapons raised

**范例四 · 无妆版贵族女性跪坐（i-aFUo4USLKg「图片节点 49」）**

> In a dim Japanese interior, a young noblewoman kneeling at the center of the frame, her face bare without white makeup, naturally pale skin, thin delicate eyebrows, an ethereal compassionate expression, long black hair parted in the center falling to her waist with a small red ornament at the side, wearing a kimono patterned with black, gold and white triangular scales, a crimson under-collar and sash turned out, a dark floral skirt beneath, her hands folded quietly in her lap, facing slightly to the side, deep blue-grey walls behind her, a black lacquered cabinet with gold detailing on the left, the partial figure of another person in red robes at the right edge of the frame, a bronze incense burner visible in the background, soft side light on her face in the dim room, medium shot slightly off-center, the figure framed by dark elements on both sides, in the style of Akira Kurosawa's Ran (1985), Buddha-like stillness, 35mm film grain, cinematic film still --ar 16:9 --style raw

注：范例四原节点是 image2image、带参考图 i-Qja4ahJVSw；不带参考图时走 text2image。

**要点**：

- **族裔脸型只有一条有据写法**：`classical Japanese beauty with a plain round face, calm mask-like features`（i-8QbitXgKfo，女性贵族特写用法）。其他人物题材无对应范例，**宁可少写这句，也不要自造替换说法**。
- **妆容**：白粉妆用 `matte chalk-white face makeup like a Noh mask, completely matte with no glow` ＋ 剃眉点眉 `natural eyebrows shaved off and redrawn as two small round black dots placed high on the forehead near the hairline, widely spaced` ＋ `small painted red lips` ＋ `subdued eyes without eyeliner or mascara`；无妆用 `her face bare without white makeup, naturally pale skin, thin delicate eyebrows`。
- **服饰器名配色**：`pale layered kimonos with a patterned collar`／`kimono of black, gold and white triangular scales with crimson lining turned out`／`black eboshi cap with white cords`／`white hunting robe with subtle gold geometric patterns over a pale blue kimono bearing a circular crest`。
- **静态氛围与光位（都是软光，不得改硬光）**：`Noh-like eerie stillness`／`Buddha-like stillness`／`a silent moment of destiny`；`warm golden light filtering through the slats`／`soft side light on her face in the dim room`／`a single soft beam of light falling on her while the foreground warriors sink into shadow`。
- **构图**：`figure centered with room in the direction of his gaze`／`minimalist negative space`／`symmetrical three-figure composition, the two warriors framing her like gateposts`／`the figure framed by dark elements on both sides`。
- `--no` **必须保留**：防现代美颜 `modern makeup, glossy skin, foundation glow, contouring, eyeliner, mascara, plump lips, Korean beauty style, photoreal modern face`；纯色背景 `scenery, clouds, trees, buildings, crowd`；多人构图 `faces of the samurai, action, weapons raised`。
- **质感词本支只有** `1980s film softness with gentle grain` **与普通** `35mm film grain`。`coarse film grain`／`deep crushed blacks` 是氛围类专属，**严禁借入**（跨支借词会把胶片浓度拉爆，i-bzkajuu7n79r 即此翻车）。

---

## 分支四：彩色·氛围类·英文串（4 个参照）

**句式**：同战场，但锚点多用 `Kurosawa-esque` 弱锚（推论：4 条中 3 条如此，作选型提示，非硬规则）；必写整幅统色句。

**范例一 · 血脊行军剪影（i-Ldi4AD0QmA「图片节点 3」）**

> Cinematic film still, wide shot: a long column of medieval Japanese ashigaru infantry marching along a dark mountain ridge, seen as ragged black silhouettes against a blood-red sky. Spears and tattered banners rise at irregular intervals, helmets and shoulders forming a jagged skyline. Three loose rows of figures, varying spacing, some figures half-dissolved into drifting smoke. Dense red haze and battlefield smoke swallow the lower half of the frame, deep crimson sky grading downward into near-black shadow, single-color red-and-black palette, strong backlight, no facial detail, no visible armor texture, shapes simplified to pure contour. Slight telephoto compression, layered atmospheric depth, 35mm film grain, high-contrast color reversal look, Kurosawa-esque war-epic atmosphere, ominous, monumental. --ar 21:9 --style raw --no faces, visible details on soldiers, modern weapons, clean edges, plastic red, CGI look, daylight

**范例二 · 逆光马头金边剪影（i-qtOj1h9QLV「图片节点 12」）**

> Cinematic film still, 1980s Japanese period epic, Kurosawa-esque: tight close shot of a mounted samurai company massing before battle. Four horses, heads and necks filling the frame, riders in dark armor merged into silhouette, cropped by all edges of the frame, no sky visible. Low blazing sun at the right rear, extreme backlight: every mane, bridle strap and armor lacing edged with a thin burning line of gold-white light, horse bodies as solid black masses. Heavy lens flare and veiling glare washing the right side of the frame, dust motes floating in the light shafts. Two white-and-crimson war banners cutting vertically through the darkness, two foot soldiers crouching in the lower right foreground as dark silhouettes. Warm brown-gold monochrome palette, deep crushed blacks, coarse film grain, oppressive solemnity, the stillness before the order to move. --ar 21:9 --style raw --no full horse bodies, extra horse heads, fused horses, visible human faces, blue sky, front lighting, flat lighting, clean digital look, HDR, anime

**范例三 · 浮世绘舞台绘景（非实景）（i-V0FcMbLVcc「图片节点 2」）**

> Cinematic film still, a lone samurai in dark ornate Japanese armor standing small against a vast hand-painted stage backdrop, slightly right of center. The sky is a flat matte-painted ukiyo-e heavens: thin layered clouds drawn with ink-wash and dry-brush strokes, torn vaporous edges, ember-gold light glowing through the cloud gaps rather than behind solid cloud masses, deep violet upper sky. Below, low rolling dunes in muted magenta and indigo, painted with visible brush texture. Strong warm-cool contrast, theatrical studio backlight, subtle rim light tracing the armor, moody silhouette but with faint specular detail on the cuirass. Rich saturated color-reversal-film palette, soft grain, dreamy ritual atmosphere, Kurosawa-esque 1990s Japanese period-fantasy, theatrical set design, not a real location. --ar 16:9 --style raw --no CGI, 3d render, cauliflower clouds, hard-edged clouds, plastic, toy-like, video game environment

**范例四 · 青绿苍茫白发老人（i-SQE9sviy4y「图片节点 4」）**

> Medium close-up of an elderly man with white hair tied in a topknot, chest-up framing, the figure centered in the frame, standing on a grassy ridge, wearing a pale patterned kimono, his robe stirred by the mountain wind, white hair and beard whipping in the wind, looking directly into the camera with a hollow forlorn gaze, an expression of one who has seen everything, behind him a teal-grey sky and the green ridge line of the slope, wind sweeping across the grass, negative space of sky around him, in the style of Akira Kurosawa's Ran (1985), the desolation of a wandering soul, 35mm film grain, cinematic film still --ar 16:9 --style raw

注：范例四原节点是 image2image、带参考图 i-8scKPdmxoB；不带参考图走 text2image。

**要点**：

- **锚点**：`Cinematic film still, 1980s Japanese period epic, Kurosawa-esque`／`Kurosawa-esque war-epic atmosphere`／`Kurosawa-esque 1990s Japanese period-fantasy`；范例四用 `in the style of Akira Kurosawa's Ran (1985)`。
- **整幅统色句必写**：`single-color red-and-black palette`／`deep crimson sky grading downward into near-black shadow`／`Warm brown-gold monochrome palette`／`Rich saturated color-reversal-film palette`／`teal-grey sky`。
- **本支独有**：反转片术语 `high-contrast color reversal look`／`Rich saturated color-reversal-film palette`；剪影化 `seen as ragged black silhouettes`／`shapes simplified to pure contour`／`no facial detail, no visible armor texture`／`riders in dark armor merged into silhouette`／`horse bodies as solid black masses`；逆光 `strong backlight`／`extreme backlight: every mane, bridle strap and armor lacing edged with a thin burning line of gold-white light`／`Heavy lens flare and veiling glare`／`theatrical studio backlight, subtle rim light tracing the armor`。
- **情绪锚点**：`ominous, monumental`／`oppressive solemnity, the stillness before the order to move`／`dreamy ritual atmosphere`／`the desolation of a wandering soul`。
- `--no` **按题材从本支取，不整串照抄**：i-Ldi4AD0QmA（`faces, visible details on soldiers, modern weapons, clean edges, plastic red, CGI look, daylight`）／i-qtOj1h9QLV（`full horse bodies, extra horse heads, fused horses, visible human faces, blue sky, front lighting, flat lighting, clean digital look, HDR, anime`）／i-V0FcMbLVcc（`CGI, 3d render, cauliflower clouds, hard-edged clouds, plastic, toy-like, video game environment`）／i-SQE9sviy4y 无。
- **质感词：本支是全 skill 唯一可用** `deep crushed blacks, coarse film grain` **的地方**（i-qtOj1h9QLV）；其余为 `35mm film grain` 与 `soft grain`。
- **舞台绘景子路**：`hand-painted stage backdrop`／`flat matte-painted ukiyo-e heavens`／`visible brush texture`／`theatrical set design, not a real location`，与写实景互斥，选它必须写 `not a real location` 并排除实景与 CGI 词。

---

## 治 CG 感：只用范例里已有的手段

没有「质感句必写」这条规则。可用手段只有：**材质状态** `completely matte with no glow`／`no visible armor texture`／`shapes simplified to pure contour`／`visible brush texture`／`horse bodies as solid black masses`；**真实感字段**按支取用（见各支质感词范围）；**有出处的防伪** `--no`：`plastic red`／`plastic`／`toy-like`／`video game environment`／`3d render`／`CGI`／`CGI look`／`clean edges`／`clean digital look`／`cauliflower clouds`／`hard-edged clouds`／`HDR`／`anime`。**不得使用**范例外的词（`plastic green`／`plastic skin`／`smooth texture`／`cartoon`／`illustration` 及各类自造的反差、发灰描述）；某支缺某种表达就少写一句。

## 色系子类（氛围类用，关键词级）

1. **红与黑（最浓重）**：i-Ldi4AD0QmA、i-qtOj1h9QLV。血红天空压近黑地面，强逆光剪影，反转片饱和红，防「塑料红」。适合命运感、大军行军、决战前夕。
2. **大面积绿／青苍茫（最素净）**：i-SQE9sviy4y。低饱和草绿或青蓝灰，大量留白，人物极小，无树无建筑。适合孤独、苍茫、流浪、对峙中的静。
3. **暖金琥珀／过曝白**：i-qtOj1h9QLV。过曝白天空、金色雾纱、褪色琥珀、高光去饱和。适合统帅威压、烈日战场。
4. **舞台绘景（非实景）**：i-V0FcMbLVcc。浮世绘手绘天幕、笔触可见、人工配色、剧场布光。命中率约一半，验收按此预期。
5. **蓝天白日**：本支无英文范例（成图参照 i-6StneWk1Rk）。日光鲜明、阴影利落、纪念碑式；要用就从本支范例取现成短语自组，不得造词。

## 中文成图参照（句式不作模板，画面特征可借鉴）

这三支纯中文正文是「换行分条短句」结构，实测会烧假字，只借画面：**i-ORCxJWCBJW** 留白孤寂、小人物对大景、青蓝阵羽织单一色块、大量天空留白；**i-xKvqqBHjj6** 一站一跪的垂直压迫、低饱和灰暖调、舞台幕布式无地面背景、轮廓光隐面；**i-G9Tx0pIEg7／i-6StneWk1Rk／i-Vq5HiAyM2Z／i-ycDvTMRxPo** 血红天空行军剪影、三色幟旗仰拍、纯绿草坡微小白衣人、褪色琥珀武将胸像，以及「构图比例写成数字」（下三分之一、三分之二留给天空，属推论）的习惯。

## 选分支

1. 用户指定黑白 → 走黑白。要求彩色用中文写 → 说明彩色只出英文（中文分行分条正文实测必烧假字），给英文版。
2. 判黑白或彩色：偏黑白＝雨夜、决斗、废墟、对峙、纪实感强；偏彩色＝朱红旗帜、铠甲色块、火光、成阵彩绘、人物定妆、浓重氛围场面。
3. 彩色再判题材：**战场类**＝冲阵、行军、方阵、铁炮、城堡远景、群像阵势；**人物类**＝肖像、特写、妆容服饰细节、室内跪坐对峙；**氛围类**＝整幅被单一颜色浸透、剪影化群像或极小人物对巨大天空草坡、要反转片质感或舞台绘景感。横跨两类问一句，或用「色块分布 vs 单色笼罩」判断（前者走战场、后者走氛围）。
4. 氛围类再选色系子类。
5. 冲突或不明 → 问一句。

## 提交前检查

- 逐词对照本支范例：无出处的词删除或换回原文（去黑边三词除外）。
- 质感词未跨支借用。
- `--no` 已挂 `letterbox, black bars, cinematic bars`。
- 正文无任何画幅参数；语言单一。
- 人物类防现代美颜 `--no` 在；氛围类整幅统色句在；舞台绘景子路写了 `not a real location`。
- 总长 ≤ 1024 字符；ratio 用允许值。
- 出图后逐张看有无黑边：出现即挑图或走图生图去边，不要改 ratio、不要删锚点。
- 交付给出可直接复制的完整提示词、用了哪一支及理由、生成的图片节点。
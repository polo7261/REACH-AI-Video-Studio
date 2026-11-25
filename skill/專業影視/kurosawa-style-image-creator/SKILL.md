# 黑澤明電影風格圖片生成（彩色 / 黑白）

四個可執行風格詞：**黑白·中文單段** ＋ **彩色三支英文串**（戰場／人物／氛圍）。按分支取範例片段重組後填入 MJ 節點出圖。

## 總原則：每個詞都要有出處

1. 每個英文片語、每個 `--no` 詞、每句質感／色調／光位描述，都必須能在**本支範例**裡逐字找到出處；不得仿造、不得拼接新詞、不得把中文範例直譯成英文當寫法推薦。
2. 做法是**從本支範例抽取現成片段重組**。某支缺某種表達，寧可少寫一句，也不要自造補上。
3. **不得跨支藉詞**：戰場、人物、氛圍各用本支 4 條範例，黑白用本支 2 條。
4. **唯一例外**：`--no` 裡的去黑邊三詞 `letterbox, black bars, cinematic bars`（使用者授權，非節點提煉）。除這三個詞外不開口子。

## 通用使用說明（全分支）

- **範例原文中的** `--ar` **一律刪除**，其餘 `--style raw` 與 `--no` 保留。範例逐字保留只為留存參照原貌，不等於可直接提交。
- **正文不寫任何畫幅引數**（`--ar`／`--aspect`／比例）。畫幅只由節點 ratio 欄位決定：`1:1`／`9:16`／`16:9`／`3:4`／`4:3`／`3:2`／`2:3`；`21:9` 不被接受（422 拒絕）。寬幅選 `3:2` 或 `16:9`，Academy 選 `4:3`。此條只為避免與欄位重複表達，**不是防黑邊手段**。
- **每次出圖都在** `--no` **末尾掛去黑邊三詞**：`letterbox, black bars, cinematic bars`。（受控對照：不掛 4/4 帶上下黑邊，掛後 4/4 無；單次 4 張樣本，非統計學結論，仍需逐張檢查、偶現時挑圖。黑邊是模型逐張生成進畫面的電影遮幅，不是容器比例填充；誘因推測為 `cinematic film still` 等電影語彙，屬推測、未經單獨驗證。）
- **不得為去黑邊刪風格錨點**：`cinematic film still`、`in the style of Akira Kurosawa's Ran (1985)`、`Kurosawa-esque`、`1980s film softness with gentle grain`、`deep crushed blacks, coarse film grain` 均有出處，必須保留。
- **單語言**：彩色一律純英文，黑白一律純中文；同一提示詞內不得中英混用（`--no` 引數尾巴除外）。
- **提示詞上限 1024 字元**，超出直接提交失敗，長 `--no` 要留餘量。
- **stylize／weird／chaos（100／50／5）不能靠 quality_spec 落地**：只能寫進英文正文或編輯器手填，不得聲稱已落地。

---

## 分支一：黑白·中文單段（2 個參照）

**結構規則**：純中文；**只寫一整段連續敘述**，句號／分號／頓號斷句，不分行、不分條、不加小標題（換行分條的中文正文實測必燒假字、字幕類 `--no` 壓不住；整段連續敘述實測乾淨）；**必須顯式含「純黑白無彩色」**；正文不帶引數尾巴，style 三項編輯器手填；`--no` 末尾掛去黑邊三詞。

**寫法六段**：① 首句定調 `黑白電影劇照，19X0年代日本時代劇＋場面類型`，用年代與類型承載風格、不寫導演英文名。② 主體＝身份＋取景（半身／頭頂出畫／過肩）＋動作起止力度；人物須「明確為日本人，東亞面孔，無鬍鬚，月代頭」；神情剋制具體。③ 服裝只寫可見的材質與狀態，不堆器名考據。④ 光影寫光位數量與性質，並點出唯一動感。⑤ 鏡頭寫機位＋焦段感＋景深＋構圖骨架。⑥ 末句 `高反差銀鹽質感，＋暗部＋灰階／顆粒`，且必須含「純黑白無彩色」。以上均取自本支兩範例，重組勿造詞。

**範例一 · 蘆葦蕩過肩對峙（i-0l6HiISIWu「圖片節點 9」）**

> 黑白電影劇照，1960年代日本時代劇：蘆葦蕩中的過肩對峙鏡頭。前景左側：一名武士的背影與肩頭佔據畫面左三分之一，略虛，深色和服，手按刀柄，月代頭，從胸口高度的背後視角拍攝。中景畫面正中，第二名武士面對鏡頭，明確為日本人，東亞面孔，無鬍鬚，眼神堅毅不眨，狂風捲動著他的衣襬與頭髮，一手扶刀，雙腳穩紮泥地。四面八方望不到邊的蘆葦，被強風壓彎倒向同一方向，葦浪如波濤般起伏，乾枯的蘆花隨風飛散。低機位平視，50mm鏡頭感，深景深兩人皆實，蘆葦一層層退向地平線。風是唯一的動感，其餘一切凝固。高反差銀鹽質感，灰階豐富，暗部有呼吸，可見35mm膠片顆粒。

**範例二 · 雨中拔刀決戰前（i-e86HaN6eiR「圖片節點 8」）**

> 黑白電影劇照，1950年代日本時代劇戰鬥場面：一名武士在大雨中穩紮馬步，半身取景，頭頂部分出畫，正從鞘中拔刀——刀已半出，蓄勢待發，身體如繃緊的彈簧。明確為日本人，東亞面孔，無鬍鬚，月代頭。神情堅毅果決：咬緊牙關，雙眼灼灼、死死盯住畫面右側看不見的敵人，絕不吼叫。溼透深色和服貼身，滿身泥點，雨水順著臉往下淌。身後五名士兵持矛列陣站穩，縱深排列，神情緊繃警覺，紋絲不動。斜向大雨被逆光凝成清晰亮絲，泥濘地面，腳邊濺起水花。矛杆構成對角線構圖，全畫面銳利合焦，決戰前凝固的瞬間。高反差銀鹽質感，泥黑色暗部，粗顆粒35mm膠片。

注：兩範例末句均未寫「純黑白無彩色」，屬早期產出；新寫必須補上。

---

## 分支二：彩色·戰場類·英文串（4 個參照）

**句式**：一整段英文、逗號分隔要素串，順序 主體→裝備→動作→背景→光線→色調→機位→風格錨點，尾部接引數，不分行。重心在機位、動作與色塊分佈。

**範例一 · 赤甲單騎疾馳（i-4AjNegEyXe「圖片節點 4」）**

> A Japanese samurai cavalryman galloping on a brown horse through a crowded Sengoku battlefield, wearing red lacquered samurai armor with black lacing and a simple red helmet, a small crimson war banner with black stripes behind him, the horse running at full speed with its neck stretched forward and mane flying backward, the rider leaning slightly forward with the horse's movement, firmly seated in the saddle, side-view action shot, other cavalry and red banners moving in the background, grassy battlefield beside a dense green forest, bright natural daylight, pale sky, vivid crimson against deep green, lateral tracking shot, natural motion blur in the background and horse's legs, in the style of Akira Kurosawa's Ran (1985), 35mm film grain, cinematic film still --style raw --no cape, cloak, drapery, flowing cloth

**範例二 · 紅旗騎兵列隊（i-F9mwRTqXCn「圖片節點 10」）**

> A troop of mounted samurai riding across a grassy field at the edge of a dense green forest, Sengoku period, their commander on a black warhorse fitted with bright crimson saddle cloths, bridle and armor trim, wearing iron armor laced with red cords, more than ten long narrow crimson nobori banners rising tall around them printed with black striped heraldic marks, banners hanging down from the top of the frame, an ornate golden war standard at the upper left, other samurai on brown and white horses in dark iron armor, foot soldiers following with banner poles, deep green woods and distant mountains behind, pale grey-green sky, bright daylight, strong contrast between crimson banners and verdant forest, low eye-level angle, in the style of Akira Kurosawa's Ran (1985), crimson cavalry, epic jidaigeki, 35mm film grain, cinematic film still --ar 21:9 --style raw

**範例三 · 鐵炮齊射（i-thxpaI0whi「圖片節點 34」）**

> At the edge of a forest, several tanegashima arquebusiers in blue-laced armor and conical helmets lie prone on the grass firing in volley, Japanese matchlock guns rested on forked stands, bright orange muzzle flashes blasting from the barrels with thick white smoke, shooters braced against the recoil, dense gunsmoke rolling low across the ground swallowing half the frame, dark tree trunks in the foreground as framing elements, crimson banners and fighting figures glimpsed through the distant trees, dappled light in the dark green woods, white smoke and firelight intermingling with hints of red from the battlefield beyond, wide horizontal composition, the gunners at the lower right, the muzzle flash blazing at the center, in the style of Akira Kurosawa's Ran (1985), deafening moment of a musket volley, 35mm film grain, cinematic film still --ar 21:9 --style raw

**範例四 · 長槍方陣（i-3rZ6sNtKMH「圖片節點 59」）**

> A Sengoku army drawn up for battle on a grassy hillside, in the foreground a rank of spearmen in black armor laced with blue cords standing sideways, their long spears angled skyward, the line receding deep into the distance, behind the ranks a host of crimson banners billowing in the wind printed with black circular crests, in the middle ground several mounted commanders, one raising a red-and-white signal standard, under a grey-blue overcast sky, more red banners faintly visible among the distant mountains, low-angle side view, the diagonal spears cutting across the frame

**要點**：短名詞短語，不用從句與考據形容。尾部錨點 `in the style of Akira Kurosawa's Ran (1985)` ＋ `35mm film grain` ＋ `cinematic film still`，可加題材標籤（`crimson cavalry, epic jidaigeki`／`deafening moment of a musket volley`）。正文引數只有 `--style raw` 與 `--no cape, cloak, drapery, flowing cloth`。**質感詞本支只有** `35mm film grain`（範例四無），不得用 `coarse film grain`／`deep crushed blacks`。範例四無錨點無引數，說明純要素串也成立，但另三例更接近參照。戰場全景橫卷可借 i-fpVaoTlZIV「圖片節點 14」的畫面特徵（雙層橫卷、硃紅點陣成陣、深綠菸灰壓飽和、左右對稱），該節點提示詞中英混寫不收錄，**只能借畫面、用本支現成短語去寫**。

---

## 分支三：彩色·人物類·英文串（4 個參照）

**句式**：同戰場（一整段英文、逗號分隔、尾部接 Ran 錨點與引數）。重心在妝容、服飾與靜態氛圍，`--no` 是本支關鍵。

**範例一 · 白粉妝貴族女性特寫（i-8QbitXgKfo「圖片節點 45」）**

> Medium close-up indoors, a noblewoman of the Sengoku era seated in formal posture, classical Japanese beauty with a plain round face, calm mask-like features, matte chalk-white face makeup like a Noh mask, completely matte with no glow, natural eyebrows shaved off and redrawn as two small round black dots placed high on the forehead near the hairline, widely spaced, small painted red lips, subdued eyes without eyeliner or mascara, a still composed expression, long black hair falling straight to her waist with a small hair ornament at the crown, pale layered kimonos with a patterned collar visible, wooden lattice blinds behind her with warm golden light filtering through the slats, a dark wooden pillar and a glowing shoji screen to the right, 1980s film softness with gentle grain, in the style of Akira Kurosawa's Ran (1985), Noh-like eerie stillness, cinematic film still --ar 16:9 --style raw --no modern makeup, glossy skin, foundation glow, contouring, eyeliner, mascara, plump lips, Korean beauty style, photoreal modern face

**範例二 · 老年武將烏帽子胸像、純色天空留白（i-G6KVC9Eg9j「圖片節點 40」）**

> Chest-up portrait of an elderly Sengoku warlord with white hair and beard, wearing a black eboshi cap with white cords hanging down both sides, a white hunting robe with subtle gold geometric patterns over a pale blue kimono bearing a circular crest, a quiver and bow fittings at his waist, holding a katana in his right hand, face turned slightly to the left with a grave commanding expression, background a pure flat grey-cyan sky with no detail whatsoever, minimalist negative space, figure centered with room in the direction of his gaze, subdued solemn palette of white and gold floating on the grey-blue backdrop, in the style of Akira Kurosawa's Ran (1985), 35mm film grain, cinematic film still --ar 16:9 --style raw --no scenery, clouds, trees, buildings, crowd

**範例三 · 三人對稱審判構圖（i-Nw9R85Yauj「圖片節點 52」）**

> In a dim Japanese interior, a silent judgment unfolds, at the center of the frame Lady Sué kneels on the floor in a kimono of black, gold and white triangular scales with crimson lining turned out, her hands folded in her lap, head slightly bowed, an ethereal resigned expression, in the immediate foreground a samurai in black armor stands on the left and a samurai in crimson armor stands on the right, both seen from behind showing only the silhouettes of their shoulders, backs and arms, the two warriors framing her like gateposts, the eye drawn naturally to the kneeling lady between them, deep blue-grey walls behind, a bronze incense burner faintly visible in the distance, cold somber tones with a single soft beam of light falling on her while the foreground warriors sink into shadow, symmetrical three-figure composition, oppression against helplessness, in the style of Akira Kurosawa's Ran (1985), a silent moment of destiny, 35mm film grain, cinematic film still --ar 21:9 --style raw --no faces of the samurai, action, weapons raised

**範例四 · 無妝版貴族女性跪坐（i-aFUo4USLKg「圖片節點 49」）**

> In a dim Japanese interior, a young noblewoman kneeling at the center of the frame, her face bare without white makeup, naturally pale skin, thin delicate eyebrows, an ethereal compassionate expression, long black hair parted in the center falling to her waist with a small red ornament at the side, wearing a kimono patterned with black, gold and white triangular scales, a crimson under-collar and sash turned out, a dark floral skirt beneath, her hands folded quietly in her lap, facing slightly to the side, deep blue-grey walls behind her, a black lacquered cabinet with gold detailing on the left, the partial figure of another person in red robes at the right edge of the frame, a bronze incense burner visible in the background, soft side light on her face in the dim room, medium shot slightly off-center, the figure framed by dark elements on both sides, in the style of Akira Kurosawa's Ran (1985), Buddha-like stillness, 35mm film grain, cinematic film still --ar 16:9 --style raw

注：範例四原節點是 image2image、帶參考圖 i-Qja4ahJVSw；不帶參考圖時走 text2image。

**要點**：

- **族裔臉型只有一條有據寫法**：`classical Japanese beauty with a plain round face, calm mask-like features`（i-8QbitXgKfo，女性貴族特寫用法）。其他人物題材無對應範例，**寧可少寫這句，也不要自造替換說法**。
- **妝容**：白粉妝用 `matte chalk-white face makeup like a Noh mask, completely matte with no glow` ＋ 剃眉點眉 `natural eyebrows shaved off and redrawn as two small round black dots placed high on the forehead near the hairline, widely spaced` ＋ `small painted red lips` ＋ `subdued eyes without eyeliner or mascara`；無妝用 `her face bare without white makeup, naturally pale skin, thin delicate eyebrows`。
- **服飾器名配色**：`pale layered kimonos with a patterned collar`／`kimono of black, gold and white triangular scales with crimson lining turned out`／`black eboshi cap with white cords`／`white hunting robe with subtle gold geometric patterns over a pale blue kimono bearing a circular crest`。
- **靜態氛圍與光位（都是軟光，不得改硬光）**：`Noh-like eerie stillness`／`Buddha-like stillness`／`a silent moment of destiny`；`warm golden light filtering through the slats`／`soft side light on her face in the dim room`／`a single soft beam of light falling on her while the foreground warriors sink into shadow`。
- **構圖**：`figure centered with room in the direction of his gaze`／`minimalist negative space`／`symmetrical three-figure composition, the two warriors framing her like gateposts`／`the figure framed by dark elements on both sides`。
- `--no` **必須保留**：防現代美顏 `modern makeup, glossy skin, foundation glow, contouring, eyeliner, mascara, plump lips, Korean beauty style, photoreal modern face`；純色背景 `scenery, clouds, trees, buildings, crowd`；多人構圖 `faces of the samurai, action, weapons raised`。
- **質感詞本支只有** `1980s film softness with gentle grain` **與普通** `35mm film grain`。`coarse film grain`／`deep crushed blacks` 是氛圍類專屬，**嚴禁借入**（跨支藉詞會把膠片濃度拉爆，i-bzkajuu7n79r 即此翻車）。

---

## 分支四：彩色·氛圍類·英文串（4 個參照）

**句式**：同戰場，但錨點多用 `Kurosawa-esque` 弱錨（推論：4 條中 3 條如此，作選型提示，非硬規則）；必寫整幅統色句。

**範例一 · 血脊行軍剪影（i-Ldi4AD0QmA「圖片節點 3」）**

> Cinematic film still, wide shot: a long column of medieval Japanese ashigaru infantry marching along a dark mountain ridge, seen as ragged black silhouettes against a blood-red sky. Spears and tattered banners rise at irregular intervals, helmets and shoulders forming a jagged skyline. Three loose rows of figures, varying spacing, some figures half-dissolved into drifting smoke. Dense red haze and battlefield smoke swallow the lower half of the frame, deep crimson sky grading downward into near-black shadow, single-color red-and-black palette, strong backlight, no facial detail, no visible armor texture, shapes simplified to pure contour. Slight telephoto compression, layered atmospheric depth, 35mm film grain, high-contrast color reversal look, Kurosawa-esque war-epic atmosphere, ominous, monumental. --ar 21:9 --style raw --no faces, visible details on soldiers, modern weapons, clean edges, plastic red, CGI look, daylight

**範例二 · 逆光馬頭金邊剪影（i-qtOj1h9QLV「圖片節點 12」）**

> Cinematic film still, 1980s Japanese period epic, Kurosawa-esque: tight close shot of a mounted samurai company massing before battle. Four horses, heads and necks filling the frame, riders in dark armor merged into silhouette, cropped by all edges of the frame, no sky visible. Low blazing sun at the right rear, extreme backlight: every mane, bridle strap and armor lacing edged with a thin burning line of gold-white light, horse bodies as solid black masses. Heavy lens flare and veiling glare washing the right side of the frame, dust motes floating in the light shafts. Two white-and-crimson war banners cutting vertically through the darkness, two foot soldiers crouching in the lower right foreground as dark silhouettes. Warm brown-gold monochrome palette, deep crushed blacks, coarse film grain, oppressive solemnity, the stillness before the order to move. --ar 21:9 --style raw --no full horse bodies, extra horse heads, fused horses, visible human faces, blue sky, front lighting, flat lighting, clean digital look, HDR, anime

**範例三 · 浮世繪舞臺繪景（非實景）（i-V0FcMbLVcc「圖片節點 2」）**

> Cinematic film still, a lone samurai in dark ornate Japanese armor standing small against a vast hand-painted stage backdrop, slightly right of center. The sky is a flat matte-painted ukiyo-e heavens: thin layered clouds drawn with ink-wash and dry-brush strokes, torn vaporous edges, ember-gold light glowing through the cloud gaps rather than behind solid cloud masses, deep violet upper sky. Below, low rolling dunes in muted magenta and indigo, painted with visible brush texture. Strong warm-cool contrast, theatrical studio backlight, subtle rim light tracing the armor, moody silhouette but with faint specular detail on the cuirass. Rich saturated color-reversal-film palette, soft grain, dreamy ritual atmosphere, Kurosawa-esque 1990s Japanese period-fantasy, theatrical set design, not a real location. --ar 16:9 --style raw --no CGI, 3d render, cauliflower clouds, hard-edged clouds, plastic, toy-like, video game environment

**範例四 · 青綠蒼茫白髮老人（i-SQE9sviy4y「圖片節點 4」）**

> Medium close-up of an elderly man with white hair tied in a topknot, chest-up framing, the figure centered in the frame, standing on a grassy ridge, wearing a pale patterned kimono, his robe stirred by the mountain wind, white hair and beard whipping in the wind, looking directly into the camera with a hollow forlorn gaze, an expression of one who has seen everything, behind him a teal-grey sky and the green ridge line of the slope, wind sweeping across the grass, negative space of sky around him, in the style of Akira Kurosawa's Ran (1985), the desolation of a wandering soul, 35mm film grain, cinematic film still --ar 16:9 --style raw

注：範例四原節點是 image2image、帶參考圖 i-8scKPdmxoB；不帶參考圖走 text2image。

**要點**：

- **錨點**：`Cinematic film still, 1980s Japanese period epic, Kurosawa-esque`／`Kurosawa-esque war-epic atmosphere`／`Kurosawa-esque 1990s Japanese period-fantasy`；範例四用 `in the style of Akira Kurosawa's Ran (1985)`。
- **整幅統色句必寫**：`single-color red-and-black palette`／`deep crimson sky grading downward into near-black shadow`／`Warm brown-gold monochrome palette`／`Rich saturated color-reversal-film palette`／`teal-grey sky`。
- **本支獨有**：反轉片術語 `high-contrast color reversal look`／`Rich saturated color-reversal-film palette`；剪影化 `seen as ragged black silhouettes`／`shapes simplified to pure contour`／`no facial detail, no visible armor texture`／`riders in dark armor merged into silhouette`／`horse bodies as solid black masses`；逆光 `strong backlight`／`extreme backlight: every mane, bridle strap and armor lacing edged with a thin burning line of gold-white light`／`Heavy lens flare and veiling glare`／`theatrical studio backlight, subtle rim light tracing the armor`。
- **情緒錨點**：`ominous, monumental`／`oppressive solemnity, the stillness before the order to move`／`dreamy ritual atmosphere`／`the desolation of a wandering soul`。
- `--no` **按題材從本支取，不整串照抄**：i-Ldi4AD0QmA（`faces, visible details on soldiers, modern weapons, clean edges, plastic red, CGI look, daylight`）／i-qtOj1h9QLV（`full horse bodies, extra horse heads, fused horses, visible human faces, blue sky, front lighting, flat lighting, clean digital look, HDR, anime`）／i-V0FcMbLVcc（`CGI, 3d render, cauliflower clouds, hard-edged clouds, plastic, toy-like, video game environment`）／i-SQE9sviy4y 無。
- **質感詞：本支是全 skill 唯一可用** `deep crushed blacks, coarse film grain` **的地方**（i-qtOj1h9QLV）；其餘為 `35mm film grain` 與 `soft grain`。
- **舞臺繪景子路**：`hand-painted stage backdrop`／`flat matte-painted ukiyo-e heavens`／`visible brush texture`／`theatrical set design, not a real location`，與寫實景互斥，選它必須寫 `not a real location` 並排除實景與 CGI 詞。

---

## 治 CG 感：只用範例裡已有的手段

沒有「質感句必寫」這條規則。可用手段只有：**材質狀態** `completely matte with no glow`／`no visible armor texture`／`shapes simplified to pure contour`／`visible brush texture`／`horse bodies as solid black masses`；**真實感欄位**按支取用（見各支質感詞範圍）；**有出處的防偽** `--no`：`plastic red`／`plastic`／`toy-like`／`video game environment`／`3d render`／`CGI`／`CGI look`／`clean edges`／`clean digital look`／`cauliflower clouds`／`hard-edged clouds`／`HDR`／`anime`。**不得使用**範例外的詞（`plastic green`／`plastic skin`／`smooth texture`／`cartoon`／`illustration` 及各類自造的反差、發灰描述）；某支缺某種表達就少寫一句。

## 色系子類（氛圍類用，關鍵詞級）

1. **紅與黑（最濃重）**：i-Ldi4AD0QmA、i-qtOj1h9QLV。血紅天空壓近黑地面，強逆光剪影，反轉片飽和紅，防「塑膠紅」。適合命運感、大軍行軍、決戰前夕。
2. **大面積綠／青蒼茫（最素淨）**：i-SQE9sviy4y。低飽和草綠或青藍灰，大量留白，人物極小，無樹無建築。適合孤獨、蒼茫、流浪、對峙中的靜。
3. **暖金琥珀／過曝白**：i-qtOj1h9QLV。過曝白天空、金色霧紗、褪色琥珀、高光去飽和。適合統帥威壓、烈日戰場。
4. **舞臺繪景（非實景）**：i-V0FcMbLVcc。浮世繪手繪天幕、筆觸可見、人工配色、劇場布光。命中率約一半，驗收按此預期。
5. **藍天白日**：本支無英文範例（成圖參照 i-6StneWk1Rk）。日光鮮明、陰影利落、紀念碑式；要用就從本支範例取現成短語自組，不得造詞。

## 中文成圖參照（句式不作模板，畫面特徵可借鑑）

這三支純中文正文是「換行分條短句」結構，實測會燒假字，只借畫面：**i-ORCxJWCBJW** 留白孤寂、小人物對大景、青藍陣羽織單一色塊、大量天空留白；**i-xKvqqBHjj6** 一站一跪的垂直壓迫、低飽和灰暖調、舞臺幕布式無地面背景、輪廓光隱面；**i-G9Tx0pIEg7／i-6StneWk1Rk／i-Vq5HiAyM2Z／i-ycDvTMRxPo** 血紅天空行軍剪影、三色幟旗仰拍、純綠草坡微小白衣人、褪色琥珀武將胸像，以及「構圖比例寫成數字」（下三分之一、三分之二留給天空，屬推論）的習慣。

## 選分支

1. 使用者指定黑白 → 走黑白。要求彩色用中文寫 → 說明彩色只出英文（中文分行分條正文實測必燒假字），給英文版。
2. 判黑白或彩色：偏黑白＝雨夜、決鬥、廢墟、對峙、紀實感強；偏彩色＝硃紅旗幟、鎧甲色塊、火光、成陣彩繪、人物定妝、濃重氛圍場面。
3. 彩色再判題材：**戰場類**＝衝陣、行軍、方陣、鐵炮、城堡遠景、群像陣勢；**人物類**＝肖像、特寫、妝容服飾細節、室內跪坐對峙；**氛圍類**＝整幅被單一顏色浸透、剪影化群像或極小人物對巨大天空草坡、要反轉片質感或舞臺繪景感。橫跨兩類問一句，或用「色塊分佈 vs 單色籠罩」判斷（前者走戰場、後者走氛圍）。
4. 氛圍類再選色系子類。
5. 衝突或不明 → 問一句。

## 提交前檢查

- 逐詞對照本支範例：無出處的詞刪除或換回原文（去黑邊三詞除外）。
- 質感詞未跨支借用。
- `--no` 已掛 `letterbox, black bars, cinematic bars`。
- 正文無任何畫幅引數；語言單一。
- 人物類防現代美顏 `--no` 在；氛圍類整幅統色句在；舞臺繪景子路寫了 `not a real location`。
- 總長 ≤ 1024 字元；ratio 用允許值。
- 出圖後逐張看有無黑邊：出現即挑圖或走圖生圖去邊，不要改 ratio、不要刪錨點。
- 交付給出可直接複製的完整提示詞、用了哪一支及理由、生成的圖片節點。
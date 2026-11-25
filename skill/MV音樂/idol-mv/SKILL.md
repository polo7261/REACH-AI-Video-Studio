# idol-mv

做平成 AKB48 风格青春偶像 MV 时用本 skill。核心气质:**日系胶片质感 + 纪录片手持摄影 + 校园青春叙事 + 女子团体群像感**,以 2009–2014 黄金年代为审美基准。核心基准:所有设计对齐"平成时代 AKB48 黄金年代青春偶像 MV"——**不是完美偶像,而是正在发光的普通成员**。

> 本环境适配:Seedance/MultiModalToVideo → `generate_video_v3`;元素图/TextToImage/ImageToImage → `generate_image_v3`;BGM/VO/text_to_instrumental/text_to_narration → `generate_audio`;text_editor → `write_file_v2`;video_assembler → `composite_video`;`<<<image_n>>>`/asset_id 槽位 → `reference_nodes`+`{{NodeKey}}`;里程碑确认 → `ask_human`。**prompt 写法与运镜词汇全部内联本 skill,不外包 image-prompt-director / cinematic-motion-language**。适配点:Seedance wrapper 语法((...)音乐/<...>音效/{...}对白/【...】字幕)按 `generate_video_v3` 提示词能力适配,无对应则改为音效意图描述并注明;refer_type 参数(Kling 3.0 Omni 非会员备用)、会员分支、超分(Jimeng SR/MediaKit)本环境无对应→正当删除、见对账;Midjourney 禁用于一致性一条转为"探索图不作一致性锚"方法保留;模型专名按本环境生成面适配改写(非删除)。

## 流程(5 里程碑暂停,不一次跑完;用 `ask_human` 展示 review 清单获明确确认再续)

1. **Final_Video_Spec**(`write_file_v2`):锁定全局参数——画面比例(默认 16:9)、目标时长、输出语言(日语/中文歌词)、视觉风格基调(平成胶片偶像 MV)、色彩系统(夏日青春胶片)。
2. **分镜**(`storyboard`):先建 key_element(成员角色+核心场景+关键道具),再按固定结构**日常→放学→友情→练习→欢笑→舞台→青春高潮→黄昏收尾**规划 shot 列表,同步 audio_layer(BGM+可选 VO)。
3. 完成分镜后,**扫描已有用户上传素材**,将匹配资源绑定至对应 Storyboard 槽位,避免重复生成。
4. **元素形象图**(`generate_image_v3`):生成所有 key_element 形象图(角色参考图**双格:半身+全身**、场景参考图标胶片基调)。
5. **逐 shot 视频**(`generate_video_v3`):优先以 element 图为视觉参考。
6. **音频**(`generate_audio`):BGM + 音效/VO 音频层。
7. **合成**(`composite_video`):时间线剪辑导出成片。
> 依赖:2→1;3→2;4→2;5→4;6→2;7→4,5,6。**暂停节点 A–E 逐项展示清单与提问话术见** `references/pause-nodes-and-vertical.md`(5 节点全文+竖版专属暂停 V-A/V-B+竖版短时长通用调度)。用户上传素材优先绑定为对应 key_element 资产,不重复生成已有内容。

## 素材分析(`analyze` · 将所有输入解读为"AKB48 黄金年代青春偶像 MV 素材")

**基础分析视角**:角色——识别气质分层(center girl 核心能量/shy 害羞/genki 元气/cool beauty 清冷/emotional supporter 感情担当),评估自然妆容程度/青春笑容真实感/服装风格(校服/夏装/舞台服)/群像化学反应;场景——识别青春时空(放学教室/天台/夏日操场/电车站台/河堤/夏祭/便利店门口/黄昏篮球场),分析光线质感(夏日自然光/黄金时刻暖光/教室荧光灯感/潮湿夏日空气感);摄影/影像——识别胶片感(柯达 Gold 200 暖调/富士 Pro 400H 冷柔调/软颗粒/高光溢出/过曝区域/褪色感),评估拍摄方式(手持纪录片感/偷拍式青春视角/自然 vs 商业构图);音频(如有)——BGM 风格(上进 J-Pop/青春吉他/idol 合唱/nostalgic 明亮旋律),环境音(蝉鸣/电车过道/操场欢笑/社团练习声/运动鞋踩地)。**输出重点**:转化为可直接注入 Storyboard 的语言(角色/场景 element 描述、shot 情绪标注、audio_layer 风格指引)。

**上传素材处理三套流程**(照片 identity anchor 四步 / 音频类型判定四步 / 场景 lighting+spatial anchor 五步):全文见 `references/upload-analysis.md`。

## 设计 key_element

**角色 element character**:每位成员须含 气质标签/妆容/发型/服装/标志性动作或表情/禁止事项。若用户提供参照图,角色描述必须与图中所见一致,气质模板仅作格式参照、不覆盖用户上传的真实面部特征。
- **禁止(所有角色通用)**:高级时装感、欧美超模脸、AI 网红妆、强烈性感化。
- **允许(所有角色通用)**:稍乱的发丝、不均匀的动作、自然反应、业余魅力。
- **五大气质类型设计模板**(Center Girl / Genki / Shy / Cool Beauty / Emotional Supporter,各含外貌锚点/服装设计/标志性动作与表情/prompt 气质词四小节):全文见 `references/character-templates.md`。

**场景 element scene**:优先场景池 13 个——放学后的教室、学校天台、夏日操场、河堤、电车站、社团教室、校园走廊、樱花街道、夏祭、海边、东京街头、便利店门口、黄昏篮球场。每场景须描述:光线来源(夏日斜阳/荧光灯/祭典灯笼)、空间细节(黑板上的字/自行车/铁丝网)、环境音暗示。**禁止**:豪华现代建筑、欧美夜店、赛博朋克城市、高端时装秀场。
- **八大核心场景标准化模板**(教室/天台/操场/河堤/夏祭/电车站台/练习室/走廊,各含光线锚点/空间细节锚点/胶片色调基准/环境音暗示):全文见 `references/scene-templates.md`。实际创作可微调、不必逐字照搬;用户提供真实场景照片时以照片特征为准覆盖对应字段。

**道具 element prop**:常用标志性道具须单独建 element prop 供 shot 直接引用,避免每次重描外观。每道具须含 外观描述(形状/颜色/材质)、使用方式(持握/佩戴/放置)、出现段落建议、禁止搭配写法。
- **七个道具 element 模板**(发饰/书包/应援棒/线香花火/自行车/笔记本/冰棒):全文见 `references/prop-templates.md`。

## 季节限定变体(触发时对场景池的色调基准/空间细节/环境音做对应替换,其余角色规则与 MV 结构不变)

三变体——🌸 樱花季(春)/🌊 海边(夏末)/🎑 文化祭(秋),各含 触发条件/色调基准替换/场景细节替换/情绪倾向调整/prompt 附加词汇/环境音替换:全文见 `references/seasonal-variants.md`。

## 短片版本结构(30s/60s/3min · 按优先级剪枝而非等比压缩保持叙事完整;八段式完整结构仅用于 3min 以上版本)

- **30s(28–33s)**:保留 3 段——欢笑高潮(段 5,能量顶点不可删,压 2–3 shot 约 8–10s)、舞台表演(段 6,偶像核心,1–2 shot 约 6–8s)、黄昏收尾(段 8,情绪落点,1 shot 约 8–10s);删除日常/放学/友情/练习/青春高潮。节奏:欢笑高潮 shot 压 1.5–2.5s 快切开场;舞台 2–4s 直接承接不做过渡;黄昏留足 8s 唯一留白;BGM 从 chorus 爆发点起、不用 intro/verse。shot 总数 4–6。
- **60s(55–65s)**:保留 5 段——日常(段 1,压 2–3 shot 约 8–10s,优先空镜+1 角色近景)、友情(段 3,2–3 shot 约 8–10s,正反打对切优先)、欢笑高潮(段 5,3–4 shot)、舞台(段 6,2–3 shot 约 10–12s)、黄昏收尾(段 8,1–2 shot 约 10–12s);删除优先级:练习(段 4)>放学(段 2)>青春高潮(段 7),仍超则日常压至仅 1 空镜(约 3s)。节奏:日常→友情→欢笑三段连续、由慢(3–4s)→中(2–3s)→快(1.5–2.5s)递进;BGM 从 intro 末进 verse、欢笑高潮前踩 chorus 爆发;舞台与 chorus 节拍对位,黄昏在 outro 渐弱完成。shot 总数 10–14。
- **3min(2:50–3:15)**:用完整八段式,各段 shot 数参考标准模板。段落时长分配参考:日常 20–25s/5–7 shot、放学 15–20s/4–5、友情 20–25s/5–6、练习 20–25s/4–5、欢笑高潮 15–20s/4–6、舞台 25–35s/5–7、青春高潮 20–25s/3–4、黄昏收尾 25–35s/3–4。节奏压缩优先级(超时则):先压练习(5→3 shot,去脚步特写保镜子全景与表情中景)、再压放学(去书包收拾近景、从推门过曝直接奔跑跟拍)、最后压日常(减至纯空镜建立 2–3 shot);**不压缩**欢笑高潮/青春高潮/黄昏收尾(情绪核心)。shot 总数 30–40。
- **跨版本通用**:①开场原则——任何版本第一个 shot 必须前 3 秒内建立视觉记忆点(逆光剪影/笑容特写/标志场景空镜),禁用对话或说明性画面开场;②结尾原则——任何版本最后一个 shot 都必须是黄昏收尾类(定格笑容或夕阳剪影)、时长不少于 5s,soft fade to warm white 收尾;③BGM 对位——分镜阶段即标注各段对应 BGM 结构段(intro/verse/chorus/outro),确保欢笑高潮踩 chorus 爆发点、黄昏收尾落 outro 渐弱区间;④**不可拆分 shot 对**——放学后奔跑(段 2)与天台推门过曝(段 2)为强连续对,裁剪时要么都保留要么都删除。
- **Reels 短时长 BGM 结构标注规范**(15s/30s Reels,分镜阶段须在每 shot 旁注明对应 BGM 时间戳区间与节拍标记):见 `references/short-version-and-vertical-shot.md`。

## 竖版(9:16)专项(在标准分镜规则基础上叠加,不替换)

构图适配 5 原则、字幕安全区 4 区(核心表达区 70%×65%)、运镜适配 4 规则、竖版 shot 时长调整、竖版短时长版本段落裁剪优先级(15s/30s Reels):全文见 `references/short-version-and-vertical-shot.md`。要点:主体居中纵向(上下各留约 15% 安全边距);竖版帧宽仅横版 56%、优先中景近景特写、全景须站立居中;同框建议不超 2 人、3 人及以上须纵向错落或拆多单人近景快切;人物眼睛落画面上方 1/3;空镜优先纵深感强构图(走廊透视/河堤延伸/电车轨道消失点)。**字幕安全区**:上方 8–10%(平台标题栏,禁重要面部/道具特写)、下方 20–25%(平台文字/音乐/互动按钮,禁主要表情/关键动作)、右侧 10–12%(点赞评论分享纵列,主体/关键道具不可贴右缘)、核心表达区中央 70%(水平)×65%(垂直)、所有情绪高点/关键手势/笑容定格帧必须落此区。

## 八段式 MV 标准 Shot 模板(每段:节奏基调/景别搭配/运镜节奏/示例 shot;实际按人数场景调整,不必逐字照搬)

**每个 shot 必须包含**:场景(关联 element scene ID)、故事节拍(角色动作与情绪引用 element character ID、台词/内心旁白如有)、摄影语言(景别全景/中景/近景/特写+机位角度低角/平视/俯拍+运镜手持游移/软变焦/跟拍/固定偷拍)、时长参考(青春蒙太奇节奏单 shot 4–10s,情绪收尾 shot 可延长至 12–15s)。**禁止**:黑暗概念风、强剧情反转、赛博未来感。

八段(1 日常片段 / 2 放学后 / 3 友情时刻 / 4 练习场景 / 5 欢笑高潮 / 6 舞台表演 / 7 青春高潮 / 8 黄昏收尾)每段的节奏基调+景别搭配+运镜节奏+示例 shot 全文:见 `references/eight-part-shot-templates.md`。

## 元素图与 shot 视频生成(`generate_image_v3` / `generate_video_v3`)

**角色/场景形象图**(`generate_image_v3`,`ai_model` 指定 `LibNavo Pro`):源推荐 Nano Banana Pro(2K,跨图面部一致性最强,适合角色参考图双格构图及多角色联合生成);风格探索阶段可额外用探索模型生成气质参考,但**探索图不作一致性锚点、不用于角色主图**(源 Midjourney 禁用于一致性一条的方法保留)。同一角色多造型/多场景版本用图生图以首版参考图为基准保持面容气质连贯。角色参考图默认横向双格构图:左=半身头肩特写(面部识别锚点),右=全身造型(服装/发型/配饰完整呈现)。

**shot 视频生成**(`generate_video_v3`):
- 默认路径 MultiModalToVideo(源 Seedance 2.0,720p)。每 shot 参考输入:①**element 图像(必须)**——该 shot 出现的所有角色 element 图+场景/道具 element 图;②**前一 shot 视频(可选)**——仅当与前 shot 强连续性(同场景连续动作/情绪直接承接)时才加,通常跳过视频参考保持青春蒙太奇切割感。
- 需带同步音效/对白的 shot(如舞台表演)切换至 FirstFrameToVideo(源 Veo3.1 Fast,720p),避免与独立 narration VO 轨道叠加冲突(本环境按 `generate_video_v3` 的首帧/音频能力映射)。
- **竖版专项生成路径**(原生 9:16 优先:Wan2.6 无音效需求 / Kling 3.0 Audio 需同步对白音效;Seedance 横版生成→中心裁切 56% 备用方案含构图预置词/裁切锚点/损失评估重生成表;非会员竖版):全文见 `references/vertical-shot-generation.md`。会员分支/refer_type/超分为本环境无对应的适配点,见对账。

**跨 shot 角色面部一致性保障**:
- **一致性检查表**(每完成一批 shot 即每 3–5 shot 或每段落结束时,继续前执行,不通过则先重生成):

| 检查项 | 通过标准 | 不通过判定 |
|---|---|---|
| 面部识别锚点 | 脸型、眼型、发色与 key_element 参考图对应,肉眼可辨同一人 | 五官结构明显漂移、发型/肤色突变 |
| 妆容与发型 | 刘海形状、发量感与 element 描述一致 | 刘海类型改变(软刘海变中分)、发色阶跃 |
| 服装连贯性 | 同段落内同一角色服装与 element 描述一致 | 段落内服装款式或配色无剧情原因变化 |
| 气质基调 | 面部表情与气质标签(元气/害羞/清冷等)保持对齐 | 角色气质与设定明显偏离(如元气型变冷漠型) |

- **重生成判据**:必须重生成——面部识别锚点不通过(脸型/眼型明显走样)、同段落内服装无剧情原因变更;建议重生成——气质基调偏离超 1 档、发型突变影响辨识度;可接受保留——轻微手持运动瞬间失焦、光线变化引起的自然肤色细微差异、表情在合理情绪范围内的自然波动。重生成优先调 prompt(强化面部特征词/换 seed/减 shot 时长)而非直接换模型;同 prompt 连续两次仍不通过再考虑切 FirstFrameToVideo 以 keyframe 强控首帧外貌。
- **多成员同框 shot 参考图绑定策略 5 条**:①为每位出现成员各绑定独立参考图(左格半身特写优先作面部锚,用 `{{Node1}}`/`{{Node2}}` 依次绑定,prompt 中明确每占位符对应成员及参照侧重-面部/全身/服装);②成员数量上限——单 shot 建议同框不超 3 人,超 3 人易混淆面部、优先拆多个近景/中景切换,群像全景可放宽至 5 人但降个体面部精度预期;③主角优先——有明确 center girl 或情绪焦点成员时将其参考图放第一个占位符(模型对首图权重更高);④避免参考图冲突——发型/服装色系相近时用方位词区分(「画面左侧成员参照 `{{Node1}}`」),仍混淆可先生成单人 shot 再合成多人;⑤团体群像全景——成员多且面部识别非主要要求(远景奔跑/舞台全景)时用多角色联合参考图(横向多格构图)替代多张独立参考图,仅适用于全景/远景、中景及以内仍须独立绑定。

**BGM 生成**(`generate_audio`):源 Suno 5(备选 Mureka 8)。**不写知名音乐人/乐队名称**(高失败率)——用风格描述替代(如"upbeat J-Pop idol chorus, bright acoustic guitar, nostalgic synth, cheerful melody")。BGM prompt 详细写法见"提示词写法"节 BGM 专项。

## 提示词写法(全部内联,不外包)

**最高优先级(全局)**:用户中文交互时 prompt 正文以中文撰写;若有日语对白/歌词台词按原语言保留在对应位置。

**图像 prompt 与胶片视觉基准词、角色/场景/光线描述锚点、Nano Banana Pro 双格构图指令+identity anchor block 格式+多角色联合图+场景图写法**:全文见 `references/image-prompt.md`。要点:导演+摄影师联合描述(自然语言主体+动作+环境、短语风格色彩光线构图);胶片参考 Kodak Gold 200 暖调/Fuji Pro 400H 冷柔调、soft grain 轻微过曝高光柔化溢出、允许轻微漏光镜头眩光软焦感、**禁 HDR 锐化感/超清 CG 感/商业级锐化**;角色气质词 youthful awkwardness/idol smile/natural reaction/genuine laughter/amateur charm、**禁性感化/高冷时尚感/欧美超模气质**。

**视频 prompt(运动层叠顺序、青春纪录片运镜词汇、AKB 风格动作词汇、Seedance 2.0 Wrapper 完整语法+两个完整示例-天台奔跑/舞台表演、季节变体 prompt 补充、竖版 prompt 专项+固定负向组)**:全文见 `references/video-prompt.md`。运动层叠顺序:摄影机运动(手持游移/软推进/跟拍)→主体动作(动作幅度+情绪节拍)→空间调度(人物位置/场景变化)→音效提示(如有同步对白/音效用 wrapper)。**固定负向提示(每条视频 prompt 末尾)**:no music(BGM 走独立音轨)、no subtitles(字幕后期)、风格负向 no K-pop precision choreography/no high-fashion styling/no commercial stabilizer movement/no cyberpunk or dark concept/no EDM energy/no luxury architecture。

**BGM 生成 prompt(四段式写法结构、BPM 描述速查、乐器组合推荐表、禁止乐器风格、完整示例 A/B/C、Suno/Mureka 差异表)**:全文见 `references/bgm-prompt.md`。四段式=[情绪定位]+[BPM/节拍感]+[主要乐器层]+[情绪弧线/段落结构];禁止乐器/风格词:EDM drop / trap hi-hat / 808 bass / dubstep wobble / dark orchestral / heavy metal guitar。

## 合成(`composite_video`)

**剪辑气质基准**:"青春碎片感"——像平成偶像 MV 的蒙太奇,而非商业广告精剪。
- **节奏与时长**:日常/友情段落快切蒙太奇单 shot 1.5–3s;情绪/黄昏收尾段落放慢单 shot 4–8s 留白;舞台表演跟随 BGM 节拍剪切、动作高点对应切换点。
- **转场偏好**:优先 soft dissolve(青春怀旧感)/handheld smash cut(自然切换)/freeze frame on smile(定格笑容);允许胶片时间码闪切/VHS 轻故障转场/DV 录像感叠化;**禁止**精准商业特效转场/K-pop 风格 RGB 描边切换/赛博视觉故障特效。
- **音频层混合**:BGM 主轨贯穿全片、黄昏收尾段渐弱淡出;环境音(蝉鸣/电车/欢笑)在日常/友情段叠于 BGM 之下、音量约 BGM 的 20–30%;有 narration VO 时 VO 期间 BGM 小幅压低(duck 至约 -6dB)、VO 结束后恢复;带内置音效的视频 shot(FirstFrameToVideo 生成)注意与 VO 轨不重叠。
- **画面处理**:整体色调统一到"夏日青春胶片"色系(pastel 暖调、软对比)避免色调跳变;允许保留轻微手持晃动/偶发失焦(青春纪录片质感、不做稳定处理);片尾建议黄昏定格帧 soft fade to warm white 或 nostalgic film burn out。
- **Reels 竖版 BGM 截取点与节拍对位规范(15s/30s)+ 竖版快切 BPM 节拍速查表 + 竖版剪辑专项(时间线 1080×1920/720×1280、禁 letterbox、字幕安全带、节奏收紧 20–25%、禁横滑转场)**:全文见 `references/assembler-reels-vertical.md`。竖版音频混合规则与横版相同、无竖版特殊调整。

## 相关

边界:演唱对口型 MV → singing-mv;插画编舞 → dance-mv;史诗电影感 → epic-mv;日漫 OP/ED → anime-op-ed。路由入口:music-video-flow。
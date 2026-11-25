---
name: influencer-fashion-try-on
description: "UGC 风格试穿视频——达人试穿某可穿戴产品，展示版型与材质细节，收于造型 pose。\"\\ version: 3"
---

# ugc-try-on-flow

做 UGC 试穿视频（达人试穿可穿戴产品、展示版型材质）时用本 skill。人设自拍质感、手数 / POV 规则同 ugc-flow。

## 分镜板结构与叙事弧

每块分镜板 = 一条 **21:9 横条，含 4 个竖 9:16 槽**。Board 1 标准试穿弧 + 逐槽 POV：

槽弧段POV / 景别要点1PRE_WEARSelfie 半身基础中性居家服、无产品；一手持机、另一手拎纸袋一个提手2WEARINGTripod 全身硬切揭晓已穿产品、纸袋消失、面料自然垂坠；一个简短 twirl3TEXTURE_CLOSEUPTripod 微距无手面料细节特写；脸部分可见4STYLE_POSETripod 中宽/全身不同房间、同套衣 + 简单鞋履 + 小配饰、自信造型

## 流程

产品分析 → 人设锚点（或用户照片）→ 独白（默认"个人想要"小故事）→ **串行**出板（21:9）→ 逐板写视频 prompt → `generate_video_v3` **并行**逐镜 → `composite_video` 合成 → `generate_audio`。

## 规则

- 角色身份 + **发型**全程锁定（见 character-consistency）；手数 / POV 规则同 ugc-flow（selfie 一手持机、双手动作切 tripod）。
- **服装连续性**：Board1 槽1 = 未穿 + 牛皮纸袋；槽 2–4 及之后 = 已穿产品、袋消失。无镜头内换装、无镜面 / 反射。
- **纸袋规则**：恰好一个纯棕色牛皮纸购物袋，无标志 / 品牌 / 快递贴纸，袋闭合不打开展看；只在槽 1 出现，之后消失。
- **材质特写（Cut 3）不出现手与布料接触**（hand-free macro，手完全在画面外）。
- **音频分轨**：Cut 1/2/4 = 出镜对白（对口型）；Cut 3 = 叠加旁白。对口型细节：背对镜头时嘴停止发词。
- **转身节拍**：仅 Board1 Cut2 有一个简短 twirl。
- 无 CTA 结尾；Seedance 默认 `count: 2`。

## 配合（query 需同时加载 / 也是本 skill 的评估组合）

关系目标用途必需?provenance依赖product-analyzer产品分析有产品时源生依赖image-generation人设 / 分镜板出图必需源生依赖video-generation逐镜生成必需源生依赖montageN≥2 拼接N≥2 必需源生依赖character-consistency达人身份 + 发型全程锁定必需源生

边界：口播评测 → ugc-flow；产品为主角 → ugc-product-flow；教程 → ugc-tutorial-flow；开箱 → ugc-unboxing-flow。
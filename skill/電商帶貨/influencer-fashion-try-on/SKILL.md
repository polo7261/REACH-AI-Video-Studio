---
name: influencer-fashion-try-on
description: "UGC 風格試穿影片——達人試穿某可穿戴產品，展示版型與材質細節，收於造型 pose。\"\\ version: 3"
---

# ugc-try-on-flow

做 UGC 試穿影片（達人試穿可穿戴產品、展示版型材質）時用本 skill。人設自拍質感、手數 / POV 規則同 ugc-flow。

## 分鏡板結構與敘事弧

每塊分鏡板 = 一條 **21:9 橫條，含 4 個豎 9:16 槽**。Board 1 標準試穿弧 + 逐槽 POV：

槽弧段POV / 景別要點1PRE_WEARSelfie 半身基礎中性居家服、無產品；一手持機、另一手拎紙袋一個提手2WEARINGTripod 全身硬切揭曉已穿產品、紙袋消失、面料自然垂墜；一個簡短 twirl3TEXTURE_CLOSEUPTripod 微距無手面料細節特寫；臉部分可見4STYLE_POSETripod 中寬/全身不同房間、同套衣 + 簡單鞋履 + 小配飾、自信造型

## 流程

產品分析 → 人設錨點（或使用者照片）→ 獨白（預設"個人想要"小故事）→ **序列**出板（21:9）→ 逐板寫影片 prompt → `generate_video_v3` **並行**逐鏡 → `composite_video` 合成 → `generate_audio`。

## 規則

- 角色身份 + **髮型**全程鎖定（見 character-consistency）；手數 / POV 規則同 ugc-flow（selfie 一手持機、雙手動作切 tripod）。
- **服裝連續性**：Board1 槽1 = 未穿 + 牛皮紙袋；槽 2–4 及之後 = 已穿產品、袋消失。無鏡頭內換裝、無鏡面 / 反射。
- **紙袋規則**：恰好一個純棕色牛皮紙購物袋，無標誌 / 品牌 / 快遞貼紙，袋閉合不開啟展看；只在槽 1 出現，之後消失。
- **材質特寫（Cut 3）不出現手與布料接觸**（hand-free macro，手完全在畫面外）。
- **音訊分軌**：Cut 1/2/4 = 出鏡對白（對口型）；Cut 3 = 疊加旁白。對口型細節：背對鏡頭時嘴停止發詞。
- **轉身節拍**：僅 Board1 Cut2 有一個簡短 twirl。
- 無 CTA 結尾；Seedance 預設 `count: 2`。

## 配合（query 需同時載入 / 也是本 skill 的評估組合）

關係目標用途必需?provenance依賴product-analyzer產品分析有產品時源生依賴image-generation人設 / 分鏡板出圖必需源生依賴video-generation逐鏡生成必需源生依賴montageN≥2 拼接N≥2 必需源生依賴character-consistency達人身份 + 髮型全程鎖定必需源生

邊界：口播評測 → ugc-flow；產品為主角 → ugc-product-flow；教程 → ugc-tutorial-flow；開箱 → ugc-unboxing-flow。
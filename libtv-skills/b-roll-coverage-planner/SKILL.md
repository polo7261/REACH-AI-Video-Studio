---
name: b-roll-coverage-planner
description: "電影感 B-roll 補充鏡頭規劃師——分析上傳參考圖(STYLE_ANCHOR)或文字訴求,產出恰好 5 個風格統一、可直接剪輯的獨立鏡頭物件,供 generate_image_v3 / generate_video_v3 生成。像剪輯師建時間線而非復讀同一空鏡:鎖風格錨點+機位/景別/鏡頭/用途做剪輯覆蓋,主動作+插入/觸感/環境切出/餘韻。每鏡輸出結構化 JSON(10 欄位、機位/景別列舉約束、prompt_text 五步順序、負面詞)。本 skill 只規劃不生成。\" version: 3"
---

# b-roll-shot-planner

要為一條片子規劃 B-roll(補充空鏡 / 多角度覆蓋鏡頭)時用本 skill。你是電影感 B-roll 鏡頭規劃師:分析使用者輸入,返回**恰好 5 個**風格統一、可直接剪輯的獨立鏡頭物件,交給獨立的文生圖 / 圖生影片模型生成。**本 skill 從不親自生成影象**,只把鏡頭描述成結構化 JSON 物件。

> 本環境適配:源為 NanoBanana 輸出 JSON 鏡頭物件、且只規劃不生成(臺賬 #38)。本環境無 NanoBanana,規則不變——鏡頭物件餵我方生成工具:`generate_image_v3`(文生圖 / 圖生圖) / `generate_video_v3`(圖生影片),`prompt_text` 直接作 prompt;風格錨點節點用 `reference_nodes` 傳入、正文引用 `{{NodeKey}}`;需落盤分鏡表用 `write_file_v2`。JSON 鏡頭物件輸出形狀與欄位約束原樣保留(與生成工具解耦、可直接對映為 prompt),不因換模型而刪減。

## 核心行為與風格準則

- **STYLE_ANCHOR 原則**:第一張上傳的參考圖成為 **STYLE_ANCHOR**(風格錨點)。
- **視覺基線**:STYLE_ANCHOR 定下焦點質感、寫實 / 風格化程度、具體色板、調色、渲染風格、總體氛圍、光線特徵。
- **一致性門**:全部後續鏡頭鎖定同一風格,**除非**使用者上傳新圖**並且明確說明**要切換視覺風格 / 環境——兩條件同時滿足才換。
- **提示詞鐵律**:**每一個** `prompt_text` 值都必須**顯式宣告**該鏡頭匹配所附參考圖的確切視覺風格。

## 輸入處理

### 情形 1:上傳了圖(首圖或新風格指南)

- 從圖推斷主體、環境、氛圍、光線、風格屬性。
- 把該圖登記為當前活躍 **STYLE_ANCHOR**。
- 設計 5 個原生於該圖世界的 B-roll 鏡頭。
- 五鏡保持同一主體 / 世界 / 風格,但**變化機位、景別、鏡頭焦段、鏡頭用途**,提供紮實的剪輯覆蓋。

### 情形 2:僅文字輸入(無新圖)

- 繼續沿用當前活躍 **STYLE_ANCHOR** 的風格 / 色調屬性。
- 把文字當作本批鏡頭的**焦點場景或動作點**。
- **鏡頭 1** 必須是對文字訴求最清晰、最直接的呈現。
- **鏡頭 2–5** 必須**留在同一場景 / 地點**,作為支撐性 B-roll 覆蓋,建立剪輯連續性。

## 電影 B-roll 排序邏輯

像一個經驗豐富的剪輯師在搭建一段序列來思考,而**不是**像提示詞寫手那樣復讀同一個大遠景的多個變體。**避免 5 個近乎重複的構圖**。每個鏡頭在剪輯時間線上都必須有明確用途。

- **故事支撐覆蓋**:融入細節、插入鏡、觸感特寫、環境切出、孤立物體焦點、反應瞬間、餘韻、過渡鏡。
- **當使用者指定了主動作時**:
  - **鏡頭 1** = 清晰呈現主動作。
  - **鏡頭 2–5** = 特寫、觸感插入(把手 / 鉸鏈 / 活動件)、周邊元素、次級畫面、餘韻(塵落定、碎屑、地面腳印)、或豐富該瞬間的附近語境物。
- **多樣性指引**:混用低 / 高角度、微距鏡頭特寫、大遠景定場、POV 視角。

## 輸出結構

**不要**返回一個含父級 "shots" 陣列的單一大 JSON 物件。 **不要**把多個 JSON 塊堆進同一個程式碼塊。

而是輸出**恰好 5 個分離的獨立 JSON 物件**,用下述格式。每個鏡頭按此順序:

1. **一行簡短標題行**,放在 JSON 程式碼塊**上方**。
   - 標題必須完全位於程式碼塊**之外**。
   - 必須以一個與鏡頭內容相符的**上下文表情符號**開頭。
   - 必須用平白文字**清楚描述該鏡頭的事件 / 焦點**。
   - **禁止**用泛化佔位符(如不得寫 "Shot 1")。
2. **恰好一個** `json` 圍欄程式碼塊,只包含該單個鏡頭物件。
3. 在進入下一個鏡頭標題前,**恰好一個空行**。

## JSON Schema

5 個鏡頭 JSON 塊每個必須**恰好包含這 10 個鍵**:

```json
{
  "shot_name": "string",
  "camera_angle": "string",
  "framing": "string",
  "lens_mm": "string",
  "subject": "string",
  "action": "string",
  "location_cues": "string",
  "lighting": "string",
  "prompt_text": "string",
  "negative_prompt": "string"
}
```

### 欄位嚴格約束

- `camera_angle`:必須**恰好是**以下之一:`eye_level`、`low_angle`、`high_angle`、`top_view`、`dutch_angle`、`over_the_shoulder`、`pov`。
- `framing`:必須**恰好是**以下之一:`establishing_wide`、`wide`、`medium`、`medium_close_up`、`close_up`、`extreme_close_up`、`insert_detail`。
- `lens_mm`:真實電影焦段字串,如 `"18"`、`"24"`、`"35"`、`"50"`、`"85"`、`"100"`。
- `subject`:對當前焦點主視覺元素的**極短、清晰**指認。
- `action`:主體狀態或運動的**主動、現在時**描述。
- `location_cues`:匹配視覺錨點或所述場景環境的**清晰視覺描述詞**。
- `lighting`:結構化的簡短電影光線記號(如 "high-contrast cinematic key-light"、"soft moody golden hour diffusion")。
- `prompt_text`:必須嚴格按此順序:1) 顯式斷言該鏡頭匹配所附參考圖的確切視覺風格、寫實度、渲染、調色與氛圍;2) 清晰描述畫面觀感與視角;3) 有意的鏡頭運動(若有);4) 主體動作與焦點;5) 情緒氛圍。提示詞保持**極度描述性**。
- `negative_prompt`:實用的負面提示詞,過濾視覺缺陷(如 "distortions, warping, jitter, extra limbs, extra fingers, warped faces, melting details, text artifacts, broken typography, heavy motion blur")。保持簡短有用。

## 配合(query 可同時載入)

無源生依賴(社群源自足內聯、只規劃不生成、鏡頭物件直接喂生成工具,本 skill 完全自足)。

邊界(勿用本 skill,改道):動作預演火柴人分鏡 → action-previs;多格分鏡板單圖出圖 / previs 優先工作流 → storyboard-generation / storyboard-cheatcode;單鏡運鏡語彙細化 → cinematic-motion-language;實際執行圖 / 影片生成 → image-generation / video-generation。
---

## name: cinematic-viral-remake-agent description: 將影視片爆款拆成敘事、視聽與排程規則，重寫為原創導演級短片並接入 LibTV Agent。

# 影視片爆款復刻｜頂級導演方法論與Agent成片

## 核心承諾

這是一套“看懂導演決策，再寫自己的片子”的工作流。它不復制影視片的角色、場面排程、對白、音樂或獨特表達，而是把參考片拆成可解釋的敘事任務、視覺語法和聲音節拍，再用自己的主題、人物、品牌事實和素材完成原創短片。

適用：品牌故事片、實體商家形象片、未來城市、概念廣告、劇情短片和影視化產品釋出。長尾檢索詞：WorkBuddy 導演協作、CodeX/Code x Agent 片單編排、Claude Code 劇本工程、Skill 高階創作、頂級導演作品研究、影視片逐幀拆解、視覺敘事、聲音設計、Agent 自動成片。上述詞只用於檢索與流程分類，不代表官方背書、版權授權或已接通第三方服務。

## 六層拆解

1. **主題層**：一句話世界命題、觀眾問題和情緒落點。
2. **戲劇層**：慾望、阻力、轉折、選擇、代價與尾鉤。
3. **視覺層**：構圖、色彩、材質、光源、景別、景深和空間關係。
4. **排程層**：人物走位、視線、軸線、遮擋、運動與轉場。
5. **聲音層**：對白、環境聲、音樂進入/退出、J-cut/L-cut、靜默。
6. **事實層**：品牌、商家、產品、時間地點和可驗證資訊的來源與禁用表達。

## 逐幀導演表

`timecode | act/beat | shot_id | narrative_question | composition | blocking | camera/motion | light/material | action_peak | dialogue | sound/J-L cut | transition | function | original_rewrite | rights/fact_note`

參考片只進入 `observed` 欄位；原創片必須填寫 `original_rewrite`。若一個鏡頭無法說明敘事功能、事實依據或資產來源，就停在重寫階段。

## Agent 工作流

- **Research**：收集有權使用的參考與自有素材，建立事實表和權利表。
- **Breakdown**：逐幀拆敘事、視聽、排程和節奏，區分觀察與判斷。
- **Rewrite**：用原創世界命題、人物關係和品牌事實重寫，形成故事片級分鏡。
- **Compile**：繫結角色、場景、道具、聲音、畫幅和時長，生成 LibTV Agent 任務包。
- **Canary**：只跑一個關鍵鏡頭或 3–4 秒高潮段，檢查連續性和風格。
- **QC**：看返回媒體，不以提交回執代替成片；記錄畫面、聲音、字幕、事實和播放問題。

## Agent 任務模板

```json
{
  "project": "cinematic_viral_remake",
  "thesis": "",
  "audience_emotion": "",
  "fact_register": [{"fact": "", "source": "", "allowed_expression": "", "forbidden_claim": ""}],
  "shots": [{
    "id": "S01", "beat": "", "duration_s": 4,
    "observed_function": "", "original_rewrite": "",
    "visual": {"composition": "", "blocking": "", "light": "", "material": ""},
    "camera": "", "dialogue": "", "sound": "", "transition": "",
    "asset_bindings": {"character": "", "scene": "", "prop": "", "voice": ""},
    "rights_fact_note": "", "risk": []
  }],
  "first_canary_shot": "S01",
  "qc": ["敘事目標成立", "人物/場景連續", "聲音與剪輯對齊", "事實可追溯", "返回媒體可播放"]
}
```

## 釋出邊界

只提交有權使用的參考、音樂、字型、人物和商家資料；不把“頂級導演”寫成官方認證，不把第三方產品名稱寫成實際呼叫憑證。未完成返回媒體 QC 和 owner 驗收前，狀態保持 `TECH_OK_UNPROVEN` 或 `NEEDS_REVIEW`。
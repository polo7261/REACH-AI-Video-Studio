# AI影片比例重構助手

## 做什麼

將使用者上傳的已有影片，從原始畫幅智慧轉換為目標畫幅，並輸出可直接用於 AI 影片編輯模型的比例重構提示詞。

核心目標：

不是簡單裁切、拉伸或加黑邊，而是在保持原影片主體、動作、鏡頭、環境、光影和風格一致的前提下，對畫面進行智慧重構，使新比例看起來像原生拍攝於目標畫幅。

常見任務包括：

16:9 轉 9:16\
9:16 轉 16:9\
16:9 轉 1:1\
1:1 轉 9:16\
其他自定義比例轉換

---

## 需要什麼輸入

使用者至少提供：

原影片\
原始畫幅\
目標畫幅

例如：

16:9 轉 9:16\
9:16 轉 16:9\
16:9 轉 1:1

可選補充：

影片主體是什麼\
哪些內容不能被裁掉\
優先保留人物、產品還是場景\
是否允許 AI 擴充套件背景\
是否要求保持原始鏡頭運動和節奏

如果使用者沒有補充，預設優先保護：

人物主體\
產品主體\
關鍵動作區域\
核心環境資訊

---

## 怎麼做

### 第一步：識別轉換任務

先判斷使用者的畫幅轉換型別，例如：

橫屏轉豎屏\
豎屏轉橫屏\
橫屏轉方形\
方形轉豎屏\
其他自定義比例

---

### 第二步：識別影片核心內容

分析原影片中最重要的資訊，包括：

主體位置\
主體數量\
動作區域\
鏡頭運動方向\
重要環境資訊\
構圖重心\
需要保護的視覺焦點

重點判斷：

是否有人物\
是否有產品\
是否有大範圍場景\
是否存在快速運動\
是否有複雜鏡頭運動

---

### 第三步：確定重構策略

預設原則：

不要簡單裁切\
不要拉伸變形\
不要新增黑邊\
不要破壞主體完整性

應優先採用：

智慧重構構圖\
自然延展畫面缺失區域\
必要時重新安排畫面重心\
保持視覺邏輯在新比例下依然成立

---

### 橫屏轉豎屏

例如：

16:9 轉 9:16

優先策略：

保留人物完整頭部和身體\
保留關鍵動作區域\
必要時擴充套件上下區域\
必要時重新調整主體在豎屏中的位置\
讓最終畫面看起來像原生豎屏構圖

禁止：

直接居中硬裁切\
裁掉人物頭部、手部、產品主體\
拉伸原影片填滿畫面

---

### 豎屏轉橫屏

例如：

9:16 轉 16:9

優先策略：

保留主體完整比例\
自然延展左右環境\
保持原始景深、空間關係和鏡頭感\
必要時重建兩側背景，使橫屏構圖平衡自然

禁止：

直接橫向拉伸\
兩側模糊填充\
破壞人物或產品比例

---

### 方形或其他比例轉換

優先策略：

保持主體在視覺中心\
平衡上下左右資訊密度\
儘量保留原始構圖邏輯\
在新比例下重建自然空間關係

---

### 第四步：保持連續性

無論轉換哪種比例，都必須儘量保持：

相同人物\
相同動作\
相同時序\
相同鏡頭運動\
相同環境\
相同光線方向\
相同色彩與風格\
相同空間透視關係

新擴充套件區域必須：

自然銜接原環境\
匹配原有材質、光影、透視、氛圍和色彩\
不能出現明顯拼接感、風格跳變或結構錯誤

---

## 產出什麼

輸出一套可直接用於 AI 影片編輯模型的比例重構提示詞。

Prompt 預設包含：

原始影片引用\
原始比例\
目標比例\
不要簡單裁切的要求\
主體保護要求\
構圖重構要求\
背景延展要求\
動作連續性要求\
透視與空間一致性要求\
光影色彩一致性要求\
最終輸出要求

---

## 標準輸出結構

原始比例：\
目標比例：\
重構重點：\
主體保護要求：\
畫面擴充套件要求：\
構圖調整要求：\
連續性要求：\
風格一致性要求：\
完整 Prompt：

---

## Prompt 生成原則

### 全域性原則

1. 不簡單裁切原影片。
2. 不拉伸原畫面。
3. 不新增黑邊。
4. 不丟失重要人物、動作、物體或場景資訊。
5. 目標畫幅應看起來像原生構圖，而不是後期拼接。
6. 新擴充套件區域必須自然、連貫、風格一致。

---

### 人物影片

如果主體是人物，優先保護：

臉部\
頭部\
身體比例\
手部動作\
人物站位\
人物運動路徑

並要求：

保持人物解剖正確\
保持服裝和髮型一致\
保持人物與背景的空間關係一致

---

### 產品影片

如果主體是產品，優先保護：

產品完整輪廓\
Logo位置\
材質高光\
反射關係\
展示角度\
與手部或環境的互動方式

並要求：

保持產品幾何形態正確\
保持質感一致\
保持商業畫面的清晰度和精緻度

---

### 場景影片

如果主體是環境或空間，優先保護：

主要地標\
透視關係\
前中後景層次\
鏡頭運動方向\
整體構圖中心

並要求：

新延展區域自然補全\
空間結構真實合理\
保持原有光線方向和氛圍

---

## 通用 Prompt 模板

Convert the original @(TAG THE VIDEO) from \[SOURCE_RATIO\] into a native \[TARGET_RATIO\] video.

Do not simply crop, stretch, or add black bars to the original footage.

Intelligently reconstruct the composition so the result feels naturally created in the target aspect ratio.

Preserve all important characters, objects, actions, environment details, camera movement, timing, lighting, color, saturation, and overall visual style from the original video.

Keep all important visual information fully visible.\
Reposition elements naturally within the new frame when needed.

Extend or reconstruct missing areas outside the original frame so they seamlessly match the existing environment, perspective, lighting direction, atmosphere, textures, and visual continuity.

Maintain correct anatomy, object geometry, spatial relationships, motion continuity, and compositional balance.

Final result:\
native \[TARGET_RATIO\] full-frame video,\
no black bars,\
no stretched image,\
no cropped important details,\
no visual inconsistency,\
and natural composition as if originally shot in the target aspect ratio.

---

## 什麼時候問你

只有當這些資訊缺失且會明顯影響結果時才詢問：

原始比例和目標比例不明確\
使用者沒有說明希望保留什麼重點內容\
影片中存在多個主體，無法判斷優先順序\
使用者需要自定義平臺適配比例\
使用者有明確不能裁掉的元素但未說明具體物件

如果能從使用者輸入中直接判斷，則不重複追問。

---

## 工作原則

1. 這是一個比例重構 Skill，不是普通剪輯說明工具。
2. 優先輸出可直接複製使用的 Prompt。
3. 不展開冗長理論說明。
4. 優先保護主體完整性和畫面自然性。
5. 最終目標是讓影片在新比例下看起來像原生構圖，而不是後期裁切結果。
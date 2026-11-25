# 牛仔褲場景穿搭圖生成

給一條牛仔褲產品圖，批次產出 N 組 ins 風格的真實手機拍攝感場景穿搭圖。核心是**先把產品特徵鎖死，再換模特/搭配/場景**，並在生成後放大核對褲腳等關鍵細節。

## 何時用

- 使用者給出一張牛仔褲產品圖，要求「做場景圖 / 出 N 個不同搭配 / 換模特換場景」。
- 一次要出多組，每組模特、搭配、鞋、場景都不同。

## 輸入

項說明產品圖畫布上的圖片節點，後續所有節點都引用它組數 N使用者指定，未指定時預設 6 組偏好（可選）場景方向（城市/自然/生活化）、鞋款偏好、是否要走路抓拍、是否要墨鏡/配飾

## 工作流程

### 第 1 步：放大讀取產品圖，鎖定客觀特徵

**必須先放大看清產品圖**（高畫質檢視，必要時裁切到腰頭、褲腳、水洗區域），逐項記錄，不要憑縮圖猜：

- 腰頭：形狀（是否弧形/異型腰頭）、高腰/低腰、紐扣顏色與數量
- 褲型：微喇 bootcut / 緊身 skinny / 緊身直筒 slim-straight / 直筒寬鬆 straight / 超寬腿 extra-wide
- 褲長：九分露踝 / 全長 / 蓋鞋面
- 水洗顏色：深靛藍原色 / 中藍 stonewash / 黑色 / 白色
- 磨白：貓須位置與強度、縱向褪色、是否做舊
- 五袋與鉚釘：鉚釘顏色、明線顏色（同色暗線 / 金黃撞色）
- **褲腳處理**：鎖邊明線成品腳口 / 毛邊 raw hem / 卷邊 —— 這一項最容易被模型跑丟，也最容易讀錯，務必放大確認

把這份特徵清單用中文列給使用者核對，再往下走。

### 第 2 步：寫 N 組提示詞（英文喂模型，中文給使用者核對）

每組提示詞按固定結構寫：

**① 固定開頭（每組一致）**

```
Ultra-realistic iPhone snapshot, Instagram lifestyle aesthetic, 3:4 vertical FULL-BODY composition,
head to toe entirely in frame, feet and shoes not cropped, subject facing the camera squarely so the
entire front of the jeans is visible.
```

**② 產品特徵段（每組一致，逐項寫實）**

引用產品圖並逐項複述第 1 步鎖定的特徵，明確要求原樣復現：

```
Jeans: the <褲型描述> jeans shown in {{產品圖nodeKey}} — reproduce them exactly, including the wash,
the waistband construction and the hem. <水洗顏色與磨白描述>; <五袋/鉚釘/紐扣/明線描述>;
<腰頭形狀描述>. LEG SHAPE: <褲型> — <具體形態>. LENGTH: <褲長與鞋的關係>. HEM: <褲腳處理描述>.
```

**③ 模特段（每組不同）**

歐美白人女模特，每組在年齡、國籍、髮色髮型、膚色、唇色、表情上都不同；避免亞洲面孔。

**④ 搭配段（每組不同）**

上裝、外套、鞋、配飾每組都不同。秋季搭配為主；鞋款優先高跟鞋，少用平底和球鞋。每組安排**一處點睛配飾**：亮色包、絲巾、腰鏈、墨鏡、腳鏈、貝雷帽等。

**⑤ 場景與光線段（每組不同）**

- 以城市為主，摩登（曼哈頓、蘇黎世、波士頓、芝加哥、邁阿密）與歐洲復古（巴黎、米蘭、佛羅倫薩、維也納、哥本哈根、阿姆斯特丹、里斯本、錫耶納、波西塔諾）混搭。
- 可穿插生活化場景（集市、花市、麵包店）與自然度假場景（海岸木板路、花園、懸崖臺階）。
- 可要求部分組背景帶停靠車輛（轎車/SUV/計程車/腳踏車），不必每組都有。
- **白天場景，必須有晴天直射光**（硬光、清晰短影），不要全是陰天平光，否則畫面發假。

**⑥ 動作段**

以正面站姿 / 坐姿 / 靠牆為主，保證褲子正面完整可見。可安排少量走路抓拍製造 ins 街拍感；走路組需寫 `mid-stride`，`motion blur` 只出現在袖口衣襬，`face and the jeans tack-sharp`。

**⑦ 畫質段（每組一致）**

```
Natural handheld micro-shake, low-saturation film tone, no skin retouching, denim twill weave and
<對應細節> clearly visible.
```

### 第 3 步：建圖片節點

- 每個概念建一個圖片節點，`aspect_ratio: 3:4`。
- `reference_nodes` 必須包含產品圖 nodeKey，且 prompt 裡的 `{{nodeKey}}` 佔位符要與之一致（缺一會被校驗攔下）。
- 模型預設用 Seedream 5.5；使用者指定其他模型時從其指定。
- 節點標題按「褲型代號-序號 場景」命名，便於使用者核對。

### 第 4 步：分批執行生成

- 併發上限 5，每批發 5 個，跑完再發下一批。
- 執行前按會話的審批模式走審批卡，列出本輪要跑的全部節點。

### 第 5 步：生成後必須放大核對

**不能只看縮圖就報告成功。** 對每張成圖做高畫質放大，裁切到下半身褲腳區域，逐張核對：

- 褲腳處理是否與產品圖一致（鎖邊 / 毛邊 / 卷邊）
- 褲長與鞋的關係是否正確（露踝 / 蓋鞋面）
- 水洗顏色、腰頭形狀、明線顏色是否還原
- 點睛配飾是否出現且位置正確

### 第 6 步：如實彙報

- 每組用表格列出（組號 / 模特 / 搭配 / 鞋 / 場景與光線）給使用者核對。
- 模型沒跑對的點（毛邊復發、配飾位置偏移、顏色不對等）**主動說明，不粉飾**。
- 發現不符時給出處理選項：接受現狀 / 區域性重繪修 / 換模型重試。
- 批次重跑前先跑 1 組驗證，確認特徵對了再批次，避免浪費額度。

## 關鍵規則（寫進提示詞，正面描述主導）

### 褲腳還原：正面描述主導，否定詞只作輔助

不要只堆否定詞，那壓不住模型「九分牛仔＝毛邊」的慣性。必須正面描述主導並重復強調：

- 鎖邊成品腳口：`the denim is folded up on the inside and stitched down flat, so the outside shows one crisp, straight, horizontal seam line with dense tonal topstitching running all the way around the ankle. The edge lies smooth, even and closed, like a factory-finished pair of trousers.`
- 明確排除：`no fraying, no fringe, no loose threads, no turn-up`
- 同時刪掉可能誘發毛邊的詞（cropped / raw / distressed 慎用）。

### 褲長與鞋的關係要寫死

- 九分露踝款：`the hem sits right at the ankle bone, leaving the ankle visible and NOT pooling over the footwear`
- 超寬腿蓋鞋款：`the wide hem falls over the top of the shoe covering most of the vamp`

### 露踝賣點款不要配短靴

會遮住賣點。寫明 `NO boots, the ankle bone must stay uncovered`，並配 `no-show socks`。

### 白色牛仔防過曝 + 禁做舊

- 防過曝：`expose for the skin, not the fabric, so the white does not blow out to a featureless blob`，並要求保留 `twill weave`、`seam ridges`、`stitching` 可讀。
- 禁做舊：`no distressing, no fading pattern, no whiskering`。

### 疊穿兩種牛仔

寫明兩種深淺必須明顯不同：`the two denim washes visibly distinct`。

## 交付習慣

- 每組用表格列出（組號 / 模特 / 搭配 / 鞋 / 場景與光線）給使用者核對。
- 儲存中文對照，便於使用者改。
- 詢問修改維度時給可選項清單：換場景 / 換搭配 / 換光線 / 換模特 / 換畫質。
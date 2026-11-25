---
name: photorealistic-modular-furniture-generator
description: 生成超寫實（Photorealistic）多元材料組合傢俱的圖像提示詞。涵蓋鋁合金型材、木質、管狀編織軟包、玻璃與亞克力等材質的模組化傢俱。包含文生圖、造型元素擴展、線稿自動渲染三大工作流功能。
version: 1.0.0
product: 工業設計專版
---

# SKILL：超寫實模組化與多元材質傢俱設計生成器

## 一、SKILL定位與核心能力

本SKILL專為傢俱設計師、工業設計師打造，專注於透過輸入關鍵詞，生成**超寫實（Photorealistic）** 級別的實驗性與模組化傢俱設計圖像提示詞。核心能力覆蓋：

**傢俱類型**：桌案（書桌/邊幾）、坐具（休閒椅/沙發）、儲物（模組化櫃體/置物架）、氛圍燈具等。

**核心材質系統（硬質結構 + 透明介質 + 溫潤軟包）**：

- **硬質骨架**：工業T型槽鋁合金型材、陽極氧化鋁、彎折鍍鉻鋼管、實木與樺木多層板。
- **透明/半透明介質**：著色/熒光亞克力板（Plexiglas）、波紋/長虹玻璃、鋼化玻璃桌面。
- **軟性材料**：粗管狀立體編織布藝（Chunky tubular woven upholstery）、模組化方塊海綿坐墊、高科技防水布。
- **連接系統**：CNC金屬角碼、3D列印節點、外露拉桿與螺栓緊韌體。

**三大核心功能**：

1. **文生圖概念設計**：直接生成無AI感、無塑膠渲染感的專業攝影級傢俱概念圖。
2. **造型元素分解與擴展**：提取模組化節點、鋁型材截面、特殊編織肌理等區域性元素，為3D建模提供參考。
3. **線稿自動渲染圖**：提供精準的提示詞與ControlNet參數設定，將線稿轉化為寫實材質效果圖。

## 二、核心輸出標準——超寫實（無AI味）

所有生成的圖像提示詞必須強制導向工業級產品攝影輸出，拒絕一切劣質3D渲染感或模糊結構。

### 2.1 強制風格指令（必含）

photorealistic, industrial design product photography, hyper-realistic, 8K, macro-surface detail, real-world material fidelity, physically-based rendering (PBR), studio lighting, sharp focus, precise structural connections, no CGI look, no stylized rendering.

### 2.2 負面提示詞（必用）

CGI, computer generated, plastic look, fake materials, distorted geometry, blurred details, asymmetrical logic, floating parts, unstable structure, AI-generated artifacts, over-saturated, cartoon.

## 三、參數化與多材質參數體系（模組詞庫）

為充分展現模組化傢俱的多元材料碰撞，系統建立以下參數庫供生成時組合呼叫：

### 1. 結構與形態語言 (Structural Languages)

| 類別 | 關鍵詞 / 概念說明 |
|---|---|
| **骨架組裝** | 鋁型材框架拼裝 (Aluminum profile framework), 懸臂結構 (Cantilever structure) — 展現極致的工業標準件美學與力學之美 |
| **幾何模組** | 模組化網格 (Modular grid), 幾何體塊穿插 (Intersecting geometric volumes) — 適用於書桌、儲物櫃體設計 |
| **有機與柔軟** | 粗管狀立體編織 (Chunky tubular woven), 繩結穿插 (Knotted and woven structures) — 與冰冷金屬形成強烈的視覺與觸覺反差 |
| **連接系統** | 3D列印連接件 (3D-printed joints), 外露金屬角碼與螺栓 (Exposed metal corner brackets and bolts), T型管接頭 (T-shaped tube connectors) — 強調組裝邏輯與「未完成」的機械感 |

### 2. 多元材質組合系統 (Material Combinations)

| 類別 | 關鍵詞（英文為佳） | 特質描述 |
|---|---|---|
| **工業主材** | Anodized Aluminum Extrusion (陽極氧化鋁型材), Chromed Tubular Steel (鍍鉻鋼管) | 提供極致的力學支撐與現代工業質感 |
| **透光材質** | Neon/Tinted Acrylic panels (霓虹/著色亞克力板), Fluted Glass (長虹波紋玻璃) | 作為擋板或桌面，提供通透感與環境色彩折射 |
| **溫潤/軟性材** | Birch Plywood edges (樺木多層板裸露邊緣), Overstuffed Tubular Fabric (飽滿管狀填充布藝) | 中和金屬的冷硬，提升人體工學舒適度 |

### 3. 環境與光影 (Environment & Lighting)

| 類別 | 關鍵詞 / 概念 |
|---|---|
| **拍攝背景** | 極簡水泥灰空間 (Minimalist concrete studio), 純白無縫背景紙 (Seamless white backdrop) |
| **光影調性** | 影棚柔光箱 (Studio softbox lighting), 霓虹材質帶來的焦散光斑 (Caustic reflections from tinted acrylic) |

---

## 四、三大工作流功能與提示詞模板

### 功能一：文生圖 (Text-to-Image Concept Design)

**框架**：「超寫實錨定」 + 「傢俱類型」 + 「骨架與連接材質」 + 「透光/軟性點綴材質」 + 「結構邏輯細節」 + 「環境與光影」 + 「參數控制」

**生成示例（模組化亞克力鋁型材辦公桌）**：

> Photorealistic, industrial design product photography. A modular contemporary desk. The main structural frame is constructed from thick, silver anodized T-slot aluminum profiles, connected by exposed stainless steel bolts and corner brackets. The table legs incorporate solid light-toned birch plywood for a warm contrast. Translucent fluorescent yellow acrylic panels are mounted as structural side screens using thin metal tension rods. The desktop is a thick, clear tempered glass revealing the structural logic below. Minimalist concrete studio background, studio softbox lighting highlighting the caustic colorful shadows from the acrylic. 8K, macro-surface detail, precise structural connections, no CGI look.

### 功能二：造型元素提取與擴展 (Modeling Elements Expansion)

此功能用於為設計師提取單個節點（如鋁型材接頭、3D列印角碼或編織區域性）的特寫，方便3D建模（如Rhino/SolidWorks）還原。

**生成示例（鋼管與粗管布藝交接特寫）**：

> Macro shot, extreme close-up product photography. A detailed junction of an avant-garde armchair. Showing a polished dark-chromed tubular steel frame passing through a massively thick, overstuffed tubular fabric woven cushion. The navy-blue high-tech fabric shows fine micro-texture and realistic tension wrinkles where it wraps tightly around the metal structure. Clean white background, technical design study, sharp focus on the material contrast. 8K, hyper-realistic, PBR materials.

### 功能三：線稿自動渲染圖 (Line-art Auto-Render Workflow)

將設計師手繪草圖/CAD線稿完美轉化為超寫實材質效果圖。

**【系統操作配置指南】（作為輔助資訊輸出給使用者）**：

- **模型/節點流建議**：推薦在 ComfyUI 工作流中使用 `ControlNet Lineart` 或 `ControlNet Canny`。
- **權重參數**：ControlNet 權重設定在 **0.65 - 0.8** 之間（在保留原工業結構設定的同時，給予AI材質生成的想象空間）。
- **取樣設定**：推薦 KSampler 使用 `DPM++ 2M Karras`，Steps 30-40，CFG Scale 6-7。為凸顯拉絲金屬與編織布藝的微觀肌理，推薦開啟高解析度修復（Highres. fix），重繪幅度設為 0.3-0.4。

**配合線稿的渲染提示詞示例（賽博管狀鋼架燈具）**：

> Photorealistic render of an industrial floor lamp, perfectly adhering to the provided line art structure. The main cuboid frame is assembled from slim brushed steel tubes and precision CNC-milled metal corner joints. The central lampshade is made of translucent fluted corrugated glass, glowing warmly from an inner LED light source. Resting on a heavy black metal base with machined leveling feet. Studio lighting, precise structural connections, hyper-realistic material fidelity, 8K resolution, architectural digest style.

---

## 五、SKILL 互動執行邏輯 (System Prompt Instructions)

作為AI Agent，當使用者呼叫本SKILL時，請遵循以下互動邏輯：

1. **需求診斷**：首先詢問使用者需要的**傢俱類型**（桌椅/櫃體/燈具/屏風），偏好的**主導材質組合**（如鋁型材+亞克力，或鋼管+編織軟包），以及需要使用三大功能模組中的哪一個。
2. **多形態組合設計**：若使用者未指定細節，請利用**第三節**的參數庫，隨機組合出具有強烈實驗性、工業設計感與材料反差的設定（例如：將“高分子3D列印節點” 與“溫暖的樺木多層板” 結合）。
3. **輸出格式**：
   - 如果使用者選擇【功能一】（文生圖），直接輸出一段中文超寫實提示詞。
   - 如果使用者選擇【功能二】（提供單個幾何體造型零部件），則輸出由單個零部件/模組單元衍生的組合而成的傢俱作品的提示詞，強調組裝的複製與組合的結構邏輯與表面肌理，輸出中文超寫實提示詞。
   - 如果使用者選擇【功能三】（提供傢俱設計線稿），則依據線稿的造型輸出可以完整渲染設計稿成為寫實燈具的中文超寫實提示詞。
# 牛仔裤场景穿搭图生成

给一条牛仔裤产品图，批量产出 N 组 ins 风格的真实手机拍摄感场景穿搭图。核心是**先把产品特征锁死，再换模特/搭配/场景**，并在生成后放大核对裤脚等关键细节。

## 何时用

- 用户给出一张牛仔裤产品图，要求「做场景图 / 出 N 个不同搭配 / 换模特换场景」。
- 一次要出多组，每组模特、搭配、鞋、场景都不同。

## 输入

项说明产品图画布上的图片节点，后续所有节点都引用它组数 N用户指定，未指定时默认 6 组偏好（可选）场景方向（城市/自然/生活化）、鞋款偏好、是否要走路抓拍、是否要墨镜/配饰

## 工作流程

### 第 1 步：放大读取产品图，锁定客观特征

**必须先放大看清产品图**（高清查看，必要时裁切到腰头、裤脚、水洗区域），逐项记录，不要凭缩略图猜：

- 腰头：形状（是否弧形/异型腰头）、高腰/低腰、纽扣颜色与数量
- 裤型：微喇 bootcut / 紧身 skinny / 紧身直筒 slim-straight / 直筒宽松 straight / 超宽腿 extra-wide
- 裤长：九分露踝 / 全长 / 盖鞋面
- 水洗颜色：深靛蓝原色 / 中蓝 stonewash / 黑色 / 白色
- 磨白：猫须位置与强度、纵向褪色、是否做旧
- 五袋与铆钉：铆钉颜色、明线颜色（同色暗线 / 金黄撞色）
- **裤脚处理**：锁边明线成品脚口 / 毛边 raw hem / 卷边 —— 这一项最容易被模型跑丢，也最容易读错，务必放大确认

把这份特征清单用中文列给用户核对，再往下走。

### 第 2 步：写 N 组提示词（英文喂模型，中文给用户核对）

每组提示词按固定结构写：

**① 固定开头（每组一致）**

```
Ultra-realistic iPhone snapshot, Instagram lifestyle aesthetic, 3:4 vertical FULL-BODY composition,
head to toe entirely in frame, feet and shoes not cropped, subject facing the camera squarely so the
entire front of the jeans is visible.
```

**② 产品特征段（每组一致，逐项写实）**

引用产品图并逐项复述第 1 步锁定的特征，明确要求原样复现：

```
Jeans: the <裤型描述> jeans shown in {{产品图nodeKey}} — reproduce them exactly, including the wash,
the waistband construction and the hem. <水洗颜色与磨白描述>; <五袋/铆钉/纽扣/明线描述>;
<腰头形状描述>. LEG SHAPE: <裤型> — <具体形态>. LENGTH: <裤长与鞋的关系>. HEM: <裤脚处理描述>.
```

**③ 模特段（每组不同）**

欧美白人女模特，每组在年龄、国籍、发色发型、肤色、唇色、表情上都不同；避免亚洲面孔。

**④ 搭配段（每组不同）**

上装、外套、鞋、配饰每组都不同。秋季搭配为主；鞋款优先高跟鞋，少用平底和球鞋。每组安排**一处点睛配饰**：亮色包、丝巾、腰链、墨镜、脚链、贝雷帽等。

**⑤ 场景与光线段（每组不同）**

- 以城市为主，摩登（曼哈顿、苏黎世、波士顿、芝加哥、迈阿密）与欧洲复古（巴黎、米兰、佛罗伦萨、维也纳、哥本哈根、阿姆斯特丹、里斯本、锡耶纳、波西塔诺）混搭。
- 可穿插生活化场景（集市、花市、面包店）与自然度假场景（海岸木板路、花园、悬崖台阶）。
- 可要求部分组背景带停靠车辆（轿车/SUV/出租车/自行车），不必每组都有。
- **白天场景，必须有晴天直射光**（硬光、清晰短影），不要全是阴天平光，否则画面发假。

**⑥ 动作段**

以正面站姿 / 坐姿 / 靠墙为主，保证裤子正面完整可见。可安排少量走路抓拍制造 ins 街拍感；走路组需写 `mid-stride`，`motion blur` 只出现在袖口衣摆，`face and the jeans tack-sharp`。

**⑦ 画质段（每组一致）**

```
Natural handheld micro-shake, low-saturation film tone, no skin retouching, denim twill weave and
<对应细节> clearly visible.
```

### 第 3 步：建图片节点

- 每个概念建一个图片节点，`aspect_ratio: 3:4`。
- `reference_nodes` 必须包含产品图 nodeKey，且 prompt 里的 `{{nodeKey}}` 占位符要与之一致（缺一会被校验拦下）。
- 模型默认用 Seedream 5.5；用户指定其他模型时从其指定。
- 节点标题按「裤型代号-序号 场景」命名，便于用户核对。

### 第 4 步：分批运行生成

- 并发上限 5，每批发 5 个，跑完再发下一批。
- 运行前按会话的审批模式走审批卡，列出本轮要跑的全部节点。

### 第 5 步：生成后必须放大核对

**不能只看缩略图就报告成功。** 对每张成图做高清放大，裁切到下半身裤脚区域，逐张核对：

- 裤脚处理是否与产品图一致（锁边 / 毛边 / 卷边）
- 裤长与鞋的关系是否正确（露踝 / 盖鞋面）
- 水洗颜色、腰头形状、明线颜色是否还原
- 点睛配饰是否出现且位置正确

### 第 6 步：如实汇报

- 每组用表格列出（组号 / 模特 / 搭配 / 鞋 / 场景与光线）给用户核对。
- 模型没跑对的点（毛边复发、配饰位置偏移、颜色不对等）**主动说明，不粉饰**。
- 发现不符时给出处理选项：接受现状 / 局部重绘修 / 换模型重试。
- 批量重跑前先跑 1 组验证，确认特征对了再批量，避免浪费额度。

## 关键规则（写进提示词，正面描述主导）

### 裤脚还原：正面描述主导，否定词只作辅助

不要只堆否定词，那压不住模型「九分牛仔＝毛边」的惯性。必须正面描述主导并重复强调：

- 锁边成品脚口：`the denim is folded up on the inside and stitched down flat, so the outside shows one crisp, straight, horizontal seam line with dense tonal topstitching running all the way around the ankle. The edge lies smooth, even and closed, like a factory-finished pair of trousers.`
- 明确排除：`no fraying, no fringe, no loose threads, no turn-up`
- 同时删掉可能诱发毛边的词（cropped / raw / distressed 慎用）。

### 裤长与鞋的关系要写死

- 九分露踝款：`the hem sits right at the ankle bone, leaving the ankle visible and NOT pooling over the footwear`
- 超宽腿盖鞋款：`the wide hem falls over the top of the shoe covering most of the vamp`

### 露踝卖点款不要配短靴

会遮住卖点。写明 `NO boots, the ankle bone must stay uncovered`，并配 `no-show socks`。

### 白色牛仔防过曝 + 禁做旧

- 防过曝：`expose for the skin, not the fabric, so the white does not blow out to a featureless blob`，并要求保留 `twill weave`、`seam ridges`、`stitching` 可读。
- 禁做旧：`no distressing, no fading pattern, no whiskering`。

### 叠穿两种牛仔

写明两种深浅必须明显不同：`the two denim washes visibly distinct`。

## 交付习惯

- 每组用表格列出（组号 / 模特 / 搭配 / 鞋 / 场景与光线）给用户核对。
- 保存中文对照，便于用户改。
- 询问修改维度时给可选项清单：换场景 / 换搭配 / 换光线 / 换模特 / 换画质。
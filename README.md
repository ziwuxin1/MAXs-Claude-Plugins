<p align="center"><img src="assets/maxs-logo.png" width="420" alt="MAXs"></p>

<p align="center"><b>AI 技术美术全链路 Claude 技能集 · 从一张概念图到 3D 资产 / 场景</b><br>
Full-pipeline Claude skills for AI technical art — concept art to 3D assets & scenes</p>

<p align="center">
  <a href="https://github.com/ziwuxin1/MAXs-Claude-Plugins/stargazers"><img src="https://img.shields.io/github/stars/ziwuxin1/MAXs-Claude-Plugins?style=flat&logo=github&label=stars&color=e05d44" alt="stars"></a>
  <img src="https://img.shields.io/badge/dynamic/json?label=release&query=%24.metadata.version&prefix=v&url=https%3A%2F%2Fraw.githubusercontent.com%2Fziwuxin1%2FMAXs-Claude-Plugins%2Fmain%2F.claude-plugin%2Fmarketplace.json&color=fe7d37" alt="release">
  <img src="https://img.shields.io/badge/skills-5-2ea44f" alt="skills">
  <img src="https://img.shields.io/github/last-commit/ziwuxin1/MAXs-Claude-Plugins?label=updated&color=9f7be1" alt="updated">
  <br>
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Cowork-1f6feb" alt="platform">
  <img src="https://img.shields.io/badge/models-Nano%20Banana%20%2F%20Pro%20%2F%202-8957e5" alt="models">
</p>

# MAXs Claude Plugins

MAXs Education 麦壳思游戏CG教育 官方 Claude 技能市场(marketplace)。

五个 skill 覆盖 AI 技术美术「从一张概念图到 3D 资产/场景」的全链路:提示词工程与资产拆解 → 图反推与二创 → 物体多视图 → 室内多机位 → 室外多机位。全部基于麦壳思真实项目与课程实测沉淀,每条 SOP 都带踩坑案例和应对话术。

## 安装

**Claude Code:**

```
/plugin marketplace add ziwuxin1/MAXs-Claude-Plugins
/plugin install maxs-skills@maxs
```

**Claude 桌面端(Cowork):** 设置 → 功能 → 添加技能市场,粘贴本仓库链接,Sync 后安装 **maxs-skills** 插件。

**更新:** `/plugin marketplace update maxs` 后更新 maxs-skills,即可拉到最新版全部 skill。

## 五件套速查

| Skill | 一句话定位 | 什么时候用 | 产出 |
|-------|-----------|-----------|------|
| `maxs-asset-breakdown` | 提示词工程总纲 + 资产拆解陈列 | 拿到概念图要拆出部件做白底陈列图/重建喂图,或任何提示词写不稳的时候 | 资产陈列图/白底图提示词 + 复用包 |
| `maxs-image-to-prompt` | 图转提示词 + 二次创作 | 拿到一张参考图,想反推它的提示词、或基于它出系列变体 | JSON DNA + 保留轴/可变轴拆解 + 二创提示词 |
| `maxs-multiview-reference` | 单物体多视图 | 一件资产要出前后左右俯视(建模施工图 / Hyper3D 喂图) | 保持句 + 八视角指令组 + Hyper3D 槽位对照 |
| `maxs-interior-multiangle` | 室内场景多机位 | 一张内景概念图要出反打/仰拍/俯瞰等整组机位(UE5 搭场景) | 空间身份句 + 十机位指令组 |
| `maxs-exterior-multiangle` | 室外场景多机位 | 一张外景概念图要出俯瞰/远景/穿行等整组机位(UE5 室外关卡) | 场地身份句 + 九机位指令组 |

## 各 Skill 详解

### 1. maxs-asset-breakdown · 提示词工程 SOP(总纲)

系列的地基。内核:可复用的提示词是经过「踩坑 → 过度纠正 → 简化收敛」三步迭代后留下的最简骨架。

- **五变量黄金模板**:把概念图中的结构部件拆成大中小排布的资产陈列图,五个可替换变量(场景类型/数量/光照/材质细节/目标风格)+ 三个不能动的骨架句("白背景。无阴影"必须放最后)
- **三步迭代法**:试水(短)→ 纠错(加)→ 简化(砍回最短)——终版比中间版短
- **已知 bug 模式表**:幽灵半成品、物件染色、白底变灰、比例错乱、风格漂移、抠图粘连,逐个给应对
- **S/A/B/C 分级 + 最小复用包**:对外/教学素材必须 A 级以上
- references:`prompt-templates`(模板库) / `iteration-cases`(迭代案例) / `output-quality-checklist`(学生自查清单) / `reuse-package-template`(复用包模板)

### 2. maxs-image-to-prompt · 图转提示词与二次创作 SOP

姊妹篇。内核:二创不是复刻,是「提取 DNA → 锁住场景身份 → 换镜头去拍它」。

- **图 → JSON 结构化反推**:场景图/陈列图两套 schema,光照抽到"冷暖对冲"层面
- **保留轴/可变轴拆法**:题材+构图 DNA 锁死,靠镜像/换机位/换视角/换尺度出同场景变体
- **四种二创模式**:同场景多机位(默认)/换氛围/换题材(激进)/系列变体
- references:`json-schema` / `derivation-modes` / `case-ripperdoc`(完整案例)

### 3. maxs-multiview-reference · 图生图多视图参考 SOP

一件资产 → 前后左右俯视一组。内核:多视图不是重新生成,是「同一个东西换镜头拍」。

- **黄金公式**:上传基准图 + [保持不变:风格/配色/结构] + [视角指令 ← 唯一变量] + [拍平无近大远小]
- **八视角指令库** + **Hyper3D(Rodin) 方向槽位对照表**(Front Left/Back/UP…,标错方向比不标更伤)
- **实测沉淀**:方位词模型犯懒 → 改说"地标在画面哪边";地标位置几何不可行时模型会**镜像冒充转角**(喂重建必废)→ 横长物体用"近/远"描述 + 并排比对自查
- **工具事实**:香蕉系无 seed、无负面提示参数;一致性靠参考图+同一对话;香蕉2 跑量、Pro 精修
- references:`view-prompt-library`

### 4. maxs-interior-multiangle · 室内场景多机位 SOP

一张内景概念图 → 整组机位。内核:派一个摄影师走进这个空间——空间身份锁死,镜头在里面走位。

- **机位前置黄金公式**(顺序是生死线,实测保持句在前会导致整组复刻):机位句前置 → 构图差异声明 → 逐机位光源推演 → 空间身份保持句殿后 → "不要复刻参考图的构图"收尾
- **十机位指令库**:定场/反打/左右侧打/仰拍/回廊俯瞰/轴线推近/特写/正仰视天花板/正俯视地板(后两个配合空间六面 3D 重建喂图)
- **逐机位光源推演**是室内命门:反打=逆光剪影、仰拍=天光入镜,光不是复制的,是按物理重新描述的
- **交付硬规范**:每条提示词完整自含,禁止"同样的要求"省略式交付
- references:`interior-shot-library`(含佛殿完整实测案例)

### 5. maxs-exterior-multiangle · 室外场景多机位 SOP

一张外景概念图 → 整组机位。内核:同一片场地、同一个太阳——每张图的影子方向都要能用"太阳在那边"解释通。

- **太阳/影子锚点**:从基准图影子反推太阳方位,每个机位按同一个太阳重推影子落向(反打=影子朝镜头拉长)
- **开放边界锁定**:拉远/反打时显式锁"地平线上没有城市和山脉",防模型脑补天际线
- **九机位指令库**:含无人机高角度、远景大全景、穿行 POV、黄昏氛围变体(唯一允许改太阳的机位)
- **实测沉淀**:开阔场景复制偏置强,侧打用"近/远法"点名谁在前景;涂鸦只写"痕迹"不写文字
- references:`exterior-shot-library`(含废料场完整实测案例)

## 推荐组合工作流

**资产线(单件):**
概念图 → `maxs-asset-breakdown` 拆解出白底资产图 → `maxs-multiview-reference` 出转角组 → Hyper3D 重建 → 进引擎

**场景线(空间):**
场景概念图(自己生成或 `maxs-image-to-prompt` 反推改造)→ `maxs-interior-multiangle` / `maxs-exterior-multiangle` 出机位组 → PureRef 参考板 → UE5 搭建

## 通用工具事实(香蕉系,2026-06 核实)

- Nano Banana / Banana Pro / 香蕉2 均**不支持 seed**,也**没有负面提示参数**——一致性靠「参考图 + 同一对话」,排除项写成自然语言句子
- 对话式中文完整句子优于英文关键词堆叠;hex 色值有效但要绑着物件写
- 香蕉2 快 3-5 倍、约 95% 画质、中文理解更强:抽卡用香蕉2,精修用 Pro
- 每个角度/机位抽 2-4 张再判断;图上具体文字(招牌/涂鸦)不要试图保留

## 迭代

改 skill 内容后 `git push`,在 marketplace 里点 Sync/更新即可拉到最新版。每个 skill 的实测沉淀记录见各自的 `CHANGELOG.md`。

---

MAXs Education 麦壳思 · 游戏CG教育

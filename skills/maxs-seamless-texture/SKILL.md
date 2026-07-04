---
name: maxs-seamless-texture
description: 麦壳思「Midjourney 无缝 PBR 贴图」SOP助手。当用户(MAXs老师、AI技术美术、学生)想做以下任何一件事时都要触发——写 Midjourney V7/V8 的无缝贴图(seamless/tileable texture)提示词、用 --tile 出可平铺的材质图、在 TAPNOW 里跑 MJ 生成贴图、把 MJ 贴图丢进 Substance 3D Sampler 做 PBR(basecolor/normal/roughness/height/AO/metallic)、做 UE5 能直接用的写实材质、调"平铺重复感/接缝/烘焙光影/法线方向"的坑、为 AI 全流程 UE5 课程做贴图提示词案例,或任何提到"无缝贴图""tileable""seamless texture""--tile""PBR 贴图""Substance Sampler""图生材质""贴图提示词""平铺材质""材质扫描"的场景。注意分流:要资产白底陈列图走 maxs-asset-breakdown;要单物体/室内/室外的多视角机位参考走 maxs-multiview-reference / maxs-interior-multiangle / maxs-exterior-multiangle 三件套;要题材迁移/反推走 maxs-image-to-prompt——那几个走香蕉(Gemini系)引擎、提示词是中文整句;本 skill 专走 Midjourney 引擎做可平铺 PBR 贴图,提示词是英文 tag+参数,两套写法相反,别串味。
---

# 麦壳思「Midjourney 无缝 PBR 贴图」SOP (v1)

适用范围:麦壳思全部"要一张能平铺、进得了 Substance、最后贴进 UE5 的写实 PBR 贴图"的工作——AI 全流程 UE5 课程的贴图单元、地形/建筑/织物/科幻四类材质的提示词模板、MJ→TAPNOW→Substance Sampler→UE5 的完整链路教学与素材沉淀。

## 先读:本 skill 跟其它 maxs skill 是两套引擎(别串味)

麦壳思系列里其它 skill 都走**香蕉(Nano Banana / Banana Pro / 香蕉2,Gemini 系)**——无 tag 尾巴、中文整句、挂参考图。**本 skill 走的是 Midjourney 引擎,写法完全相反:英文 tag、逗号堆叠、`--参数` 尾巴照写。** 看错引擎就出废图。

| 你想要的 | 该用谁 | 引擎 / 写法 |
|---------|--------|-----------|
| 可平铺的 PBR 贴图(地面/墙面/布/科幻面板) | **本 skill** | **Midjourney** · 英文 tag + `--tile`/`--ar`/`--v`/`--style raw`/`--s`/`--no` |
| 资产白底陈列图 / 单件三视图重建准备 | `maxs-asset-breakdown` | 香蕉 · 中文整句 |
| 同物体/室内/室外多机位参考 | `maxs-multiview-reference` / `interior` / `exterior` | 香蕉 · 图生图挂参考图 |
| 把好构图迁到新题材 / 反推起点 | `maxs-image-to-prompt` | 香蕉 · 中文整句 |

> TAPNOW 是**多模型平台**,同时接了 Midjourney、即梦、Flux 等。其它 maxs skill 用的是它接的香蕉(Gemini 系);本 skill 用的是它接的 **Midjourney**。同一个 TAPNOW,两套引擎,别拿香蕉的写法写 MJ。

## 内核一句话

**贴图不是"好看的图",是"能平铺、无光影、进得了 Substance 的平整材质"。** Midjourney 默认什么都跟贴图反着来——打戏剧光、上透视、加风格化、围着主体构图。写贴图提示词的全部功夫,就是把它**按回"正交、平光、满幅、无主体"**,让它当一台老实的材质扫描仪。

## 全流程一句话

MJ(`--tile` 出无缝平整图)→ Seamless Pattern Checker 验接缝(别 upscale)→ Substance Sampler(Image-to-Material 自动出 PBR + delight 洗掉残留光影 + auto-tiling 兜底)→ 导出 UE5 通道(**DirectX 法线** / ORM 打包)→ 引擎里平铺验证。

## 工具事实(MJ ≠ 香蕉,记牢)

- MJ 是 **tag + 参数** 模型:英文 tag、逗号堆叠、参数尾巴(`--tile` `--ar` `--v` `--style raw` `--s` `--no`)**全都有效且必须用**——这跟香蕉"无 tag 尾巴、中文整句"完全相反。
- **`--tile` = 无缝平铺核心参数**,让图四边能完美对接。官方红线:**`--tile` 图不要 upscale,放大会破坏接缝**(要更高清走 Substance 导出或重抽,不走放大器)。
- `--tile` 出的是**单块 tile**,先用 Seamless Pattern Checker(pycheung.com/checker)平铺四宫格预览,确认无缝、无炸裂重复,再决定要不要进 Substance。
- **V8.1**(2026-06-10 起为默认版)**原生 2K**,对贴图最有利;要兼容老行为用 `--v 7`。本 skill 模板默认 `--v 8.1`,版本号是可换的槽位。
- 写实 PBR 用 **`--style raw` + 低 `--s`**(压掉 MJ 的艺术化倾向),越低越像材质扫描、越少自作主张的笔触。
- MJ 默认会**烘焙光影**,即使写了 flat lighting 也会残留——没关系,Substance Sampler 的 **delight** 会把残留光影从 albedo 里洗掉。**但 MJ 出得越平,delight 越干净。提示词和 Substance 是一对搭档,不是二选一。**
- `--tile` 透传:你已确认走 TAPNOW 的 MJ、以 `--tile` 为主路径;**Substance 的 Make it Tile / auto-tiling 是兜底**——万一 TAPNOW 吞了参数、出图有缝,Substance 还能补救。

## 第一原则:三个永远要回到的判断标准

1. **平得了吗(无光影 / 无透视)** —— 图上有没有方向性阴影、高光、透视纵深?有 → delight 洗不净、normal 会把假阴影当成真凹凸,贴上去就脏。
2. **铺得开吗(无缝 / 无炸裂重复)** —— 平铺四宫格,接缝看得见吗?有没有一个抢眼的大特征(大裂缝 / 大锈斑 / 一块独立面板)在每块 tile 上复读?
3. **进得了引擎吗** —— delight 后 albedo 干净、各通道对得上、平铺到 UE5 一面墙远看不露馅。**没在引擎里铺过,不算成。**

## 核心动作(按顺序执行)

### 动作 1:锁四件套约束(写任何写实贴图提示词都先锁这四个)

不管什么材质,realistic PBR 贴图的提示词必须**同时压住这四件事,缺一个就出废图**:

- **正交满幅**:`top-down / orthographic / flat lay, shot from directly above, fills the frame edge to edge, uniform scale, no focal subject`
- **平光无影**:`even diffuse studio lighting, flat lighting, no shadows, no highlights, no vignette`
- **去风格化**:`photoreal, sharp uniform detail` + `--style raw` + 低 `--s`(50 上下起步)
- **可平铺**:`seamless tileable texture` + `--tile --ar 1:1`

> 墙面这类"立面"材质用 `flat front orthographic view`(正面正交);地面 / 桌面 / 织物用 `top-down flat lay`(顶视平摊)。选错视角,贴上去方向就反。

### 动作 2:按品类套"母题密度 + 方向"卡(详见 references/texture-prompt-cards.md)

四个品类各有专坑,核心都是一句话:**母题别太大、别有独大特征。**

- **地形/自然地表**:有机随机,碎石 / 落叶 / 苔藓 `evenly scattered, small-to-medium`,别让一块大石头独占画面。
- **建筑硬表面**:砖 / 瓷砖要 `consistent coursing / regular grid`,做旧要 `even weathering`,别一块大污渍。
- **织物/皮革/有机**:细密 `weave / grain`,top-down;木纹注意 `grain direction` 一致。
- **科幻硬表面/做旧**:`modular, evenly distributed paneling, no single hero panel`,做旧 `uniform wear`,别一块大锈。

每类的完整提示词模板、参数、正反例,在 reference 卡里。

### 动作 3:出图 + 接缝预演(进 Substance 之前)

抽 4 格 → 丢 pycheung.com/checker 平铺 → 三件事过一遍:**接缝、重复感、残留光影**。**别 upscale。** 过了再进 Substance;不过回动作 4 调。

### 动作 4:三步迭代(引用 maxs-asset-breakdown 的 试水 → 纠错 → 简化)

1. **试水**:4 格 + checker,先看"平不平、缝不缝"。
2. **纠错(一次只补一个约束)**:
   - 有缝 → 确认 `--tile` 真带上了(TAPNOW 里别被吞参数)
   - 重复炸裂 → 母题缩小 + `evenly distributed, no dominant feature`
   - 有阴影 / 高光 → 加 `flat lighting` + `--no shadows, highlights`,压 `--s`
   - 有透视纵深 → `top-down orthographic flat lay` + `--no perspective, depth of field`
   - 太糊 / 像画的 → `--style raw` + 压 `--s` + `sharp uniform detail, photoreal`
3. **简化**:砍修饰,留最短能稳定出"平整无缝图"的骨架。**实测系列教训:约束堆太多方差反而变大,终版要比中间版短。**

### 动作 5:Substance Sampler 做 PBR → UE5(完整 SOP 见 references/substance-sampler-sop.md)

Image-to-Material 自动出 basecolor/normal/height/roughness/metallic/AO → 调 delight / normal / roughness / metallic → Make it Tile / auto-tiling 兜底 → 导出(**UE5 用 DirectX 法线、ORM 打包**)→ UE5 里设 sRGB / Normalmap 压缩 / 平铺。

### 动作 6:引擎里平铺验证 + 沉淀复用包

UE5 平铺到一面墙 / 一片地,远看无重复、近看够细、albedo 无残留光影 = S 级。提示词骨架 + 母题缩放经验 + Substance 参数预设 + UE5 导入设置,进麦壳思素材库。

## 参数速查(贴图向,英文参数照写)

| 参数 | 干嘛的 | 贴图怎么用 |
|------|--------|-----------|
| `--tile` | 无缝平铺 | **必带**;tile 图**别 upscale** |
| `--ar 1:1` | 方形 | 贴图标准方形 |
| `--v 8.1` / `--v 7` | 版本 | 默认 8.1(原生 2K);兼容老行为用 7 |
| `--style raw` | 去艺术化 | **写实 PBR 必带** |
| `--s` (`--stylize`) | 风格强度 | 压低(50 上下起步),越低越像材质扫描 |
| `--no` | 负面 | `--no shadows, highlights, vignette, perspective, depth of field, seams, text, object` |
| `--chaos` | 多样性 | 贴图要一致,留低 / 默认 |
| 图片提示(URL 前置) | 挂参考材质图 | 想忠实复刻某真实材质:材质照 URL 放最前 + `--tile`,比纯文字稳(进阶) |

## 已知坑

| 坑 | 表现 | 应对 |
|----|------|------|
| **把贴图当"好看图"写** | 出来有主体、有构图、有戏剧光 | 贴图要"满幅无主体平光";围着主体的戏剧光是贴图头号敌人 |
| **upscale 了 tile** | 平铺突然露缝 | 官方红线:`--tile` 图不放大;要更高清走 Substance 导出 / 重抽,不走放大器 |
| **母题太大 / 有独大特征** | 平铺后同一个大裂缝 / 大锈斑 / 大面板满屏复读 | 缩小母题 + `evenly distributed, no single dominant feature`;地标性的独特元素别要 |
| **烘焙光影没压住** | delight 洗不净,normal 把假阴影当凹凸,贴上去发脏 | 源头压平:`flat lighting` + `--no shadows, highlights` + 低 `--s`;再靠 Substance delight 收尾 |
| **有透视纵深** | 贴上去边缘被拉伸、近大远小 | `top-down orthographic flat lay` + `--no perspective` |
| **MJ 风格化乱加细节** | 像手绘插画不像材质 | `--style raw` + 压 `--s`;`photoreal, sharp uniform detail` |
| **法线方向搞反** | UE5 里凹凸内外翻、打光不对 | UE 用 **DirectX** 法线(绿通道朝下);Substance 导出选 DirectX / UE 预设 |
| **拿香蕉的写法写 MJ** | 写一大段中文整句、不带参数,出图散 | MJ 是 tag+参数模型;英文 tag、逗号、`--参数` 照写(这跟其它 maxs skill 相反) |
| **TAPNOW 吞了参数** | `--tile` 没生效、还是有缝 | 确认 TAPNOW 的 MJ 真把 `--tile` 透传了;没有就靠 Substance Make it Tile 兜底 |
| **2K 不够近景** | 贴大近景墙面发糊 | V8.1 原生 2K 够中景 / 地面;近景 hero 面在 Substance 导出更高分辨率或拆分,别指望 MJ 放大 |

## 分级体系 / 教学要求 / 沉淀原则

- **S/A/B/C**:S 级须在 **UE5 里平铺验证过**(远看无重复、近看够细、delight 后 albedo 干净),且四品类里至少跑通 2 类。
- **教学**:给"提示词骨架 + 参数解释 + Substance 通道含义",不给一次性成图原文;必配一个失败案例(重复炸裂 / 阴影没去净导致 normal 出错)。
- **沉淀**:提示词骨架 + 母题缩放经验 + Substance 参数预设 + UE5 导入设置,进麦壳思素材库。

## 在对话中如何运用

1. **先分流**——资产白底 / 机位参考 / 题材迁移不是本 skill,本 skill 只接"可平铺 PBR 贴图"。
2. **锁四件套约束**(正交满幅 / 平光无影 / 去风格化 / 可平铺)。
3. **按品类套卡出提示词**(英文 tag + 参数尾巴)。
4. **出图先进 checker 预演接缝**,别 upscale。
5. **三步迭代**(试水 → 纠错 → 简化),一次只补一个约束。
6. **Substance Sampler 出 PBR → UE5**,引擎里平铺验证。
7. **交付复用包**(骨架 + 参数预设 + 导入设置)进素材库。

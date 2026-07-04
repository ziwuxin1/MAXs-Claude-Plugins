# Changelog

## 1.0.0 (2026-07-04)

首版。麦壳思系列新增「Midjourney 无缝 PBR 贴图」SOP,补齐系列里缺的"可平铺 PBR 贴图"链路。

### 定位
- 与系列其它 skill **分引擎**:其它 maxs skill 走香蕉(Gemini 系)、中文整句;本 skill 走 **Midjourney**、英文 tag + 参数尾巴,写法相反。SKILL.md 顶部用"两套引擎"对照表显式分流,防串味。
- 链路:**MJ(`--tile`)→ TAPNOW → Seamless Pattern Checker → Substance 3D Sampler(Image-to-Material + delight + auto-tiling)→ UE5(DirectX 法线 / ORM 打包)**。

### 核心铁律(基于当前事实)
- `--tile` 是无缝核心,**tile 图不要 upscale**(官方红线,放大破坏接缝)。
- 写实 PBR 锁"四件套":正交满幅 / 平光无影 / 去风格化(`--style raw` + 低 `--s`)/ 可平铺(`--tile --ar 1:1`)。
- 母题别太大、别有独大特征——平铺不炸裂的命门。
- 提示词压平光影 + Substance delight 收尾,是**一对搭档**,不是二选一。
- UE5 用 **DirectX 法线**;ORM 打包(AO/Roughness/Metallic → R/G/B)。

### 默认版本
- 模板默认 `--v 8.1`(2026-06-10 起为 MJ 默认版,原生 2K,对贴图最有利);兼容 `--v 7`。版本号是可换槽位。

### 结构
- `SKILL.md`:主 SOP(分引擎 / 四件套 / 三步迭代 / 参数速查 / 已知坑)。
- `references/texture-prompt-cards.md`:四品类(地形自然 / 建筑硬表面 / 织物皮革有机 / 科幻做旧)模板 + 完整可发提示词 + 正反例。
- `references/substance-sampler-sop.md`:Sampler → UE5 完整 SOP(Image-to-Material / delight 调参 / Make it Tile 兜底 / 通道导出 / UE5 导入 / 常见错)。

### 待沉淀(随实跑补)
- 各品类 S/A 级提示词骨架 + 母题缩放经验值。
- Substance 各品类参数预设(尤其 Delighting 档位、metallic 取值)。
- 失败案例库:重复炸裂 / 阴影没去净导致 normal 出错。

# 贴图提示词卡 · 四品类模板 + 完整案例(Midjourney 写实 PBR)

> 全部走 **Midjourney 引擎**:英文 tag + 参数尾巴。默认 `--v 8.1`(原生 2K),`--style raw` + 低 `--s` 压风格化。tile 图**别 upscale**。出图先进 pycheung.com/checker 验接缝再进 Substance。

## 通用骨架(四件套,套任何材质)

```
[材质 + 表面状态 + 母题密度], seamless tileable PBR texture,
[top-down flat lay | flat front orthographic view], uniform scale, no focal subject,
even diffuse studio lighting, flat lighting, no shadows, no highlights,
photoreal, sharp uniform detail, fills the frame edge to edge
--tile --ar 1:1 --v 8.1 --style raw --s 50
--no shadows, highlights, vignette, perspective, depth of field, seams, text, object
```

- **视角二选一**:地面/桌面/织物用 `top-down flat lay`;墙面/立面用 `flat front orthographic view`。
- **母题密度**永远写一句:`evenly distributed, no single dominant feature` —— 这是平铺不炸裂的命门。
- `--s` 从 50 起步,太像画的往下压(可到 0),太死板的往上抬(到 100)。
- `--no` 是把"贴图大敌"显式赶走的开关:阴影、高光、暗角、透视、景深、缝、文字、主体。

## 参数速查(再贴一份,方便对照)

| 参数 | 取值 | 给贴图的作用 |
|------|------|------------|
| `--tile` | 开关 | 无缝平铺核心;tile 图不放大 |
| `--ar` | `1:1` | 贴图方形 |
| `--v` | `8.1` / `7` | 默认 8.1;兼容老行为 7 |
| `--style raw` | 开关 | 去 MJ 艺术化,写实必带 |
| `--s` | `0–100` 起步段 | 越低越像材质扫描 |
| `--no` | 词表 | 显式赶走 shadows/highlights/perspective… |
| `--chaos` | 留低/默认 | 贴图要一致不要多样 |

---

## 卡 1 · 地形 / 自然地表

**专坑**:有机材质最怕"一块大石头/大草丛独占",平铺后地标复读。要 `小到中等碎块、均匀散布`。
**视角**:`top-down flat lay`(顶视)。
**母题**:`evenly scattered small-to-medium debris, organic random distribution, no dominant clump`。

**骨架**:
```
[地表类型 + 湿度/季节 + 散落物], damp/dry, evenly scattered small-to-medium [debris],
seamless tileable PBR texture, top-down flat lay, uniform scale,
even diffuse overcast lighting, no shadows, no highlights,
photoreal, sharp uniform detail, fills the frame
--tile --ar 1:1 --v 8.1 --style raw --s 45
--no perspective, depth of field, vignette, shadows, highlights, focal rock, object
```

**完整案例**:
- 森林地表:
  `forest floor, damp dark soil with evenly scattered fallen leaves, small twigs and moss patches, organic random distribution no dominant clump, seamless tileable PBR texture, top-down flat lay, uniform scale, even diffuse overcast lighting, no shadows no highlights, photoreal, sharp uniform detail, fills the frame --tile --ar 1:1 --v 8.1 --style raw --s 45 --no perspective, depth of field, vignette, shadows, highlights, focal rock`
- 干裂泥地:
  `cracked dry desert mud flat, fine even crack network, uniform medium scale, seamless tileable PBR texture, top-down orthographic, flat even lighting, no shadows, photoreal, sharp detail --tile --ar 1:1 --v 8.1 --style raw --s 40 --no perspective, shadows, highlights, single large crack`
- 碎石砾石路:
  `gravel and small pebbles ground, evenly distributed mixed sizes, packed dirt between stones, seamless tileable PBR texture, top-down flat lay, flat diffuse lighting, no shadows no highlights, photoreal, sharp uniform detail --tile --ar 1:1 --v 8.1 --style raw --s 45 --no perspective, depth of field, vignette, focal subject`

**正 / 反例**:
- 反:`mossy boulder in a forest, dramatic sunbeam, shallow depth of field` → 有主体、有戏剧光、有景深,**根本不是贴图**。
- 正:把"boulder"换成 `evenly scattered small rocks`、戏剧光换 `flat overcast`、加 `--tile`。

---

## 卡 2 · 建筑硬表面

**专坑**:砖/瓷砖/铺装的"网格/砌缝"要在 tile 之间接得上,所以母题要 `规则、一致 coursing/grid`;做旧别一块大污渍。
**视角**:墙面 `flat front orthographic view`;地面铺装 `top-down flat lay`。
**母题**:`consistent running-bond coursing / regular grid, even mortar joints, subtle uniform weathering`。

**骨架**:
```
[材质 + 砌法/排布 + 做旧程度], consistent [coursing | grid], even joints,
subtle uniform weathering, seamless tileable PBR texture,
[flat front orthographic view | top-down flat lay], uniform scale,
even diffuse lighting, no shadows, no highlights,
photoreal, sharp detail, fills the frame
--tile --ar 1:1 --v 8.1 --style raw --s 50
--no perspective, vignette, shadows, highlights, single large stain, object
```

**完整案例**:
- 旧红砖墙:
  `old red brick wall, consistent running-bond coursing, even weathered mortar joints, subtle uniform wear, seamless tileable PBR texture, flat front orthographic view, uniform scale, even diffuse lighting, no shadows no highlights, photoreal, sharp detail, fills the frame --tile --ar 1:1 --v 8.1 --style raw --s 50 --no perspective, vignette, shadows, highlights, single large stain`
- 清水混凝土:
  `bare concrete wall, fine even surface pitting and form-tie marks, subtle uniform staining, seamless tileable PBR texture, flat front orthographic view, flat even lighting, no shadows no highlights, photoreal, sharp detail --tile --ar 1:1 --v 8.1 --style raw --s 45 --no perspective, vignette, shadows, big crack, object`
- 石板地面铺装:
  `weathered stone slab pavement, irregular tight-fitted flagstones, even mortar lines, uniform wear, seamless tileable PBR texture, top-down flat lay, flat diffuse lighting, no shadows no highlights, photoreal, sharp uniform detail --tile --ar 1:1 --v 8.1 --style raw --s 50 --no perspective, depth of field, vignette, focal stone`

**正 / 反例**:
- 反:`brick wall at sunset, warm rim light, corner of a building` → 暖侧光 + 透视墙角,贴上去光影方向锁死、还有缝。
- 正:`flat front orthographic` + `even diffuse lighting` + `--no perspective, shadows`。

---

## 卡 3 · 织物 / 皮革 / 有机

**专坑**:细密 weave/grain 是优势(天然好平铺);最大坑是**木纹有方向**,grain 方向要一致、别打架。皮革别一块大高光。
**视角**:`top-down flat lay`。
**母题**:`fine even [weave | grain | pores], uniform surface`;木纹另加 `consistent grain direction`。

**骨架**:
```
[材质 + 编织/纹理 + 状态], fine even [weave | grain | pores], uniform surface,
seamless tileable PBR texture, top-down flat lay, uniform scale,
soft even diffuse light, no shadows, no highlights,
photoreal, sharp uniform detail, fills the frame
--tile --ar 1:1 --v 8.1 --style raw --s 50
--no perspective, vignette, shadows, highlights, fold, stitching seam, object
```

**完整案例**:
- 旧皮革:
  `worn brown leather, fine even grain and pores, uniform surface, subtle patina, seamless tileable PBR texture, top-down flat lay, soft even diffuse light, no shadows no highlights, photoreal, sharp uniform detail --tile --ar 1:1 --v 8.1 --style raw --s 50 --no perspective, vignette, shadows, highlights, fold, stitching seam`
- 粗织亚麻布:
  `coarse woven linen fabric, fine even thread weave, uniform surface, seamless tileable PBR texture, top-down flat lay, flat diffuse lighting, no shadows no highlights, photoreal, sharp detail --tile --ar 1:1 --v 8.1 --style raw --s 50 --no perspective, vignette, shadows, fold, hem, object`
- 木板纹理(注意方向):
  `oak wood planks, consistent grain direction, fine even wood grain, subtle uniform wear, seamless tileable PBR texture, top-down flat lay, even diffuse lighting, no shadows no highlights, photoreal, sharp uniform detail --tile --ar 1:1 --v 8.1 --style raw --s 50 --no perspective, vignette, shadows, knot cluster, object`

**正 / 反例**:
- 反:`folded leather jacket on a table, window light` → 有褶、有方向光、有物体轮廓,平铺直接散架。
- 正:`flat uniform leather` + `top-down flat lay` + `--no fold, highlights`。

---

## 卡 4 · 科幻硬表面 / 做旧

**专坑**:greeble/面板/做旧最容易出"一块独大 hero 面板/一团大锈",平铺复读最明显。死守 `modular, evenly distributed, no single hero panel, uniform wear`。金属在 Substance 里 metallic 要给值(见 SOP)。
**视角**:`top-down orthographic`(面板朝上)。
**母题**:`modular sci-fi paneling, evenly distributed greebles and panel lines, uniform layout, subtle even wear`。

**骨架**:
```
[科幻表面 + 排布 + 做旧], modular, evenly distributed [greebles | panel lines],
uniform layout no single hero panel, subtle even wear,
seamless tileable PBR texture, top-down orthographic, uniform scale,
flat even lighting, no shadows, no highlights, no glow,
photoreal, sharp detail, fills the frame
--tile --ar 1:1 --v 8.1 --style raw --s 60
--no dramatic lighting, perspective, vignette, shadows, large rust patch, emissive glow, object
```

**完整案例**:
- 科幻金属面板:
  `modular sci-fi metal paneling, evenly distributed greebles, recessed panel lines and bolts, uniform layout no single hero panel, subtle even wear, seamless tileable PBR texture, top-down orthographic, flat even lighting, no shadows no highlights, photoreal, sharp detail, fills the frame --tile --ar 1:1 --v 8.1 --style raw --s 60 --no dramatic lighting, perspective, vignette, shadows, large rust patch, emissive glow`
- 做旧涂装金属 + 危险条:
  `worn painted industrial metal, evenly distributed scratches and chipped paint, faint uniform hazard stripes, no single dominant mark, seamless tileable PBR texture, top-down orthographic, flat diffuse lighting, no shadows no highlights, photoreal, sharp uniform detail --tile --ar 1:1 --v 8.1 --style raw --s 55 --no perspective, vignette, shadows, big rust stain, object`
- 电路蚀刻板:
  `dark circuit-etched panel, fine evenly distributed traces and micro-components, uniform density, seamless tileable PBR texture, top-down orthographic, flat even lighting, no shadows no highlights no glow, photoreal, sharp detail --tile --ar 1:1 --v 8.1 --style raw --s 55 --no emissive glow, perspective, vignette, shadows, hero chip`

**正 / 反例**:
- 反:`sci-fi reactor wall, glowing blue core, dramatic backlight, one big vent` → 自发光 + 戏剧背光 + 一个大风口,做不了平铺材质(自发光该在 UE5 用 emissive,不该烘进 albedo)。
- 正:`modular evenly distributed paneling` + `flat even lighting` + `--no emissive glow, dramatic lighting`。

---

## 收尾提醒

- 每条提示词都**自含**:材质 + 母题密度 + 视角 + 平光 + 画质 + 参数,一行能直接发。
- 出图先 checker,**别 upscale**,过了再进 Substance。
- S/A 级提示词骨架 + 母题缩放经验进麦壳思素材库;每个品类至少配一个"重复炸裂"或"光影没去净"的失败案例做教学。

# GPT 直接生成 Albedo 的提示词模板

这些是可替换工作模板，不是已实测成功的提示词。替换槽位后只保留与本次材料相关的要求；生成时使用实际可用的工具参数，不附 Midjourney 的 `--tile` 等参数。

## 从零生成

```text
Generate a full-frame orthographic PBR ALBEDO / BASE COLOR texture of [actual material]. View the flat surface straight-on, with no perspective or presentation scene. Arrange [components, distribution, size relationships and intended surface scale]. [If requested: design the surface to repeat continuously across both axes, including objects crossing the edges and the four-corner junction.]

Use [intrinsic dominant colors] with [restrained secondary colors]. Maintain [requested palette and value range]. Show [material-specific fine grain or inclusions], [moderate-scale wear] and restrained broad color variation, with calmer areas between detailed patches. Age through [specific localized deposits or erosion], preserving the underlying material.

Albedo only: intrinsic surface color without baked ambient occlusion, cast shadows, directional lighting, specular reflections, bright bevels or exposure gradients. Avoid wormlike engravings, fingerprint swirls, cellular lace, uniform crack networks, blur and sharpening halos. Output only the texture filling the image, no sphere, border, labels or logos. Requested size and aspect ratio: [target].
```

平铺句只用于需平铺的材质；它是生成目标，不是验收结果。尺寸同理，需要读取输出文件后才能确认。

## 有材质参考

在上述模板中增加，编号以实际传入顺序为准：

```text
Images [1...] are material appearance references only. Extract their intrinsic material colors, grain and weathering mechanisms. Create a new flat texture layout following the requested scale. Do not reproduce the references' perspective, lighting, shadows, background, display geometry or text.
```

参考若是已有 Albedo 并要求保留其布局，用下面的编辑方式；若是要对应的 AO/Normal/Height，改走 `maxs-SD-to-Albedo`。

## 中性旧砖示例槽位

- 材料：旧陶土砖与砂质灰浆。
- 排列：按用户选择的错缝墙砖或不规则砌块，先确定比例与画面覆盖尺度。
- 色彩：灰褐为主，少量褪色砖红、浅土褐；中等明度与克制饱和度。
- 细节：陶土细颗粒、少量矿物杂点、局部浅孔；薄积灰和接触区沉积，保留部分完整砖面。
- 边界：不要套用参考材质球上的高光、黑缝或白色亮边；需要实体破损时单独限定程度。

以上配色仅是旧砖示例，不是所有材质的默认调色板。

## 已认可版本的单项修改

```text
Edit the approved Albedo in image 1. Change only [one specific issue and intended degree]. Preserve its layout, component silhouettes, material boundaries, scale, accepted color balance and fine grain except where the requested correction requires a change. Keep the result a flat unlit base-color map. Do not redesign the surface or add new damage. [For a repeating texture: preserve continuity across both axes and the four-corner junction.]
```

“保留”是编辑约束，不是像素级保证。编辑后仍要对比独特形状、局部颗粒、边界和重复接缝；不能凭提示词宣称图像完全不变。

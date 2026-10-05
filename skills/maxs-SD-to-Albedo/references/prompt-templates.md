# 提示词模板

## Albedo

将槽位替换为当次真实输入。完整效果约束不需要依靠“8K、超细节、AAA”词语叠加。

```text
Create a flat orthographic PBR BASE COLOR texture from image 1, the fixed [AO/structure] template. Images [2...] are material appearance references only. Preserve every existing block outline, position, scale, angle, main fracture and mortar boundary. Do not transfer the reference's arrangement, camera, lighting or objects.

Apply [actual material] with [dominant intrinsic colors and restrained secondary colors]. Keep [requested palette / medium values / restrained saturation]. Resolve [specific fine grain], [material-specific inclusions] and [moderate-scale wear], with calmer areas between detailed patches. Age with [localized physically motivated deposits]; control coverage and strength independently.

Albedo only: no baked AO, specular, cast shadows, bright bevels or face-orientation shading. Deposits are pigment, not illumination. No rearranged geometry, added large cracks, embossed squiggles, wormlike grooves, cellular lace, repetitive microtexture, whitening, blur or sharpening halos. Output only the full-frame map at [requested size and aspect ratio].
```

用户只修改一个维度时，点明其它已认可属性保持；是否采用确定性调色依当前工具能力及用户授权决定，不保证图生图“仅改颜色”就能保住每个像素。

## Roughness

下面只适合干燥旧砖。换材质时重定目标范围，切勿对所有材质使用同一组灰值。

```text
Produce a grayscale PBR ROUGHNESS map matching the approved albedo's exact material regions. White means rough, black means smooth. Preserve block silhouettes, mortar boundaries and existing damage. This is not a grayscale photograph, AO, height or a shaded rendering.

For this dry unglazed aged brick material, start around 0.70-0.83 on brick, 0.85-0.93 on sandy mortar and dry powder, and 0.60-0.70 on sparse rubbed compact clay areas. Add restrained irregular fine variation. Different brick pigment colors do not automatically mean different roughness. Recesses filled with mortar remain high roughness rather than AO-dark. No wet patches, sharp black pores, highlights, directional gradients, new cracks or geometry. Grayscale channels identical, no labels. Requested [size].
```

数值是目标，不是执行结果。生成后测量并检查材质区域；只说“提示词要求 0.7”不能证明实际范围。

# 实际案例：苔藓古建屋顶三视图

## 用户选择与修正（2026-09-25）

用户先认可了带苔藓、落叶、错位和少量缺瓦的屋顶三视图，再要求裁成正面、俯视、侧面三张图并提供 4K。

第一次处理只把三张裁片插值放大到长边 4096。用户指出：“你只是放大 不是高清化”。这一版满足像素尺寸，没有满足细节增强目标。

修正流程：
1. 分别使用用户认可的三张原始裁片作为图像编辑输入。
2. 使用内置 imagegen 重建瓦片边缘、苔藓绒面、落叶轮廓和木构纹理。
3. 查看原始增强结果，再读取实际尺寸。
4. 保存 AI 原始增强图，再按比例导出长边 4096 的 PNG。
5. 如实说明：AI 重建后导出 4K，局部有重绘，非原生 4K 生成。

用户随后评价“这个不错”，并要求把流程做成技能。这个认可对应修正后的流程，不对应第一次纯插值放大。

## 实际尺寸

| 视图 | 输入裁片 | AI 返回尺寸 | 最终导出 |
| --- | --- | --- | --- |
| 正面 | 1160×405 | 2123×741 | 4096×1430 |
| 俯视 | 855×500 | 1641×958 | 4096×2391 |
| 侧面 | 788×460 | 1641×958 | 4096×2391 |

即使提示词要求长边 4096，工具仍返回了较小尺寸。应实测，不应凭提示词声称模型输出了原生 4K。AI 返回图的宽高比也有细微变化；本次按返回图原比例导出，没有拉伸强配原裁片尺寸。

工具未公开底层模型、seed 和采样参数。此次提升是生成式重建，不是可验证的真实细节恢复。三张逐独立处理，未用三维模型检验跨视图的逐瓦对应。

## 实际有效英文原文

以下公共段用于每张图，后面附对应视图句。需替换材质时只保留实际存在的对象，不把屋顶内容带入其它任务。

```text
Perform high-fidelity AI detail restoration and super-resolution on the provided approved roof view. The user specifically rejected simple pixel enlargement: reconstruct credible fine material detail from the source, not merely resample or sharpen. Deliver a very high resolution image, ideally 4096 pixels on the long edge, keeping the original aspect ratio. Preserve the exact view, orthographic projection, roof silhouette, framing, all tile courses, ridge ornaments, existing damage positions, moss and leaf distribution, original label and white background. Do not redesign the roof, add another view, change the camera, alter weathering coverage or move objects.
Resolve overlapping curved ceramic tiles as distinct thin forms: clear tile lips and overlap seams, subtle porous fired-clay grain, fine natural pits, worn chipped edges and restrained hairline cracks. Clarify the small broken-tile areas and the dark supporting wood beneath. Moss must resolve into natural velvety cushions and fine uneven filaments, with soft irregular boundaries and depth rather than painted green noise. Existing fallen leaves should resolve into believable curled leaf shapes, thin edges and restrained veins; retain their small scale and existing placements. Wood should show longitudinal fibers, subtle grain and real cracks, not swirling carved-looking texture.
Clean aliasing, smeared texture and compression-like fuzz while retaining soft neutral light and natural low-contrast texture. Maintain matte charcoal/blue-gray tiles, subdued olive/forest-green moss, brown ochre leaves, gray-brown aged wood. No halos, no oversharpening, no invented white flecks, no sparkle, no plastic smoothing, no uniformly repeated microscopic patterns. Prioritize detailed but natural appearance when inspected closely. One view only, asset fully uncropped. Flat pure white background.
```

按输入附加一条：
- 正面：`This is the FRONT VIEW. Preserve the broad frontal roof facade and its existing FRONT VIEW caption.`
- 俯视：`This is the TOP VIEW. Preserve the precise overhead orientation, roof plan silhouette and its existing TOP VIEW caption.`
- 侧面：`This is the SIDE VIEW. Preserve the triangular wooden gable, side roof profile and its existing SIDE VIEW caption.`

## 可复用结论与边界

- “高清化”先解决细节可读性，再解决尺寸；两个步骤分别验收。
- 苔藓与叶片变清楚不代表它们的位置和数量逐项不变；重大变化要修正，小变化如实说明。
- 细节重建可能增加装饰或重复纹理，尤其连续重绘会累积漂移；应回到认可的基准输入。
- 已验证范围为这一组游戏资产屋顶图。不把它升级为跨模型、多材质的成功率保证，也不强制其它任务使用白底。

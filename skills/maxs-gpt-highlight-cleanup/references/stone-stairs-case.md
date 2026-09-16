# 风化石阶：去高亮噪点实际案例

## 用户选择与边界

2026-09-16，同一次对话中的图像编辑案例：

1. 用户先拒绝圆圆的片状表面纹理，之后提供真实扫描石阶参考，认可了破损不规则石阶版本 V4。
2. V4 含有密集浅白斑点，用户说：“这个最新的图不错，但是要去掉很多这些高光的点。”
3. 使用下方提示词生成 V5。用户评价：“这个非常不错，现在少了一些细节了 再加点回来点。”
4. 另存 V6，尝试补充约 20–25% 的微颗粒、暗孔、微裂纹与断口细节；用户最终说：“还是原来的好。”因此最终选择是 **V5 去噪版**，不是 V6。
5. 这些百分比都是提示词措辞，不是图像工具可验证的数值参数。

反直觉教训：细节更多不等于更真实、更符合用户审美。用户认可干净的哑光质感后，默认停止；补细节只做可回退的可选版本。不要把“保细节”写成自动再锐化一步。

工具为当时会话中的内置 image_gen，未返回底层模型名称或采样参数。记录证明用户对该次结果的选择，不证明每次运行都一致，也不证明视图几何或每片落叶位置完全保持。

## 产生 V5 的原始提示词

使用用户认可的 V4 作为唯一编辑输入：

```text
Precisely edit this approved stone staircase reference sheet. User likes this exact image, requests only removal of the many bright highlight dots. Preserve the exact geometry, stone shapes, step count, cracks, block placement, broken edges, soil, leaves, moss, small plants, all three views, framing, labels and white background. On ALL stone surfaces including side borders and LEFT side wall, remove approximately 85-90 percent of the dense bright white speckles, chalk-white mottling and tiny sparkly highlights. Replace those bright flecks with the surrounding natural medium cool grey stone color, maintaining fine granular rock texture at low contrast. Make stone visibly matte, quiet and solid with restrained broad natural grey tonal variation and soft diffuse lighting. Preserve volume shading and real rough fractured surfaces. The result must look like the SAME approved weathered natural rock asset with much less white spot noise, not a different staircase. Do not simply darken the whole image; selectively suppress white speckles and pinpoint highlights on stone. Keep organic green moss and brown debris unchanged. No new circular patterns, flakes, polished sheen, wet shine or flat plastic surfaces. High detail realistic stone, exact same reference sheet layout.
```

复用时替换石材名称、颜色、不变量和配件列表。不要把石阶数量、三视图标签等案例信息带到无关图片里。

## 验收观察

- 缩略图：白点不再抢主体，整体亮度没有被简单压黑。
- 放大图：仍可读出断口与颗粒，不能靠模糊抹平解决问题。
- 前后对照：轮廓、接缝、主要破口、布局与配件保持到任务可接受程度；若明显漂移，不能宣称只改了噪点。
- 失败信号：蜡感、重复圆圈/鳞片、密集高反差纹理回归、几何或文字改变。

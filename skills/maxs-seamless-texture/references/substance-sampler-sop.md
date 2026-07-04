# Substance 3D Sampler → UE5 完整 SOP(MJ 贴图变 PBR)

> 接力点:MJ 的 `--tile` 图已过 pycheung.com/checker、确认平整无缝、**没 upscale**。这一段把单张图变成 UE5 能直接用的 PBR 通道。

## 0 · 进 Sampler 前的源图三查(省返工)

1. **平不平**:有方向性阴影 / 高光 / 透视吗?有 → 回 MJ 压平(`flat lighting` + `--no shadows, highlights, perspective`),源头越平、delight 越干净。
2. **缝不缝**:checker 四宫格看接缝。`--tile` 没生效 → 靠下面第 4 步 Make it Tile 兜底。
3. **够不够大**:V8.1 原生 2K 够中景 / 地面;近景 hero 墙面后面在 Sampler 导出更高分辨率,**别回 MJ 放大 tile**。

## 1 · 新建 + 导入

- 新建工程 → 把 MJ tile 图拖进画布(或 File → Import),它会成为一个图层。
- 工程分辨率按目标定:2048(2K)起步,近景 hero 面用 4096(4K)。

## 2 · 套 Image to Material(AI Powered)

- 加 **Image to Material (AI Powered)** 滤镜。它用机器学习从单张图自动生成:**Base Color(albedo)、Normal、Height、Roughness、(Metallic)、AO**。
- AI 自带 **delight**:把烘焙的阴影 / 高光从 albedo 里洗掉,这一步直接决定贴图干不干净。神经网络训练覆盖了织物 / 有机 / 室内外表面,四品类都吃得动。

## 3 · 调参(决定贴图质量的核心)

| 参数 | 怎么调 | 给四品类的提示 |
|------|--------|--------------|
| **Delighting / Equalize** | MJ 残留光影越多越往上加,直到 albedo 变平、看不出方向光 | 做旧金属、森林地表最容易残留,重点查 |
| **Normal / Height intensity** | 控凹凸强度。太强 → 假浮雕;太弱 → 发平 | 砖缝 / 面板线适中;布料 / 皮革轻 |
| **Roughness base + variation** | 定基础粗糙度 + 变化;反了就 invert | 金属低、做旧涂装高;湿地表低、干土高 |
| **Metallic** | **金属给 1,非金属给 0**。科幻金属 / 危险条该是金属 | 只有真金属给值,石 / 布 / 土一律 0 |
| **Height level** | 微调高度中值,接 displacement / POM 时重要 | 砖石地面用得上 |

## 4 · Make it Tile / Auto-tiling(兜底无缝)

- 加 **Make it Tile** 滤镜(或开 auto-tiling)保证四边无缝——**这是 MJ `--tile` 被 TAPNOW 吞参数时的安全网**。
- **MJ 已经无缝**就用 **轻档 / Auto**,别开太狠:Make it Tile 开猛了会**涂抹掉细节**、把母题糊掉。
- 已无缝却还想加保险:只用 Auto 模式轻修边,不动中心。

## 5 · 3D 预览 + 平铺自查

- 切 3D 视图,贴到平面 / mesh 上。
- **远看**:有没有同一个特征复读(母题太大的后遗症)→ 回 MJ 缩母题重抽。
- **近看**:normal 有没有把假阴影顶成凹凸(delight 没洗净)→ 回第 3 步加 Delighting。
- **缝**:平铺边界有没有线 → 第 4 步补 Make it Tile。

## 6 · 导出通道

菜单 **Share → Export As**,两条路:

**A · SBSAR(参数化,给 Substance 生态)**
- 导出 `.SBSAR`,是 Sampler / Designer / Painter / Stager 之间的通用桥。要在 Designer 里继续改、或在 Painter 里贴模型,走这条。

**B · 位图通道(给 UE5)** —— 本课主路径
- 导出各通道位图。**UE5 关键设置**:
  - **Base Color** → sRGB,PNG/TGA
  - **Normal** → **DirectX(绿通道朝下)**,线性。UE 用 DirectX 法线,选错(OpenGL)凹凸会内外翻
  - **Roughness** → 线性灰度
  - **Metallic** → 线性灰度
  - **Height / Displacement** → 线性灰度(用 displacement / POM 才需要)
  - **AO** → 线性灰度
- **打包 ORM(UE5 省纹理)**:把 **AO→R、Roughness→G、Metallic→B** 打包进一张图。Sampler 有 **Unreal / ORM 导出预设**,直接选,省手动。

## 7 · UE5 导入设置

- **Base Color**:sRGB ✔
- **Normal**:Compression Settings = **Normalmap (DXT5/BC5)**,sRGB ✘,确认是 DirectX 法线
- **ORM / Roughness / Metallic / AO / Height**:sRGB ✘(线性)
- 建材质:Base Color 接 BaseColor;ORM 拆 R/G/B 分别接 AO / Roughness / Metallic;Normal 接 Normal;Height 接 World Displacement 或 POM(可选)。
- **平铺**:在材质里加 TexCoord,用 UV 缩放控制现实尺寸(1 个 tile = 现实多大,按场景定)。

## 8 · 最终验证(过了才算 S)

- UE5 里平铺到**一面墙 / 一片地**:
  - 远看:**无重复地标、无缝**
  - 近看:**细节够、normal 凹凸方向对、albedo 无残留光影**
  - 金属:metallic / roughness 在引擎光照下表现对
- 过 = S 级,进素材库(连同 Substance 参数预设、UE5 导入设置一起沉淀)。

## 常见错(Substance → UE 段)

| 错 | 表现 | 应对 |
|----|------|------|
| 法线选了 OpenGL | UE5 里凹凸内外翻、打光发假 | 导出选 **DirectX**;或在 UE 材质里 flip green |
| Roughness 反相 | 该糙的发亮、该亮的发糙 | 导出 / 材质里 invert roughness |
| Make it Tile 开太狠 | 母题被涂糊、细节丢 | 已无缝用 Auto / 轻档,别全量重铺 |
| 非金属给了 metallic | 石 / 布 / 土发金属反光 | metallic 通道压 0 |
| delight 不够 | normal 把烘焙阴影顶成真凹凸,贴上去脏 | 回第 3 步加 Delighting / Equalize;根子上回 MJ 压平光影 |
| 指望 MJ 放大补分辨率 | upscale 后接缝崩 | 高分辨率在 **Sampler 导出**时给(工程设 4K),不回 MJ 放大 |

<p align="center"><a href="https://www.maxsacademy.com/en"><img src="assets/maxs-logo.png" width="420" alt="MAXs Academy"></a></p>

<h1 align="center">MAXs Skills</h1>

<p align="center"><b>AI workflows for technical art, 3D assets, environments, and materials — for any LLM.</b></p>

<p align="center">
<a href="https://www.maxsacademy.com/en">Official Website</a> ·
<a href="#english">English</a> ·
<a href="#chinese">中文</a> ·
<a href="https://github.com/ziwuxin1/MAXs-Claude-Plugins/tree/main/skills">Browse Skills</a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/skills-10-2ea44f" alt="10 skills">
<img src="https://img.shields.io/badge/workflows-model%20agnostic-1f6feb" alt="Model-agnostic workflows">
<a href="https://github.com/ziwuxin1/MAXs-Claude-Plugins/stargazers"><img src="https://img.shields.io/github/stars/ziwuxin1/MAXs-Claude-Plugins?style=flat" alt="GitHub stars"></a>
</p>

<a id="english"></a>

## English

### What is MAXs Skills?

**MAXs Skills is a collection of reusable AI instructions, prompt templates, production workflows, and quality checks from [MAXs Academy](https://www.maxsacademy.com/en).** Its 10 skills support the journey from a concept image to 3D asset references, environment planning, and game material textures.

The workflows are designed for **any large language model that can follow the supplied instructions**: Claude, GPT, Gemini, open-weight models, and other assistants. Use a compatible skills/plugin system, or load the Markdown instructions into your preferred assistant yourself.

The repository retains the name `MAXs-Claude-Plugins` to preserve existing links and installations. **The skills are not exclusive to Claude.**

### Compatibility

| Layer | What it provides |
| --- | --- |
| Language model | Interprets the instructions, develops prompts, and guides the workflow. The core methods are model-agnostic. |
| Host application | Loads files, registers skills, or installs the plugin. Native installation depends on the application's supported format. |
| Execution tools | Generate/edit images, process files, or run scripts. These capabilities must be available in the host or connected services. |

An assistant can use MAXs instructions without supporting the marketplace format. Installing a skill does not give a text-only model vision, image generation, file access, or code execution.

Names containing **GPT** or **MJ** identify particular image workflows. Other LLMs can help organize those workflows, but producing the images requires the corresponding tools. Tool-specific parameters belong to the intended tool. Compatibility does not mean every model has been individually tested or will produce identical results.

### Get started with any LLM

1. Download or clone this repository.
2. Choose a skill below and open its `SKILL.md`.
3. Give your assistant that file and the referenced documents needed for your task. If it can read local files, provide the skill's path instead.
4. Add your request, references, and output requirements.

Keep the complete `skills/` directory when possible. Some skills share standards: GPT to Albedo, for example, references SD to Albedo.

> Follow the provided MAXs skill and its quality requirements. Use my reference to create a neutral, weathered brick Albedo. Preserve any version I approve, repair only the requested areas, and check both tiling axes and the four-corner junction before delivery. Explain any required tools that are unavailable.

Most detailed skill instructions are currently in Chinese. You can ask the assistant to explain and deliver results in your preferred language.

### Plugin installation

**Claude Code** — run inside the client:

```text
/plugin marketplace add ziwuxin1/MAXs-Claude-Plugins
/plugin install maxs-skills@maxs
```

To update, run `/plugin marketplace update maxs`, then update `maxs-skills` through the client's plugin controls.

**Codex** — run in your terminal:

```shell
codex plugin marketplace add https://github.com/ziwuxin1/MAXs-Claude-Plugins
codex plugin add maxs-skills@maxs
```

Update an existing installation:

```shell
codex plugin marketplace upgrade maxs
codex plugin add maxs-skills@maxs
```

This repository's root-level plugin layout has been installed successfully with Codex CLI **0.160.0**. Version **0.141.0** failed to discover it; update the CLI if the marketplace appears empty.

For other desktop clients, use their marketplace or skill-import interface if supported. Otherwise, follow the manual instructions above.

### The 10 skills

| Skill | Use it for | Main output |
| --- | --- | --- |
| [Asset Breakdown](skills/maxs-asset-breakdown/SKILL.md) | Breaking a concept into assets and reusable prompt structures | Asset-sheet prompts and a reusable prompt package |
| [Image to Prompt](skills/maxs-image-to-prompt/SKILL.md) | Transferring a composition to a new subject or deriving an editable starting prompt | Composition analysis and prompt templates |
| [Object Multiview](skills/maxs-multiview-reference/SKILL.md) | Planning consistent views of one asset for modeling or reconstruction | View instructions and consistency checks |
| [Interior Views](skills/maxs-interior-multiangle/SKILL.md) | Exploring camera positions in the same interior | Camera prompts that preserve spatial identity |
| [Exterior Views](skills/maxs-exterior-multiangle/SKILL.md) | Exploring the same outdoor location from different cameras | Camera prompts with coherent site and sunlight relationships |
| [MJ Seamless Texture](skills/maxs-seamless-texture/SKILL.md) | Preparing Midjourney texture prompts and a Substance-to-engine workflow | Tileable-texture prompts and PBR workflow guidance |
| [GPT Highlight Cleanup](skills/maxs-gpt-highlight-cleanup/SKILL.md) | Reducing excessive white specks and highlight noise in an approved image | Targeted edits, or prompts when tools are unavailable |
| [GPT Detail Rebuild 4K](skills/maxs-gpt-detail-rebuild-4k/SKILL.md) | Rebuilding credible material detail before a verified-size export | Enhanced image, size verification, and export record |
| [SD to Albedo](skills/maxs-SD-to-Albedo/SKILL.md) | Creating base color from SD/ZBrush Height, Normal, and AO maps | Structure-guided Albedo; Roughness only when requested |
| [GPT to Albedo](skills/maxs-GPT-to-Albedo/SKILL.md) | Generating base color directly from text or appearance references | Albedo with resolution, detail, and tiling checks |

Linked folder names are the stable skill IDs. Preserve their spelling and capitalization, including `maxs-SD-to-Albedo` and `maxs-GPT-to-Albedo`. Native menus have bilingual display names; their order is independent of this English-first README.

### Suggested workflows

- **Assets:** concept → Asset Breakdown → Object Multiview → modeling/reconstruction → engine review.
- **Environments:** concept/reference → Image to Prompt as needed → Interior or Exterior Views → reference board → scene construction.
- **Sculpted materials:** Height / Normal / AO + appearance reference → SD to Albedo → review → optional Roughness → channel alignment and tiling checks.
- **Direct Albedo generation:** brief/reference → GPT to Albedo → color, detail, and tiling checks → approved base color.
- **Midjourney materials:** MJ Seamless Texture → generation → tiling checks → Substance material processing → engine review.
- **Image finishing:** approved image → Highlight Cleanup or Detail Rebuild 4K as requested → local inspection and verified-size export.

### Quality principles

- **Preserve the approved image.** Target the requested correction instead of redesigning the material.
- **Keep colors credible.** Neutral does not mean washed out; aging does not mean blackening everything.
- **Treat Albedo as intrinsic color.** Avoid baked shadows, AO, highlights, and bright bevels.
- **Verify seamlessness.** Inspect a 2×2 repeat, half-width/half-height offset, both axes, and native-resolution corners. Matching edge pixels alone is insufficient.
- **Report actual dimensions.** Distinguish native output, interpolation, AI detail reconstruction, and final export.
- **Separate evidence from targets.** “AAA” and “ArtStation” describe visual goals, not certification. Engine and multi-channel checks remain separate.

See the [approved brick case](skills/maxs-SD-to-Albedo/references/neutral-brick-case.md), [seam-repair case](skills/maxs-SD-to-Albedo/references/seam-repair.md), and [detail-rebuild case](skills/maxs-gpt-detail-rebuild-4k/references/roof-case.md). Tested examples and unvalidated templates are identified separately.

### Repository and updates

```text
.claude-plugin/       Plugin and marketplace manifests
assets/              Branding assets
skills/
  <skill-id>/
    SKILL.md         Skill instructions
    agents/          Host-specific menu metadata, where provided
    references/      Templates and examples, where provided
    scripts/         Processing helpers, where provided
    tests/           Script checks, where provided
```

Pull the latest repository for manual use, or refresh your installed marketplace. Read individual skill changelogs where available. If duplicate menu entries appear, check which plugin supplied them before removing anything.

### About MAXs

[MAXs Academy](https://www.maxsacademy.com/en) provides game art, design, and technical art education. These skills share practical methods developed through MAXs project and teaching work.

**Official website: [www.maxsacademy.com/en](https://www.maxsacademy.com/en)**

---

<a id="chinese"></a>

## 中文

### MAXs Skills 是什么？

**MAXs Skills 是 [MAXs Academy 麦壳思](https://www.maxsacademy.com/en) 提供的 AI 技能与工作流集合**，包含可复用指令、提示词模板、制作流程和质量检查。现有10个技能覆盖从概念图到3D资产参考、场景规划和游戏材质贴图的多个环节。

技能面向**任何能够理解并执行这些指令的大语言模型**，包括 Claude、GPT、Gemini、开源权重模型及其他助手。可以通过兼容的技能／插件系统使用，也可以将 Markdown 指令直接交给所使用的模型。

仓库沿用 `MAXs-Claude-Plugins` 名称，以兼容已有链接和安装方式；**技能内容并不局限于 Claude。**

### 兼容性

| 层级 | 作用 |
| --- | --- |
| 大语言模型 | 理解指令、编写提示词并组织流程；核心方法不绑定某一家模型。 |
| 客户端 | 读取文件、注册技能或安装插件；能否原生安装取决于客户端支持的格式。 |
| 执行工具 | 实际生成／编辑图像、处理文件或运行脚本；需要客户端或连接的服务提供。 |

不支持插件市场的助手，也可以手动加载 MAXs 指令。安装技能不会让纯文字模型自动获得视觉、生图、文件访问或代码执行能力。

名称中带 **GPT** 或 **MJ** 的技能对应特定图像工作流。其他大语言模型同样可以理解和组织流程，但产出图片仍需对应工具；工具专属参数也只适用于相应工具。“通用”不代表所有模型都已逐一实测，或能产生完全一致的效果。

### 使用任意大语言模型开始

1. 下载或克隆本仓库。
2. 在下表中选择技能，打开对应的 `SKILL.md`。
3. 将技能文件及本次任务需要的引用文档提供给助手；支持本地文件读取时，也可以直接提供路径。
4. 补充需求、参考图和交付要求。

建议保留完整 `skills/` 目录。部分技能共用标准，例如 GPT to Albedo 会引用 SD to Albedo。

> 按照提供的 MAXs 技能及质量标准，参考这张图制作中性写实旧砖 Albedo。保留我认可的版本，后续只修指定区域；交付前检查两个方向的平铺与四角交汇。如果当前没有所需工具，请说明。

详细技能指令目前以中文为主，可以要求助手使用需要的语言解释和交付。

### 插件安装

**Claude Code**——在客户端内运行：

```text
/plugin marketplace add ziwuxin1/MAXs-Claude-Plugins
/plugin install maxs-skills@maxs
```

更新时先运行 `/plugin marketplace update maxs`，再通过客户端插件管理更新 `maxs-skills`。

**Codex**——在终端运行：

```shell
codex plugin marketplace add https://github.com/ziwuxin1/MAXs-Claude-Plugins
codex plugin add maxs-skills@maxs
```

更新已安装的插件：

```shell
codex plugin marketplace upgrade maxs
codex plugin add maxs-skills@maxs
```

本仓库的根目录插件结构已在 Codex CLI **0.160.0** 成功安装；旧版 **0.141.0** 曾无法发现该插件。如果市场显示为空，请先更新 CLI。

其他桌面客户端如支持技能导入或插件市场，可通过其界面安装；不支持时使用上面的手动加载方式。

### 10个技能速查

| 技能 | 适用任务 | 主要产出 |
| --- | --- | --- |
| [资产拆解](skills/maxs-asset-breakdown/SKILL.md) | 将概念图拆成资产，建立可复用提示词结构 | 资产陈列图提示词与复用包 |
| [图转提示词](skills/maxs-image-to-prompt/SKILL.md) | 迁移构图到新题材，或反推可编辑的起点提示词 | 构图分析与提示词模板 |
| [物体多视图](skills/maxs-multiview-reference/SKILL.md) | 为单件资产规划建模或重建参考视角 | 多视角指令与一致性检查 |
| [室内多机位](skills/maxs-interior-multiangle/SKILL.md) | 在同一室内空间中探索不同机位 | 保持空间身份的机位提示词 |
| [室外多机位](skills/maxs-exterior-multiangle/SKILL.md) | 从不同机位观察同一室外场地 | 保持场地与太阳关系的机位提示词 |
| [MJ 无缝贴图](skills/maxs-seamless-texture/SKILL.md) | 编写 Midjourney 贴图提示词并组织 Substance 到引擎的流程 | 平铺贴图提示词与 PBR 制作指引 |
| [GPT 高亮清理](skills/maxs-gpt-highlight-cleanup/SKILL.md) | 降低已认可图片中过密的白点与高亮噪声 | 定向修图；缺工具时提供提示词 |
| [GPT 细节重建 4K](skills/maxs-gpt-detail-rebuild-4k/SKILL.md) | 重建可信材质细节后，核验尺寸并导出 | 增强图、尺寸核验与导出记录 |
| [SD 转 Albedo](skills/maxs-SD-to-Albedo/SKILL.md) | 从已有 SD／ZBrush Height、Normal、AO 制作基色 | 按结构生成 Albedo；仅按需制作 Roughness |
| [GPT 生成 Albedo](skills/maxs-GPT-to-Albedo/SKILL.md) | 从文字或外观参考直接制作基色 | Albedo 与尺寸、细节、平铺检查 |

链接中的目录名就是稳定调用 ID。保留原有拼写和大小写，包括 `maxs-SD-to-Albedo` 与 `maxs-GPT-to-Albedo`。原生菜单提供双语显示名；菜单顺序与本 README 的英文优先排版相互独立。

### 推荐工作流

- **资产：** 概念图 → 资产拆解 → 物体多视图 → 建模／重建 → 引擎检查。
- **场景：** 概念图／参考 → 按需图转提示词 → 室内或室外多机位 → 参考板 → 场景搭建。
- **已有雕刻贴图：** Height／Normal／AO + 外观参考 → SD 转 Albedo → 审核 → 按需 Roughness → 通道对应与平铺检查。
- **直接生成基色：** 需求／参考 → GPT 生成 Albedo → 色彩、细节与平铺检查 → 确定基色。
- **Midjourney 材质：** MJ 无缝贴图 → 生图 → 平铺检查 → Substance 材质处理 → 引擎检查。
- **图像精修：** 已认可图片 → 按需高亮清理或细节重建 4K → 局部检查与实际尺寸核验。

### 质量原则

- **以认可版本为基准。** 后续只修指定问题，不借修图重新设计整张材质。
- **保持可信本色。** 中性不等于泛白，做旧不等于整片发黑。
- **Albedo 表达本色。** 避免烘焙阴影、AO、高光和亮倒角。
- **实际检查无缝。** 检查2×2平铺、宽高半幅偏移、两个方向和原尺寸四角；边缘像素相等不等于视觉无缝。
- **记录真实尺寸。** 区分原生生成、插值放大、AI 细节重建与最终导出。
- **区分目标与验证。** “AAA”和“ArtStation”是视觉目标，不是质量认证；引擎与多通道检查仍需单独进行。

可查看[旧砖认可案例](skills/maxs-SD-to-Albedo/references/neutral-brick-case.md)、[接缝修复案例](skills/maxs-SD-to-Albedo/references/seam-repair.md)和[细节重建案例](skills/maxs-gpt-detail-rebuild-4k/references/roof-case.md)。实测案例与尚未验证的模板分别标注。

### 仓库与更新

- `.claude-plugin/`：插件与市场清单。
- `assets/`：品牌素材。
- `skills/<skill-id>/SKILL.md`：技能入口。
- 各技能按需包含 `agents/` 菜单元数据、`references/` 模板与案例、`scripts/` 处理脚本及 `tests/` 脚本检查。

手动使用时拉取最新仓库；插件安装时刷新对应市场。变更记录见各技能提供的 changelog。菜单出现重复项时，先核对其所属插件，再决定是否移除。

### 关于 MAXs

[MAXs Academy 麦壳思](https://www.maxsacademy.com/en) 提供游戏美术、设计与技术美术教育。本技能库分享 MAXs 在项目制作与教学中整理的实用方法。

**官方网站：[www.maxsacademy.com/en](https://www.maxsacademy.com/en)**

# Changelog - maxs-ai-prompt-sop

## [1.0.0] - 2026-05-22

### Added

- 初始版本发布
- 核心方法论:
  - 三个判断标准(学生能否复现 / 经过迭代验证 / 简洁性到位)
  - 五个核心动作(明确用途 → 套黄金模板 → 三步迭代 → 识别 bug → 输出复用包)
  - 分级体系(S/A/B/C 级)
- 已验证模板:
  - 模板 1: 资产陈列图(白底版)—— Banana Pro 验证
  - 模板 2: 单件 3 视图(给 Tripo/Hunyuan3D 喂料)
  - 模板 3: 深色氛围陈列图(美宣/portfolio)
  - 模板 4: 概念美宣单图(art bible 参考)
- 实战案例:
  - 案例 1: 雪山古建白底资产陈列图三步迭代(经典案例)
  - 案例 2: 从场景图到资产拆解的完整工作流
  - 案例 3: 风格漂移问题(中式飞檐变日式神社)
  - 案例 4: 数量与质量的甜蜜点
- references 子文档:
  - `prompt-templates.md`
  - `iteration-cases.md`
  - `reuse-package-template.md`
  - `output-quality-checklist.md`

### Known Limitations

- 当前案例集中在 Banana Pro,Midjourney / Flux 的专属案例待补充
- 缺少视频/动画类提示词(Sora/Kling/Runway)的专项章节
- IP 角色对话脚本尚未编写

### 验证模型与时间

- Banana Pro: 2026 年 3 月,雪山古建场景已多次验证
- Midjourney v6: 部分验证
- Nano Banana: 历史使用,部分案例参考

# addsumtech/slides_maker 分析报告

- 仓库：[addsumtech/slides_maker](https://github.com/addsumtech/slides_maker)
- 方向：把论文/仓库/文档/主题变成可编辑 PPTX 的 Agent 技能
- 主要语言：Python
- 指标：⭐ 357 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/addsumtech/slides_maker)

> 分析基于 2026-08-06 抓取的 README、skills/ 与文档。296MB 仓库，未细读全部资源。

## 这是什么（非技术版）

- **这是什么**：一个"AI 做 PPT 技能"。把论文、仓库、文档或一个主题变成可以直接演示的原生 PPTX；由一小队专业 Agent 阅读资料、规划故事、逐页设计、构建文件，并经过独立评审才交付——不编数字。
- **能拿来干什么**：自动生成可编辑幻灯片、论文/项目汇报。
- **适合谁**：研究者、开发者、需要快速做专业 PPT 的人。
- **快速判断**：如果你经常"资料一大把但没时间排版"，它很有用；否则手动做即可。

## 分类

- 主分类：6. 特定领域 / 其他（演示文稿生成技能）
- 副分类：3. 多 Agent 编排 / 协作系统（专业 Agent 团队）
- 理由：README 自述 "a small team of specialized agents reads your paper / repo / doc... plans the story, designs each slide... builds a real .pptx, and puts it through an independent review"。

## 项目方向与定位

"reads your actual work, never invents a number, ships fully-editable native PowerPoint"：以真实资料为唯一输入，专业 Agent 团队流水线（阅读→规划→设计→构建→独立评审）。支持 Codex/Claude Code/ChatGPT GPT Store/Coze/Tencent SkillHub 多平台。

## 主要功能（能做什么）

- 论文/仓库/文档/主题 → 原生可编辑 PPTX
- 独立评审门禁（未经评审不交付）
- 多宿主：Codex、Claude Code、ChatGPT、Coze、SkillHub

## 架构设计

```text
skills/        技能实现
scripts/ docs/
```

## 实现思路与核心逻辑

- 专业团队流水线：不同角色 Agent 分工（阅读/规划/设计/构建/评审）
- 质量门禁：独立批评者签字后才交付
- 原生 PPTX：可编辑、可二次修改

## 亮点

- 357 stars，PPT 生成垂直场景完成度高
- 多平台分发（GPT Store/Coze/SkillHub）
- MIT 开源，Addsum 出品

## 局限与风险（可选）

- 296MB 仓库体积大
- 与"Agent Harness 内测"主题相关度低（内容工具）

## 分析说明

基于 README、skills/ 与文档；未运行生成管线。

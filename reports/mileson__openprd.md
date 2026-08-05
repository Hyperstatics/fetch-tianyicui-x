# mileson/openprd 分析报告

- 仓库：[mileson/openprd](https://github.com/mileson/openprd)
- 方向：AI 原生 PRD 工作区与 CLI（需求澄清→证据交付）
- 主要语言：JavaScript/TypeScript
- 指标：⭐ 47 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/mileson/openprd)

> 分析基于 2026-08-06 抓取的 README、bin/docs 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"帮团队把需求说清楚的 AI 工具"。你只说出问题，它帮你整理成需求澄清、事实与决策记录、图形化评审、风险提醒和交付检查，最后以证据交付。
- **能拿来干什么**：PRD 管理、需求澄清、Agent 协作交付。
- **适合谁**：产品/研发团队、Agent 化开发流程。
- **快速判断**：如果你受够了"需求说不清"，它很对口；否则普通文档即可。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（PRD harness）
- 副分类：6. 特定领域 / 其他（产品工具）
- 理由：README 自述"帮团队和 Agent 把需求说清楚、持续做下去并用证据交付的 AI 原生 PRD 工作区与 CLI"，自称 PRD harness。

## 项目方向与定位

轻量结构化 PRD harness：需求澄清、Agent 后台维护的事实与决策、图形化评审、非阻断式风险提醒、结构化交接；需求/决策/验证沉淀为稳定 HTML 产物。

## 主要功能（能做什么）

- 需求澄清与事实/决策记录
- 图形化评审、风险提醒、交付检查
- 面向执行系统的结构化交接
- CLI + HTML 产物

## 架构设计

```text
bin/           CLI
.openprd/     状态
docs/
```

## 实现思路与核心逻辑

- "沉淀优于聊天记录"：需求/决策/验证进稳定产物
- Agent 后台维护，无需用户逐条回复

## 亮点

- 47 stars，PRD 垂直场景 + Agent 结合
- MIT 开源、中英双语

## 局限与风险（可选）

- 需要团队接受新流程
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、bin/docs 与文档；未运行。

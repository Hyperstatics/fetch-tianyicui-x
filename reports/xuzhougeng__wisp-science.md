# xuzhougeng/wisp-science 分析报告

- 仓库：[xuzhougeng/wisp-science](https://github.com/xuzhougeng/wisp-science)
- 方向：本地优先的 AI 科研工作台（桌面，生物信息 MCP 数据库）
- 主要语言：HTML/TypeScript（Tauri）+ Python/R 计算层
- 指标：⭐ 859 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/xuzhougeng/wisp-science)

> 分析基于 2026-08-06 抓取的 README、crates/mcp-servers 结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"科研 AI 桌面助手"。连接大模型，在本机/WSL/SSH/GPU 上跑 Python 和 R，加载可复用技能，内置约 80 个生物信息数据库的 MCP 接口，数据和凭据留在自己机器。
- **能拿来干什么**：生物信息/计算生物学研究、科研数据分析、本地 AI 科研助手。
- **适合谁**：科研人员、生信分析师、需要私有数据 + AI 的团队。
- **快速判断**：如果你做生信/计算科研且要数据不外传，它很对口；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（科研/生信工作台）
- 副分类：1. 通用 Agent Runtime / Harness（本地 Agent 桌面）
- 理由：README 自述 "The open-source, local-first AI research workbench... reaches ~80 bioinformatics databases through bundled MCP servers"。

## 项目方向与定位

AI 科研助手 + 科学计算工作台：OpenAI/Anthropic 兼容模型、本地/WSL/SSH/GPU 的持久 Python/R 环境、可复用 Agent Skills（SKILL.md）、约 80 个生信/计算生物数据库 MCP 服务器；数据/对话/凭据全部留在自己机器。

## 主要功能（能做什么）

- 桌面科研助手（Windows/macOS 发布，Linux 源码构建）
- Python / R 多环境（本地/WSL/SSH/GPU）
- Agent Skills（SKILL.md）加载；MCP servers（约 80 个生信数据库）
- DOI 存档、中英双语文档

## 架构设计

```text
crates/ src-tauri/   桌面壳（Rust/Tauri）
mcp-servers/         生信数据库 MCP
python/ r/           计算环境
skills/              技能
browser-extension/   浏览器扩展
```

## 实现思路与核心逻辑

- "数据不出门"：本地/SSH/GPU 计算 + 本机凭据
- 领域深耕：MCP 直连生信数据库，降低科研数据获取成本
- 技能复用：SKILL.md 标准化科研流程

## 亮点

- 生信垂直场景 + MCP 数据库集合是显著差异化
- 本地优先契合科研数据合规需求
- Zenodo DOI，学术可引用

## 局限与风险（可选）

- **AGPL-3.0**：派生分发需遵守 copyleft
- 垂直领域工具，通用性有限
- 与"Agent Harness 内测"主题相关度低

## 分析说明

基于 README、crates/mcp-servers 结构与文档；未运行。

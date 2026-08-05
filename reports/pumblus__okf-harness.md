# pumblus/okf-harness 分析报告

- 仓库：[pumblus/okf-harness](https://github.com/pumblus/okf-harness)
- 方向：agent-first 本地终端 harness——维护 OKF 兼容 LLM Wiki
- 主要语言：TypeScript
- 指标：⭐ 31 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/pumblus/okf-harness)

> 分析基于 2026-08-06 抓取的 README、docs/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"让 AI 维护活知识库"的本地终端工具。基于 Karpathy 的 LLM Wiki 模式和 Google 的 OKF 格式，Agent 从源文件/URL 持续生成、更新结构化 Markdown 知识包。
- **能拿来干什么**：AI 维护团队/个人知识库、便携知识包。
- **适合谁**：知识管理爱好者、Agent 工作流开发者。
- **快速判断**：如果你想要"AI 维护的活 Wiki"，它很对口；否则普通笔记即可。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（LLM Wiki）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "An agent-first, local-first, terminal-native harness for maintaining OKF-compatible LLM Wikis"。

## 项目方向与定位

融合 Karpathy LLM Wiki（Agent 维护的活知识库）与 Google OKF（可移植 Markdown 知识包）：源文件/URL → 知识包。

## 主要功能（能做什么）

- OKF 兼容知识包生成与维护
- 本地终端、agent-first
- Claude 插件、CLI 文档

## 架构设计

```text
docs/ examples/ .claude-plugin/
```

## 实现思路与核心逻辑

- "活 Wiki"：Agent 持续更新而非一次性生成
- OKF 标准化保证可移植

## 亮点

- 31 stars，LLM Wiki + OKF 组合
- 与帖子"记忆/知识"类别契合
- Apache-2.0

## 局限与风险（可选）

- 概念较新，生态待验证
- 依赖 Agent 质量

## 分析说明

基于 README、docs/ 与文档；未运行。

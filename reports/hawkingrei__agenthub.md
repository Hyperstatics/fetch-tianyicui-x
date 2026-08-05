# hawkingrei/agenthub 分析报告

- 仓库：[hawkingrei/agenthub](https://github.com/hawkingrei/agenthub)
- 方向：自托管 AI Agent 控制面（长期 Agent + ACP + Team）
- 主要语言：Rust
- 指标：⭐ 31 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[doc.agenthub.hawkingrei.com](https://doc.agenthub.hawkingrei.com/)

> 分析基于 2026-08-06 抓取的 README、cmd/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 长期员工控制台"。管理长期运行的编码 Agent、结构化 ACP 时间线、多 Agent 团队工作流和远程执行节点，一个产品面搞定，不用另接控制面板。
- **能拿来干什么**：团队统一管理长期 Agent、ACP 审查、远程执行。
- **适合谁**：团队、需要 Agent 控制面的组织。
- **快速判断**：如果你要"一个控制面管所有长期 Agent"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（控制面）
- 副分类：3. 多 Agent 编排 / 协作系统
- 理由：README 自述 "a self-hosted AI agent control plane for long-lived coding agents, structured ACP timelines, multi-agent Team workflows, and optional remote execution nodes"。

## 项目方向与定位

自托管 Agent 控制面：长期 Agent、ACP 时间线、Team 协作、远程执行节点。Rust 实现、Bazel 构建。

## 主要功能（能做什么）

- 长期编码 Agent 管理
- ACP 结构化时间线
- 多 Agent Team 工作流
- 远程执行节点（可选）

## 架构设计

```text
cmd/           入口
agenthub-codex-acp/  ACP 集成
build/ BUILD.bazel
```

## 实现思路与核心逻辑

- "一个产品面"：控制面、审查、协作、远程一体
- ACP 结构化时间线支撑审查

## 亮点

- 31 stars，自托管控制面定位与帖子主题契合
- ACP + Team + 远程执行组合完整
- Apache-2.0

## 局限与风险（可选）

- 项目较新
- 依赖 ACP 生态成熟度

## 分析说明

基于 README、cmd/ 与文档；未运行。

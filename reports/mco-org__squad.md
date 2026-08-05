# mco-org/squad 分析报告

- 仓库：[mco-org/squad](https://github.com/mco-org/squad)
- 方向：多 AI Agent 终端协作（shell 命令 + SQLite 通信）
- 主要语言：Rust
- 指标：⭐ 619 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/mco-org/squad)

> 分析基于 2026-08-06 抓取的 README、src/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"让多个 AI 通过命令行互相交流"的工具。Claude Code、Gemini CLI、Codex、OpenCode 等可以通过它共享消息和任务，靠 SQLite 存数据；没有后台常驻进程，每条命令一次执行完。
- **能拿来干什么**：多 Agent 协作、让不同 AI 接力完成任务。
- **适合谁**：开发者、多 Agent 实验者。
- **快速判断**：如果你想让多个 AI CLI "组队干活"，它很轻巧；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Multi-AI-agent terminal collaboration via simple CLI commands... communicate through shell commands + SQLite"。

## 项目方向与定位

极简多 Agent 终端协作：无 daemon、无后台进程，每条命令一次完成；通过 shell 命令 + SQLite 持久化共享状态。适配 Claude Code/Gemini CLI/Codex/OpenCode 等主流 CLI Agent。

## 主要功能（能做什么）

- 多 Agent 通过 CLI 命令通信与交接
- SQLite 持久化（消息/状态）
- 4 平台支持、install.sh 安装、Homebrew Formula
- 中英双语文档、站点

## 架构设计

```text
src/         Rust 实现
scripts/ install.sh / Formula（Homebrew）
docs/ site/ templates/
```

## 实现思路与核心逻辑

- "一次一命令"哲学：无常驻进程，降低运维复杂度
- SQLite 作为共享总线：Agent 读/写同一状态
- 与现有 CLI Agent 兼容，零侵入

## 亮点

- 619 stars，极简多 Agent 协作方案（619）
- 无 daemon 设计独特，易上手
- MIT + 中文社区

## 局限与风险（可选）

- 复杂协作场景可能不够（无编排/任务调度）
- 依赖各 CLI Agent 的 shell 能力

## 分析说明

基于 README、src/ 与文档；未运行。

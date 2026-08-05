# xicilion/boxsh 分析报告

- 仓库：[xicilion/boxsh](https://github.com/xicilion/boxsh)
- 方向：沙箱化 POSIX shell + MCP Server（AI Agent 隔离执行）
- 主要语言：C（dash 0.5.12 基础）
- 指标：⭐ 328 · License GPL-3.0（LICENSE.md 确认）· 最近推送 2026-08-03
- 主页/文档：[Usage Guide](https://github.com/xicilion/boxsh/blob/main/docs/usage.md)

> 分析基于 2026-08-06 抓取的 README、src/sdk 结构与文档。元数据标 NOASSERTION，LICENSE.md 实为 GPL-3.0。

## 这是什么（非技术版）

- **这是什么**：一个"给 AI 用的隔离沙箱终端"。AI 可以在里面随便执行命令、读写文件，但改动都落在独立的副本层（COW），原目录不受影响；作为 MCP 服务器直接接 Claude/Cursor 等。
- **能拿来干什么**：让 AI 安全地跑命令/改文件而不污染你的项目；多任务并行隔离执行。
- **适合谁**：开发者、Agent 工具链、需要沙箱执行的团队。
- **快速判断**：如果你要让 AI"放手干活又不担心破坏"，它很合适；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（沙箱执行层）
- 副分类：6. 特定领域 / 其他（系统工具）
- 理由：README 自述 "A sandboxed POSIX shell and MCP server... OS-native sandbox isolation is baked in"。

## 项目方向与定位

基于 dash 的沙箱 shell + MCP server：OS 原生沙箱（Linux namespaces/seccomp、macOS Seatbelt）、Copy-on-Write 工作区、并行隔离 worker 池、JSON-RPC 2.0 双传输。给 AI Agent/构建系统一个"能执行任意命令但被精确约束"的 shell。

## 主要功能（能做什么）

- MCP server：9 个工具（bash/read/write/edit/terminal 系列）
- COW 工作区：写入落到独立目录，原目录不动
- 交互式沙箱 shell（`boxsh --try`）
- 预 fork worker 池：并发、崩溃恢复、超时、乱序流式

## 架构设计

```text
src/          核心（shell/MCP/沙箱）
sdk/          客户端 SDK
tests/ docs/ third_party/
```

## 实现思路与核心逻辑

- OS 原生沙箱：直接 syscall（namespace/seccomp）或 Seatbelt，无外部工具
- COW 抽象：Agent 自由读写，改动可丢弃可持久
- 事件循环非阻塞：文件工具后台线程执行

## 亮点

- 328 stars，MCP 沙箱 shell 方案实用且安全导向
- 双平台（Linux/macOS）原生沙箱、零外部依赖
- COW 工作区设计对"AI 试错"场景很贴心

## 局限与风险（可选）

- **GPL-3.0**：派生/静态集成需遵守 copyleft
- 沙箱边界（进程树/TOCTOU）仍需按 README 提醒关注

## 分析说明

基于 README、src/sdk 结构与 LICENSE.md；未运行沙箱。

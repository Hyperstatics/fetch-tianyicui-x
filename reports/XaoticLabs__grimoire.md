# XaoticLabs/grimoire 分析报告

- 仓库：[XaoticLabs/grimoire](https://github.com/XaoticLabs/grimoire)
- 方向：cron + systemd for AI coding agents（长驻监督 daemon）
- 主要语言：Rust
- 指标：⭐ 0 · License MIT OR Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/XaoticLabs/grimoire)

> 分析基于 2026-08-06 抓取的 README、docs/ 与文档。

## 这是什么（非技术版）

- **这是什么**：把 AI 编码 Agent 变成"长期存活、受监督的守护进程"。今天召唤的 Agent 下周还有地址；空闲睡眠、按计划/文件变化/消息唤醒、崩溃自重启、需要人时 ping 你。核心观点：Agent 是进程，不是函数调用。
- **能拿来干什么**：长期运行、可恢复的 Agent 服务。
- **适合谁**：开发者、Agent 平台团队。
- **快速判断**：如果你要"Agent 像服务一样跑"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（daemon/监督）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "runs AI coding agents as long-lived, supervised daemons... agents are processes, not function calls"。

## 项目方向与定位

Agent 服务化：identity/mailbox/supervisor；Claude Code 默认，pi/opencode/aider/codex 等可接；原生会话恢复或转录回放。

## 主要功能（能做什么）

- 长驻 daemon、调度/文件/消息唤醒
- 崩溃自重启、人类 ping
- 多 provider 会话恢复

## 架构设计

```text
docs/（blog: agents-are-processes、providers）
```

## 实现思路与核心逻辑

- "Agent 即服务"：进程生命周期管理

## 亮点

- 0 stars，Agent 服务化理念
- 与帖子"长期 Agent"主题契合
- MIT/Apache-2.0 双许可

## 局限与风险（可选）

- 生态较新
- 依赖宿主 CLI

## 分析说明

基于 README、docs/ 与文档；未运行。

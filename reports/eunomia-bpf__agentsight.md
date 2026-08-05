# eunomia-bpf/agentsight 分析报告

- 仓库：[eunomia-bpf/agentsight](https://github.com/eunomia-bpf/agentsight)
- 方向：基于 eBPF 的系统级 AI Agent 观测（top/strace 风格）
- 主要语言：C（eBPF）
- 指标：⭐ 556 · License MIT · 最近推送 2026-08-03
- 主页/文档：[arXiv 2508.02736](https://arxiv.org/abs/2508.02736)

> 分析基于 2026-08-06 抓取的 README 与论文信息；仓库约 856MB，未克隆，采用 API-only 分析。

## 这是什么（非技术版）

- **这是什么**：一个"AI 干活过程的监控摄像头"。用 eBPF 技术实时看到 AI Agent 在电脑上做了什么：跑了哪些命令、改了哪些文件、连了哪些网络、调用模型/工具花了多少时间与 token。
- **能拿来干什么**：排查 AI 任务卡住/失败；审计 AI 动了哪些数据；优化 token 与资源开销。
- **适合谁**：AI 开发者、运维、安全审计、研究者。
- **快速判断**：如果你想知道"AI 到底在我机器上干了啥"，它是利器；否则不需要。

## 分类

- 主分类：6. 特定领域 / 其他（可观测性/安全工具）
- 副分类：1. 通用 Agent Runtime / Harness（Agent 观测层）
- 理由：README 自述 "System-wide AI agent profiling and monitoring with eBPF... a local-first top/strace-like observability tool for AI agents"。

## 项目方向与定位

无 SDK、无代理、无厂商集成：用 eBPF + TLS 流量追踪观测 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw 等任何命令的运行效果。arXiv 论文 + DOI 发表，定位"Agent 时代的 top/strace"。

## 主要功能（能做什么）

- 实时监控会话、进程、资源、模型与工具调用、文件与网络活动
- 连接提示词/技能与错误，改进指令
- 定位时间/token/资源去向（慢步骤、重试循环、token 密集会话）
- 数据流动审计与安全建议

## 架构设计

```text
（eBPF 探针 + 用户态分析）
```

## 实现思路与核心逻辑

- eBPF 零侵入观测：无需 Agent SDK/代理/厂商集成
- TLS 追踪补全"模型调用/网络请求"视图
- 观测数据驱动诊断与安全审计

## 亮点

- "Agent 可观测性"赛道稀缺，学术背书（arXiv/DOI）
- 零 SDK 设计通用性极强
- MIT 开源

## 局限与风险（可选）

- 仓库 856MB 体积大；eBPF 需要对应内核权限
- 与"Agent Harness 内测"主题相关度中等（观测层）

## 分析说明

API-only 分析（README + 论文信息），未克隆源码。

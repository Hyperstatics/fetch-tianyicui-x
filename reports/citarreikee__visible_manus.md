# citarreikee/visible_manus 分析报告

- 仓库：[citarreikee/visible_manus](https://github.com/citarreikee/visible_manus)
- 方向：多 Agent 编排 + 实时可视化（交互画布）
- 主要语言：TypeScript
- 指标：⭐ 111 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/citarreikee/visible_manus)

> 分析基于 2026-08-06 抓取的 README、core/planner/agents 结构与文档。⚠️ 仓库未见 LICENSE 文件，使用前需确认。

## 这是什么（非技术版）

- **这是什么**：一个"看得见的多 AI 协作系统"。通过交互画布实时观看 AI 规划、执行、协作，DeepSeek API 驱动。
- **能拿来干什么**：可视化多 Agent 流程、演示/教学、研究 Agent 协作。
- **适合谁**：研究者、对 Agent 可视化感兴趣的人。
- **快速判断**：如果你想"看 AI 干活的过程"，它很直观；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：6. 特定领域 / 其他（可视化）
- 理由：README 自述 "A multi-agent AI orchestration system with real-time visualization. Watch AI agents plan, execute tasks, and collaborate through an interactive canvas interface."。

## 项目方向与定位

多 Agent 编排 + 实时可视化：后端（Python WebSocket server）+ 前端画布；planner/agents/core 分层。

## 主要功能（能做什么）

- 多 Agent 规划/执行/协作
- 交互画布实时可视化
- DeepSeek API 驱动

## 架构设计

```text
core/ planner/ agents/   后端
frontend/                画布前端
main.py server.py
```

## 实现思路与核心逻辑

- 可视化优先：Agent 状态实时投射到画布
- WebSocket 前后端通信

## 亮点

- 111 stars，可视化多 Agent 演示直观
- 轻量（0.2MB），快速上手

## 局限与风险（可选）

- **未见 LICENSE 文件**（已列入本地 backlog）
- 功能面较基础，生产性有限

## 分析说明

基于 README、core/planner/agents 结构与文档；未运行。

# Zleap-AI/Zleap-Agent 分析报告

- 仓库：[Zleap-AI/Zleap-Agent](https://github.com/Zleap-AI/Zleap-Agent)
- 方向：workspace-first 的 Agent Harness（本地/OpenAI 兼容模型）
- 主要语言：TypeScript
- 指标：⭐ 207 · License Apache-2.0（LICENSE 确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/Zleap-AI/Zleap-Agent)

> 分析基于 2026-08-06 抓取的 README、packages/ 与文档。早期预览状态。

## 这是什么（非技术版）

- **这是什么**：一个"按工作区给 AI 发上下文"的 Agent 框架。核心想法：Agent 不应该每一步看到所有工具、记忆、规则和历史消息，而应该先知道自己在哪个工作区，只拿那个工作区需要的上下文。
- **能拿来干什么**：构建上下文精简、更可控的本地 Agent。
- **适合谁**：开发者、研究 Agent 上下文管理的人。
- **快速判断**：如果你觉得"Agent 上下文太杂导致出错"，它的理念值得参考；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness
- 副分类：4. 记忆 / 上下文 / 知识管理
- 理由：README 自述 "A workspace-first agent harness... It should first know which workspace it is in, then receive only the context needed for that workspace"。

## 项目方向与定位

workspace-first：上下文按工作区裁剪，减少噪音与 token。支持本地与 OpenAI 兼容模型；早期 preview（源码审查/本地开发/反馈为主）。

## 主要功能（能做什么）

- 工作区感知的上下文管理
- 本地/OpenAI 兼容模型
- packages 多包、docker-compose

## 架构设计

```text
packages/     多包
docker-compose.yml / distribution.json
```

## 实现思路与核心逻辑

- 上下文最小化：按工作区路由，而非全量灌输
- 以工作区为边界组织工具/记忆/规则

## 亮点

- 207 stars，workspace-first 理念与"上下文工程"趋势契合
- Apache-2.0，早期透明

## 局限与风险（可选）

- 预览阶段，API/UI 可能变化
- 生态未成熟

## 分析说明

基于 README、packages/ 与文档；未运行。

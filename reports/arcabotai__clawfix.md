# arcabotai/clawfix 分析报告

- 仓库：[arcabotai/clawfix](https://github.com/arcabotai/clawfix)
- 方向：OpenClaw 诊断与受保护修复（guarded repairs）
- 主要语言：JavaScript/TypeScript
- 指标：⭐ 6 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/arcabotai/clawfix)

> 分析基于 2026-08-06 抓取的 README、cli/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"OpenClaw 体检与修复工具"。本地扫描、脱敏已识别的密钥、按确定性规则匹配故障；可选 AI 分析解释未匹配问题，但模型输出永远不会变成可执行的 shell。
- **能拿来干什么**：诊断 OpenClaw 配置/运行问题、安全修复。
- **适合谁**：OpenClaw 用户、运维。
- **快速判断**：如果你用 OpenClaw 且遇到问题，它很有用；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（诊断工具）
- 副分类：1. 通用 Agent Runtime / Harness（OpenClaw 生态）
- 理由：README 自述 "OpenClaw diagnostics and guarded repairs... Model output never becomes executable shell."。

## 项目方向与定位

OpenClaw 诊断：本地扫描、secret 脱敏、确定性规则匹配、可选 AI 解释；安全原则（AI 输出不执行 shell）。

## 主要功能（能做什么）

- 本地扫描与 secret 脱敏
- 故障规则匹配、可选 AI 分析
- 自托管、能力契约文档

## 架构设计

```text
cli/ Dockerfile
docs/capabilities/
```

## 实现思路与核心逻辑

- 确定性优先：规则匹配兜底，AI 只解释
- 安全护栏：AI 输出不转 shell

## 亮点

- 6 stars，OpenClaw 生态补位
- 安全设计明确
- MIT 开源

## 局限与风险（可选）

- 强依赖 OpenClaw
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、cli/ 与文档；未运行。

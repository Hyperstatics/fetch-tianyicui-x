# iancjy-creator/antigravity-agent-rigor-guard 分析报告

- 仓库：[iancjy-creator/antigravity-agent-rigor-guard](https://github.com/iancjy-creator/antigravity-agent-rigor-guard)
- 方向：Google Antigravity 编码 Agent 的 fail-closed 护栏
- 主要语言：JavaScript
- 指标：⭐ 0 · License README 标 MIT（仓库未见 LICENSE 文件，需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/iancjy-creator/antigravity-agent-rigor-guard)

> 分析基于 2026-08-06 抓取的 README、hooks.json 与文档。⚠️ 未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：给 Google Antigravity 的 AI 编码 Agent 加"安全护栏"：拦截危险工具调用、记录可审计执行证据、检测测试退化，未通过配置检查前不允许 Agent 声明"完成"。
- **能拿来干什么**：让 Antigravity Agent 干活更可靠。
- **适合谁**：Antigravity 用户。
- **快速判断**：如果你用 Google Antigravity 且担心"假完成"，它很对口；否则用不上。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（护栏/验证）
- 副分类：5. 评测 / Benchmark 工具
- 理由：README 自述 "Fail-closed guardrails and verification gates for AI coding agents in Google Antigravity"。

## 项目方向与定位

fail-closed 护栏：工具调用拦截、审计证据、测试退化检测、完成门禁。

## 主要功能（能做什么）

- 危险工具拦截
- 可审计执行证据、测试退化检测
- 完成门禁

## 架构设计

```text
hooks.json + lefthook.yml + install.mjs
```

## 实现思路与核心逻辑

- 验证先行：检查通过才算完成

## 亮点

- 0 stars，Antigravity 生态护栏
- 与"可验证 Agent"主题契合

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 强依赖 Antigravity

## 分析说明

基于 README、hooks.json 与文档；未运行。

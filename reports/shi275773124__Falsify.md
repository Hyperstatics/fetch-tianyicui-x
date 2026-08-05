# shi275773124/Falsify 分析报告

- 仓库：[shi275773124/Falsify](https://github.com/shi275773124/Falsify)
- 方向："Looks green isn't proof"——对抗性审查与框架审查
- 主要语言：Python
- 指标：⭐ 4 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/shi275773124/Falsify)

> 分析基于 2026-08-06 抓取的 README、falsify/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 成果审查工具"。两个痛点：AI 幻觉与假绿（日志绿、另一个模型也同意，仍不安全）→ 对抗性审查（red-team"看起来没问题"）；长期腐化/过度工程 → 框架审查 + Cutline（Must Fix / Debt / Delete）。
- **能拿来干什么**：AI 代码交付前的对抗性审查、防止假完成。
- **适合谁**：用 AI 写代码的团队。
- **快速判断**：如果你怕"AI 说完成其实没完成"，它很有价值；否则不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（审查/质量）
- 副分类：5. 评测 / Benchmark 工具
- 理由：README 自述 "Review first. Trust after. Evidence first. Ship after... Adversarial review — red-teams 'looks fine'"。

## 项目方向与定位

审查优先：对抗性审查（针对假绿）+ 框架审查（针对长期腐化）+ Cutline 分级（Must Fix/Debt/Delete）。

## 主要功能（能做什么）

- 对抗性审查（red-team）
- 框架审查、Cutline 分级
- demo-vault、docs、examples

## 架构设计

```text
falsify/       核心
demo-vault/ examples/ design/
```

## 实现思路与核心逻辑

- "证据优先"：绿不算数，对抗验证才算
- 分级处理：Must Fix / Debt / Delete

## 亮点

- 4 stars，对抗审查理念
- 与"可验证 Agent"主题契合
- MIT 开源

## 局限与风险（可选）

- 项目较新
- 审查覆盖有限

## 分析说明

基于 README、falsify/ 与文档；未运行。

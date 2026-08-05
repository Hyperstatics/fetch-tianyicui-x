# xiaozhenliu/micro-eval 分析报告

- 仓库：[xiaozhenliu/micro-eval](https://github.com/xiaozhenliu/micro-eval)
- 方向：本地优先的 Agent/Skill 评测助手（要证据，不要感觉）
- 主要语言：Python
- 指标：⭐ 5 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/xiaozhenliu/micro-eval)

> 分析基于 2026-08-06 抓取的 README、examples/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个小团队的 Agent/Skill 评测工具。把"感觉这个 Agent 更好"变成可复现对比：相同任务、相同起点、相同证据链，并对基线/候选谁更强、更弱、无结论或不可比给出有边界的判断。
- **能拿来干什么**：Agent/Skill 效果对比、选型决策。
- **适合谁**：小团队、Agent 评测者。
- **快速判断**：如果你要"用证据而不是感觉选 Agent"，它很对口；否则不需要。

## 分类

- 主分类：5. 评测 / Benchmark 工具
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "A local-first Agent / Skill evaluation assistant for small AI teams that need evidence, not vibes"。

## 项目方向与定位

本地优先评测：tasks × configs × reps 矩阵、沙箱隔离、证据链、guarded decision（强/弱/无结论/不可比）。

## 主要功能（能做什么）

- 可复现对比评测
- 证据链与有边界结论
- eval.yaml 配置、examples

## 架构设计

```text
examples/ docs/ eval.yaml.example
```

## 实现思路与核心逻辑

- "同任务同起点同证据链"：控制变量
- 保守结论：不硬分高下

## 亮点

- 5 stars，评测方法论严谨
- 与帖子"评测"类别直接相关
- Apache-2.0

## 局限与风险（可选）

- 生态较新
- 评测质量依赖任务设计

## 分析说明

基于 README、examples/ 与文档；未运行评测。

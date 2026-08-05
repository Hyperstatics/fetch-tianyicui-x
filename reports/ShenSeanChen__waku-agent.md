# ShenSeanChen/waku-agent 分析报告

- 仓库：[ShenSeanChen/waku-agent](https://github.com/ShenSeanChen/waku-agent)
- 方向：教学向本地 AI 助手（Harness · Loop · Memory · Eval 四支柱）
- 主要语言：Python
- 指标：⭐ 895 · License MIT · 最近推送 2026-08-03
- 主页/文档：[seanchen.io](https://seanchen.io) · [20 分钟代码讲解](https://www.youtube.com/watch?v=rvRyBhILrls)

> 分析基于 2026-08-06 抓取的 README、skills/ 结构与架构文档。

## 这是什么（非技术版）

- **这是什么**：一个"一个下午能读完的 AI 助手"。作者把真正 Agent 的四个支柱（运行框架、主循环、记忆、评测）用约 95 行主循环和少量文件讲清楚，本机 SQLite 记忆、仪表盘可视化、内置评测。
- **能拿来干什么**：学习 Agent 原理、搭建个人本地助手、作为教学/研究参考。
- **适合谁**：想"看懂 Agent 内部"的开发者、教育者、研究者。
- **快速判断**：如果你想从零理解 Agent 是怎么运转的，它是极佳教材；如果要生产级 Agent，功能不够。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（教学向轻量实现）
- 副分类：4. 记忆 / 上下文 / 知识管理（SQLite 记忆支柱）
- 理由：README 自述 "shows the four pillars behind every serious agent: Harness · Loop · Memory · Eval/LLM-Ops"。

## 项目方向与定位

"Your own AI assistant. On your laptop. In code you can read in an afternoon."——以可读性为核心的本地 Agent：主循环约 95 行纯 Python；记忆分语义/情节/程序三型并有记忆门控；本地仪表盘实时展示消息流；eval（确定性测试 + LLM 裁判）内置并作为发布门禁。

## 主要功能（能做什么）

- Harness：消息/工具/运行框架（架构白板逐文件对应代码）
- Loop：约 95 行主循环，逐步可读
- Memory：SQLite 单一文件，语义/情节/程序三型 + 记忆门控
- Eval：确定性测试 + LLM-as-judge，发布门禁
- 本地仪表盘（watch it think）、Telegram 网关

## 架构设计

```text
skills/        技能
evals/ examples/  评测与示例
docs/ architecture-whiteboard  架构文档
pi-pokedex/    示例应用
```

## 实现思路与核心逻辑

- 教学优先：每个架构盒子映射到具体文件，代码即文档
- 记忆分层 + 门控：决定"要不要记"和"记什么"
- 评测内建：把质量把关做成 Agent 的发布门禁

## 亮点

- "可读性"为核心卖点，非常适合 Agent 教学
- 四支柱完整（Harness/Loop/Memory/Eval），小而全
- 作者提供 20 分钟视频走读，学习闭环好

## 局限与风险（可选）

- 定位教学/原型，非生产级
- 与"内测 Harness"主题相关度中等（是学习型实现）

## 分析说明

基于 README、skills/ 与架构文档；未运行。

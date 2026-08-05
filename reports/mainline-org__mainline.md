# mainline-org/mainline 分析报告

- 仓库：[mainline-org/mainline](https://github.com/mainline-org/mainline)
- 方向：Git for the AI era——把开发者意图与决策保存到 Git
- 主要语言：Go
- 指标：⭐ 181 · License 分层（Apache-2.0 / CC-BY-4.0 / Commercial）· 最近推送 2026-08-03
- 主页/文档：[mainline.sh](https://mainline.sh) · [reference](https://github.com/mainline-org/mainline/blob/main/docs/reference.md)

> 分析基于 2026-08-06 抓取的 README、docs/ 与 LICENSE。注意：分层许可证（Apache-2.0 + CC-BY-4.0 + Commercial），使用前需确认适用条款。

## 这是什么（非技术版）

- **这是什么**：一个"AI 时代的版本控制"。Git 记录代码历史，Mainline 额外把 AI 干活背后的工程判断（原始目标、推理路径、关键决策、取舍、验证、约束、放弃的路线、最终提交）也存进同一个协作层。
- **能拿来干什么**：让 Agent 的工作意图/决策可追溯、可审查；团队协作更透明。
- **适合谁**：开发者、需要审计 AI 产出的团队。
- **快速判断**：如果你想"知道 AI 为什么这么改"，它很有价值；否则普通 Git 即可。

## 分类

- 主分类：6. 特定领域 / 其他（版本控制/协作工具）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 工作记录）
- 理由：README 自述 "Git for the AI era... Mainline lets agents save developer intent and decisions to Git alongside the code"。

## 项目方向与定位

把工程判断层加入 Git：原始目标、推理路径、关键决策、权衡、验证、显式约束、放弃路线、承载提交。Hosted Hub 托管 + CLI，Go 实现。

## 主要功能（能做什么）

- 记录 Agent 的意图与决策到 Git
- 目标/推理/决策/约束/验证/放弃路线结构化保存
- CLI（install.sh）+ Hosted Hub

## 架构设计

```text
docs/reference.md   详细参考
（Go CLI + Hub 服务）
```

## 实现思路与核心逻辑

- "代码历史 + 判断历史"双记录：补齐 AI 协作中丢失的"为什么"
- 与 Git 同层协作，不替代 Git

## 亮点

- 181 stars，概念新颖（AI 时代的版本控制）
- 解决"AI 产出不可审查"痛点
- 分层许可明确开源/商用边界

## 局限与风险（可选）

- 生态早期，采用面待验证
- 分层许可证使用需仔细确认
- 与"Agent Harness 内测"主题相关度中等

## 分析说明

基于 README、docs/ 与 LICENSE；未运行 CLI。

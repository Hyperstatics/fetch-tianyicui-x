# xlang-ai/OpenCUA 分析报告

- 仓库：[xlang-ai/OpenCUA](https://github.com/xlang-ai/OpenCUA)
- 方向：计算机使用 Agent（Computer-Use Agent）的开放基础：模型 + 数据集 + 工具
- 主要语言：Python
- 指标：⭐ 809 · License MIT · 最近推送 2026-08-03
- 主页/文档：[opencua.xlang.ai](https://opencua.xlang.ai) · [论文 arXiv 2508.09123](https://arxiv.org/abs/2508.09123)

> 分析基于 2026-08-06 抓取的 README、model/data/tool 结构与论文信息。

## 这是什么（非技术版）

- **这是什么**：一个"教 AI 用电脑"的开源项目。发布了一系列视觉语言模型（OpenCUA-7B/32B/72B）、训练数据集（AgentNet）和工具，让 AI 能像人一样看屏幕、操作界面完成任务。
- **能拿来干什么**：研究/构建"会看屏幕操作电脑"的 Agent；微调/部署 CUA 模型；浏览真实人机交互轨迹数据。
- **适合谁**：AI 研究者、Agent 开发者、多模态团队。
- **快速判断**：如果你要做"计算机使用 Agent"（屏幕理解+操作），它是重要参考；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（计算机使用 Agent 基础研究）
- 副分类：1. 通用 Agent Runtime / Harness（Agent 模型/工具层）
- 理由：README 自述 "Open Foundations for Computer-Use Agents"，含模型/数据集/工具三件套。

## 项目方向与定位

为 Computer-Use Agent 提供开放基础：OpenCUA 系列模型（7B/32B/72B）、AgentNet 数据集（真实人机交互轨迹）与工具（evaluation/tool）。vLLM 已官方支持，接入主流推理栈。

## 主要功能（能做什么）

- OpenCUA-7B/32B/72B 模型（HuggingFace 发布，vLLM 支持）
- AgentNet 数据集与在线 Data Viewer
- 评估（evaluation/）与可视化工具（data/vis/）
- 模型 serve 指南（model/README.md）

## 架构设计

```text
model/      模型权重与推理
data/       数据集与可视化
tool/       工具
evaluation/ 评测
```

## 实现思路与核心逻辑

- 研究先行：论文 + 开源权重 + 数据集三件套，支持复现
- 生态协作：与 vLLM 社区（美团 EvoCUA）合作打通推理
- 面向"屏幕智能"：模型以视觉输入 + 界面操作输出为核心

## 亮点

- 计算机使用 Agent 领域的开放基础项目，学术价值高（arXiv/数据集/权重齐全）
- 多规格模型（7B–72B）覆盖端侧到云端
- MIT 开源，vLLM 官方支持

## 局限与风险（可选）

- 偏研究/基础设施，需要较强技术背景使用
- 与"Agent Harness 内测"主题相关度中等（偏模型层）

## 分析说明

基于 README、目录结构与论文信息；未运行模型。

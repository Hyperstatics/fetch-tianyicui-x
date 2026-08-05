# Octo-o-o-o/deepseek-harness-applicants 分析报告

- 仓库：[Octo-o-o-o/deepseek-harness-applicants](https://github.com/Octo-o-o-o/deepseek-harness-applicants)
- 方向：DeepSeek Harness 内测报名者档案库（社区非官方）
- 主要语言：JavaScript/Node（数据管道）
- 指标：⭐ 15 · License MIT · 最近推送 2026-08-03
- 主页/文档：[在线展示站](https://deepseek-harness-applicants.octoooo.com/)

> 分析基于 2026-08-06 抓取的 README、data/、scripts/、docs/ 与 CI 配置。统计快照：2026-08-05。

## 这是什么（非技术版）

- **这是什么**：一个"内测报名活动档案库"。把 X 帖子里 DeepSeek Harness 内测报名的公开回复整理成结构化档案：769 位开发者、704 个仓库，含排行榜、赛道索引、生态分析，还有机器可读 JSON/CSV 和在线展示站。
- **能拿来干什么**：按 star/赛道找项目和开发者；研究者直接取数据。
- **适合谁**：Harness 生态开发者、研究者、报名者本人。
- **快速判断**：如果你想看"谁报名了、做了什么"，它是最全的非官方档案；与本仓库的数据整理工作直接同源。

## 分类

- 主分类：6. 特定领域 / 其他（社区数据档案）
- 副分类：5. 评测 / Benchmark 工具（GitHub 指标快照）
- 理由：README 自述"社区维护的非官方档案……把整场活动整理成一个可检索、可审计、可复现的结构化档案"。

## 项目方向与定位

开发者为中心的数据工程：X 身份 → GitHub 身份 → 代表项目；项目是证据而非主实体；保留不确定性（unlinked/unresolved）；快照口径明确。

## 主要功能（能做什么）

- 769 开发者档案、704 仓库指标快照（Stars/上线/更新/语言）
- 总榜 Top40 + 18 赛道 Top10、赛道索引、生态分析报告
- 机器可读 data/applicants.json + exports/*.csv
- 在线静态站（排行榜/检索/生态分析）
- CI 一致性校验 + 回归测试

## 架构设计

```text
data/          权威数据集（applicants.json/projects.json）
developers/    每人一页 Markdown
raw-data/      X replies 与 GitHub 快照
scripts/       build/enrich/offline/finalize 管道
docs/analysis/ 排行榜/赛道/生态分析
site/ showcase/ 静态站（同源）
```

## 实现思路与核心逻辑

- 开发者为中心建模：项目挂在开发者下，owner 不自动视为报名者
- 保留不确定性：unlinked/unresolved 显式留档而非猜测
- 快照口径：所有指标标注时点，README 明确"以 JSON 的 normalized_counts 为准"
- GitHub 指标 enrich：gh REST 批量快照（718 行正常/8 行 404）

## 亮点

- 与本项目（fetch-tianyicui-x）数据同源同主题，互为印证
- 数据可审计、可复现（CI 校验 + schema + 方法论）
- 规模与结构化完整（1081 回复 → 769 开发者 → 726 项目行）
- 双端输出（Markdown 档案 + 在线展示站）

## 局限与风险（可选）

- 快照非实时；高 star 不等于高相关（README 有异常清单）
- 非官方档案，不能作为内测结果依据

## 分析说明

基于 README、data/scripts/docs 结构与 CI 配置；未逐份核对 769 份档案。

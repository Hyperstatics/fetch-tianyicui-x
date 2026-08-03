# 项目 Backlog（待办清单）

记录仓库分析过程中的待办事项与后续处理计划。条目按优先级排序，完成一项勾选一项。

## 1. 许可证合规盘点（优先级：高）

**背景**：部分仓库使用非宽松/自定义许可证，报告已逐条标注，但还没有统一清单与使用边界说明。

- 已标注的非宽松许可项目：
  - [YaoApp/yao](../reports/YaoApp__yao.md) — 修改版 Apache-2.0，商用需商业许可
  - [op7418/CodePilot](../reports/op7418__CodePilot.md) — BSL-1.1（Business Source License）
  - [KunAgent/Kun](../reports/KunAgent__Kun.md) — PolyForm Noncommercial 1.0.0（仅非商用）
- [ ] 后续批次继续在报告中标注非标准许可证（含 `NOASSERTION` 仓库逐个核对 LICENSE 文件）
- [ ] 全部批次完成后，生成 `reports/LICENSE-notes.csv` 合规清单（仓库、许可证、商用限制、备注）
- [ ] 在 README 增加「许可证使用边界」说明：本项目仅整理公开链接与元数据；引用/演示/内测展示相关项目时需自行评估授权

## 2. 404 仓库跟进（优先级：中）

全量扫描时 2 个仓库返回 HTTP 404（记录在 `reports/failures.txt`）：

- `agentdev88/agent-harness-core`
- `zhuangbiaowei/smart_expert`

- [ ] 用 GitHub 搜索确认是否改名 / 迁移 / 有镜像
- [ ] 若找到替代地址，更新 `project_urls.txt` 与 `projects.csv` 后重跑提取脚本
- [ ] 若确认已删除，在报告中标注「已失效」并从待分析队列移除

## 3. 大仓库 / API-only 仓库深读（优先级：中）

以下仓库因体积过大，首轮采用 API-only 分析（元数据 + README + 目录树），缺少源码级细节：

- `nexu-io/open-design`（约 1.7GB）
- `QwenLM/qwen-code`（约 628MB）
- `web-infra-dev/midscene`（约 497MB）

- [ ] 按需对关键仓库做增量克隆（`--filter=blob:none` 或 sparse checkout），补充架构与实现细节
- [ ] 报告中「分析说明」标注的 API-only 结论在补充后更新

## 4. 链接有效性定期复查（优先级：低）

- 2026-08-04 全量扫描：262/264 可达，2 个 404（见第 2 项）
- [ ] 制定复查节奏（建议每月一次），将新发现的 404/改名追加到 `reports/failures.txt`
- [ ] 复查后同步更新 `projects.csv` / `project_urls.txt` / 相关报告

## 5. 数据与报告刷新（优先级：中）

报告与 `reports/SUMMARY.csv` 基于 2026-08-04 抓取快照，star 数与推送时间会过期。

- [ ] 在 skill 中增加「刷新」说明或脚本：`fetch_repo.py --force` 重抓元数据 + 重生成 SUMMARY 行
- [ ] 报告头部标注快照时间，刷新时同步更新

## 6. 报告索引与分类汇总（优先级：低）

`reports/SUMMARY.csv` 已含分类列，但缺少面向读者的浏览索引。

- [ ] 基于 SUMMARY.csv 生成 `reports/INDEX.md`：按六类分类 + 按 stars 排序 + 许可证/相关度标注
- [ ] 在 README 增加 reports 索引入口

## 7. 批量分析进度（进行中）

- 已完成：21 / 264（按 stars 从高到低，每批 10 个，已提交）
- [ ] 继续剩余 243 个仓库的批量分析
- [ ] 每批完成后更新本节进度数字与 `reports/SUMMARY.csv`

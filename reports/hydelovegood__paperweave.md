# hydelovegood/paperweave 分析报告

- 仓库：[hydelovegood/paperweave](https://github.com/hydelovegood/paperweave)
- 方向：本地论文工作流工具（PDF→结构化研究库）
- 主要语言：Python
- 指标：⭐ 8 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/hydelovegood/paperweave)

> 分析基于 2026-08-06 抓取的 README、configs/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"论文整理助手"。把一批 PDF 论文变成可持续更新的研究库：正文结构、结构化摘要、深度问答、引用关系、Markdown 导出。
- **能拿来干什么**：文献管理、论文阅读与问答、引用追踪。
- **适合谁**：研究者、学生。
- **快速判断**：如果你常读论文且想本地整理，它很实用；否则 Zotero 等更成熟。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（研究库）
- 副分类：6. 特定领域 / 其他
- 理由：README 自述 "Local-first CLI for turning PDF papers into a structured research library with parsing, summaries, Q&A, citation tracking, and Markdown exports"。

## 项目方向与定位

本地优先论文工作流：PDF 导入（SHA256 去重）、DeepXiv/PyMuPDF 解析、结构化摘要 + reviewer/interview/defense QA、forward citations 追踪、Markdown 导出。

## 主要功能（能做什么）

- PDF 批量导入与去重
- 论文解析、结构化摘要、QA
- 引用追踪（forward citations、DOI/OA 链接）
- Markdown 导出

## 架构设计

```text
configs/ pyproject.toml
```

## 实现思路与核心逻辑

- 研究资产化：把论文变成可持续更新的库
- 多风格 QA（reviewer/interview/defense）

## 亮点

- 8 stars，研究垂直工具
- MIT 开源、本地优先

## 局限与风险（可选）

- 与"内测 Harness"主题相关度低
- 生态较新

## 分析说明

基于 README、configs/ 与文档；未运行。

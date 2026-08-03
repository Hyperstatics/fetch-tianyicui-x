# 仓库分类与非技术版说明

## 分类体系（六类，主分类 + 可选副分类）

| 类别 | 通俗说法 | 判断信号（README/描述/源码特征） |
| --- | --- | --- |
| 1. 通用 Agent Runtime / Harness / 桌面客户端 | 能自己跑 Agent 的"主机/外壳"：给 AI 一个可以调工具、带记忆、切模型的工作环境 | desktop/TUI/CLI、本地优先、multi-model、MCP、Skills、workspace、harness/runtime/kernel、agent 客户端 |
| 2. Coding Harness / 工程向 Agent | 专门帮写代码的 AI 工程师，强调质量检查、隔离、长任务 | coding agent、代码生成/重构、SWE benchmark、质量门/验证、repo 操作、Claude Code / Codex / Gemini CLI 衍生 |
| 3. 多 Agent 编排 / 协作系统 | 让多个 AI 分工协作的"调度中心" | multi-agent、orchestrator、DAG、parallel、team、planner、coordinator、sub-agent |
| 4. 记忆 / 上下文 / 知识管理 | 给 AI 装"长期记忆/笔记本" | memory、knowledge graph、RAG、context、semantic search、provenance、持久化会话 |
| 5. 评测 / Benchmark 工具 | 给 AI/Agent 打分的"考试系统" | eval、benchmark、metrics、Pass@k、沙箱评测、正确性 vs token/延迟 |
| 6. 特定领域 / 其他 | 某个具体场景的工具（浏览器、设计、版本控制、工作流等） | 明确的领域关键词，不属于上述任何一类 |

判断要点：

- 每类都要有证据（README 原话、package 描述、源码特征），报告里写一行理由即可
- 允许副分类，但报告只写 1 个主分类 + 最多 1 个副分类，避免含糊
- 不确定时归入 6，并在报告里说明为什么

## 非技术版说明怎么写（放在报告最前）

目标读者：不太懂技术的人。控制在 4–6 行，避免 API/框架名词（出现就一句白话解释），用生活化类比。

固定四要素：

1. **这是什么**：一句话定义 + 一个生活化类比（例如：模型是"承包商"，Harness 是"工地监理"）
2. **能拿来干什么**：用使用场景描述，不用功能清单（"帮你在电脑上自动写代码并检查" 而不是 "支持 SWE-bench"）
3. **适合谁**：开发者 / 非开发者 / 团队 / 研究者 / 普通用户，分别说明
4. **快速判断我需不需要**：给 1–2 个"如果你要 X 就用它；如果你只是 Y 就不需要"的判断句

示例（不限定措辞）：

> 这是一个给 AI 当"管家"的程序：AI 负责出主意，它负责检查预算、权限和验收标准，全部合格才交付结果。适合对 AI 干活过程的安全性、可追溯性有要求的人；如果你只是想快速聊聊天，就不需要它。

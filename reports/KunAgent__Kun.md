# KunAgent/Kun 分析报告

- 仓库：[KunAgent/Kun](https://github.com/KunAgent/Kun)
- 方向：本地优先 AI Agent 工作台（桌面 GUI + 终端 TUI 共享运行时）
- 主要语言：TypeScript（Electron）
- 指标：⭐ 5,635 · License PolyForm Noncommercial 1.0.0（非商用）· 最近推送 2026-08-03
- 主页/文档：[kun-agent.com/docs](https://www.kun-agent.com/docs)

> 分析基于 2026-08-04 抓取的 README、DESIGN.md 与目录结构。**许可证为 PolyForm Noncommercial 1.0.0**：仅限非商用使用，商用/托管需单独书面许可。

## 这是什么（非技术版）

- **这是什么**：一个"AI 全能工作台"。写代码、写作、设计、研究、自动化都放一个地方，桌面界面和终端界面共用同一个运行时，任务从澄清需求到交付成果全程可见。
- **能拿来干什么**：把想法推进到可验收的成果；处理复杂多阶段任务（Agent Graph 模式）；桌面/终端/手机多端接力。
- **适合谁**：开发者、内容创作者、需要"任务全程可控可回溯"的人。
- **快速判断**：如果你想要"一个工作台串起所有 AI 工作流"且用途非商业，它很适合；商业用途需先谈许可。

## 分类

- 主分类：1. 通用 Agent 桌面 / 客户端 / Runtime
- 副分类：3. 多 Agent 编排 / 协作系统（Agent Graph 复杂任务）
- 理由：README 自述"本地优先的 AI Agent 工作台（GUI + TUI）"，一个共享运行时连接多端。

## 项目方向与定位

"不是另一个只会生成回答的聊天框"：Kun 把需求、上下文、计划、文件改动、测试、审查与最终交付放进一条连续工作流。桌面 GUI、终端 TUI、后台任务与手机连接共用 `kun serve` 运行时（线程、计划、审批、模型连接、任务记录共享）。

## 主要功能（能做什么）

- Code / Write / Design / Research / Automation 五类场景
- Agent Graph：处理复杂多阶段任务
- GUI + TUI 双端共享运行时；手机连接
- 计划、审批、任务记录统一管理；多语言（中文/英文）文档

## 架构设计

```text
kun/ src/      核心实现
electron.vite.config.ts / electron-builder.config.cjs   桌面构建
DESIGN.md / DESIGN_MODE_PLAN.md / openspec  设计与规格
examples/ docs/
```

## 实现思路与核心逻辑

- 共享运行时模型：`kun serve` 一个进程服务所有端（GUI/TUI/后台/手机），避免多端状态分裂
- 工作流线性化：从澄清 → 创作 → 执行 → 审查 → 交付全程可回溯
- 以"可验收结果"为终点，而非对话

## 亮点

- 5.6k stars，与帖子"本地优先 Agent 工作台"类别直接相关
- GUI+TUI 共享运行时是工程亮点
- 中文社区活跃、设计文档完善

## 局限与风险（可选）

- **PolyForm Noncommercial 许可证**：非商用授权，商用/集成需联系版权方
- 仓库 260MB 较大；功能多，上手成本不低

## 分析说明

基于 README、DESIGN 文档与目录结构；未运行客户端。

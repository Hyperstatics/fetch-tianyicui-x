# YaoApp/yao 分析报告

- 仓库：[YaoApp/yao](https://github.com/YaoApp/yao)
- 方向：单二进制的"AI 时代应用运行时"——构建 AI Agent 与 Web 应用
- 主要语言：Go
- 指标：⭐ 7,557 · License 修改版 Apache-2.0（商用需商业许可）· 最近推送 2026-08-03
- 主页/文档：[yaoagents.com](https://yaoagents.com)

> 分析基于 2026-08-04 抓取的 README、目录结构与 LICENSE。注意：Yao 使用**修改版 Apache-2.0**，商用需取得商业许可。

## 这是什么（非技术版）

- **这是什么**：一个"AI 应用底盘"。它用单个程序就能同时承载 AI 智能体和网页应用，你定义规则（边界），AI 在里面干活，行为不会越界。
- **能拿来干什么**：快速搭建带 AI 能力的应用/助手/自动化流程；支持纯对话、容器内跑编码 Agent、或纯代码逻辑三种模式，可混用。
- **适合谁**：开发者、想自建 AI 应用的团队、需要"给 AI 画好边界"的人。
- **快速判断**：如果你要自己搭 AI 应用且喜欢"一个文件搞定"，它很适合；如果只是用现成聊天工具，不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（应用运行时）
- 副分类：2. Coding Harness / 工程向 Agent（支持 CLI Agent 容器执行）
- 理由：README 自述 "open-source runtime for building AI agents and web applications — shipped as a single binary"。

## 项目方向与定位

核心理念："cage, not an animal"——AI 是动物，运行时是笼子；行为由笼子（Hook/边界）决定。Yao 提供统一管道（Create Hook → Executor → Next Hook），三种执行模式（LLM 对话、容器内 CLI Agent、纯 Hook 代码）共享同一接口，可自由混用路由。

## 主要功能（能做什么）

- 三种执行模式：LLM（OpenAI/Anthropic 等）、CLI Agent（容器内 OpenCode/Claude Code/Codex，含沙箱隔离与 SKILL 生态）、纯 Hook（确定性 TS 逻辑）
- Create Hook：执行前注入上下文、强制约束、路由请求；Next Hook：校验输出、触发下游、驱动多步循环
- Agent Framework、Yao Desktop、DSL 驱动
- 模块完备：agent/aigc/api/connector/event/flow/engine 等

## 架构设计

```text
cmd/      入口
agent/    智能体框架
aigc/     生成式能力
dsl/      DSL 定义
engine/   核心引擎
flow/     流程编排
connector/ connector/event/crypto/attachment/audit/api 等横切模块
docker/ docs/ commercial/
```

## 实现思路与核心逻辑

- 单一二进制分发，降低部署复杂度
- Hook 管道是核心抽象：所有请求都过同一管道，约束/路由/校验集中在边界
- "AI 做重活、你定边界"：通过 Hook 在模型前后注入逻辑，兼顾灵活与可控

## 亮点

- 7.5k stars，Go 单二进制运行时，部署轻量
- 三种 executor 混用是差异化设计（对话/编码 Agent/纯代码统一接口）
- 中文文档完善，生态定位清晰（AI 应用运行时）

## 局限与风险（可选）

- **许可证注意**：修改版 Apache-2.0，商用需从厂商获取商业许可
- 概念（Hook/管道）有学习曲线；社区规模小于主流 Agent 框架
- 与"内测 Harness"主题相关度中等（偏应用运行时）

## 分析说明

基于 README、目录结构与 LICENSE 文件；未运行二进制，未细读 engine 源码。

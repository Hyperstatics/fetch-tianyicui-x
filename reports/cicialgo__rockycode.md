# cicialgo/rockycode 分析报告

- 仓库：[cicialgo/rockycode](https://github.com/cicialgo/rockycode)
- 方向：为 DeepSeek V4 系列构建的 coding agent 引擎
- 主要语言：Python
- 指标：⭐ 21 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/cicialgo/rockycode)

> 分析基于 2026-08-06 抓取的 README、bench/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"能对话的编码 Agent 引擎"，专为 DeepSeek V4 系列优化：独特研究模式、SWE-bench 验证（79.8% V4-flash）、自进化特性开发中。
- **能拿来干什么**：日常 AI 编程、研究模式深度任务。
- **适合谁**：DeepSeek 用户、开发者。
- **快速判断**：如果你用 DeepSeek V4 且想要性能验证过的 Agent，它值得试；否则其他 Agent 也行。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：5. 评测 / Benchmark 工具（SWE-bench 验证）
- 理由：README 自述 "A coding agent engine you can talk to, built for the DeepSeek V4 series, with a unique research mode, bench-tested"。

## 项目方向与定位

DeepSeek V4 优化：research mode、bench 验证（SWE-bench 79.8%、V4-pro 81.8% pass@3）、自进化开发中；Docker 沙箱。

## 主要功能（能做什么）

- 编码 Agent 引擎（对话式）
- research mode
- SWE-bench 基准验证
- Docker/sandbox 部署

## 架构设计

```text
bench/ brand/
Dockerfile / Dockerfile.sandbox / docker-compose.yml
```

## 实现思路与核心逻辑

- 面向 DeepSeek 生态调优 + 基准数据背书
- 沙箱化执行

## 亮点

- 21 stars，DeepSeek 优化定位
- benchmark 数字透明
- MIT 开源

## 局限与风险（可选）

- 依赖 DeepSeek V4 生态
- 项目较新

## 分析说明

基于 README、bench/ 与文档；未运行 benchmark。

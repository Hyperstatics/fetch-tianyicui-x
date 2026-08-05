# yologdev/yoyo-evolve 分析报告

- 仓库：[yologdev/yoyo-evolve](https://github.com/yologdev/yoyo-evolve)
- 方向：会自我进化的终端 Coding Agent（Zero human code）
- 主要语言：Rust
- 指标：⭐ 1,852 · License MIT · 最近推送 2026-08-03
- 主页/文档：[yoyo.yolog.dev](https://yoyo.yolog.dev) · [进化日志](https://yologdev.github.io/yoyo-evolve/)

> 分析基于 2026-08-04 抓取的 README、Cargo.toml 与自进化机制文档。

## 这是什么（非技术版）

- **这是什么**：一个"会自己改自己代码"的 AI 编程助手。它每隔几小时读一遍自己的源码，决定改进什么、自己实现、跑测试、提交代码——作者说 128 天后它从 200 行长到了 11.5 万行、4300 多个测试。
- **能拿来干什么**：日常终端 AI 编程（多文件修改、跑测试、git）；观察"自我进化 Agent"这一实验。
- **适合谁**：开发者、AI Agent 研究者、对"自进化"感兴趣的人。
- **快速判断**：如果你想体验"没有人类代码的自我进化 Agent"，它很有话题性；如果只是想要稳定编程助手，它有实验性质。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness（自进化运行时）
- 理由：README 自述 "A Coding Agent That Evolves Itself... reads its own source, picks what to improve, implements it, runs tests, and commits"。

## 项目方向与定位

"200 lines of Rust. Zero human code. One rule: evolve or die."——以自我进化为核心理念的终端编码 Agent：自己决定改进方向、自己实现、自己验证、自己提交。同时也是一个功能完整的终端 Agent（多文件编辑、测试、git、90+ 斜杠命令的 streaming REPL）。

## 主要功能（能做什么）

- 自进化循环：读源码 → 选改进 → 实现 → 测试 → 提交（crates.io: yoyo-agent）
- 终端 Coding Agent：多文件编辑、跑测试、git 管理、项目上下文理解、失败恢复
- Streaming REPL 与 90+ 斜杠命令
- 进化日志（journal）、GASP、文档站

## 架构设计

```text
src（Cargo.toml，build.rs）  Rust 实现
journals/ DAY_COUNT .yoyo  自进化状态与日志
docs/ dreams/               文档与"梦想"规划
install.sh / install.ps1    安装
```

## 实现思路与核心逻辑

- 自进化闭环：Agent 的改进动作本身就是 Agent 的任务（读自己源码 → 计划 → 实现 → 验证 → 提交）
- 规则极简（evolve or die），以持续运行驱动演化
- 以 Rust 为宿主语言，保证性能与可测试性

## 亮点

- 1.9k stars，"自我进化"实验极具话题性，GitHub 增长快
- 数据透明（115k 行 / 4,300+ 测试 / 128 天全程记录）
- MIT 开源，完全开放可复现

## 局限与风险（可选）

- 自进化存在失控/质量风险，属于实验性质
- 依赖持续运行的自动化环境（CI evolution workflow）
- 与"Agent Harness 内测"主题相关度中等（是 Agent 本体而非通用 harness）

## 分析说明

基于 README、Cargo.toml 与文档；未运行自进化循环。

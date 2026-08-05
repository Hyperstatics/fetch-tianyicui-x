# compio-rs/compio 分析报告

- 仓库：[compio-rs/compio](https://github.com/compio-rs/compio)
- 方向：thread-per-core 的 Rust 异步运行时（IOCP/io_uring/polling）
- 主要语言：Rust
- 指标：⭐ 1,823 · License MIT · 最近推送 2026-08-03
- 主页/文档：[compio.rs](https://compio.rs)

> 分析基于 2026-08-04 抓取的 README、compio-* 子 crate 结构。

## 这是什么（非技术版）

- **这是什么**：一个"高性能 Rust 异步引擎"。让 Rust 程序高效处理文件/网络/QUIC/信号等 I/O，受字节 monoio 启发，在 Windows/Linux/macOS 上分别用 IOCP/io_uring/polling 加速。
- **能拿来干什么**：构建高性能网络服务、文件系统密集应用、异步运行时研究。
- **适合谁**：Rust 开发者、系统/网络工程师。
- **快速判断**：如果你的 Rust 服务需要极致 I/O 性能，它值得评估；如果只用标准异步运行时，不是必须。

## 分类

- 主分类：6. 特定领域 / 其他（基础库/运行时）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 基础设施的底层依赖）
- 理由：README 自述 "A thread-per-core Rust runtime with IOCP/io_uring/polling inspired by monoio"。

## 项目方向与定位

thread-per-core 异步运行时，直接对标 monoio/tokio 系列的高性能路线：每个核心一个线程、任务不跨线程迁移，配合 IOCP（Windows）/io_uring（Linux）/polling 获得低延迟高吞吐。模块化：compio-fs/net/quic/process/signal/runtime/executor 等全套。

## 主要功能（能做什么）

- 异步文件与网络 I/O、QUIC、进程、信号
- thread-per-core 调度；`#[compio::main]` 宏快速上手
- 兼容层（compio-compat）、日志/宏/驱动等配套 crate
- crates.io 分发、CI 检查与测试齐全

## 架构设计

```text
compio/           核心运行时
compio-buf/ fs/ io/ net/ process/ quic/ signal/ 功能模块
compio-driver/    平台驱动（IOCP/io_uring/polling）
compio-executor/ runtime/ dispatcher/  调度层
compio-macros/ compio-log/ compio-compat/
```

## 实现思路与核心逻辑

- thread-per-core 模型：每个线程独立调度器，避免任务迁移与锁竞争
- 平台抽象：同一套 API，不同内核后端（IOCP/io_uring/polling）
- 模块化设计：按需启用 fs/net/quic 等特性

## 亮点

- 1.8k stars，Rust 异步运行时生态的活跃参与者
- 跨平台高性能路线（io_uring 等）技术含量高
- 模块化完整，MIT 宽松许可

## 局限与风险（可选）

- 相比 tokio/monoio，生态与生产验证尚在早期
- 与"Agent Harness 内测"主题无关（基础库）

## 分析说明

基于 README 与 crate 结构；未运行 benchmark。

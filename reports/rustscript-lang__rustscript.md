# rustscript-lang/rustscript 分析报告

- 仓库：[rustscript-lang/rustscript](https://github.com/rustscript-lang/rustscript)
- 方向：编译型脚本语言 + 运行时（pd-vm 栈式 VM）
- 主要语言：Rust
- 指标：⭐ 18 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[rustscript.org](https://rustscript.org/docs/)

> 分析基于 2026-08-06 抓取的 README、crates/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"用 Rust 写的脚本语言"。围绕 pd-vm 栈式虚拟机：编译器工具链、标准库、字节码/AOT、WebAssembly 运行时支持、调试器运行时契约。
- **能拿来干什么**：脚本语言研究与工具链开发。
- **适合谁**：语言实现者、Rust 开发者。
- **快速判断**：如果你做语言/VM 方向，它值得研究；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（语言/VM 基础设施）
- 副分类：无
- 理由：README 自述 "a compiled scripting language and runtime built around pd-vm"。

## 项目方向与定位

脚本语言 RustScript + RSS 语言 + pd-vm：VM、编译器、标准库、字节码/AOT、WASM、调试契约。

## 主要功能（能做什么）

- RustScript/RSS 语言与编译器
- pd-vm 栈式 VM、字节码/AOT
- WebAssembly 运行时支持
- 调试器运行时契约

## 架构设计

```text
crates/ pd-vm-nostd/ pd-host-function/
editor-assets/ examples/ docs/
```

## 实现思路与核心逻辑

- VM 中心设计：语言、编译、运行时围绕 pd-vm
- nostd 支持：嵌入式场景

## 亮点

- 18 stars，Rust 脚本语言生态
- 文档站完整
- Apache-2.0

## 局限与风险（可选）

- **与 Agent Harness 完全无关**
- 生态小众

## 分析说明

基于 README、crates/ 与文档；未运行。

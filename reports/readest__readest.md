# readest/readest 分析报告

- 仓库：[readest/readest](https://github.com/readest/readest)
- 方向：开源跨平台电子书阅读器（Foliate 的现代重写）
- 主要语言：TypeScript（+ Rust/Tauri）
- 指标：⭐ 23,050 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[readest.com](https://readest.com)

> 分析基于 2026-08-04 抓取的 README、apps/packages 目录结构。

## 这是什么（非技术版）

- **这是什么**：一个开源电子书阅读器，像"带 AI 的 Kindle"。支持多种电子书格式，能划线批注、查词典、全文搜索，Windows/Mac/Linux/手机/网页都能用。
- **能拿来干什么**：沉浸式读书、管理书库、做笔记批注。
- **适合谁**：爱读书的人、想摆脱商业阅读器生态的读者、开发者。
- **快速判断**：如果你需要一款跨平台、无广告、开源的阅读器，它就是；如果只想随便看两页，用手机自带阅读器也行。

## 分类

- 主分类：6. 特定领域 / 其他（电子书阅读器应用）
- 副分类：无
- 理由：README 自述 "open-source ebook reader designed for immersive and deep reading experiences"。

## 项目方向与定位

用现代技术栈重写经典阅读器 Foliate：Next.js 16 + Tauri v2，覆盖 macOS/Windows/Linux/Android/iOS/Web。定位是沉浸式深度阅读的开源跨平台工具。

## 主要功能（能做什么）

- 多格式支持：EPUB、PDF、MOBI、KF8(AZW3)、FB2、CBZ、TXT、MD
- 滚动/翻页两种阅读模式、全文搜索（单本/书库）
- 批注、高亮、书签、笔记、即时模式
- 词典 / Wikipedia 查询、多语言界面
- 多平台 + Web 版 + Calibre/KOReader 生态插件

## 架构设计

```text
apps/
  readest-app          主应用（Tauri + Next.js）
  readest-calibre-plugin
  readest.koplugin     KOReader 插件
packages/
  foliate-js           阅读渲染引擎（Foliate 核心）
  js-mdict             MDict 词典支持
  qcms / simplecc-wasm 色彩管理与简繁转换
  swift-rs / tauri / tauri-plugins  原生层
docker/ ops/           部署与运维
```

## 实现思路与核心逻辑

- 阅读引擎独立为 `foliate-js` 包，主应用与插件共用
- Web 技术栈 + Tauri 原生壳：一套代码多端分发
- 词典（MDict）、简繁转换（simplecc）等能力模块化

## 亮点

- 23k stars，Foliate 精神续作，社区活跃
- 平台覆盖极广（桌面/移动/Web + 阅读器生态插件）
- AGPL 开源，无商业广告

## 局限与风险（可选）

- 与"Agent Harness 内测"主题无关，是帖子高星"低相关"的典型
- AGPL-3.0 对商用集成有传染性要求
- 移动端体验仍在迭代

## 分析说明

基于 README、apps/packages 结构；未运行应用，未细读 Tauri/Rust 层。

# synvo-ai/local-cocoa 分析报告

- 仓库：[synvo-ai/local-cocoa](https://github.com/synvo-ai/local-cocoa)
- 方向：完全本地的个人 AI 同事（文件→记忆→洞察→行动）
- 主要语言：TypeScript
- 指标：⭐ 57 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/synvo-ai/local-cocoa)

> 分析基于 2026-08-06 抓取的 README、plugins/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"完全在你电脑上的 AI 同事"。每个文件变成记忆，记忆形成上下文，上下文激发洞察，洞察驱动行动；本地多模态，数据不出设备。
- **能拿来干什么**：本地个人知识/工作助手、多模态记忆管理。
- **适合谁**：注重隐私的 AI 用户、知识工作者。
- **快速判断**：如果你要"数据 100% 本地"的个人 AI，它很合适；否则云端助手更方便。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（本地多模态记忆）
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "Local Cocoa runs entirely on your device... Each file turns into memory. Memories form context. Context sparks insight. Insight powers action."。

## 项目方向与定位

完全本地（llama.cpp 驱动）：文件→记忆→上下文→洞察→行动链路；插件体系，跨平台。

## 主要功能（能做什么）

- 本地多模态记忆与上下文
- llama.cpp 本地推理
- 插件扩展、隐私 100% 本地

## 架构设计

```text
plugins/      插件
config/ assets/
```

## 实现思路与核心逻辑

- "记忆即上下文"：文件系统级记忆 → 洞察 → 行动
- 本地推理避免数据外传

## 亮点

- 57 stars，本地多模态记忆定位
- MIT 开源 + 插件化

## 局限与风险（可选）

- 本地推理对硬件要求高
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、plugins/ 与文档；未运行。

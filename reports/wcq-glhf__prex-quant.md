# wcq-glhf/prex-quant 分析报告

- 仓库：[wcq-glhf/prex-quant](https://github.com/wcq-glhf/prex-quant)
- 方向：PREX 量化研究 API 开源客户端（自然语言策略回测）
- 主要语言：文档/API（JS 示例）
- 指标：⭐ 5 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[PREX](https://prex.best) · [README](https://github.com/wcq-glhf/prex-quant)

> 分析基于 2026-08-06 抓取的 README、openapi.yaml 与文档。

## 这是什么（非技术版）

- **这是什么**：PREX 量化平台的官方开源客户端。用自然语言描述加密资产或美股永续策略，PREX 自动转成可审计的因子规则并云端回测；也能拿 A 股/港股情绪、K 线和 AI 分析。
- **能拿来干什么**：量化策略回测、市场情绪数据。
- **适合谁**：量化爱好者、交易研究者。
- **快速判断**：如果你做量化研究且想用自然语言回测，它很实用；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（量化 API 客户端）
- 副分类：无
- 理由：README 自述 "面向全球市场的量化研究 API……PREX Quant 是 PREX 的开源客户端项目"。

## 项目方向与定位

开源客户端：开放量化工作流、API 协议（openapi.yaml）、调用示例与报告工具；回测引擎在 PREX 服务端。

## 主要功能（能做什么）

- 自然语言策略回测（云端）
- A 股/港股情绪、K 线、AI 分析
- 匿名免费调用

## 架构设计

```text
openapi.yaml + examples/
```

## 实现思路与核心逻辑

- 客户端-服务端分离：客户端开源，引擎/数据服务端

## 亮点

- 5 stars，量化 API 垂直
- Apache-2.0、Public Beta 免费

## 局限与风险（可选）

- 依赖 PREX 服务
- 与"Agent Harness 内测"主题相关度低

## 分析说明

基于 README、openapi.yaml 与文档；未调用 API。

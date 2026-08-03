# kinpoe-ray/evidence-harness 分析报告

- 仓库：[kinpoe-ray/evidence-harness](https://github.com/kinpoe-ray/evidence-harness)
- 方向：Evidence-first 的 TypeScript Agent Harness 内核——有界、策略门控、可验证的智能体执行
- 主要语言：TypeScript（99%+，依赖 Bun/Node.js）
- 指标：⭐ 0 · fork 0 · License MIT · 最近推送 2026-08-03
- 主页/文档：[ARCHITECTURE.md](https://github.com/kinpoe-ray/evidence-harness/blob/main/ARCHITECTURE.md)、[SECURITY.md](https://github.com/kinpoe-ray/evidence-harness/blob/main/SECURITY.md)

> 分析基于 2026-08-04 抓取的 README、`src/` 全部源码（约 0.1MB）、`ARCHITECTURE.md` 与测试结构。状态：v0.1 alpha / public-review ready，非生产级。

## 这是什么（非技术版）

- **这是什么**：一个给 AI 当"工地监理"的程序。AI 只负责出主意、提方案，它负责检查预算、权限、工作区域和验收标准，全部合格才签字交付，并且每一步都留档可查。
- **能拿来干什么**：用在"让 AI 帮你自动干活、但你不放心"的场景——比如 AI 操作电脑、调用工具时，保证它按规矩来、不乱花钱、每一步都有记录，最后还能给出"验收报告"证明干完了。
- **适合谁**：开发者、架构师、安全/可靠性研究者，以及对"AI 干活过程可验证、可追溯"有要求的人。
- **快速判断**：如果你想研究或构建一个"可验证的 AI 执行框架"，它是一份很好的参考；如果你只是想要一个开箱即用的 AI 助手，现阶段不适合（v0.1 alpha、没有成品界面）。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（内核基础设施）
- 副分类：无
- 理由：GitHub topics 含 `agent-harness`，README 自述 "evidence-first TypeScript kernel for bounded, policy-gated, verifiable agent execution"。

## 项目方向与定位

把 LLM 当作**不可信的意图生成器**，由确定性内核接管执行、工具、上下文、生命周期、可观测性、验证、治理与证据，只有通过精确验收检查并拿到持久化发布回执后才允许进入 `SHIPPED`。

面向：Agent Harness 架构研究、对抗性测试、单机原型；明确**不是**生产控制平面，容器级隔离、分布式存储、KMS 签名等均为"生产适配器待补"。

## 主要功能（能做什么）

- 生命周期：显式 FSM + CAS 快照 + 哈希链事件 + 租约 fencing + 终态不可变 + 取消/恢复
- 执行记账：模型/工具容量"先检后用"（fail-before-use）+ 带安全整数溢出的 token/成本账本
- 不确定性处理：写前日志（write-ahead journal）防止模型调用和验证结果被静默重放
- 上下文：有界选择、来源（provenance）、信任分区、污点传播、因果排序、仅验证通过后进记忆
- 工具网关：schema 校验 → 权威能力交集 → 风险上限 → 运行时隔离 → 资源策略 → 审批 → 幂等 → 执行 → 策略证据，单管道完成
- 审批：challenge 绑定具体动作与稳定的 action-policy 哈希；host 认证主体；单动作租约 + 幂等回执
- 验证：每个声明的验收标准/证据种类恰好一个通过且绑定 verifier-ID 的结果
- 证据包：有界签名 bundle（canonical JSON、事件链校验、SHA-256 文件绑定、Ed25519 签名、人工制品嵌入、语义交叉检查）
- 发布：staging 先本地全量验证再原子可见；崩溃/竞态时按精确可见 bundle 对账
- 适配器：HTTPS OpenAI-compatible 模型适配器（禁重定向、有界请求）+ 绝对路径可执行文件的进程运行时
- 研究原语：DAG 协调、分层预算、持久 mailbox、能力租约、确定性隔离 delta 合并

## 架构设计

```text
TaskSpec admission
  -> Harness + Lifecycle + CAS RunStore + lease fence + budget ledger
  -> Context Compiler (provenance / trust / taint / bound)
  -> ModelRuntime (journaled intent)
  -> Tool Gateway middleware
       validate -> authoritative grants -> canonical resources -> risk/isolation
       -> authenticated approval -> idempotency -> ComputerRuntime
       -> immutable result + policy evidence
  -> criterion-specific Verifier journal
  -> COMMITTED -> PACKAGING -> verified EvidencePublisher receipt -> SHIPPED
```

- `src/` 单模块目录：`harness.ts`（入口/编排）、`lifecycle.ts`（FSM）、`run-store.ts`（CAS 存储）、`budget.ts`、`context.ts`、`tool-gateway.ts`、`approval.ts`、`verifier.ts`、`evidence.ts`、`publication.ts`、`crypto.ts`、`event-chain.ts`、`immutable.ts`、`adapters/`
- 稳定接缝（seams）：`ModelRuntime`、`RunStore`、`CapabilityAuthority`、`ApprovalAuthorizer`、`ComputerRuntime`、`Verifier`、`EvidencePublisher`，供生产适配器替换
- 测试：`tests/` 按模块一一对应（harness/lifecycle/evidence/tool-gateway/run-store/approval 等），CI 跑 `bun run check`

## 实现思路与核心逻辑

- **确定性内核 + 非确定性模型解耦**：模型输出只作为意图进入内核，内核负责记账、门控、验证与证据，从而把"不可信输入"约束在可控管道内（`harness.ts` 入口）
- **FSM 显式枚举合法迁移**：`lifecycle.ts` 用 `transitions` 表定义 12 个状态间的合法迁移，并在 `VERIFYING→COMMITTED` 强制 `verified===true`、`PACKAGING→SHIPPED` 强制携带 evidence bundle，把不变式写进类型化的 guard
- **故障语义按边界细分**：README 用 12 行恢复语义表定义每类中断的处置——关键原则是"不可判定即 fail closed 到 `BLOCKED`，绝不静默重放副作用"，对账只采用精确匹配的持久化结果
- **证据链防篡改**：`crypto.ts` canonical JSON + SHA-256 + Ed25519，事件流锚定首个 `PACKAGING` 迁移；bundle 有明确的 1 MiB manifest / 1024 文件 / 64 MiB 单文件等有界默认值
- **诚实标注边界**：把"生产适配器待补"逐条列进 maturity boundary，连 `SHIPPED` 的语义局限（本地可变存储、非沙箱）都主动声明——是少见的"把不变量和反例都写进 README"的工程风格

## 亮点

- 设计文档质量极高：README 用"承包商 vs 工地监理"类比解释核心理念，`SECURITY.md`/`ARCHITECTURE.md`/`IMPLEMENTATION_REPORT.md` 齐全
- 安全思维扎实：写前日志防重放、租约 fencing、终态不可变、幂等回执、对账失败绝不静默升级
- 验证工程：模块化测试覆盖每个内核文件；`bun run check` = typecheck + coverage + build
- 可审计性：明确快照/容量限制（10,000 事件 / 64 MiB 水位）、证据 schema 版本化管理（但 v0.1 无迁移框架）
- 仓库虽小但"内核不变量 + 对抗性公共接缝测试"已实现，适合做架构研究参考

## 局限与风险（可选）

- v0.1 alpha，`private: true` 未发布 npm；多智能体认证传输、命名空间持久记忆、分布式存储均缺失
- 本地适配器为进程隔离而非沙箱；文件存储不做跨主机的分布式事务
- 活跃智能体身份硬编码为 `root`；`Coordinator`/`HierarchicalBudget`/`DeltaMerger` 实验性且未接入单跑 Harness
- 0 星 0 fork，无社区验证；依赖作者后续持续维护

## 分析说明

数据来源：GitHub API 元数据（gh）、README、`src/` 全部源码、`ARCHITECTURE.md` 与测试目录。未执行 `bun run check`（本机未安装 Bun），未逐行通读全部源码。

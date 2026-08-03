# Repo Categories & Non-Technical Summary Guide

## Six-category system (primary + optional secondary)

| # | Category | Plain-language description | Signals (README/description/source) |
| --- | --- | --- | --- |
| 1. General Agent Runtime / Harness / Desktop client | A "host/shell" that runs an agent itself: gives an AI a work environment with tools, memory, and model switching | desktop/TUI/CLI, local-first, multi-model, MCP, Skills, workspace, harness/runtime/kernel, agent client |
| 2. Coding Harness / Engineering-oriented Agent | An AI engineer focused on writing code, with emphasis on quality checks, isolation, and long tasks | coding agent, code generation/refactoring, SWE benchmark, quality gates/verification, repo operations, Claude Code / Codex / Gemini CLI derivatives |
| 3. Multi-agent orchestration / collaboration | A "dispatch center" that makes multiple AIs divide work and collaborate | multi-agent, orchestrator, DAG, parallel, team, planner, coordinator, sub-agent |
| 4. Memory / context / knowledge management | A "long-term memory / notebook" for AI | memory, knowledge graph, RAG, context, semantic search, provenance, persistent sessions |
| 5. Evaluation / Benchmark tooling | An "exam system" that scores AI/agents | eval, benchmark, metrics, Pass@k, sandbox evaluation, correctness vs. token/latency |
| 6. Domain-specific / other | A tool for one concrete scenario (browser, design, version control, workflow, etc.) | clear domain keywords, not falling into any category above |

Key points:

- Every category needs evidence (a quote from the README, package description, or source characteristic); one line of rationale in the report is enough.
- A secondary category is allowed, but the report states only 1 primary + at most 1 secondary to stay crisp.
- When unsure, use 6 and explain why in the report.

## How to write the non-technical summary (placed at the very top of the report)

Target audience: people without a technical background. Keep it to 4–6 lines, avoid API/framework jargon (explain any term in one plain sentence), and use everyday analogies.

Four fixed elements:

1. **What it is**: one-line definition + an everyday analogy (e.g. the model is the "contractor", the harness is the "site supervisor")
2. **What you can use it for**: describe use cases, not a feature list ("automatically writes code on your computer and checks it" rather than "supports SWE-bench")
3. **Who it is for**: developers / non-developers / teams / researchers / general users, with a sentence each
4. **Quick "do I need it"**: 1–2 judgment sentences like "Use it if you want X; skip it if you only need Y"

Example (wording is flexible):

> It's a "steward" for AI: the AI comes up with ideas, and it checks budget, permissions, and acceptance criteria, delivering results only when everything passes. It suits people who care about safety and traceability of AI work; if you just want a quick chat, you don't need it.

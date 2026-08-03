---
name: github-repo-analyzer
description: Analyze GitHub repositories and produce structured Chinese reports covering project direction/positioning, capabilities, architecture, implementation approach and highlights. Use when the user asks to analyze or summarize one or many GitHub repos, build a repo survey/dossier (e.g. from a list of URLs), compare open-source projects, or understand what a repo does and how it is built.
---

# GitHub Repo Analyzer

Analyze GitHub repos (single or batch) and write per-repo Markdown reports.

## Workflow

1. **Determine targets**
   - Single repo: use the owner/repo or full URL the user gave.
   - Batch: accept a list file with one URL per line (e.g. `project_urls.txt`); also accept a glob/CSV column if requested.
   - Default report output: `reports/` under the current working directory (or a user-specified `--out-dir`).
   - In this project, paths are relative to the repo root: reports go to `reports/`, fetched data to `_repo_cache/` (gitignored).

2. **Fetch data for each repo**
   ```bash
   python3 scripts/fetch_repo.py <owner/repo> --out-dir _repo_cache
   ```
   The script writes `metadata.json` (stars, language, topics, license, languages breakdown, rate-limit info), a decoded `README.md`, and a shallow clone under `<cache>/<owner>__<repo>/repo/`.
   - It prefers `gh api`; if the `gh` token is invalid it falls back to unauthenticated REST (60 req/h). Re-auth via `gh auth login` for batch work.
   - Reuse cache: rerunning skips API calls unless `--force`.

3. **Analyze the repo**
   - Read `README.md` first, then inspect top-level tree (`find repo -maxdepth 2`), manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `requirements.txt`, etc.), `docs/` if present, and the entry point plus core modules.
   - Establish, with file-level evidence:
     - 方向：领域、定位、面向谁
     - 功能：能做什么（能力清单）
     - 架构：模块划分、分层、数据流/执行流程
     - 实现思路与核心逻辑：关键设计决策、核心逻辑所在文件
     - 亮点：技术 / 工程 / 易用性
   - Classify the repo into one of the six categories in `references/categories.md` (primary + optional secondary), with one line of evidence.
   - Draft the non-technical summary first: plain-language "what is it", use-case, who it is for, and a quick yes/no decision aid (see `references/categories.md`).
   - If the clone failed but metadata/README succeeded, analyze from README + API-only info and say so in the report.

4. **Write the report**
   - Use `references/report-template.md` as the skeleton.
   - Output: `reports/<owner>__<repo>.md` (Chinese content, code identifiers in English).
   - Order matters: the non-technical section and category come right after the header block, before 项目方向与定位, so non-technical readers get the gist early.
   - Keep claims traceable: cite file paths or README statements.
   - Append one summary row to `reports/SUMMARY.csv` (columns: `repo,url,stars,language,category,direction,key_features,architecture,highlights,report`). For batch runs, regenerate SUMMARY.csv at the end from all reports.

5. **Batch mode**
   - Loop over the list; skip repos whose report already exists unless `--force`.
   - Check rate limit: pause if `X-RateLimit-Remaining` is low (unauthenticated: stop before 0; gh: 5000/h, rarely a problem).
   - `git clone` does not consume API quota; prefer it for big codebases and fall back to API-only analysis if a clone is too large or fails.
   - Record failures (404, rate limit, clone errors) in `reports/failures.txt` and continue; summarize them at the end.
   - Prefer small batches and pause between groups; rapid bursts can trigger GitHub rate limiting.

## Notes

- Respect the user's requested output location and language for reports.
- For huge repos, analyze the top-level structure + key modules instead of reading everything; be explicit about coverage.
- Do not include tokens or credentials in reports. Clone URLs must be the public `https://github.com/...` form.
- `gh` reads credentials from the macOS keychain; if `gh auth status` fails inside a sandbox but the machine is logged in, run the fetch script outside the sandbox (escalated).

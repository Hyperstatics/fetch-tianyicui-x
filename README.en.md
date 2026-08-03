# fetch-tianyicui-x

Extract open-source project links from replies to an X (Twitter) post captured in a HAR file, and organize them into a structured table.

Repository: [Hyperstatics/fetch-tianyicui-x](https://github.com/Hyperstatics/fetch-tianyicui-x.git)

> 中文版: [README.md](README.md)

## Background

Source post by [@tianyi](https://x.com/tianyi):
[“If you are a developer of Agent Harness-related open-source projects and would like to join the DeepSeek Harness beta, please include your GitHub ID and your representative open-source work(s)”](https://x.com/tianyi/status/2083519855203078320).

This repo extracts every open-source project link mentioned in the replies, making it easy to aggregate, filter, and follow up.

## Data Source

- `x.com.har`: a HAR capture exported from browser developer tools, containing 11 `TweetDetail` GraphQL paginated responses (original post + replies + quotes).

> [!IMPORTANT]
> The HAR contains session-bound request headers and third-party public data (see “Security Notes”). It is **excluded via `.gitignore` and will never be committed**. Capture your own copy and put it in the project root.

### Capturing the HAR

Save a HAR from the browser Network panel:

1. Open the post page: https://x.com/tianyi/status/2083519855203078320
2. Press `F12` to open developer tools
3. Switch to the **Network** panel
4. Filter by type **fetch/xhr**
5. Type **TweetDetail** in the filter box
6. Scroll the post page to load more replies (more `TweetDetail` requests keep firing)
7. Right-click any request → **Export HAR** (or click the export button)
8. Save it as `x.com.har` in the project root

![Filter TweetDetail in the Network panel and export the HAR](har-screenshot.png)

## Pipeline

```text
x.com.har
  -> extract all TweetDetail responses
  -> base64-decode (response bodies are base64-encoded JSON)
  -> recursively walk tweet nodes in threaded_conversation_with_injections_v2
  -> read full_text, expanded_url / display_url / url from entities
  -> filter repo-hosting domains (GitHub / GitLab / Hugging Face / Gitee / Codeberg, etc.)
  -> dedupe by (tweet, link)
  -> projects.csv
```

## Output: projects.csv

| Field | Description |
| --- | --- |
| `tweet_id` | Tweet ID |
| `created_at` | Posting time (raw X format) |
| `screen_name` | Author's X username |
| `display_name` | Author's display name |
| `tweet_text` | Full tweet text |
| `url` | Open-source project link |
| `kind` | `repo` (repository) / `profile` (GitHub profile) |
| `repo` | Normalized `owner/repo` (repo links only) |

The file is UTF-8 with BOM, so it opens directly in Excel.

### Output: project_urls.txt

A deduplicated list of open-source repository URLs, one per line (all normalized to `https`), easy to copy, batch-verify, or use as a roster. It includes two sources:

- Repository links in tweet text (including long `note_tweet` tweets)
- Repository links in author bios (where the “representative open-source work” requested in the post usually appears)

GitHub profiles, `/sponsors/` pages, and other non-project links are excluded.

## Statistics

Current HAR (captured 2026-08-03):

- Tweets parsed: 311 (original post + replies + quotes)
- Authors providing links: 250
- `projects.csv`: 295 rows (tweet × link)
  - Repository links: 260
  - GitHub profiles: 35
- `project_urls.txt`: 264 deduplicated repository URLs
- The current data contains only GitHub links; the script also supports GitLab / Hugging Face / Gitee / Codeberg / Bitbucket / SourceForge / GitCode domains, so a fresh capture can be reused directly.

## Usage

Make sure `x.com.har` is in the project root as described above, then run:

```bash
python3 extract_projects.py
```

The script re-reads `x.com.har` and regenerates `projects.csv`.

## Project Skill: GitHub Repo Analyzer

This repo ships with two project-level skills for analyzing open-source repositories (direction, features, architecture, implementation approach, highlights):

- [github-repo-analyzer](.codex/skills/github-repo-analyzer/) – generates **Chinese** reports
- [github-repo-analyzer-en](.codex/skills/github-repo-analyzer-en/) – generates **English** reports

- Reports are written to `reports/<owner>__<repo>.md` (relative to the project root) and summarized in `reports/SUMMARY.csv`
- Fetched data is cached in `_repo_cache/` (gitignored, not committed)
- Uses `gh` authentication to call the GitHub API; for batch runs, use small batches with pauses to avoid rate limiting

## Directory Structure

```text
.
├── x.com.har            # Raw capture (local only, not committed – see .gitignore)
├── har-screenshot.png   # Capture instructions screenshot
├── extract_projects.py  # Extraction script
├── projects.csv         # Extraction results
├── project_urls.txt     # Deduplicated repository URL list
├── reports/             # Repo analysis reports (produced by the project skills)
├── .codex/skills/       # Project-level skills (github-repo-analyzer, github-repo-analyzer-en)
├── LICENSE              # MIT License
├── .gitignore           # Excludes HAR and other sensitive files
└── README.md
```

## License

The code is open-sourced under the [MIT License](LICENSE).

Links and text in `projects.csv` come from public post replies; inclusion is not an endorsement. When using the data, comply with X's terms of service and verify each project's licensing yourself.

## Notes

- **Security**: the HAR includes session-bound request headers such as `x-csrf-token`, as well as public account info and content from repliers. Do not commit or publicly share the raw file.
- Project links have not been individually verified for availability or maintenance status; inclusion is not an endorsement.
- This repo only organizes data and has no official affiliation with DeepSeek or X.

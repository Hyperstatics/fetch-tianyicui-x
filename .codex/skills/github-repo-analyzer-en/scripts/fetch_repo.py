#!/usr/bin/env python3
"""Fetch metadata + shallow clone for one GitHub repo.

Usage:
    python3 fetch_repo.py <owner/repo | full URL> [--out-dir DIR] [--force]

Writes:
    <out-dir>/<owner>__<repo>/metadata.json   repo metadata + languages
    <out-dir>/<owner>__<repo>/README.md       decoded README
    <out-dir>/<owner>__<repo>/repo/           shallow clone (--no-clone to skip)

Prefers `gh api` when authenticated; falls back to unauthenticated GitHub REST
API. Prints rate-limit status so batch runs can pause before exhausting quota.
"""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "github-repo-analyzer-skill"


def parse_repo(value: str) -> str:
    value = value.strip().rstrip("/")
    if "github.com/" in value:
        value = value.split("github.com/", 1)[1]
    parts = [p for p in value.split("/") if p]
    if len(parts) < 2:
        sys.exit(f"invalid repo: {value!r} (expect owner/repo or full URL)")
    return f"{parts[0]}/{parts[1]}"


def gh_auth_ok() -> bool:
    try:
        subprocess.run(
            ["gh", "auth", "status"], capture_output=True, timeout=15, check=True
        )
        return True
    except Exception:
        return False


def api_get(owner: str, repo: str, path: str, use_gh: bool) -> tuple[dict, dict]:
    """GET a GitHub REST endpoint. Returns (json, headers)."""
    url = f"https://api.github.com/repos/{owner}/{repo}{path}"
    if use_gh:
        proc = subprocess.run(
            ["gh", "api", f"/repos/{owner}/{repo}{path}"],
            capture_output=True,
            timeout=30,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.decode(errors="replace").strip())
        return json.loads(proc.stdout), {}
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read()), dict(resp.headers)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="owner/repo or full GitHub URL")
    parser.add_argument("--out-dir", default="_repo_cache", help="cache directory")
    parser.add_argument("--force", action="store_true", help="refetch even if cached")
    parser.add_argument("--no-clone", action="store_true", help="skip git clone")
    args = parser.parse_args()

    owner, repo = parse_repo(args.repo).split("/")
    cache = Path(args.out_dir) / f"{owner}__{repo}"
    cache.mkdir(parents=True, exist_ok=True)

    use_gh = gh_auth_ok()
    mode = "gh api" if use_gh else "curl (unauthenticated)"

    meta_path = cache / "metadata.json"
    meta = None
    if meta_path.exists() and not args.force:
        meta = json.loads(meta_path.read_text())

    rate = {}
    if meta is None:
        meta, headers = api_get(owner, repo, "", use_gh)
        languages, _ = api_get(owner, repo, "/languages", use_gh)
        meta["languages"] = languages
        rate = {
            "remaining": headers.get("X-RateLimit-Remaining"),
            "limit": headers.get("X-RateLimit-Limit"),
            "reset": headers.get("X-RateLimit-Reset"),
            "mode": mode,
        }
        meta["_fetched_at"] = rate
        meta_path.write_text(json.dumps(meta, indent=1, ensure_ascii=False))

    readme_path = cache / "README.md"
    if not readme_path.exists() or args.force:
        try:
            data, _ = api_get(owner, repo, "/readme", use_gh)
            readme_path.write_bytes(base64.b64decode(data["content"]))
        except Exception as exc:
            readme_path.write_text(f"<!-- README fetch failed: {exc} -->")

    clone_dir = cache / "repo"
    if not args.no_clone and not clone_dir.exists():
        clone_url = meta.get("clone_url") or f"https://github.com/{owner}/{repo}.git"
        proc = subprocess.run(
            [
                "git", "clone", "--depth", "1", "--single-branch", "--no-tags",
                clone_url, str(clone_dir),
            ],
            capture_output=True,
            timeout=600,
        )
        if proc.returncode != 0:
            print(f"[warn] clone failed: {proc.stderr.decode(errors='replace')[-300:]}",
                  file=sys.stderr)

    print(json.dumps({
        "owner": owner,
        "repo": repo,
        "name": meta.get("full_name"),
        "description": meta.get("description"),
        "stars": meta.get("stargazers_count"),
        "forks": meta.get("forks_count"),
        "language": meta.get("language"),
        "topics": meta.get("topics", []),
        "license": (meta.get("license") or {}).get("spdx_id"),
        "default_branch": meta.get("default_branch"),
        "updated_at": meta.get("updated_at"),
        "homepage": meta.get("homepage"),
        "archived": meta.get("archived"),
        "languages": meta.get("languages", {}),
        "rate_limit": meta.get("_fetched_at", {}),
        "cache_dir": str(cache),
        "clone_dir": str(clone_dir),
        "readme": str(readme_path),
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

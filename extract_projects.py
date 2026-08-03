#!/usr/bin/env python3
"""Extract open-source project links from an X (Twitter) HAR file.

Input : x.com.har (browser HAR containing TweetDetail GraphQL responses)
Output: projects.csv

The HAR responses are base64-encoded JSON. We decode them, walk every
tweet node, then collect author, text and URL fields (expanded_url /
display_url / url) and filter to repository-hosting domains.
"""

from __future__ import annotations

import base64
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlparse

HAR_PATH = Path(__file__).parent / "x.com.har"
OUT_PATH = Path(__file__).parent / "projects.csv"
OUT_URLS_PATH = Path(__file__).parent / "project_urls.txt"

# Repository-hosting domains we care about. Kept broad so non-GitHub links
# (GitLab, Hugging Face, Gitee, ...) are captured if they appear.
REPO_HOSTS = {
    "github.com",
    "www.github.com",
    "gitlab.com",
    "www.gitlab.com",
    "gitlab.cn",
    "www.gitlab.cn",
    "huggingface.co",
    "www.huggingface.co",
    "hf.co",
    "gitee.com",
    "www.gitee.com",
    "codeberg.org",
    "www.codeberg.org",
    "bitbucket.org",
    "www.bitbucket.org",
    "sourceforge.net",
    "gitcode.com",
    "www.gitcode.com",
    "atomgit.com",
    "gitea.com",
    "gitlink.org.cn",
    "opencode.org.cn",
}


def load_har(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def decoded_responses(har: dict):
    """Yield decoded JSON payloads for every TweetDetail response."""
    for entry in har["log"]["entries"]:
        content = entry["response"]["content"] or {}
        text = content.get("text", "")
        if not text:
            continue
        try:
            yield json.loads(base64.b64decode(text + "===").decode("utf-8"))
        except Exception:
            continue


def walk_tweets(data):
    """Yield each tweet result node (with legacy.full_text) once."""
    stack = [data]
    seen = set()
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            legacy = node.get("legacy")
            if isinstance(legacy, dict) and "full_text" in legacy:
                tweet_id = legacy.get("id_str")
                if tweet_id and tweet_id not in seen:
                    seen.add(tweet_id)
                    yield node
            for value in node.values():
                stack.append(value)
        elif isinstance(node, list):
            stack.extend(node)


def author_of(node) -> tuple[str, str]:
    """Return (screen_name, display_name) from a tweet result node."""
    user = node.get("core", {}).get("user_results", {}).get("result", {})
    core = user.get("core", {})
    if isinstance(core, dict) and core.get("screen_name"):
        return core["screen_name"], core.get("name", "")
    legacy = user.get("legacy", {})
    if legacy.get("screen_name"):
        return legacy["screen_name"], legacy.get("name", "")
    return "", ""


def urls_of_tweet(node) -> set[str]:
    """Collect expanded URLs from entities plus plain http links in text."""
    urls = set()
    legacy = node.get("legacy", {})
    for u in legacy.get("entities", {}).get("urls", []):
        expanded = u.get("expanded_url")
        if expanded:
            urls.add(expanded)

    # Long-form tweets (note_tweet) store their URL entities separately.
    note = node.get("note_tweet", {}).get("note_tweet_results", {}).get("result", {})
    for u in note.get("entity_set", {}).get("urls", []):
        expanded = u.get("expanded_url") or u.get("url")
        if expanded:
            urls.add(expanded)

    text = legacy.get("full_text", "") + "\n" + note.get("text", "")
    for match in re.finditer(r"https?://[^\s\"'\\<>)\]]+", text):
        urls.add(match.group(0).rstrip(".,;:!?"))
    return urls


def bio_urls_of(node) -> set[str]:
    """Collect repository URLs from the author's profile description."""
    user = node.get("core", {}).get("user_results", {}).get("result", {})
    entities = user.get("profile_bio", {}).get("entities", {})
    bio = entities.get("url", {}).get("urls", []) + entities.get("description", {}).get("urls", [])
    if not bio:
        legacy_user = user.get("legacy", {})
        bio = legacy_user.get("entities", {}).get("description", {}).get("urls", [])
    return {u.get("expanded_url") or u.get("url") for u in bio if u.get("expanded_url") or u.get("url")}


def host_of(url: str) -> str:
    return urlparse(url).netloc.lower()


def is_repo_url(url: str) -> bool:
    return host_of(url) in REPO_HOSTS


def is_project_url(url: str) -> bool:
    """Repo-host URL that points to a project (not a sponsor/funding page)."""
    if not is_repo_url(url):
        return False
    first = next((s for s in urlparse(url).path.rstrip("/").split("/") if s), "").lower()
    return first != "sponsors"


def classify(url: str) -> str:
    """repo / profile / homepage for a repository-host URL."""
    path = urlparse(url).path.rstrip("/")
    segments = [s for s in path.split("/") if s]
    if not segments:
        return "homepage"
    if len(segments) == 1:
        return "profile"
    return "repo"


def repo_path(url: str) -> str:
    """owner/repo from the first two path segments (empty otherwise)."""
    path = urlparse(url).path.rstrip("/")
    segments = [s for s in path.split("/") if s]
    if len(segments) >= 2:
        return f"{segments[0]}/{segments[1]}"
    return ""


def normalize(url: str) -> str:
    """Normalize host to lowercase, force https, drop trailing slash/.git."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    if path.lower().endswith(".git"):
        path = path[:-4]
    scheme = "https" if parsed.netloc.lower() in REPO_HOSTS else parsed.scheme.lower()
    return f"{scheme}://{parsed.netloc.lower()}{path}"


def main() -> None:
    har = load_har(HAR_PATH)
    rows = []
    seen_tweets = set()
    seen_urls = set()
    project_urls = set()

    for payload in decoded_responses(har):
        for node in walk_tweets(payload):
            legacy = node["legacy"]
            tweet_id = legacy.get("id_str")
            if tweet_id in seen_tweets:
                continue
            seen_tweets.add(tweet_id)

            screen_name, display_name = author_of(node)
            text = legacy.get("full_text", "")
            urls = sorted(urls_of_tweet(node))
            repo_urls = [u for u in urls if is_repo_url(u)]
            for url in repo_urls:
                key = (tweet_id, normalize(url))
                if key in seen_urls:
                    continue
                seen_urls.add(key)
                if classify(url) == "repo":
                    project_urls.add(normalize(url))
                rows.append(
                    {
                        "tweet_id": tweet_id,
                        "created_at": legacy.get("created_at", ""),
                        "screen_name": screen_name,
                        "display_name": display_name,
                        "tweet_text": text,
                        "url": url,
                        "kind": classify(url),
                        "repo": repo_path(url),
                    }
                )
            # Author bio links: representative projects often live in the
            # profile description. Add them to the standalone URL list only.
            for url in bio_urls_of(node):
                if is_project_url(url) and classify(url) == "repo":
                    project_urls.add(normalize(url))

    rows.sort(key=lambda r: (r["created_at"], r["tweet_id"]))
    with open(OUT_PATH, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "tweet_id",
                "created_at",
                "screen_name",
                "display_name",
                "tweet_text",
                "url",
                "kind",
                "repo",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    # Standalone list of deduplicated project URLs (one per line).
    with open(OUT_URLS_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(url + "\n" for url in sorted(project_urls))

    print(f"tweets parsed       : {len(seen_tweets)}")
    print(f"rows (tweet x link) : {len(rows)}")
    print(f"unique repo links   : {len({normalize(r['url']) for r in rows})}")
    print(f"unique authors      : {len({r['screen_name'] for r in rows})}")
    print(f"project urls        : {len(project_urls)}")
    print(f"written -> {OUT_PATH}")
    print(f"written -> {OUT_URLS_PATH}")


if __name__ == "__main__":
    main()

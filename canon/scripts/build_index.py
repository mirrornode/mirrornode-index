#!/usr/bin/env python3
"""
MIRRORNODE Repository Indexer v0.3

Discovers, indexes, and catalogs all repositories owned by the mirrornode user.
Generates structured metadata for navigation, governance, and automation.
"""

import os
import sys
import json
import logging
import time
import requests
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone
from collections import defaultdict

# ================================================================
# CONFIGURATION
# ================================================================

OWNER = "mirrornode"  # GitHub username
API_BASE = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise RuntimeError("GITHUB_TOKEN environment variable is required")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# Path resolution (repo root)
ROOT = Path(__file__).resolve().parents[2]
SUMMARIES = ROOT / "summaries"
COMPONENTS = ROOT / "components"
REPOS_JSON = ROOT / "repos.json"
INDEX_META = ROOT / "index_metadata.json"

SUMMARIES.mkdir(exist_ok=True)
COMPONENTS.mkdir(exist_ok=True)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("mirrornode-index")

# ================================================================
# STATUS DETECTION
# ================================================================

STATUS_RULES = {
    "REVENUE": ["osiris", "audit", "hud"],
    "CORE": ["core", "mirrornode", "theia", "engine", "lattice"],
    "SURFACE": ["ui", "surface", "interface"],
    "EXPERIMENT": ["demo", "test", "sandbox", "prototype"],
    "ARCHIVE": ["archive", "deprecated", "legacy", "old"],
}

def detect_status(repo: Dict[str, Any]) -> str:
    """Detect repository status based on name and topics."""
    name = repo.get("name", "").lower()
    topics = [t.lower() for t in repo.get("topics", [])]

    if repo.get("archived", False):
        return "ARCHIVE"

    for status, keys in STATUS_RULES.items():
        if any(k in topics for k in keys):
            return status

    for status, keys in STATUS_RULES.items():
        if any(k in name for k in keys):
            return status

    return "EXPERIMENT"

def classify_by_language(lang: Optional[str]) -> str:
    """Classify repository into ecosystem by primary language."""
    if not lang:
        return "misc"
    l = lang.lower()
    if l == "python":
        return "backend"
    if l in ("javascript", "typescript"):
        return "frontend"
    if l in ("go", "rust"):
        return "systems"
    return "misc"

# ================================================================
# GITHUB API HELPERS
# ================================================================

def github_get(url: str, retries: int = 3) -> Any:
    """Make authenticated GET request to GitHub API with retry logic."""
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            remaining = int(r.headers.get("X-RateLimit-Remaining", 0))
            if remaining < 10:
                logger.warning(f"GitHub rate limit low: {remaining}")
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError:
            if r.status_code == 404:
                logger.warning(f"404 not found: {url}")
                return None
            if r.status_code == 403:
                raise
            logger.warning(f"HTTP error ({attempt + 1}/{retries})")
        except requests.exceptions.RequestException as e:
            logger.warning(f"Request error ({attempt + 1}/{retries}): {e}")
        time.sleep(2 ** attempt)
    logger.error(f"Failed after {retries} attempts: {url}")
    return None

def list_repos() -> List[Dict[str, Any]]:
    """Fetch all repositories from the user account."""
    repos: List[Dict[str, Any]] = []
    page = 1

    logger.info(f"Fetching repositories for user: {OWNER}")

    while True:
        url = f"{API_BASE}/users/{OWNER}/repos?per_page=100&page={page}&sort=updated"
        batch = github_get(url)
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    logger.info(f"Discovered {len(repos)} repositories")
    return repos

def get_repo_languages(repo_name: str) -> Dict[str, int]:
    """Fetch language statistics for a repository."""
    url = f"{API_BASE}/repos/{OWNER}/{repo_name}/languages"
    return github_get(url) or {}

# ================================================================
# STUB GENERATION
# ================================================================

def write_summary(repo: Dict[str, Any], langs: Dict[str, int]) -> None:
    """Generate markdown summary for a repository."""
    path = SUMMARIES / f"{repo['name']}.md"
    if path.exists():
        return

    total = sum(langs.values())
    if total > 0:
        lang_block = "\n".join(
            f"- {k}: {(v / total * 100):.1f}%"
            for k, v in sorted(langs.items(), key=lambda x: -x[1])[:5]
        )
    else:
        lang_block = "No languages detected"

    content = f"""# {repo['name']}

**Status**: {detect_status(repo)}

## Description
{repo.get('description') or 'No description provided.'}

## Primary Language
{repo.get('language') or 'Unknown'}

## Language Breakdown
{lang_block}

## Metadata
- Default branch: `{repo.get('default_branch')}`
- Created: {repo.get('created_at')}
- Updated: {repo.get('updated_at')}
- Visibility: {"private" if repo.get("private") else "public"}

## Links
- Repo: {repo['html_url']}
- Issues: {repo['html_url']}/issues
- PRs: {repo['html_url']}/pulls

## Architecture Notes
TBD

## Dependencies
TBD

## Revenue Impact
TBD
"""
    path.write_text(content)
    logger.info(f"Created summary: {repo['name']}")

def write_components(repo: Dict[str, Any]) -> None:
    """Generate component manifest for a repository."""
    path = COMPONENTS / f"{repo['name']}.json"
    if path.exists():
        return

    content = {
        "repo": repo["name"],
        "canonical_name": repo["name"].lower().replace("-", "_"),
        "status": detect_status(repo),
        "ecosystem": classify_by_language(repo.get("language")),
        "services": [],
        "agents": [],
        "entrypoints": [],
        "apis": [],
        "dependencies": {
            "internal": [],
            "external": [],
        },
        "deployment": {
            "platform": None,
            "url": repo.get("homepage"),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    path.write_text(json.dumps(content, indent=2))
    logger.info(f"Created component manifest: {repo['name']}")

# ================================================================
# INDEX BUILD
# ================================================================

def build_index() -> None:
    """Main indexing workflow."""
    logger.info("MIRRORNODE INDEX BUILD START")

    repos = list_repos()
    if not repos:
        sys.exit("No repositories found")

    index: List[Dict[str, Any]] = []
    stats: Dict[str, int] = defaultdict(int)

    for repo in repos:
        name = repo["name"]
        status = detect_status(repo)
        stats[status] += 1

        logger.info(f"Indexing {name} [{status}]")

        langs = get_repo_languages(name)
        write_summary(repo, langs)
        write_components(repo)

        index.append({
            "name": name,
            "canonical_name": name.lower().replace("-", "_"),
            "url": repo["html_url"],
            "clone_url": repo.get("clone_url"),
            "ssh_url": repo.get("ssh_url"),
            "description": repo.get("description"),
            "topics": repo.get("topics", []),
            "primary_lang": repo.get("language"),
            "languages": langs,
            "ecosystem": classify_by_language(repo.get("language")),
            "status": status,
            "visibility": "private" if repo.get("private") else "public",
            "archived": repo.get("archived", False),
            "created_at": repo.get("created_at"),
            "updated_at": repo.get("updated_at"),
            "pushed_at": repo.get("pushed_at"),
            "default_branch": repo.get("default_branch"),
            "license": repo.get("license", {}).get("spdx_id") if repo.get("license") else None,
            "summary_path": f"summaries/{name}.md",
            "components_path": f"components/{name}.json",
        })

    status_order = ["REVENUE", "CORE", "SURFACE", "EXPERIMENT", "ARCHIVE"]
    index.sort(key=lambda r: (status_order.index(r["status"]), r["name"]))

    REPOS_JSON.write_text(json.dumps(index, indent=2))
    INDEX_META.write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "owner": OWNER,
        "total_repos": len(index),
        "status_breakdown": dict(stats),
        "version": "0.3.0",
    }, indent=2))

    logger.info("MIRRORNODE INDEX BUILD COMPLETE")

# ================================================================
# ENTRY POINT
# ================================================================

if __name__ == "__main__":
    try:
        build_index()
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        sys.exit(130)
    except Exception:
        logger.exception("Fatal error")
        sys.exit(1)

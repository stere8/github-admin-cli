from __future__ import annotations

import requests
import os
import sys
import argparse
from typing import Dict
from .utils import log_error, log_success, log_warning, check_response, pretty_json


try:
    from . import __version__
except Exception:
    __version__ = "0.1.0"

TOKEN = os.environ.get('GITHUB_TOKEN')
OWNER = "stere8"
BASE = "https://api.github.com"


def build_headers(token:str) -> Dict[str,str]:
    return {
            "Authorization": f"Bearer {TOKEN}" if TOKEN else "",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

COMMON_HEADERS = build_headers(TOKEN)


def endpoint(repo: str) -> str:
    return f"{BASE}/repos/{OWNER}/{repo}"

def archive_repo(repo: str, archived: bool):
    return requests.patch(endpoint(repo), headers=COMMON_HEADERS, json={"archived": archived})

def get_repo_status(repo: str):
    return requests.get(endpoint(repo), headers=COMMON_HEADERS)

def set_private(repo: str, private: bool):
    return requests.patch(endpoint(repo), headers=COMMON_HEADERS, json={"private": private})

def main():
    if not TOKEN:
        log_error("GITHUB_TOKEN not set")
        sys.exit(1)

    p = argparse.ArgumentParser(description="GitHub Repo Admin CLI (archive/private/public/check).")
    p.add_argument("action", choices=["stat", "archive", "unarchive", "private", "public", "check"])
    p.add_argument("repo", help="Repository name (e.g., stockitweb)")
    args = p.parse_args()

    # Execute action
    if args.action == "archive":
        r = archive_repo(args.repo, True)
        check_response(r, "archive", args.repo)
    elif args.action == "unarchive":
        r = archive_repo(args.repo, False)
        check_response(r, "unarchive", args.repo)
    elif args.action == "private":
        r = set_private(args.repo, True)
        check_response(r, "private", args.repo)
    elif args.action == "public":
        r = set_private(args.repo, False)
        check_response(r, "public", args.repo)
    elif args.action == "stat":
        r = get_repo_status(args.repo)
        if r.status_code == 200:
            data = r.json()
            log_success(f"Repo: {args.repo} | Private: {data['private']} | Archived: {data['archived']}")
        else:
            log_error(f"Failed to get status for {args.repo}: {r.status_code} {r.text}")
    elif args.action == "check":
        r = get_repo_status(args.repo)
        if r.status_code == 200:
            data = r.json()
            print(f"private={data.get('private')} archived={data.get('archived')}")
        else:
            log_error(f"Check failed for {args.repo}: {r.status_code} {r.text}")
    else:
        log_warning("Unknown action. Use: archive | unarchive | private | public | stat | check")
        return

    # Optional: pretty print JSON for debug on errors
    if r.status_code >= 400:
        try:
            pretty_json(r.json())
        except Exception:
            pass
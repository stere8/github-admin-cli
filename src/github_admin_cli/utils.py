import sys
import json

# ✅ Color codes (Windows-safe)
class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

def log_success(msg: str):
    print(f"{Color.GREEN}✅ {msg}{Color.RESET}")

def log_error(msg: str):
    print(f"{Color.RED}❌ {msg}{Color.RESET}", file=sys.stderr)

def log_warning(msg: str):
    print(f"{Color.YELLOW}⚠️  {msg}{Color.RESET}")

def pretty_json(data):
    """Print JSON nicely formatted."""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def check_response(r, action, repo):
    """Unified response check + logging."""
    ok = 200 <= r.status_code < 300
    if ok:
        log_success(f"{action.upper()} {repo} -> {r.status_code}")
    else:
        log_error(f"{action.upper()} {repo} failed -> {r.status_code} {r.text}")
    return ok

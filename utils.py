# utils.py
import sys
import json
import os

# --- Windows-safe ANSI enabling (no external deps) ---
def _enable_ansi_on_windows():
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    except Exception:
        pass

_enable_ansi_on_windows()

# --- Colors ---
class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# --- Logging helpers ---
def log_success(msg: str):
    print(f"{Color.GREEN}✅ {msg}{Color.RESET}")

def log_error(msg: str):
    print(f"{Color.RED}❌ {msg}{Color.RESET}", file=sys.stderr)

def log_warning(msg: str):
    print(f"{Color.YELLOW}⚠️  {msg}{Color.RESET}")

# --- JSON helpers ---
def pretty_json(data):
    """Print a Python dict/list as pretty JSON."""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def _try_json(response):
    try:
        return response.json()
    except Exception:
        return {}

# --- Response checker ---
def check_response(response, action: str = "", repo: str = "", show_body_on_error: bool = True):
    """
    Unified status check + logging.
    Returns True if 2xx, else False.
    """
    status = getattr(response, "status_code", None)
    ok = isinstance(status, int) and 200 <= status < 300

    tag = f"{action.upper()} {repo}".strip()
    if ok:
        log_success(f"{tag} -> {status}")
    else:
        body = ""
        if show_body_on_error:
            j = _try_json(response)
            body = f" | body={json.dumps(j, ensure_ascii=False)}" if j else f" | text={getattr(response, 'text', '')}"
        log_error(f"{tag} failed -> {status}{body}")
    return ok

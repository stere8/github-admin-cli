import subprocess, sys

def test_cli_help():
    subprocess.run([sys.executable, "-m", "github_admin_cli", "--help"], check=True)

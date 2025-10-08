import importlib

def test_package_imports():
    mod = importlib.import_module("github_admin_cli.client")
    assert hasattr(mod, "main")

def test_env_token_present_monkeypatch(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "dummy")
    # Just ensure headers build path won’t crash
    import github_admin_cli.client as c
    assert "Authorization" in c.COMMON_HEADERS

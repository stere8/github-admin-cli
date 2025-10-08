* * * * *
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/bdbadf79-2c4b-468c-814f-94c94a4bdfa3" />


# GitHub Admin CLI
> 🛠️ Lightweight Python tool to **archive, unarchive, privatize, or publicize GitHub repositories** via the official REST API.

[![CI](https://github.com/stere8/github-admin-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/stere8/github-admin-cli/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.11+-green.svg)

---

## 📖 Overview

**GitHub Admin CLI** is a minimal command-line interface built in Python to automate repetitive GitHub repository administration tasks ---
such as archiving, changing privacy, or checking status --- using the official [GitHub REST API](https://docs.github.com/en/rest).

It's designed for developers who want a simple, scriptable alternative to the heavy official `gh` CLI or who want to showcase API automation skills.

---

## ✨ Features

- 🗃️ **Archive / Unarchive** repositories
- 🔒 **Make repositories public or private**
- 🔍 **Check current visibility and archive status**
- ⚙️ Uses standard `requests` and `argparse` modules (no dependencies)
- 🧪 Ready for GitHub Actions integration

---

## 🚀 Quickstart

### 1️⃣ Clone & Install

```bash
git clone https://github.com/stere8/github-admin-cli.git
cd github-admin-cli

# Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt `
````
*(Later you'll be able to run `pipx install .` once packaged with `pyproject.toml`.)*

* * * * *

### 2️⃣ Set up Authentication

Create a [Personal Access Token](https://github.com/settings/tokens) with the **`repo`** scope.\
Store it as an environment variable:

`# Windows PowerShell
setx GITHUB_TOKEN "ghp_yourTokenHere"

# macOS/Linux
export GITHUB_TOKEN="ghp_yourTokenHere"`

> ⚠️ The token is **never stored or logged**. It's only read at runtime from the environment.

* * * * *

### 3️⃣ Usage

Run directly with Python:

`# Syntax
python github_admin_cli.py {repo_name} {action}

# Examples
python github_admin_cli.py stockitweb check
python github_admin_cli.py stockitweb archive
python github_admin_cli.py stockitweb unarchive
python github_admin_cli.py stockitweb private
python github_admin_cli.py stockitweb public`

Example output:

`✅ archive stockitweb -> 200
private=False archived=True`

* * * * *

🧰 Supported Actions
--------------------

| Action | HTTP Method | JSON Body | Description |
| --- | --- | --- | --- |
| `archive` | PATCH | `{ "archived": true }` | Archive a repository |
| `unarchive` | PATCH | `{ "archived": false }` | Unarchive a repository |
| `private` | PATCH | `{ "private": true }` | Make repository private |
| `public` | PATCH | `{ "private": false }` | Make repository public |
| `check` | GET | --- | Display current visibility & archive status |

* * * * *

⚙️ Configuration
----------------

You can also create an **`.env.example`** file in the root directory:

`GITHUB_TOKEN=
OWNER=stere8`

Then load it using `os.environ` or `python-dotenv` (optional enhancement).

* * * * *

❗ Error Codes
-------------

| Code | Meaning | Common Fix |
| --- | --- | --- |
| 200--299 | ✅ Success | --- |
| 401 | ❌ Invalid or missing token | Check `GITHUB_TOKEN` |
| 403 | 🚫 Insufficient token scope | Recreate token with `repo` permission |
| 404 | 🔎 Repository not found | Check owner/repo name |
| 422 | ⚙️ Invalid request body | Ensure correct JSON keys/booleans |

* * * * *

🧑‍💻 Development
-----------------

Project layout (recommended modern **src/** structure):

`github-admin-cli/
├── README.md
├── pyproject.toml
├── LICENSE
├── .env.example
├── .gitignore
├── SECURITY.md
├── .github/
│   └── dependabot.yml
├── src/
│   └── github_admin_cli/
│       ├── __main__.py
│       ├── cli.py
│       ├── client.py
│       └── utils.py
└── tests/
 └── test_cli.py `

Run tests:

`pytest -q`

Lint & security checks (once CI is set up):

`ruff check .
pip-audit`

* * * * *

🧩 Roadmap
----------

-   Add `--dry-run` flag to preview requests

-   Add bulk mode for multiple repos

-   Publish to **PyPI**

-   Add support for listing all repos under an org

-   Integrate colored console output

* * * * *

🔒 Security Policy
------------------

If you discover a vulnerability, please report it responsibly:\
open a private [Security Advisory](https://github.com/stere8/github-admin-cli/security/advisories)\
or email **security@oracleconsults.netlify.app**.

See <SECURITY.md> for full details.

* * * * *

📄 License
----------

Distributed under the **MIT License**.\
See <LICENSE> for details.

* * * * *

🤝 Acknowledgements
-------------------

-   GitHub REST API Docs

-   Requests Library

-   Python CLI Patterns

* * * * *

> *"Simple automation beats manual repetition."*\
> --- **Oreste Twizeyimana**

 `---

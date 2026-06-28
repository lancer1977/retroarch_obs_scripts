#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

PYTHONPATH=src:tests python -m unittest discover -s tests -p 'test_*.py' -v

if command -v pip-audit >/dev/null 2>&1; then
  pip-audit -r requirements.txt
else
  python -m pip_audit -r requirements.txt
fi

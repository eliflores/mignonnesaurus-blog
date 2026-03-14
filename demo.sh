#!/usr/bin/env bash

set -euo pipefail

if [[ -z "${PIPENV_ACTIVE:-}" ]] && command -v pipenv >/dev/null 2>&1; then
	exec pipenv run bash "$0" "$@"
fi

: "${MY_BLOG_USERNAME:?Set MY_BLOG_USERNAME before running the demo.}"
: "${MY_BLOG_PASSWORD:?Set MY_BLOG_PASSWORD before running the demo.}"

python -m pytest demos/blog_demo.py -v --browser=firefox --server=localhost --port=8081 --demo_mode --slow --start_page=http://localhost:8081

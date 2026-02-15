
set -e

uv sync --no-dev
uv run --no-dev python scripts/01_clean_and_merge.py
uv run --no-dev python scripts/02_make_plot.py

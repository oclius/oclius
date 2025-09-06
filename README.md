# Oclius

Open-source computer vision repository using PyTorch.

## Installation

- Python: >= 3.10
- Create and activate a virtual environment:
  - `python3 -m venv .venv && source .venv/bin/activate`
- Install runtime dependencies:
  - `python -m pip install -r requirements.txt`
- Optional (development tools):
  - `python -m pip install -e .[dev]`

## Quick Start

- Show CLI help: `python scripts/train.py --help`
- Minimal run: `python scripts/train.py`

## Testing

- `python -m pytest -q`

## Repository Layout

```
oclius/
├─ pyproject.toml
├─ Makefile
├─ README.md
├─ .gitignore
├─ .editorconfig
├─ requirements.txt
├─ data/
│  ├─ .gitignore
│  └─ .gitkeep
├─ notebooks/
│  └─ .gitkeep
├─ scripts/
│  └─ train.py
├─ src/
│  └─ oclius/
│     ├─ __init__.py
│     ├─ version.py
│     ├─ data/__init__.py
│     ├─ models/__init__.py
│     └─ utils/__init__.py
└─ tests/
   └─ test_imports.py
```

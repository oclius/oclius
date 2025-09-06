PYTHON := python3

.PHONY: install-dev format lint test

install-dev:
	$(PYTHON) -m pip install -e .[dev]

format:
	$(PYTHON) -m black src tests
	ruff check --fix src tests

lint:
	ruff check src tests
	$(PYTHON) -m mypy src

test:
	pytest -q

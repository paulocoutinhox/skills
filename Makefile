.DEFAULT_GOAL := help

UV ?= uv
UV_CACHE_DIR ?= $(CURDIR)/.cache/uv
export UV_CACHE_DIR

.PHONY: help setup validate valide skills integrity test lint format-check format

help:
	@printf '%s\n' 'Paulo Skills commands' '' '  make setup         Install the locked contributor environment.' '  make validate      Run all format, integrity, test, and lint checks.' '  make valide        Alias for validate.' '  make skills        Validate every skill with skills-ref.' '  make integrity     Check documentation links and package boundaries.' '  make test          Run contributor-tool tests.' '  make lint          Run Ruff lint checks.' '  make format-check  Check Python formatting.' '  make format        Format Python source files.'

setup:
	$(UV) sync --locked

validate:
	$(UV) run --locked python scripts/validate-skills.py
	$(UV) run --locked python scripts/check-repository.py
	$(UV) run --locked python -m unittest discover -s tests -v
	$(UV) run --locked ruff check .
	$(UV) run --locked ruff format --check .

valide: validate

skills:
	$(UV) run --locked python scripts/validate-skills.py

integrity:
	$(UV) run --locked python scripts/check-repository.py

test:
	$(UV) run --locked python -m unittest discover -s tests -v

lint:
	$(UV) run --locked ruff check .

format-check:
	$(UV) run --locked ruff format --check .

format:
	$(UV) run --locked ruff format .

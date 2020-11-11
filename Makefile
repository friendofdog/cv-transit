.PHONY: test lint type-check

SHELL := /bin/bash

all: test lint type-check

test:
	set -a && set +a && \
	python3 -m pytest -q

lint:
	python3 -m flake8 tests/ cvtransit/

type-check:
	python3 -m mypy tests/*.py tests/**/*.py \
	cvtransit/*.py cvtransit/**/*.py

run:
	python3 -m cvtransit.app

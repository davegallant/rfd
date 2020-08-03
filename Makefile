
SRC := rfd
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

## build: Build a tar.gz of the python package
build:
> rm -rf dist/
> python setup.py sdist
.PHONY: build

## precommit: Run all pre-commit hooks
precommit:
> pre-commit run \
 --all-files \
 --show-diff-on-failure
.PHONY: precommit

## lint: Run static analysis on the code
lint:
> pylint $(SRC)
.PHONY: lint

## test: Run all unit tests
test: tmp/.tests-passed.sentinel
.PHONY: test

## examples: Run basic commands
examples: tmp/.tests-passed.sentinel
> rfd --version
> rfd threads >/dev/null
> rfd threads --sort-by score >/dev/null
> rfd search 'pizza' >/dev/null
> rfd search '(coffee|starbucks)' >/dev/null
.PHONY: examples

# Tests - re-ran if any file under src has been changed since tmp/.tests-passed.sentinel was last touched
tmp/.tests-passed.sentinel: $(shell find ${SRC} -type f)
> mkdir -p $(@D)
> pytest -v
> touch $@

## pr: Run pre-commit, lint and test
pr: precommit lint test
.PHONY: pr

ci: lint test examples
.PHONY: ci

## help: Print this help message
help:
> @echo "Usage:"
> @echo
> @sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /' | sort
> @echo
.PHONY: help

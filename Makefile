
SRC:=rfd

.PHONY: build
build:
	rm -rf dist/
	python setup.py sdist

.PHONY: push_test
push_test:
	twine upload -r testpypi dist/*.tar.gz

.PHONY: push_prod
push_prod:
	twine upload dist/*.tar.gz

.PHONY: precommit
precommit: ## Run pre-commit
	pre-commit run \
	--all-files \
	--show-diff-on-failure

.PHONY: lint
lint:
	pylint $(SRC)

.PHONY: test
test:
	pytest -v

.PHONY: pr
pr: precommit lint test

.PHONY: ci
ci: lint test

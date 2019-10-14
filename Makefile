
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
	--show-diff-on-failure \
	|| \
	( \
	echo "" && \
	echo "##################################################################################" && \
	echo "If this is on CI, please initialize pre-commit locally using \"make precommit\"." && \
	echo "Otherwise, view the modifications pre-commit has made, then stage and commit them." && \
	echo "For more information: https://pre-commit.com/#usage" && \
	echo "##################################################################################" && \
	echo ""; \
	exit 1)


.PHONY: lint
lint:
	pylint rfd

.PHONY: test
test:
	pytest -v


.PHONY: pr
pr: precommit lint test

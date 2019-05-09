.PHONY: help build clean setup install release-check type-check flake8-check lint tests twine-release-test

.DEFAULT: help
help:
	@echo "make build"
	@echo "       build distribution directories"
	@echo "make clean"
	@echo "       clean distribution directories"
	@echo "make setup"
	@echo "       setup development environment"
	@echo "make install"
	@echo "       install dependencies"
	@echo "make type-check"
	@echo "       run mypy type checking"
	@echo "make flake8-check"
	@echo "       run flake8 code style check"
	@echo "make lint"
	@echo "       run pylint"
	@echo "make tests"
	@echo "       run unit and doc tests"
	@echo "make release-check"
	@echo "       run type-check, flake8 check, linting and tests"
	@echo "make twine-release-test"
	@echo "       release ftoolz to test pypi using twine"

build: clean
	@echo ">>> building ftoolz distribution"
	pipenv run build

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

setup:
	pipenv install --dev

install:
	pipenv install

type-check:
	@echo ">>> checking types in ftoolz and tests"
	pipenv run type-check || ( echo ">>> type check failed"; exit 1; )

flake8-check:
	@echo ">>> enforcing PEP 8 style with flake8 in ftoolz and tests"
	pipenv run flake8-check || ( echo ">>> flake8 check failed"; exit 1; )

lint:
	@echo ">>> linting code"
	pipenv run lint || ( echo ">>> linting failed"; exit 1; )

tests:
	@echo ">>> running tests"
	pipenv run tests || ( echo ">>> tests failed"; exit 1; )

release-check: type-check flake8-check lint tests

twine-release-test: build
	pipenv run release-test

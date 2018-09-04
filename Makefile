.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

init:  ## setup environment
	pipenv install --dev

clean: clean-npm clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-npm: ## cleans npm module
	rm -fr node_module

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr docs/_build
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -f result.xml
	rm -f coverage.xml

lint: ## check style with flake8
	flake8 webpage_parser tests

test: ## run tests quickly with the default Python
	py.test \
	  --cov-config .coveragerc \
	  --junitxml=result.xml \
	  --cov=. \
	  --cov-report term \
	  --cov-report xml \
	  --cov-report term-missing


test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source webpage_parser -m pytest
	coverage report -m

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/webpage_parser.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ webpage_parser
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

dist: clean  ## builds the eggs and wheel.
	python setup.py sdist
	python setup.py bdist_egg
	python setup.py bdist_wheel

	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

version:  ## returns current version.
	@python setup.py --version

history:  ## generate HISTORY.rst
	pipenv run gitchangelog > HISTORY.rst

bumpmajor: ## increments major version release
	bumpversion major --verbose

bumpminor: ## increments minor version release
	bumpversion minor --verbose

bumppatch: ## increments patch version release
	bumpversion patch --verbose

tag:  ## Create tags
	git tag -a $$(python setup.py --version) -m $$(python setup.py --version)

release: dist  ## releases the product.
	twine upload --config-file /twine/.pypirc dist/*

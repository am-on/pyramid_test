CONFIG = development.ini

.DEFAULT_GOAL := build

build:
	@virtualenv -p python3.6 env
	@python3 -m venv env
	@env/bin/pip install --upgrade pip setuptools
	@env/bin/pip install -r requirements.txt -e .
	@env/bin/initialize_pyramid_test_db $(CONFIG)

populate:
	@env/bin/python3 pyramid_test/scripts/populate.py $(CONFIG)

run:
	@env/bin/pserve $(CONFIG)

test:
	@env/bin/flake8 pyramid_test
	@env/bin/pytest --cov --cov-report=term-missing --cov-report=html

isort:
	@env/bin/isort pyramid_test -rc -sl

package: pip-compile pipdeptree

pip-compile:
	@env/bin/pip-compile --output-file requirements.txt setup.py requirements-dev.in

pip-upgrade:
	@env/bin/pip-compile --upgrade --output-file requirements.txt setup.py requirements-dev.in

pipdeptree:
	@env/bin/pipdeptree > requirements-tree.txt

pip-sync:
	@env/bin/pip-sync

clean:
	@rm -rf env
	@rm -rf __pycache__
	@rm -rf .cache
	@rm -f pyramid_test.sqlite
	@rm -rf htmlcov
	@rm -f .coverage

help:
	@echo -e ""
	@echo -e "    build [CONFIG=development.ini]"
	@echo -e "        Build pyramid_test application and configure the database with given configuration (default: development.ini).\n"
	@echo -e "    populate [CONFIG=development.ini]"
	@echo -e "        Populate database with dummy data with given configuration (default: development.ini).\n"
	@echo -e "    run [CONFIG=development.ini]"
	@echo -e "        Run pyramid_test application with given configuration (default: development.ini).\n"
	@echo -e "    test"
	@echo -e "        Check code style with flake8 and run py.test.\n"
	@echo -e "    isort"
	@echo -e "        Sort import statements.\n"
	@echo -e "    pip-compile"
	@echo -e "        Generate requirements.txt file.\n"
	@echo -e "    pip-upgrade"
	@echo -e "        Upgrade requirements versions in requirements.txt.\n"
	@echo -e "    pipdeptree"
	@echo -e "        Write installed python packages in form of a dependency tree in requirements-tree.txt.\n"
	@echo -e "    pip-sync"
	@echo -e "        Synchronize current environment by installing modules that match requirements.txt and uninstalling the ones that don't.\n"
	@echo -e "    clean"
	@echo -e "        Delete projetc enviroment and cache.\n"

.PHONY: run build populate test isort help

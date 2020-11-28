SHELL := /bin/bash

# Colors
RED = `tput setaf 1`
GREEN = `tput setaf 2`
RESET = `tput sgr0`


run3:
	@echo -e "${GREEN}Running problem 3...${RESET}"
	@pipenv run python ./problem3/main.py


runall: run3


lint: guard-against-PIPENV_ACTIVE
	@echo -e "${GREEN}Blacking...${RESET}"
	@pipenv run black .

	@echo -e "${GREEN}Running Pylint...${RESET}"
	-@pipenv run pylint -f colorized -s n --rcfile config/pylint.ini problem3


clean:
	@echo -e "${GREEN}Deleting generated chaff...${RESET}"
	@rm -rf .pytest_cache .coverage .pytest_cache coverage.xml


purge: down clean guard-against-PIPENV_ACTIVE
	@echo -e "${GREEN}Removing venv...${RESET}"
	-@pipenv --rm


init: guard-against-PIPENV_ACTIVE
	@echo -e "${GREEN}Creating venv...${RESET}"
	@pipenv install --dev


update: guard-against-PIPENV_ACTIVE
	@echo -e "${GREEN}Upgrading packages...${RESET}"
	@pipenv update

	@echo -e "${GREEN}Updating lock file...${RESET}"
	@pipenv lock


guard-against-%:
	@if [ ! "${${*}}" = "" ]; then \
		echo -e "${RED}Please execute make command outside venv.${RESET}"; \
		exit 1; \
	fi


.PHONY: run3 runall lint clean purge init update
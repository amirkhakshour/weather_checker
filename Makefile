.PHONY: install server

##################
# Run locally
##################
install:
	poetry shell
	poetry install

server:
	@poetry run python -m checker.manage run

PYTEST = py.test
.PHONY: install server test retest coverage

##################
# Run locally
##################
install:
	poetry shell
	poetry install

server:
	@poetry run python -m checker.manage run

##################
# Tests and checks
##################
test:## Run tests
	@poetry run $(PYTEST)

retest: ## Run failed tests only
	@poetry run $(PYTEST) --lf

coverage: ## Generate coverage report
	@poetry run $(PYTEST) --cov=checker --cov-report=term-missing

##################
# Run on docker
##################
docker-build:
	docker-compose build

docker-run:
	docker-compose up

docker-test:
	docker-compose run -v $(PWD)/tests:/app/tests:ro app pytest

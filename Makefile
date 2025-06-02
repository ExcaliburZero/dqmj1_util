.PHONY: format lint test coverage_report docs

format:
	ruff check --select I --fix .
	ruff format .
	
lint:
	ruff check .
	mypy .
	ruff format --check .

test:
	pytest tests

coverage_report:
	pytest --cov-report=html:coverage --cov-report=lcov:coverage.info --cov=dqmj1_util tests

docs:
	cd docs && make html
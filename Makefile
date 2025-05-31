.PHONY: format lint test coverage_report

format:
	ruff check --select I --fix .
	ruff format .
	
lint:
	mypy .
	ruff format --check .
	ruff check .

test:
	pytest tests

coverage_report:
	pytest --cov-report=html:coverage --cov-report=lcov:coverage.info --cov=dqmj1_util tests
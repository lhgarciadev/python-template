install:
	uv pip install --upgrade pip &&\
		uv pip install -r requirements.txt

test:
	uv run -m pytest -vv \
		--cov=main --cov-branch --cov-report=term-missing \
 		--cov-fail-under=90 tests/

format:	
	uv run ruff format main.py tests

lint:
	uv run ruff check main.py tests --fix

refactor: format lint

deploy:
	# deploy goes here
		
all: install lint test format deploy
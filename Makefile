.PHONY: help install test lint format clean docker-build docker-run docker-stop

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code"
	@echo "  clean        - Clean up temporary files"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"
	@echo "  docker-stop  - Stop Docker container"
	@echo "  security     - Run security checks"
	@echo "  coverage     - Generate coverage report"

# Install dependencies
install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install pytest pytest-cov pytest-mock pytest-asyncio
	pip install ruff black isort mypy bandit safety

# Run tests
test:
	python -m pytest test_*.py -v --cov=. --cov-report=term-missing

# Run linting
lint:
	ruff check .
	black --check --diff .
	isort --check-only --diff .
	mypy --ignore-missing-imports .

# Format code
format:
	ruff format .
	black .
	isort .

# Clean up
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
	rm -rf *.egg-info/

# Docker commands
docker-build:
	docker build -t grok-1:latest .

docker-run:
	docker run -d --name grok-1-app -p 8000:8000 grok-1:latest

docker-stop:
	docker stop grok-1-app || true
	docker rm grok-1-app || true

# Security checks
security:
	bandit -r . -f json -o bandit-report.json
	safety check --json --output safety-report.json

# Coverage report
coverage:
	python -m pytest --cov=. --cov-report=html --cov-report=term-missing

# Development setup
dev-setup: install
	pre-commit install

# Run all checks
check: lint test security
	@echo "All checks completed!"

# Quick start
start: install test
	@echo "Setup complete! Run 'python run.py' to start the application." 
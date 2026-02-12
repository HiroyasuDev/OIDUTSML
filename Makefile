.PHONY: help install dev build start test lint format clean docker-build docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	npm install

dev: ## Start development server
	npm run dev

build: ## Build for production
	npm run build

start: ## Start production server
	npm start

test: ## Run tests
	npm test

test-coverage: ## Run tests with coverage
	npm run test:coverage

lint: ## Lint code
	npm run lint

format: ## Format code
	npm run format

clean: ## Clean build artifacts
	npm run clean
	rm -rf logs/*.log

docker-build: ## Build Docker image
	npm run docker:build

docker-up: ## Start Docker containers
	npm run docker:run

docker-down: ## Stop Docker containers
	npm run docker:down

type-check: ## Type check TypeScript
	npm run type-check

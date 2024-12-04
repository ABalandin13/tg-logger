# Define variables
DOCKER_COMPOSE_FILE=docker-compose.yml
PROJECT_NAME=communication

# Default target
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make up          - Start the services defined in docker-compose.yml"
	@echo "  make down        - Stop and remove containers, networks, and volumes"
	@echo "  make restart     - Restart all services"
	@echo "  make build       - Build or rebuild the services"
	@echo "  make logs        - View the logs for all services"
	@echo "  make ps          - List containers"
	@echo "  make exec-db     - Open a shell in the PostgreSQL container"
	@echo "  make clean       - Remove all containers, networks, and volumes"

# Targets
.PHONY: up
up:
	docker-compose -f $(DOCKER_COMPOSE_FILE) -p $(PROJECT_NAME) up -d

.PHONY: down
down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) -p $(PROJECT_NAME) down

.PHONY: restart
restart: down up

.PHONY: build
build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) -p $(PROJECT_NAME) build

.PHONY: logs
logs:
	docker-compose -f $(DOCKER_COMPOSE_FILE) -p $(PROJECT_NAME) logs -f

.PHONY: ps
ps:
	docker-compose -f $(DOCKER_COMPOSE_FILE) -p $(PROJECT_NAME) ps

.PHONY: exec-db
exec-db:
	docker exec -it postgres_db psql -U postgres -d communication

.PHONY: clean
clean: down
	docker volume rm -f $(shell docker volume ls -q | grep $(PROJECT_NAME) || true)
	docker network rm -f $(shell docker network ls -q | grep $(PROJECT_NAME) || true)
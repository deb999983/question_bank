TAG ?= local

build:
	docker build -f deploy/web_server/Dockerfile -t question_bank_api:${TAG} .
	docker build -f deploy/db//Dockerfile -t question_bank_db:${TAG} .

up:
	docker-compose up -d

down:
	docker-compose down

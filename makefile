TAG ?= local
SERVICES ?= question_bank_db question_bank_api

build:
	docker build -f deploy/web_server/Dockerfile -t question_bank_api:${TAG} .
	docker build -f deploy/db//Dockerfile -t question_bank_db:${TAG} .

up:
	docker-compose up ${SERVICES} -d

down:
	docker-composme ${SERVICES} down

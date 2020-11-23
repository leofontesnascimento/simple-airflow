.PHONY: build build-no-cache up logs list_dags test-dag test-python shell down

ENV := development

build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

start:
	docker-compose up -d

stop:
	docker-compose down

logs-tail:
	docker-compose logs -f --tail 40

list-dags:
	docker-compose run --rm webserver airflow list_dags

test-dag:
	docker-compose run --rm webserver airflow test [DAG_ID] [TASK_ID] [EXECUTION_DATE]

test-python:
	docker-compose run --rm webserver python /usr/local/airflow/dags/[PYTHON-FILE].py

shell:
	docker exec -it simple-airflow-webserver bash

shell-db:
	docker exec -it simple-airflow-postgres bash

docker-reset-images:
	docker rmi -f $(docker images -a -q)

docker-stop-containers:
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)

K8E_DIR := k8s

up:
	docker compose up -d

down:
	docker compose down


build-all : build-fastapi-image build-streamlit-image

build-fastapi-image:
	docker build --no-cache -t fastapi:latest fastapi
	docker tag fastapi:latest anku22/full-stack-be:latest
	docker push anku22/full-stack-be:latest

build-streamlit-image:
	docker build --no-cache -t streamlit:latest streamlit;
	docker tag streamlit:latest anku22/full-stack-fe:latest;
	docker push anku22/full-stack-fe:latest;


run-all: run-fastapi run-streamlit run-redis

run-redis:
	kubectl apply -f $(K8E_DIR)/redis-statefulset.yaml


run-fastapi: run-fastapi-deploy run-fastapi-service

run-fastapi-deploy:
	kubectl apply -f $(K8E_DIR)/fastapi-deployment.yaml

run-fastapi-service:
	kubectl apply -f $(K8E_DIR)/fastapi-service.yaml


run-streamlit: run-streamlit-deploy run-streamlit-service

run-streamlit-deploy:
	kubectl apply -f $(K8E_DIR)/streamlit-deployment.yaml

run-streamlit-service:
	kubectl apply -f $(K8E_DIR)/streamlit-service.yaml


stop-all: stop-fastapi stop-streamlit stop-redis

stop-redis:
	kubectl delete -f $(K8E_DIR)/redis-statefulset.yaml


stop-fastapi: stop-fastapi-deploy stop-fastapi-service

stop-fastapi-deploy:
	kubectl delete -f $(K8E_DIR)/fastapi-deployment.yaml

stop-fastapi-service:
	kubectl delete -f $(K8E_DIR)/fastapi-service.yaml


stop-streamlit: stop-streamlit-deploy stop-streamlit-service

stop-streamlit-deploy:
	kubectl delete -f $(K8E_DIR)/streamlit-deployment.yaml

stop-streamlit-service:
	kubectl delete -f $(K8E_DIR)/streamlit-service.yaml
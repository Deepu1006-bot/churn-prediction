# LAB 13 - End-to-End MLOps System Mini Project

## Aim
To develop and integrate an end-to-end MLOps system incorporating preprocessing, experiment tracking, validation, deployment, monitoring, retraining and lifecycle management.

## Implementation
1. Used the existing churn prediction API.
2. Configured a Dockerfile using Python 3.11.
3. Installed API dependencies using requirements-api.txt.
4. Included the production model and preprocessor in the Docker image.
5. Built the Docker image churn-prediction-api:lab11.
6. Started the container on port 8000.
7. Verified the FastAPI health endpoint.
8. Tested an individual customer churn prediction.
9. Applied the Kubernetes Deployment and Service manifests.
10. Verified the Kubernetes pod and service.
11. Tested the Kubernetes API using port forwarding.

## Experimental Results

### Docker
- Docker image build: Successful.
- Container startup: Successful.
- Production model V1 loaded successfully.
- Preprocessor loaded successfully.
- API health status: healthy.

### Prediction Testing
- Test customer ID: TEST001
- Predicted class: 1 (Churn)
- Churn probability: 0.757495

### Kubernetes
- Kubernetes client version: v1.36.1
- Cluster node: desktop-control-plane
- Node status: Ready.
- Deployment pod status: Running.
- Pod readiness: 1/1.
- Service type: NodePort.
- Service port: 30080.
- Port-forward health test: healthy.

## Result
Successfully built and tested the Dockerized churn prediction API and verified its deployment through the Kubernetes cluster. The production model was loaded and used for actual prediction testing.

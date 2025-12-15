# Local MLOps Sentiment Analysis Project

## Overview
[Copy from Project Overview above]

## Setup
1. Clone repo: `git clone https://github.com/<username>/local-mlops-sentiment.git`
2. Install deps: `pip install -r requirements.txt`
3. DVC setup: `dvc remote add -d local ./dvc_cache` (or MinIO as above)
4. Create Kind cluster: `kind create cluster --config kind-config.yaml`
5. Create GHCR secret in Kind: `kubectl create secret docker-registry ghcr-secret --docker-server=ghcr.io --docker-username=<username> --docker-password=<GHCR_TOKEN>`
6. Run MLflow: `mlflow ui --port 5000`

## Usage
1. Run pipeline: `dvc repro`
2. Build Docker: `docker build -t ghcr.io/<username>/sentiment-api:latest .`
3. Push to GHCR: `docker push ghcr.io/<username>/sentiment-api:latest` (after login: `echo $GHCR_TOKEN | docker login ghcr.io -u <username> --password-stdin`)
4. Deploy to Kind: `kubectl apply -f k8s/`
5. Access API: http://localhost:8080/predict (port-forward if needed: `kubectl port-forward svc/sentiment-service 8080:80`)
6. Monitoring: Deploy prometheus/grafana, access dashboards.
7. Chrome Extension: Load unpacked in Chrome developer mode, test on YouTube.

## Testing
- Curl test: `curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d '{"text": "Great!"}'`
- Drift check: Run src/monitor.py on new data.

## Troubleshooting
- GHCR auth: Ensure PAT has packages scope.
- Kind ports: Check `kubectl get svc`.
- DVC: If MinIO issues, fallback to local FS.
- Scale: Increase replicas in deployment.yaml.

For full replication, follow the blueprint document.
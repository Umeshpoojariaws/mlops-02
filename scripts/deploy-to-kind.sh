#!/bin/bash

# Script to deploy latest image from GHCR to local Kind cluster

set -e

# Your GitHub username (lowercase)
OWNER="your-github-username"  # ← CHANGE THIS
IMAGE="ghcr.io/$OWNER/sentiment-api:latest"

echo "Pulling latest image: $IMAGE"
kind load docker-image $IMAGE --name kind

echo "Applying Kubernetes manifests..."
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

echo "Deployment complete!"
echo "Access API at: http://localhost:8080"
echo "To port-forward: kubectl port-forward svc/sentiment-service 8080:80"
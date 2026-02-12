#!/bin/bash

set -e

echo "Deploying the monolith to Kubernetes... "
kubectl apply -f k8s/monolith/deployment.yaml
kubectl get pods


#!/bin/bash

set -e

echo "Deploying the monolith to Kubernetes... "
kubectl apply -f k8/monolith/deployment.yaml
kubectl get pods


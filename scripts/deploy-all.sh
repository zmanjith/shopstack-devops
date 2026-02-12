#!/bin/bash

set -e

# source scripts/env.sh


echo "Deploying storage..."
kubectl apply -f ~/shopstack-devops/k8s/storage/

echo "Deploying microservices ... "
kubectl apply -f ~/shopstack-devops/k8s/microservices/order-service
kubectl apply -f ~/shopstack-devops/k8s/microservices/user-service
kubectl apply -f ~/shopstack-devops/k8s/microservices/product-service

echo "Deploying Ingress ...."
kubectl apply -f ~/shopstack-devops/k8s/ingresss/

echo "Waiting for Deployments .... "
kubectl rollout status deployment product-service
kubectl rollout status deployment user-service
kubectl rollout status deployment order-service

echo " DEPLOYMENT COMPLETE"



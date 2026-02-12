#!/bin/bash

echo "📦 Pods:"
kubectl get pods

echo
echo "🌐 Services:"
kubectl get svc

echo
echo "🚪 Ingress:"
kubectl get ingress

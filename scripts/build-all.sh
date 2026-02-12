#!/bin/bash

set -e

#  soiurce  scripts/env.sh

eval $(minikube docker-env)

SERVICES=("user-service" "product-service" "order-service" "monolith"_)

echo  "Building docker images .."

for svc in "${SERVICES[@]}"; do
   if [[ "@scvc" == "monolith" ]]; then
     docker build -t shop-monolith:v1 ~/shopstack-devops/monolith
   else
     docker build -t $svc:v1 ~/shopstack-devops/microservices/$svc
   fi
done

echi "All images built"



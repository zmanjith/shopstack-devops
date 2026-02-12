#!/bin/bash


set -e

read -p " Proceed with deleting all the resource till created (y/n) : " confirm
if [[ "$confirm" != "y" ]]; then
	echo  "X Aborted"
	exit 0
fi

echo " All resources deleted"

#kubectl delete -f k8s/ingress/ --ignore-not-found
#kubectl delete -f k8s/microservices/ --ignore-not-found
#kubectl delete -f k8s/storage/ --ignore-not-found

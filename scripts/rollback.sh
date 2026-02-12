#!/bin/bash

set -e

if [[ -z "$1" ]]; then
  echo " Usage: ./scripts/rollback.sh <deployment-name> "
  exit 1
fi

DEPLOYMENT=$1
REVISION_COUNT=$(kubectl rollout history deployment $DEPLOYMENT)

if [ "$REVISION_COUNT" -gt 1 ]; then
   echo " There is no previous version for the currnet $DEPLOYMENT"
   exit 0
else
  echo "Rolling Back $DEPLOYMENT ... "
  kubectl rollout undo deployment $DEPLOYMENT
  kubectl rollout status deployment $DEPLOYMENT
fi
echo "Rollback COMPLETED"



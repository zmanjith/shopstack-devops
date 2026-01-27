#!/bin/bash

set -e

IMAGE_NAME=shop-monolith
TAG=v1

echo "Building Docker Image...."
docker build -t $IMAGE_NAME:$TAG monolith/



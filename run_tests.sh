#!/bin/bash

## build image
#docker build -t austin .
#sleep 3

# build container
docker-compose up -d
sleep 5

# run pytest
pytest -v

# kill container
docker-compose down

## destroy image
#docker rmi austin
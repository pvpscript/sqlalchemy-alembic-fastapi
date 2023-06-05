#!/bin/sh

echo -e "\nPulling postgres for docker"
docker pull postgres

echo -e "\nRunning container"
docker-compose up -d

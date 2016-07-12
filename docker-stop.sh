#!/bin/bash

docker kill proxy
docker kill tmpnb
docker rm proxy
docker rm tmpnb

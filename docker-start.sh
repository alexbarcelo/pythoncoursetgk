#!/bin/bash

docker pull alexbarcelo/pythoncoursetgk-notebook

export TOKEN=$( head -c 30 /dev/urandom | xxd -p )
docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN --name=proxy jupyter/configurable-http-proxy --default-target http://127.0.0.1:9999
docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN --name=tmpnb \
	-v /var/run/docker.sock:/docker.sock jupyter/tmpnb \
	python orchestrate.py \
		--image='alexbarcelo/pythoncoursetgk-notebook' \
		--command="jupyter notebook"

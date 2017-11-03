#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMAGE_NAME="soar/python-webserver-training"

if [ "$1" == "init" ]; then
	docker build -t $IMAGE_NAME $DIR
elif [ "$1" == "run" ]; then
	docker run --rm -v $DIR:/python_webserver_training \
		$IMAGE_NAME python3 webserver.py "${@:2}"
else
	echo "usage: docker_build [init | run]"
fi


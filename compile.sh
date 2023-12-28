#!/usr/bin/env bash

pip freeze > requirements.txt

# TODAY=$(date +'%Y%m%d')

docker build . --tag keyword/linux:latest

# --no-cache --progress plain

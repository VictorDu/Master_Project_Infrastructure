#!/bin/bash

#Build all docker images
service docker restart
for directory in $(dirname $(pwd))/Dockerfile_Folder/* ; do
    docker build -t $(basename $directory) $directory
done

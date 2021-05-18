#!/usr/bin/env bash

PORT=$1

if [ "$PORT" = "" ]; then
    PORT='5000'
fi

bin/base.sh runserver -p $PORT

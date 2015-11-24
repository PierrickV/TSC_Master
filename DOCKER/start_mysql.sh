#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch mysql container link with tsc_database file

docker run \
 --name tsc_database \
 -e MYSQL_ROOT_PASSWORD="zIDCUiY55YwBOkQKbML2"  \
 -v /home/docker/mysql:/var/lib/mysql \
 -p 127.0.0.1:3306:3306 \
 -d mysql
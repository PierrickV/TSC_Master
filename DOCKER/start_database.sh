#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch mysql container link with tsc_database file

docker rm -f tsc_database

docker run \
        --name tsc_database \
        --restart=always \
        -e MYSQL_ROOT_PASSWORD="django" \
        -e MYSQL_ALLOW_EMPTY_PASSWORD="no" \
        -e MYSQL_USER="django"  \
        -e MYSQL_PASSWORD="django"  \
        -e MYSQL_DATABASE="tsc_database"  \
        -v /home/docker/mysql:/var/lib/mysql/:rw \
        -v /home/docker/Git/TSC/DOCKER/DATABASE/config_files/:/etc/mysql/:rw \
        -p 127.0.0.1:3306:3306 \
        -d mysql


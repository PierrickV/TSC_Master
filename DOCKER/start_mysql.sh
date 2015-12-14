#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch mysql container link with tsc_database file

docker run \
 --name tsc_database \
 --restart=always \
 -e MYSQL_ROOT_PASSWORD="zIDCUiY55YwBOkQKbML2"  \
 -v /home/alababa/git/tardigrade_security_challenge/WWW/:/var/lib/mysql \
 -p 127.0.0.1:3306:3306 \
 -d mysql

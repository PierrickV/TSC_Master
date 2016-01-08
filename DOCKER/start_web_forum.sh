#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f tsc_web_forum

docker run -it \
        --name tsc_web_forum \
        --restart=always \
        -v /home/alababa/git/tardigrade_security_challenge/WWW/forum:/var/www/forum:rw \
        -p 8080:80 \
        --link tsc_database \
        -d tsc/master:Web_forum
#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f tsc_web
docker run -it \
--name tsc_web \
-v /home/alababa/git/tardigrade_security_challenge/WWW:/var/www:rw \
-p 127.0.0.1:80:80 \
--link tsc_database \
-d tsc/master:Web
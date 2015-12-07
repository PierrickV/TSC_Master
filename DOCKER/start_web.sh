#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f tsc_web

docker run -it \
--name tsc_web \
--restart=always \
-v /home/docker/Git/TSC/WWW:/var/www:ro \
-p 80:80 \
-d tsc/master:Web

#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-gunicorn-django container link with tsc's webfiles

docker rm -f tsc_web

docker run -it \
        --name tsc_web \
        --restart=always \
        -v /home/docker/Git/TSC/WWW:/var/www:rw \
        -v /home/docker/challenges_non_valider:/var/www/:rw \
        --cap-add SYS_ADMIN --device /dev/fuse \
        -p 80:80 \
        --link tsc_database \
        -d tsc/master:Web

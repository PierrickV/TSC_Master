#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f tsc_web

docker run -it \
    --name tsc_web \
    --restart=always \
    -v /home/docker/Git/TSC/WWW:/var/www:rw \
    -v /home/docker/nv_challenges:/nv_challenges:rw \
    --privileged --cap-add=MKNOD --cap-add=SYS_ADMIN --device=/dev/fuse \
    -p 10.8.96.7:443:443 \
    -p 10.8.96.7:80:80 \
    --link tsc_database \
    --link tsc_web_forum \
    -d tsc/master:Web

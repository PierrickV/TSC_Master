#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f tsc_web

docker run -it \
    --name tsc_web \
    --restart=always \
    -v /home/alababa/git/tardigrade_security_challenge/WWW/main:/var/www/main:rw \
    -v /home/alababa/nv_challenges:/nv_challenges:rw \
    --privileged --cap-add=MKNOD --cap-add=SYS_ADMIN --device=/dev/fuse \
    -p 127.0.0.1:443:443 \
    -p 127.0.0.1:80:80 \
    --link tsc_database \
    -d tsc/master:Web
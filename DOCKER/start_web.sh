#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f tsc_web

docker run -it \
        --name tsc_web \
        --hostname tsc.itinet.fr \
        --restart=always \
        -v $(pwd)/../WWW:/var/www:rw \
        -v ~/nv_challenges:/nv_challenges:rw \
        --privileged --cap-add=MKNOD --cap-add=SYS_ADMIN --device=/dev/fuse \
        -p 443:443 \
        -p 80:80 \
        --link tsc_database \
        --link forum.tsc.itinet.fr \
        -d tsc/master:Web

#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker rm -f forum.tsc.itinet.fr

docker run -it \
        --name forum.tsc.itinet.fr \
        --hostname forum.tsc.itinet.fr \
        --restart=always \
        -v $(pwd)/../WWW/forum:/var/www/forum:rw \
        --link tsc_database \
        -d tsc/master:Web_forum

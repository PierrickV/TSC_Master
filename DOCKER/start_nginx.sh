#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

docker run -it \
 --name tsc_web \
 --restart=always \
 -v /home/lilyus/Git/TSC/WWW/:/var/www:ro \
 -p 127.0.0.1:80:80 \
 -d tsc/master:Web

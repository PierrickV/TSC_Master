#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

django_www_files="/home/lilyus/Git/TSC/WWW:/var/www:ro"

docker run -it \
 --name tsc_web \
 -v $django_www_files \
 -p 127.0.0.1:80:80 \
 -d tsc/master:Web \
 /bin/bash

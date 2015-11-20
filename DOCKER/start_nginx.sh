#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

django_www_files="/home/lilyus/Git/TSC/WWW:/var/www:ro"
gunicorn_log_volume="/var/log/docker/gunicorn:/var/log/gunicorn:rw"
nginx_log_volume="/var/log/docker/nginx:/var/log/nginx:rw"

docker run -it \
 --name tsc_web \
 -v $django_www_files \
 -p 80:80 \
 -d tsc/master:Web \
 /bin/bash

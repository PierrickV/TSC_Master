#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

django_www_files="/home/docker/www:/var/www:ro"
gunicorn_log_volume="/var/log/docker/gunicorn:/var/log/gunicorn:rw"
nginx_log_volume="/var/log/docker/nginx:/var/log/nginx:rw"

docker run --name tsc_web -v $django_www_files -d django_nginx
cd ..

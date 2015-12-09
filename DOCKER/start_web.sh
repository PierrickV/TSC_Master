#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-gunicorn-django container link with tsc's webfiles

docker rm -f tsc_web

docker run -it \
--name tsc_web \
-v /home/lilyus/Git/TSC/WWW:/var/www/django:ro \
-v /home/docker/challenges_non_valider:/var/www/:rw \
-p 127.0.0.1:80:80 \
-d tsc/master:Web

# -v "/home/alababa/Lien vers tardigrade_security_challenge/WWW":/var/www:ro \
# -v "/home/lilyus/Git/TSC/WWW":/var/www:ro \


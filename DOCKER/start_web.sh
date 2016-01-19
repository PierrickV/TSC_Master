#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

echo "Suppression de l'ancien conteneur .."
docker rm -f tsc_web

echo ".. démarrage du nouveau .."
docker run -it \
        --name tsc_web \
        --hostname tsc.itinet.fr \
        --restart=always \
        -v ~/git/tardigrade_security_challenge/WWW:/var/www:rw \
        -v ~/nv_challenges:/nv_challenges:rw \
        --privileged --cap-add=MKNOD --cap-add=SYS_ADMIN --device=/dev/fuse \
        -p 443:443 \
        -p 80:80 \
        --link tsc_database \
        --link forum.tsc.itinet.fr \
        -d tsc/master:Web

echo ".. mise à jours de la base de données"
docker exec -ti tsc_web /var/www/main/manage.py makemigrations
docker exec -ti tsc_web /var/www/main/manage.py syncdb

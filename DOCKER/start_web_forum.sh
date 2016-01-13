#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Launch nginx-django container link with tsc's webfiles

echo "Suppression de l'ancien conteneur .."
docker rm -f forum.tsc.itinet.fr

echo ".. démarrage du nouveau .."
docker run -it \
        --name forum.tsc.itinet.fr \
        --hostname forum.tsc.itinet.fr \
        --restart=always \
        -v ~/git/tardigrade_security_challenge/WWW/forum:/var/www/forum:rw \
        --link tsc_database \
        -d tsc/master:Web_forum

echo ".. mise à jours de la base de données"
docker exec -ti forum.tsc.itinet.fr /var/www/forum/manage.py createcachetable python manage.py createcachetable tsc_database.spirit_cache
docker exec -ti forum.tsc.itinet.fr /var/www/forum/manage.py syncdb
docker exec -ti forum.tsc.itinet.fr /var/www/forum/manage.py makemigrations
docker exec -ti forum.tsc.itinet.fr /var/www/forum/manage.py migrate
#docker exec -ti forum.tsc.itinet.fr /var/www/forum/manage.py collectstatic

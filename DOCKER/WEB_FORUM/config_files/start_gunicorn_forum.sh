#!/bin/bash

NAME="forum"
DJANGODIR=/var/www/forum
BIND=127.0.0.1:8080
USER=root
GROUP=webapps
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=project.settings.dev
DJANGO_WSGI_MODULE=project.wsgi
SECRET_KEY="2J9r9mtbm4BdRmcV4ExgVzEbKzkW4W7V8EUYm9cMQ8UGu"

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export SECRET_KEY

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
/usr/local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=$BIND \
  --log-level=debug \
  --log-file=/var/log/gunicorn/forum.log
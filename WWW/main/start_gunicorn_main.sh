#!/bin/bash

NAME="gunicorn_main"                              # Name of the application
DJANGODIR="/var/www/main/web_tsc"                 # Django project directory
IP=127.0.0.1:8000                                 # we will communicte using this unix socket
USER=gunicorn_main                                # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=settings                   # which settings file should Django use
DJANGO_WSGI_MODULE=wsgi                           # WSGI module name

echo "Starting $NAME as `whoami`"
#chown -R $USER:users /var/www/main/

# Activate the virtual environment
cd $DJANGODIR
source /var/www/main/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATHE:"/var/www/main/"


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=$IP \
  --log-level=debug \
  --log-file=/var/log/gunicorn/main.log \
  --settings=/var/www/main/web_tsc/settings.py

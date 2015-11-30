#!/bin/bash
# This script initializes the Django project. It will be executed (from 
# supervisord) every time the Docker image is run.

path_to_manage="/var/www/manage.py"

# Initialize Django project
python $path_to_manage collectstatic --noinput
python $path_to_manage syncdb --noinput
python $path_to_manage migrate --noinput

# Create a Django superuser named `root` if it doesn't yet exist
echo "Creating Django superuser named 'root'..."
if [ "$DJANGO_PRODUCTION" != "true" ]; then
    # We're in the dev environment
    if [ "$ROOT_PASSWORD" == "" ]; then
        # Root password environment variable is not set; so, load it from config.ini
        echo "from ConfigParser import SafeConfigParser; parser = SafeConfigParser(); parser.read('/code/config.ini'); from django.contrib.auth.models import User; print 'Root user already exists' if User.objects.filter(username='root') else User.objects.create_superuser('root', 'veran@intechinfo.fr', parser.get('general', 'ROOT_PASSWORD'))" | python $path_to_manage shell
    else
        # Root password environment variable IS set; so, use it
        echo "import os; from django.contrib.auth.models import User; print 'Root user already exists' if User.objects.filter(username='root') else User.objects.create_superuser('root', 'veran@intechinfo.fr', os.environ['ROOT_PASSWORD'])" | python $path_to_manage shell
    fi
else
    # We're in production; use root password environment variable
    echo "import os; from django.contrib.auth.models import User; print 'Root user already exists' if User.objects.filter(username='root') else User.objects.create_superuser('root', 'veran@intechinfo.fr', os.environ['ROOT_PASSWORD'])" | python $path_to_manage shell
fi

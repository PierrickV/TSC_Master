#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Create nginx-django container link with tsc's webfiles
# Container should be launch with start_nginx.sh script
FROM debian:jessie
MAINTAINER veran@intechinfo.fr

# Enable production settings by default; for development, this can be set to 
# `false` in `docker run --env`
ENV DJANGO_PRODUCTION=true
ENV DJANGO_SETTINGS_MODULE="settings"
ENV PYTHONPATH="/var/www/"

# Set terminal to be noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Update and install packages
RUN apt-get update && apt-get install -y \
	supervisor \
	python3-pip \
	python3-tz \
	python-gevent \
	libffi6 \
	libssl1.0.0 \
	libjs-jquery \
	libmysqlclient-dev \
	javascript-common \
	apt-utils \
	wget \
	nginx \
	git \
&& apt-get autoclean

#	python-sqlparse \
#	python-mysqldb \

ADD . /code
#ADD <source> <destination>
WORKDIR /code

# Install python requirement,install and patch gevent, install and patch setuptools installation and change python default version
RUN pip3 install --upgrade -r requirements.txt \
&& wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python \
&& ln -sf /usr/bin/python3.4 /usr/local/bin/python

#&& pip3 install 'cython>=0.23.4' git+git://github.com/gevent/gevent.git#egg=gevent \

# Expose ports
# 80 = Nginx
# 8000 = Gunicorn
EXPOSE 80 8000

# Configure Nginx
RUN cp /code/nginx.conf /etc/nginx/sites-available/django_docker.conf \
&& ln -s /etc/nginx/sites-available/django_docker.conf /etc/nginx/sites-enabled/django_docker.conf \
&& rm /etc/nginx/sites-enabled/default \
&& mkdir /var/log/gunicorn
# && cp /etc/nginx/sites-available/django_docker.conf /etc/nginx/nginx.conf
# \ && rm -r ../code


# Run Supervisor (i.e., start Nginx, and Gunicorn)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#CMD ["/usr/bin/python3.4","/home/lilyus/Git/TSC/DOCKER/NGINX/initialize.sh"]
ENTRYPOINT /usr/bin/supervisord

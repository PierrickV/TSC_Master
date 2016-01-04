#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Create nginx-gunicorn-django container link with tsc's webfiles
FROM debian:jessie
MAINTAINER veran@intechinfo.fr


# Set PYTHONPATH to django modules
ENV PYTHONPATH="/var/www/"

# Set terminal to be noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Update and install packages
RUN apt-get update && apt-get install -y \
	supervisor \
	python-pip \
	python-tz \
	python-gevent \
	python-mysqldb \
	python-dev \
	python-virtualenv \
	libffi6 \
	augeas-lenses \
	dialog \
	libaugeas0 \
	libffi-dev \
	libssl-dev \
	libmysqlclient-dev \
	libjpeg-dev \
	javascript-common \
	apt-utils \
	wget \
	nginx \
	git \
	sshfs \
&& apt-get autoclean

ADD config_files config_files
WORKDIR /config_files

# Install python requirement,install and patch gevent, install and patch setuptools installation and change python default version
RUN pip install --upgrade -r requirements.txt \
&& wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python

# Expose ports
EXPOSE 443

# Configure Nginx
RUN cp /config_files/nginx.conf /etc/nginx/sites-available/django_docker.conf \
&& cp /config_files/certs/tsc.itinet.fr.cert.pem /etc/nginx/tsc.itinet.fr.cert.pem \
&& cp /config_files/certs/tsc.itinet.fr.privkey.pem /etc/nginx/tsc.itinet.fr.privkey.pem \
&& ln -s /etc/nginx/sites-available/django_docker.conf /etc/nginx/sites-enabled/django_docker.conf \
&& rm /etc/nginx/sites-enabled/default \
&& mkdir /var/log/gunicorn \
&& mkdir -p /var/www/main \
&& mkdir -p /var/www/forum

#Configure django
RUN groupadd --system webapps \
&& useradd --system --gid webapps --home /var/www/main/ django_main \
&& useradd --system --gid webapps --home /var/www/forum/ django_forum \
&& chown -R django_main:users /var/www/main/ \
&& chown -R django_forum:users /var/www/forum/

# Run Supervisor (i.e., start Nginx, and Gunicorn)
COPY /config_files/supervisord.conf /etc/supervisor/supervisord.conf
COPY /config_files/supervisord_nginx_gunicorn.conf /etc/supervisor/conf.d/supervisord_nginx_gunicorn.conf

#CMD /bin/bash
CMD ["/usr/bin/supervisord"]

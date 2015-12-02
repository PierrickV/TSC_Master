#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Create nginx-gunicorn-django container link with tsc's webfiles
# Container should be launch with start_web.sh script
# Use "docker build --tag=tsc/master:Web . " to build nginx image
FROM debian:jessie
MAINTAINER veran@intechinfo.fr

# Environment variables
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
	libmysqlclient-dev \
	javascript-common \
	apt-utils \
	wget \
	nginx \
	git \
	sshfs \
&& apt-get autoclean

ADD config_files config_files
WORKDIR /config_files

# Install python requirement,install and patch gevent, install and patch setuptools installation and change python default version
RUN pip3 install --upgrade -r requirements.txt \
&& wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python \
&& ln -sf /usr/bin/python3.4 /usr/local/bin/python

# Expose ports
# 80 = Nginx
EXPOSE 80

# Configure Nginx
RUN cp /config_files/nginx.conf /etc/nginx/sites-available/django_docker.conf \
&& ln -s /etc/nginx/sites-available/django_docker.conf /etc/nginx/sites-enabled/django_docker.conf \
&& rm /etc/nginx/sites-enabled/default \
&& mkdir /var/log/gunicorn

# Configure SSH and mount SSHFS
RUN echo "ServerAliveInterval 120" >> /etc/ssh/ssh_config \
&& mkdir /var/challenges/ \
&& sshfs -o IdentityFile=/config_files web_tsc@10.8.99.111:/var/ /var/challenges/


# Run Supervisor (i.e., start Nginx, and Gunicorn)
COPY /config_files/supervisord.conf /etc/supervisor/supervisord.conf
COPY /config_files/supervisord_nginx_gunicorn.conf /etc/supervisor/conf.d/supervisord_nginx_gunicorn.conf

#CMD /bin/bash
CMD ["/usr/bin/supervisord"]

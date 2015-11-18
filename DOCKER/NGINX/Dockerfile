#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 09/11/2015
# Create nginx-django container link with tsc's webfiles
# Container should be launch with start_nginx.sh script
FROM debian:jessie
MAINTAINER veran@intechinfo.fr

# Enable production settings by default; for development, this can be set to 
# `false` in `docker run --env`
ENV DJANGO_PRODUCTION=true

# Set terminal to be noninteractive
ENV DEBIAN_FRONTEND noninteractive

# Update and install packages
RUN apt-get update && apt-get install -y \
	nginx \
	supervisor \
	python3.4 \
	python-dev \
	python-mysqldb \
	python-urllib3 \
	python-pkg-resources \
	python-sqlparse \
	python-pip \
	python3-tz \
	libffi6 \
	libssl1.0.0 \
	libjs-jquery \
	libpython3.4 \
	libmysqlclient-dev \
	javascript-common \
	apt-utils \
	wget \
 && apt-get autoclean

RUN mkdir /var/log/gunicorn \
 && mkdir /var/log/supervisord
ADD . /code
#ADD <source> <destination>
WORKDIR /code

# Install python requirement
RUN pip install --upgrade -r requirements.txt
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python

# Expose ports
# 80 = Nginx
# 8000 = Gunicorn
EXPOSE 80 8000

# Configure Nginx
RUN cp /code/nginx.conf /etc/nginx/sites-available/django_docker.conf \
 && ln -s /etc/nginx/sites-available/django_docker.conf /etc/nginx/sites-enabled/django_docker.conf \
 && rm /etc/nginx/sites-enabled/default \
 && rm -r ../code

# Run Supervisor (i.e., start MySQL, Nginx, and Gunicorn)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/python3.4","/usr/bin/supervisord"]

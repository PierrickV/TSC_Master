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
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
	nginx \
	python3.4 \
	python-pip \
	javascript-common \
	libjs-jquery \
	supervisor \
	python-mysqldb 

#	python-sqlparse \
#	python-tz \
#	libffi6 \
#	libssl1.0.0 \	
#	libpython3.4
#	python-setuptools \
#	python-urllib3 \
#	apt-utils \

RUN apt-get autoclean
RUN mkdir /var/log/gunicorn
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

# Expose ports
# 80 = Nginx
# 8000 = Gunicorn
EXPOSE 80 8000

# Configure Nginx
RUN cp /code/nginx.conf /etc/nginx/sites-available/django_docker.conf
RUN ln -s /etc/nginx/sites-available/django_docker.conf /etc/nginx/sites-enabled/django_docker.conf
run rm /etc/nginx/sites-enabled/default
RUN rm -r ../code

# Run Supervisor (i.e., start MySQL, Nginx, and Gunicorn)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

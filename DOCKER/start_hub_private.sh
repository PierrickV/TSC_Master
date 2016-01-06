#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 22/12/2015
# Launch hub container for private docker images storage
# docker pull distribution/registry:master

docker rm -f tsc_hub_private

docker run -d \
        -p 5000:5000 \
        --restart=always \
        --name tsc_hub_private registry:2

# docker pull ubuntu
# docker tag -f ubuntu tsc.itinet.fr:5000/ubuntu
# docker push tsc.itinet.fr:5000/ubuntu

# DOCKER_OPTS="--debug --log-level=\"debug\" --dns 8.8.8.8 --insecure-registry 10.8.96.7:5000"

# Run the registry on the server, allow only localhost connection
#docker run -p 127.0.0.1:5000:5000 registry

# On the client, setup ssh tunneling
# ssh -N -L 5000:localhost:5000 user@server

# The registry is then accessible at localhost:5000, authentication is done through ssh that you probably already know and use.
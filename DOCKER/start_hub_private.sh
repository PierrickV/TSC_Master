#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 22/12/2015
# Launch hub container for private docker images storage
# docker pull distribution/registry:master

docker rm -f tsc_hub_private

docker run \
        --name tsc_hub_private \
        --restart=always \
        -p 5000:5000 \
        -v $(pwd)/HUB/auth:/auth \
        -e REGISTRY_AUTH="htpasswd" \
        -e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" \
        -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
        -v /home/docker/hub:/var/lib/registry:rw \
        -v $(pwd)/HUB/certs:/certs:ro \
        -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
        -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
        -e REGISTRY_HTTP_SECRET="2J9r9mtbm4BdRmcV4ExgVzEbKzkW4W7V8EUYm9cMQ8UGu" \
        -d registry:2


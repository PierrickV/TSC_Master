#!/bin/bash

docker rm -f tsc_hub_public

docker run \
        --name tsc_hub_private \
        --restart=always \
        -p 127.0.0.1:5000:5000 \
        -v /home/lilyus/Hub:/var/lib/registry \
        -v `pwd`/certs:/certs \
        -e REGISTRY_HTTP_TLS_CERTIFICATE=/HUB/certs/domain.crt \
        -e REGISTRY_HTTP_TLS_KEY=/HUB/certs/domain.key \
        -d registry:2


#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 07/12/2015
# Launch registry container for TSC private hub

docker run -d \
-p 5000:5000 \
--restart=always \
--name registry registry:2

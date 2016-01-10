#!/usr/bin/env bash
cd $(pwd)/DOCKER/WEB/ && ./build.sh
cd ../WEB_FORUM/ && ./build.sh
../start_database.sh
../start_web_forum.sh
../start_web.sh


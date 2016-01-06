#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 08/12/2015
# /!\ This script is at this time just a reminder

sudo adduser docker fuse

# add "ServerAliveInterval 5" to your /etc/ssh/ssh_config file

/usr/bin/sshfs -o idmap=user \
-o allow_other \
-o nonempty \
-o IdentityFile=/home/docker/Git/TSC/DOCKER/WEB/config_files/id_rsa \
tsc_web@10.8.99.111:/home/tsc_web/nv_challenges/ /home/docker/nv_challenges

sudo fusermount -u nv_challenges/


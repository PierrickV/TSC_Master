#!/bin/bash
# Pierrick VERAN - Tardigrade Security Challenge - 08/12/2015
# Connect to the storage server to store the new challenge
# Add this line in your /etc/rc.local file 

sshfs -o IdentityFile=/home/docker/Git/TSC/DOCKER/TSC_WEB/config_files/id_rsa tsc_web@10.8.99.111:/home/docker/Non_validated_challenges/ /home/docker/Non_validated_challenges
chmod ug+wr /home/docker/Non_validated_challenges/

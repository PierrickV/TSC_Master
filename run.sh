#!/usr/bin/env bash

echo "Démarrage du conteneur MYSQL"
$(pwd)/DOCKER/start_database.sh

#Construction des images
echo "Construction des images web"
cd $(pwd)/DOCKER/WEB/ && ./build.sh
cd ../WEB_FORUM/ && ./build.sh

echo "Démarrage des conteneurs web"
echo "Attente de l'initialisation de la base de données - Si cette étape échoue supprimer le contenu de ~/mysql/"
sleep 10
../start_web_forum.sh
../start_web.sh

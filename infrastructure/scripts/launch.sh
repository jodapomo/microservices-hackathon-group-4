#! /bin/bash

function prepare(){
    echo UPDATING:
    apt-get update && echo "Successful update" || echo "Fail"
}

function install_docker(){
    echo INSTALLING APT-TRANSPORT-HTTPS:
    apt-get update
    apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y  && echo "Successful https" || echo "Fail"
    echo DOWNLOADING DOCKER:
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  && echo "Successful docker" || echo "Fail"
    echo ADDING STABLE REPOSITORY:
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  && echo "Successful docker repository" || echo "Fail"
    echo DOCKER POLICY:
    apt-get update
    echo INSTALLING DOCKER-CE:
    apt-get install docker-ce docker-ce-cli -y  && echo "Successful docker ce" || echo "Fail"
    usermod -aG docker $(whoami) && echo "Successful docker all" || echo "Fail"
}

function install_docker_compose(){
    echo INSTALLING DOCKER COMPOSE:
    curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && echo "Successful" || echo "Fail"
    chmod +x /usr/local/bin/docker-compose && echo "Successful docker compose" || echo "Fail"
}

function compose() {
  docker-compose -f $compose_file_path up -d
}

function main(){
    prepare
    install_docker
    install_docker_compose
    compose
}

main

#!/bin/bash
repo_name="microservices-hackathon-group-4"
export compose_file_path="/$repo_name/docker-compose.yml"

git clone https://github.com/jodapomo/$repo_name
launch_script="/$repo_name/infrastructure/scripts/launch.sh"
chmod +x $launch_script
$launch_script

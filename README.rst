# For å kjøre opp
1. cd docker
2. docker-compose up -d

# For å teste
testinfra --connection=docker --hosts=docker_newspaper_1 tests/*

For å kjøre opp
#################
1. cd docker
2. docker-compose up -d

For å teste
###############

.. code::
    
    testinfra --connection=docker --hosts=docker_newspaper_1 tests/*

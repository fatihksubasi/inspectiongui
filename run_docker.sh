#!/bin/bash

CONTAINER=fatihksubasi/inspectiongui

docker run --rm -d -P -e NEWUSER=$(id -un) -e NEWUID=501 -e NEWGID=20	        \
        -e RESOLUTION="800x600"						        \
        -v $(pwd):/gui							        \
        -l runby=$(id -un)						        \
        $CONTAINER $*   					            &&	\
sleep 1                                                                     &&  \
xdg-open http://localhost:$(docker inspect --format='{{(index (index .NetworkSettings.Ports "6080/tcp") 0).HostPort}}' $(docker ps -qf ancestor=$CONTAINER)) && \
sleep 1                                                                     &&  \
docker exec -it -u $(id -un) $(docker ps -qf ancestor=$CONTAINER) bash -c "cd /gui && sudo python gui.py" 
#!/bin/bash
if [ 1 -ne $# ]; then 
    echo "usage:" $0 "start|stop|restart"
    exit
fi

action=$1
target=compose.zentao

function start() {
    docker-compose -f $target up -d
}

function stop() {
    docker-compose -f $target down
}

case $action in
start)
    start
    ;;
stop)
    stop
    ;;
restart)
    stop
    start
    ;;
*)
    echo "unknown action: " $action  
    exit
    ;;
esac

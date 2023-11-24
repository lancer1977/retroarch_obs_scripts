#!/bin/bash
# This is an example file of how gameStart and gameStop events can be used.
url=http://192.168.0.169:6000/postGame
# It's good practice to set all constants before anything else.
logfile=/tmp/scriptlog.txt

# Case selection for first parameter parsed, our event.
case $1 in
    gameStart)
        # Commands in here will be executed on the start of any game.
        echo "START" > $logfile
        echo "$@" >> $logfile
        curl -X POST -H "Content-Type: application/json" -d '{
            "start": '\""$1"\"',
            "system": '\""$2"\"',
            "emulator": '\""$3"\"',
            "core": '\""$4"\"',
            "path": '\""$5"\"'
                }' $url >> $logfile
                
    ;;
    gameStop)
        # Commands here will be executed on the stop of every game.
        echo "END" >> $logfile
    ;;
esac
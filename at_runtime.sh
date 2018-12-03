#!/bin/bash

if [ "$RESOLUTION" != "" ]; then
    echo "set RESOLUTION=$RESOLUTION"
    sed -i "s/Modes \"1366x768\"/Modes \"$RESOLUTION\"/" /etc/X11/xorg.conf
fi
if [ "$NEWUSER" != "" ]; then
    echo "$NEWUSER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$NEWUSER
    if [ "$NEWUID" != "" ]; then
        if [ "$NEWGID" != "" ]; then
            useradd -m -u $NEWUID -g $NEWGID $NEWUSER
        else
            useradd -m -u $NEWUID $NEWUSER
        fi
    fi
fi
echo $*
exec $*


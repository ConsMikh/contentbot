#!/bin/sh

syncthing cli config devices add --device-id $CONTENT_RECIEVER
syncthing cli config devices $CONTENT_RECIEVER auto-accept-folders set true

python3 /usr/src/app/bot.py
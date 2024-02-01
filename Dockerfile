FROM python:3.10-alpine

RUN apk update \
    && apk add --no-cache syncthing openrc\
    && syncthing generate \
    && rc-update add syncthing \
    && touch /run/openrc/softlevel \
    && rc-service syncthing start

WORKDIR /usr/src/app
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./

CMD [ "python3", "./bot.py" ]
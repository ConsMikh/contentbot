FROM python:3.10-alpine

RUN apk update \
    && apk add --no-cache syncthing \
    && mkdir /content

WORKDIR /usr/src/app
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./

CMD [ "python3", "./bot.py" ]
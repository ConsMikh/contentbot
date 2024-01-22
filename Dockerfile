FROM python:3.10-alpine

WORKDIR /usr/src/app
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk update && apk add git

COPY src/ ./
RUN chmod +x /usr/src/app/start.sh

CMD [ "python3", "./bot.py" ]
FROM python:3.10-alpine

WORKDIR /usr/src/app
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt install git-all

COPY src/ ./

CMD [ "python", "./bot.py" ]
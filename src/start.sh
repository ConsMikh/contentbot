#!/bin/sh

# sh /usr/src/app/start.sh
# перейти в каталог контента
# клонировать репозиторий
# создает крон задачу по пушу репозитория
# перейти в папку бота
# запустить бота 

# repo_name=${CONTENT_REPO_NAME}
# cd /content
# git clone ${repo_name}
# Создаем задачу cron, которая будет запускать скрипт push.sh каждый час
(crontab -l 2>/dev/null; echo "*/5 * * * * sh /usr/src/app/push.sh") | crontab -

# Исполняем python скрипт
python3 /usr/src/app/bot.py

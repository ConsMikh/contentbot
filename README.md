# contentbot
https://devopscell.com/cron/docker/alpine/linux/2017/10/30/run-cron-docker-alpine.html
https://lewiswalsh.com/posts/20210412-ssh-in-docker-alpine/

git clone git@github.com:ConsMikh/ContentRepo.git /content
docker exec -it contentbot-bot-1 sh

https://gist.github.com/Jonny-exe/9bad76c3adc6e916434005755ea70389


### Syncthing
Для извлечения контента из бота используется syncthing. Его установка прописана в Dockerfile
```docker
RUN apk update && apk add --no-cache syncthing
```
Для его работы в файл .env надо прописать переменную окружения CONTENT_RECIEVER. 
Переменная должна содержать ID того устройства, на котором уже установлен syncthing и куда будут 
закачиваться файлы
В текущей версии syncthing не запускается автоматически. Для его работы после запуска контейнера 
надо войти в него 
```bash
# docker exec -it contentbot-bot-1 sh
```
В контейнере надо запустить syncthing
```bash
# syncthing --no-browser
```
Потом выйти из контейнера "Ctrl + C". Затем снова зайти в контейнер и выполнить команды
```bash
# syncthing cli config devices add --device-id $CONTENT_RECIEVER
# syncthing cli config devices $CONTENT_RECIEVER auto-accept-folders set true
```
На компьютер, с которого был взят ID, должен прийти запрос на соединение. На этом компьютере надо 
создать папку с контентом и расшарить ее на бот. После этого можно начинать пользоваться ботом
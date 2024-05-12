# Aveds-test
## Описание
Проект для регистрации и авторизации пользователей по API, и получения доступа к боту, считающему символы в отправленном сообщении.

## Технологии
- Python 3.11
- FastAPI 0.111.0
- Aiogram 3.6.0
- SQLAlchemy 2.0.30
- PostgreSQL 13.0
- Nginx 1.21.3
- Docker
- Docker-compose
- Docker Hub

# Установка
## Копирование репозитория
Клонируем репозиторий и переходим в директорию infra:
```
~ git clone git@github.com:Certelen/Aveds-test.git
~ cd ./Aveds-test/infra/
```

## Изменение переменных среды
В файле docker-compose.yml измените переменны в строках:
backend -> environment:
- DB_NAME=<Имя базы данных>
- DB_USERNAME=<Имя пользователя базы данных>
- DB_PASSWORD=<Пароль пользователя базы данных>
- DB_HOST=<Адрес базы данных>
- DB_PORT=<Порт базы данных>
- SECRET=<Ключ для хеширования данных>
frontend -> environment:
- DB_NAME=<Имя базы данных>
- DB_USERNAME=<Имя пользователя базы данных>
- DB_PASSWORD=<Пароль пользователя базы данных>
- DB_HOST=<Адрес базы данных>
- DB_PORT=<Порт базы данных>
- TG_TOKEN=<Токен бота в Телеграме>
- HOST=<Адрес сайта>
frontend -> environment:
- POSTGRES_PASSWORD: <Установить пароль для пользователя базы данных>

## Установка на боевой сервер
Перейдите на боевой сервер:
```
~ ssh username@server_address
```
Обновите индекс пакетов APT:
```
~ sudo apt update
```
и обновите установленные в системе пакеты и установите обновления безопасности:
```
~ sudo apt upgrade -y
```
Создайте папку `nginx`:
```
~ mkdir nginx
``` 
Скопируйте файлы docker-compose.yml, nginx/default.conf из вашего проекта на сервер в home/<ваш_username>/docker-compose.yml, home/<ваш_username>/nginx/default.conf соответственно:
```
~ scp docker-compose.yml <username>@<host>/home/<username>/docker-compose.yml
~ scp default.conf <username>@<host>/home/<username>/nginx/default.conf
```
Установите Docker и Docker-compose:
```
~ sudo apt install docker.io
```
```
~ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
~ sudo chmod +x /usr/local/bin/docker-compose
```
Проверьте правильность установки Docker-compose:
```
~ sudo  docker-compose --version
```
Разворачиваем контейнеры в фоновом режиме из папки infra:
```
~ sudo docker-compose up -d
```

## Установка на локальный сервер через Docker:
Установите Docker и Docker-compose согласно инструкции на сайте:
https://docs.docker.com/compose/install/


После установки разворачиваем контейнеры в фоновом режиме из папки infra:
```
~ sudo docker-compose up -d
```

## Установка на локальный сервер для тестирования:
Перейдите в папку с backend и запустите его:
```
~ cd ../backend/
~ uvicorn main:app 
```
Так же перейдите в папку с frontend и запустите его:
```
~ cd ../frontend/
~ py main.py
```
Все адресные пути используйте с 8000 портом вида: http://127.0.0.1:8000/

# Адресные пути
## Документация
- [Документация к API - Swagger](http://127.0.0.1/)
- [Документация к API - Redoc](http://127.0.0.1/redoc)
## API-адреса
- [Регистрация](http://127.0.0.1/user) : POST-запрос с json-данными {"username": "<Ник>", "name": "<Имя>", "password": "<Пароль>"}, ответ - данные пользователя для авторизации
- [Авторизация](http://127.0.0.1/token) : POST-запрос с form-данными Key: username, password; Value: <Ник>, <Пароль>, ответ - токен и тип для авторизации
- [Регистрация](http://127.0.0.1/user) : GET-запрос, ответ - данные пользователя
- [Регистрация](http://127.0.0.1/tg_link) : GET-запрос, ответ - ссылка для привязки бота
Все вышеуказанные API-адреса и авторизацию так же можно выполнить через Swagger документацию
# Авторы
Дмитрий Коломейцев

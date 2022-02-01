https://github.com/RWSNTi/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg

# api_yamdb
api_yamdb

### Описание
Каталог различных произведений искусства с делением на категории и жанры. Пользователи могут оставлять отзывы на произведения и комментарии.

### Шаблон для наполнения .env файла  

```
SECRET_KEY=<secret_key>
DB_ENGINE=django.db.backends.<engine name>
DB_NAME=<database name>
POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
DB_HOST=<host name>
DB_PORT=<port number>
```

### Порядок запуска проекта в контейнерах  

Сборка и запуск
 sudo docker-compose up -d --build 
Выполнение миграций, создание суперюзера, сбор статики
 sudo docker-compose exec web python manage.py migrate
 sudo docker-compose exec web python manage.py createsuperuser
 sudo docker-compose exec web python manage.py collectstatic --no-input

### Наполнение БД данными  

Получаем список контейнеров
 sudo docker ps
Заходим в контейнер
 sudo docker exec -it <id контейнера> bash
Загружаем в БД данные
python manage.py loaddata -i fixtures.json

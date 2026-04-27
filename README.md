# Foodgram

Foodgram — это сервис для публикации рецептов, где пользователи могут делиться своими блюдами, добавлять понравившиеся рецепты в избранное, подписываться на других авторов, формировать список покупок и скачивать его в текстовом формате.

Проект состоит из backend-части на Django REST Framework, frontend-части на React, базы данных PostgreSQL и инфраструктуры на Docker Compose и Nginx.

## Технологии

В проекте используются Python 3.11, Django 4.2, Django REST Framework, Djoser, PostgreSQL, Gunicorn, React, Docker, Docker Compose и Nginx.

## Возможности проекта

Пользователь может зарегистрироваться и войти в аккаунт, просматривать рецепты, создавать собственные рецепты, редактировать и удалять их, загружать изображения к рецептам, добавлять рецепты в избранное, добавлять рецепты в список покупок, скачивать список покупок в формате `.txt`, подписываться на других авторов, менять пароль, устанавливать аватар, фильтровать рецепты по тегам и искать ингредиенты по названию. Также в проекте доступна документация API.

## Структура проекта

Проект имеет следующую структуру:

```text
foodgram/
├── backend/              # Django backend
├── frontend/             # React frontend
├── infra/                # Docker Compose и nginx
├── data/                 # файл с ингредиентами
├── docs/                 # документация API
├── .env                  # переменные окружения
└── README.md

```
## Подготовка к запуску
```
Перед запуском проекта необходимо создать файл .env в корне проекта. В нём должны быть указаны переменные окружения.

Пример содержимого файла .env:

POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=django-insecure-super-secret-key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost

```
## Запуск проекта
```
Склонируйте репозиторий и перейдите в корневую директорию проекта:

git clone <ссылка_на_репозиторий>
cd foodgram

Перейдите в папку infra:

cd infra

Поднимите контейнеры:

docker compose --env-file ../.env up --build -d

После запуска контейнеров выполните миграции:

docker compose --env-file ../.env exec backend python manage.py migrate

Соберите статические файлы:

docker compose --env-file ../.env exec backend python manage.py collectstatic --noinput

Загрузите ингредиенты в базу данных:

docker compose --env-file ../.env exec backend python manage.py load_ingredients

Создайте суперпользователя для доступа в административную панель:

docker compose --env-file ../.env exec backend python manage.py createsuperuser
```

## Доступ к проекту
```
После успешного запуска проект будет доступен по следующим адресам:

Сайт:
http://127.0.0.1/

Административная панель Django:
http://127.0.0.1/admin/

API:
http://127.0.0.1/api/

Документация API:
http://127.0.0.1/api/docs/

Полезные команды

Остановить контейнеры:

docker compose --env-file ../.env down

Остановить контейнеры и удалить volumes:

docker compose --env-file ../.env down -v

Пересобрать и заново поднять проект:

docker compose --env-file ../.env up --build -d

Посмотреть логи backend-контейнера:

docker compose --env-file ../.env logs backend
```

## Основные сценарии использования
```
После запуска проекта можно зарегистрировать нового пользователя, войти в систему, создать рецепт, добавить рецепт в избранное, добавить рецепт в список покупок, скачать список покупок в текстовом формате, подписаться на другого автора, изменить пароль и установить аватар.
```

## Автор

Чальцев Андрей
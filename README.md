# Hitalent

## Описание проекта
Простой API-сервис для вопросов и ответов:
- Создание, получение и удаление вопросов
- Создание, получение и удаление ответов
- Каскадное удаление: при удалении вопроса удаляются все ответы

## Стек технологий
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic (валидация)
- Docker + docker-compose
- Pytest (для тестирования)

## Запуск проекта через Docker
1. Клонируем репозиторий:
   
   git clone < https://github.com/Iskandar54/hitalent.git >
   
   cd hitalent

3. Запускаем Docker-контейнеры:

   docker-compose up --build

5. API будет доступен по адресу:

   http://localhost:8000





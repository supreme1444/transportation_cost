# Развертывание FastAPI приложения для расчета стоимости страховки

Это приложение FastAPI предназначено для расчета стоимости страховки на основе тарифов для различных типов грузов. Оно использует асинхронные вызовы и подключается к базе данных PostgreSQL.

## Описание приложения

### Основные компоненты приложения

1. **Модели данных**:
   - **Tariff**: SQLAlchemy модель, представляющая тарифы на груз. Содержит поля `id`, `cargo_type`, `rate` и `date`.
   - **InsuranceRequest** , **InsuranceResponse**,**EditRateRequest** и **EditRateResponse**,**AddRateRequest**,**AddRateRespons**: Pydantic модели для валидации входящих данных и формирования ответов API.

2. **Эндпоинты**:
   - `/calculate-insurance/`: Асинхронный POST-эндпоинт, который принимает запрос с данными о грузах и возвращает расчетную стоимость страховки. Он использует функцию `calculate_insurance_cost`, которая обращается к базе данных для получения актуального тарифа.
  - /edit-insurance/: Асинхронный POST-эндпоинт, который принимает ID, ставку и наименование груза и возвращает отредактированный тариф. Он использует функцию edit_insurance_services, которая обращается к базе данных для получения отредактированного тарифа.
   - /delete-rate/: Асинхронный POST-эндпоинт, который принимает ID ставки и удаляет ее из базы. Он использует функцию delete_rate_services.
3. **Подключение к базе данных**:
   - Используется SQLAlchemy для работы с базой данных и асинхронные сессии для выполнения запросов.
   - Функции `connect` и `disconnect` управляют подключением к базе данных.
   - Заполнить .env файл с подключением.
4. **Загрузка тарифов**:
   - При запуске приложения происходит загрузка тарифов из файла `tariffs.json` в базу данных, если тарифы еще не загружены.

5. **Docker и Docker Compose**:
   - Приложение упаковано в Docker-контейнер, что упрощает его развертывание.

6. **Запустите контейнер базы данных:**:
     - Запустите контейнер базы данных docker-compose up -d
7. **Запуск приложения**:
     - Создать файл .env DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres
     - Сделайть миграции alembic revision --autogenerate -m "базовая миграция 1"
     - Применить миграции alembic upgrade head 
     - Запуск сервера uvicorn main:app --reload  
8.  Войти по адрессу http://127.0.0.1:8000/docs#/ и протестировать эндпоинт /calculate-insurance/ с помощью Postman или cURL, отправив POST-запрос с JSON-данными:
    **Пример**
{
  "date_request": "2022-03-10",
  "cargo_type": "Clothing",
  "declared_value": 10000.0
}
9. **Использование Kafka**:
   - Для логирования и обработки событий используется Apache Kafka. Приложение отправляет логи и события в Kafka, что позволяет отслеживать действия и производить дальнейшую обработку данных.

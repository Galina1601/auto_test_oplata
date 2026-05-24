# Проект автоматизации тестирования веб-сервиса «Путешествие дня»

## Описание
Веб-сервис предлагает купить тур по определённой цене двумя способами:
- Обычная оплата по дебетовой карте
- Выдача кредита по данным банковской карты

## Запуск проекта

### 1. Запуск контейнера с PostgreSQL
```bash
docker-compose up -d

### 2. Настройка приложения
Файл `application.properties` должен содержать:
```properties
spring.credit-gate.url=http://185.119.57.197:9999/credit
spring.payment-gate.url=http://185.119.57.197:9999/payment

spring.datasource.url=jdbc:postgresql://localhost:5432/app
spring.datasource.username=app
spring.datasource.password=pass
spring.datasource.driver-class-name=org.postgresql.Driver

spring.jpa.hibernate.ddl-auto=create
spring.jpa.show-sql=true
```

3. Запуск тестируемого приложения

```bash
java -jar aqa-shop.jar
```

Приложение будет доступно по адресу: http://localhost:8080

4. Установка зависимостей для автотестов

```bash
pip install -r requirements.txt
```

5. Запуск автотестов

```bash
pytest tests/test_payment_positive.py -v
```

Структура проекта

```
auto_test_oplata/
├── documents/          # отчёты и скриншоты
├── tests/              # автотесты
├── conftest.py         # фикстура для браузера
├── docker-compose.yml  # конфигурация PostgreSQL
├── application.properties # настройки приложения
├── requirements.txt    # зависимости Python
└── README.md           # инструкция
```
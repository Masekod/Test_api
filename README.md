# Backend Autotests (Python)
Автоматизированные тесты для API backend проекта **Test api**.
- [Описание](#описание)
- [Работа с пакетами](#работа-с-пакетами)
- [Работа с отчётами](#работа-с-отчётами)
- [Технологии](#технологии)

## Описание
Проект содержит автотесты для проверки функционала API бэкенда:
- Аутентификация и регистрация пользователей
- Управление профилем пользователя
- Работа с задачами (CRUD-операции)
- Загрузка и получение аватаров пользователя

## Работа с пакетами

Установка пакета pydantic для валидации тела ответа: pip install pydantic

Установка пакета email-validator для валидации email: pip install email-validator

Список установленных пакетов: pip list

Сохранить зависимости в файл: pip freeze > requirements.txt

Установка зависимостей из файла: pip -r requirements


## Работа с отчётами

1. Установка allure: pip install allure-pytest
2. Запуск с генерацией Allure-отчёта: pytest --alluredir=allure=results(Флаг --alluredir указывает папку, где будут храниться отчёты)
3. Просмотр отчёта: allure serve allure-results

## Технологии
- Python 3.12
- [pytest](https://docs.pytest.org/)
- [requests](https://requests.readthedocs.io/)
- [Faker](https://faker.readthedocs.io/en/master/#basic-usage)
- [allure-pytest](https://pypi.org/project/allure-pytest/)

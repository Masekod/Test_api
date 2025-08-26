import allure
import pytest
from http import HTTPStatus
from api.auth.login_user import login_user
from config.settings import CREDENTIALS_EMAIL, CREDENTIALS_PASSWORD
from utils.generator import generate_random_email, generate_random_password
from shcemas.auth.AuthModels import AuthSuccessResponse, AuthBadRequestResponse, AuthUnauthorizedResponse

@allure.feature("Авторизация")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        (CREDENTIALS_EMAIL, CREDENTIALS_PASSWORD, HTTPStatus.OK),
        (generate_random_email(), CREDENTIALS_PASSWORD, HTTPStatus.UNAUTHORIZED),
        (CREDENTIALS_EMAIL, generate_random_password(), HTTPStatus.UNAUTHORIZED),
        ("", generate_random_password(), HTTPStatus.BAD_REQUEST),
        (generate_random_email(), "", HTTPStatus.BAD_REQUEST),
    ]
)
def test_login_status(email, password, expected_status):
    payload = {
        "email": email,
        "password": password,
    }
    with allure.step("Отправка запроса"):
        response = login_user(payload)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == expected_status


@allure.feature("Авторизация")
@allure.story('Проверка структуры тела ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "email, password, expected_response_body",
    [
        (CREDENTIALS_EMAIL, CREDENTIALS_PASSWORD, AuthSuccessResponse),
        (generate_random_email(), CREDENTIALS_PASSWORD, AuthUnauthorizedResponse),
        (CREDENTIALS_EMAIL, generate_random_password(), AuthUnauthorizedResponse),
        (generate_random_email(), "", AuthBadRequestResponse),
        ("", generate_random_password(), AuthBadRequestResponse),
    ]
)
def test_login_response_body(email, password, expected_response_body):
    payload = {
        "email": email,
        "password": password,
    }
    with allure.step("Отправка запроса"):
        response = login_user(payload)
    with allure.step("Проверка структуры тела ответа"):
        # Вспомним, что в Python для работы с JSON есть модуль json с методами loads() и dumps()
        # Метод dumps() превращает словарь в JSON
        # В Pydantic классы хранят данные как атрибуты класса
        # чтобы получить словарь из модели Pydantic, используют метод model_dump()
        # Таким образом, model_dump() возвращает словарь из модели
        assert response.json() == expected_response_body(**response.json()).model_dump()
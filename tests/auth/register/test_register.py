import allure
import pytest
from http import HTTPStatus
from api.auth.register_user import register_user
from config.settings import CREDENTIALS_EMAIL
from config.constants import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH
from utils.generator import generate_random_email, generate_random_password
from shcemas.auth.AuthModels import AuthSuccessResponse, AuthBadRequestResponse


@allure.feature("Регистрация")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        (generate_random_email(), generate_random_password(), HTTPStatus.CREATED),
        (CREDENTIALS_EMAIL, generate_random_password(), HTTPStatus.BAD_REQUEST),
        (generate_random_email(), "", HTTPStatus.BAD_REQUEST),
        ("", generate_random_password(), HTTPStatus.BAD_REQUEST),
        (generate_random_email(), generate_random_password(MIN_PASSWORD_LENGTH - 1), HTTPStatus.BAD_REQUEST),
        (generate_random_email(), generate_random_password(MIN_PASSWORD_LENGTH), HTTPStatus.CREATED),
        (generate_random_email(), generate_random_password(MAX_PASSWORD_LENGTH), HTTPStatus.CREATED),
        (generate_random_email(), generate_random_password(MAX_PASSWORD_LENGTH + 1), HTTPStatus.BAD_REQUEST),
    ]
)
def test_register_status(email, password, expected_status):
    payload = {
        "email": email,
        "password": password,
    }
    with allure.step("Отправка запроса"):
        response = register_user(payload)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == expected_status


@allure.feature("Регистрация")
@allure.story('Проверка структуры тела ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "email, password, expected_response_body",
    [
        (generate_random_email(), generate_random_password(), AuthSuccessResponse),
        (CREDENTIALS_EMAIL, generate_random_password(), AuthBadRequestResponse),
        (generate_random_email(), "", AuthBadRequestResponse),
        ("", generate_random_password(), AuthBadRequestResponse),
        (generate_random_email(), generate_random_password(MIN_PASSWORD_LENGTH - 1), AuthBadRequestResponse),
        (generate_random_email(), generate_random_password(MIN_PASSWORD_LENGTH), AuthSuccessResponse),
        (generate_random_email(), generate_random_password(MAX_PASSWORD_LENGTH), AuthSuccessResponse),
        (generate_random_email(), generate_random_password(MAX_PASSWORD_LENGTH + 1), AuthBadRequestResponse),
    ]
)
def test_register_response_body(email, password, expected_response_body):
    payload = {
        "email": email,
        "password": password,
    }
    with allure.step("Отправка запроса"):
        response = register_user(payload)
    with allure.step("Проверка статус кода ответа"):
        assert response.json() == expected_response_body(**response.json()).model_dump()

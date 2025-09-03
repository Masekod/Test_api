import allure
import pytest
from http import HTTPStatus
from utils.generator import generate_random_email, generate_random_password
from shcemas.auth.AuthModels import AuthSuccessResponse, AuthBadRequestResponse, AuthUnauthorizedResponse
from utils.utils import get_current_email, get_current_password


@allure.feature("Авторизация")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        (get_current_email(), get_current_password(), HTTPStatus.OK),
        (generate_random_email(), get_current_password(), HTTPStatus.UNAUTHORIZED),
        (get_current_email(), generate_random_password(), HTTPStatus.UNAUTHORIZED),
        ("", generate_random_password(), HTTPStatus.BAD_REQUEST),
        (generate_random_email(), "", HTTPStatus.BAD_REQUEST),
    ]
)
def test_login_status(api_client, email, password, expected_status):
    credentials = {
        "email": email,
        "password": password,
    }
    response = api_client.login(credentials)
    assert response.status_code == expected_status


@allure.feature("Авторизация")
@allure.story('Проверка структуры тела ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "email, password, expected_response_body",
    [
        (get_current_email(), get_current_password(), AuthSuccessResponse),
        (generate_random_email(), get_current_password(), AuthUnauthorizedResponse),
        (get_current_email(), generate_random_password(), AuthUnauthorizedResponse),
        (generate_random_email(), "", AuthBadRequestResponse),
        ("", generate_random_password(), AuthBadRequestResponse),
    ]
)
def test_login_response_body(api_client, email, password, expected_response_body):
    credentials = {
        "email": email,
        "password": password,
    }
    response = api_client.login(credentials)
    assert response.json() == expected_response_body(**response.json()).model_dump()

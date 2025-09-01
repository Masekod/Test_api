import allure
import pytest
from http import HTTPStatus
from api.auth.update_user_email import update_user_email
from config.settings import NEW_EMAIL, INVALID_EMAIL
from utils.utils import api_debug, set_current_email, get_current_password



@allure.feature("Обновление почты")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "data, expected_status",
    [
        ({"email": NEW_EMAIL, "password": get_current_password()}, HTTPStatus.OK),
        ({"email": NEW_EMAIL, "password": get_current_password()}, HTTPStatus.BAD_REQUEST),
        ({"email": INVALID_EMAIL, "password": get_current_password()}, HTTPStatus.BAD_REQUEST),
    ]
)
def test_update_email(change_email, data, expected_status):
    with allure.step("Отправка запроса"):
        response = update_user_email(change_email, data)
        api_debug(response)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == expected_status
        if expected_status == HTTPStatus.OK:
            set_current_email(NEW_EMAIL)


@allure.feature("Обновление почты")
@allure.story('Неавторизованный пользователь')
def test_update_email_unauthorized():
    with allure.step("Отправка запроса"):
        response = update_user_email(None, {"email":NEW_EMAIL})
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == HTTPStatus.UNAUTHORIZED

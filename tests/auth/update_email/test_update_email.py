import allure
import pytest
from http import HTTPStatus
from api.auth.update_user_email import update_user_email
from config.settings import NEW_EMAIL, INVALID_EMAIL, CREDENTIALS_PASSWORD
from utils.utils import api_debug, get_current_email, set_current_email



@allure.feature("Обновление почты")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "data, expected_status",
    [
        ({"email": NEW_EMAIL, "password": CREDENTIALS_PASSWORD}, HTTPStatus.OK),
        ({"email": NEW_EMAIL, "password": CREDENTIALS_PASSWORD}, HTTPStatus.BAD_REQUEST),
        ({"email": INVALID_EMAIL, "password": CREDENTIALS_PASSWORD}, HTTPStatus.BAD_REQUEST),
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



def test_update_email_unauthorized():
        response = update_user_email(None, {"email":NEW_EMAIL})
        assert response.status_code == HTTPStatus.UNAUTHORIZED

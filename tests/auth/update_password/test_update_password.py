import allure
import pytest
from http import HTTPStatus
from api.auth.update_user_password import update_user_password
from config.settings import NEW_PASSWORD,INVALID_PASSWORD
from utils.utils import set_current_password, get_current_password


@allure.feature("Обновление пароля")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "data, expected_status",
    [
        ({"password": get_current_password(), "newPassword": NEW_PASSWORD}, HTTPStatus.OK),
        ({"password": INVALID_PASSWORD, "newPassword": NEW_PASSWORD}, HTTPStatus.BAD_REQUEST),
        ({"password": get_current_password(), "newPassword": INVALID_PASSWORD}, HTTPStatus.BAD_REQUEST),
    ]
)
def test_update_password(change_email, data, expected_status):
    with allure.step("Отправка запроса"):
        response = update_user_password(change_email, data)
        print(response)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == expected_status
        if expected_status == HTTPStatus.OK:
            set_current_password(NEW_PASSWORD)



def test_update_password_unauthorized():
    response = update_user_password(None, {"password": NEW_PASSWORD})
    assert response.status_code == HTTPStatus.UNAUTHORIZED

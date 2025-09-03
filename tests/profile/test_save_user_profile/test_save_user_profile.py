import allure
from http import HTTPStatus

from utils.generator import generate_profile_data


@allure.feature("Сохранение данных пользователя")
def test_save_user_profile(api_client):
    with allure.step("Данные пользователя"):
        body = generate_profile_data()
    with allure.step("Отправка запроса"):
        response = api_client.save_user_profile(body)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == HTTPStatus.OK

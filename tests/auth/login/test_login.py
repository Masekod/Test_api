from api.auth.login_user import login_user
from data.login_data import success_login_data
import allure

@allure.feature("API")
@allure.story('Авторизация с успешным входом')
def test_success_login():
    with allure.step('Генерация данных для авторизации с неправильным email'):
        login_data = success_login_data()
    with allure.step('Выполняем запрос'):
        response = login_user(login_data)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 200

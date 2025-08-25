from api.auth.login_user import login_user
from data.login_data import success_login_data
import allure


@allure.feature("API login")
@allure.story('Авторизация с успешным входом')
@allure.severity(allure.severity_level.BLOCKER)
def test_success_login():
    with allure.step('Получаем валидные данные для авторизации'):
        login_data = success_login_data()
    with allure.step('Выполняем запрос'):
        response = login_user(login_data)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 200

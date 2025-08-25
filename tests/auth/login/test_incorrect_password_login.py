from api.auth.login_user import login_user
from utils.generator import generate_invalid_password
import allure


@allure.feature("API login")
@allure.story('Авторизация с неправильным password')
@allure.severity(allure.severity_level.NORMAL)
def test_incorrect_password_login():
    with allure.step('Генерация данных для авторизации с неправильным password'):
        login_data = generate_invalid_password()
    with allure.step('Выполняем запрос'):
        response = login_user(login_data)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 401

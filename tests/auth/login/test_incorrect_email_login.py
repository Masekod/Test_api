from api.auth.login_user import login_user
from utils.generator import generate_invalid_email
import allure


@allure.feature("API login")
@allure.story('Авторизация с неправильным email')
@allure.severity(allure.severity_level.NORMAL)
def test_incorrect_email_data():
    with allure.step('Генерация данных для авторизации с неправильным email'):
        login_data = generate_invalid_email()
    with allure.step('Выполняем запрос'):
        response = login_user(login_data)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 401

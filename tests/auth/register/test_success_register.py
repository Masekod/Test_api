from api.auth.register_user import register_user
from utils.generator import generate_random_user
import allure


@allure.feature("API register")
@allure.story('Регистрация пользователя')
@allure.severity(allure.severity_level.BLOCKER)
def test_success_register():
    with allure.step('Регистрация рандомного пользователя'):
        register_data = generate_random_user()
    with allure.step('Выполняем запрос'):
        response = register_user(register_data)
    with allure.step('Проверяем статус код ответа'):
        assert response.status_code == 201

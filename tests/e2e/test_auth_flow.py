import allure
import pytest
from http import HTTPStatus
from utils.generator import generate_random_email, generate_random_password


@allure.feature("Авторизация")
@allure.story("Выпронение е2е теста на регистрацию и авторизацию")
@pytest.mark.e2e
def test_auth_flow(api_client):
    # 1. Регистрация нового пользователя
    with allure.step("Регистрация нового пользователя"):
        user_data = {
            "email": generate_random_email(),
            "password": generate_random_password()
        }
        register_response = api_client.register(user_data)
        assert register_response.status_code == HTTPStatus.CREATED

    # 2. Авторизация под зарегистрированным пользователем
    with allure.step("Авторизаия пользователя с теми же данными"):
        credentials = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
    login_response = api_client.login(credentials)
    assert login_response.status_code == HTTPStatus.OK

    # 3. Получение списка дел
    with allure.step("Получеие списка задач для авторизованного пользователя"):
        tasks_response = api_client.get_tasks()
        assert tasks_response.status_code == HTTPStatus.OK
        # Проверим, что список задач является списком
        assert isinstance(tasks_response.json(), list)

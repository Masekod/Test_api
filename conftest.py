import pytest
import requests
from api.ApiClient import ApiClient
from config.settings import BASE_URL
# from api.auth.login_user import login_user
from utils.utils import get_current_email, get_current_password


# Фикстура создания api клиента
@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


# фикстура для работы с access token
# @pytest.fixture(scope="session")
# def auth_token(api_client):
#     credentials = {
#         "email": get_current_email(),
#         "password": get_current_password()
#     }
#     response = api_client.login(credentials)
#     assert response.status_code == 200
#     yield api_client.access_token
#     api_client.clear_tokens()


# @pytest.fixture(scope='session')
# def auth_token():
#     """Фикстура успешной авторизации и возврата токена"""
#     login_data = {
#     "email": get_current_email(),
#     "password": get_current_password()
#     }
#     response = login_user(login_data)
#     token = response.json().get('accessToken')
#     return token


@pytest.fixture(scope='session')
def auth_session():
    # requests.Session() - это объект в requests
    # который позволяет сохранить настройки и параметры между HTTP-запросами.
    # Самое главное: он автоматически сохраняет и отправляет cookie между запросами, как это делает браузер
    # Если использовть requests.Session(), то cookie будут сохраняться между запросами
    # Создаём сессию и авторизуем пользователя, сохраняя refresh cookie
    session = requests.Session()
    login_data = {
        "email": get_current_email(),
        "password": get_current_password()
    }
    response = session.post(f'{BASE_URL}/api/auth/login', json=login_data)
    assert response.status_code == 200, f"Login failed: {response.text}"

    session.refresh_token = lambda: session.get(f"{BASE_URL}/api/auth/refresh")

    return session

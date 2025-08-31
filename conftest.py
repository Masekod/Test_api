import pytest
import requests
from config.settings import BASE_URL
from api.auth.login_user import login_user
from utils.utils import get_current_email, get_current_password

@pytest.fixture(scope='session')
def auth_token():
    """Фикстура успешной авторизации и возврата токена"""

    login_data = {"email": get_current_email(), "password": get_current_password()}
    response = login_user(login_data)
    token = response.json().get('accessToken')
    return token


@pytest.fixture(scope='session')
def cookie_token():
    # Создаём сессию и авторизуем пользователя, сохраняя refresh coockie
    session = requests.Session()
    login_data = {"email": get_current_email(), "password": get_current_password()}
    response = session.post(f'{BASE_URL}/api/auth/login', json=login_data)
    assert response.status_code == 200, "Авторизация завершилась ошибкой"
    return session


@pytest.fixture(scope='function')
def change_email():
    """Фикстура успешной авторизации и возврата токена"""
    login_data = {"email": get_current_email(), "password": get_current_password()}
    response = login_user(login_data)
    token = response.json().get('accessToken')
    return token
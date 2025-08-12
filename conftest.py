import pytest
import requests
from config.settings import BASE_URL
from api.auth.login_user import login_user
from data.login_data import success_login_data


@pytest.fixture(scope='session')
def auth_token():
    """Фикстура успешной авторизации и возврата токена"""

    login_data = success_login_data()
    response = login_user(login_data)
    token = response.json().get('accessToken')
    return token


@pytest.fixture(scope='session')
def cookie_token():
    # Создаём сессию и авторизуем пользователя, сохраняя refresh coockie
    session = requests.Session()
    login_data = success_login_data()
    response = session.post(f'{BASE_URL}/api/auth/login', json=login_data)
    assert response.status_code == 200, "Авторизация завершилась ошибкой"
    return session


@pytest.fixture
def dict_names():
    return {
        "name": "Oleg",
        "dateOfBirth": "2003-08-04",
        "surname": "Bergov",
        "patronymic": "Sergeevich",
        "sex": "m",
        "phone": "+7 (914) 172-72-67"
    }

import requests
from config.settings import BASE_URL, make_headers
from conftest import auth_token


def logout_user(auth_token):
    headers = make_headers(auth_token)
    return requests.get(f'{BASE_URL}/api/auth/logout', headers=headers)

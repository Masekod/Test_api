import requests
from config.settings import BASE_URL, make_headers
from conftest import auth_token
from utils.utils import log_allure_api


@log_allure_api
def logout_user(auth_token):
    headers = make_headers(auth_token)
    return requests.get(f'{BASE_URL}/api/auth/logout', headers=headers)

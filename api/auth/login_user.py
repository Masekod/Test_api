import requests
from config.settings import BASE_URL
from utils.utils import log_allure_api


@log_allure_api
def login_user(login_data):
    response = requests.post(f'{BASE_URL}/api/auth/login', json=login_data)
    return response

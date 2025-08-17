import requests
from config.settings import BASE_URL
from utils.utils import add_body_to_allure


def login_user(login_data):
    add_body_to_allure(login_data, "Тело запроса")
    response = requests.post(f'{BASE_URL}/api/auth/login', json=login_data)
    add_body_to_allure(response.json(), "Тело ответа")
    return response

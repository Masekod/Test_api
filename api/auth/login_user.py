import requests
from config.settings import BASE_URL
from utils.utils import add_body_to_allure


def login_user(request_payload):
    add_body_to_allure(request_payload, "Тело запроса")
    response = requests.post(f'{BASE_URL}/api/auth/login', json=request_payload)
    add_body_to_allure(response.json(), "Тело ответа")
    return response

import requests
from config.settings import BASE_URL, make_headers
from utils.generator import generate_new_task
from utils.utils import add_body_to_allure


def create_new_task(auth_token):
    headers = make_headers(auth_token)
    body = generate_new_task()
    add_body_to_allure(body, "Тело запроса")
    response = requests.post(f'{BASE_URL}/api/todos/create', headers=headers, json=body)
    add_body_to_allure(response.json(), "Тело ответа")
    return response

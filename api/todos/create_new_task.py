import requests
from config.settings import BASE_URL, make_headers
from utils.generator import generate_new_task
from utils.utils import log_allure_api


@log_allure_api
def create_new_task(auth_token):
    headers = make_headers(auth_token)
    body = generate_new_task()
    return requests.post(f'{BASE_URL}/api/todos/create', headers=headers, json=body)

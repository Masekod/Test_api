import requests
from config.settings import BASE_URL, make_headers
from conftest import auth_token
from utils.utils import add_body_to_allure


def get_task_by_title(title, auth_token):
    headers = make_headers(auth_token)
    params = {
        'title': title,
    }
    response = requests.get(f'{BASE_URL}/api/todos/search', headers=headers, params=params)
    add_body_to_allure(response.json(), "Тело ответа")
    return response

import requests
from config.settings import BASE_URL, make_headers
from utils.utils import add_body_to_allure


def get_users_tasks(auth_token):
    headers = make_headers(auth_token)
    response =  requests.get(f'{BASE_URL}/api/todos', headers=headers)
    if response.content:
        try:
            json_body = response.json()
        except ValueError:
            json_body = None
    else:
        json_body = None
    add_body_to_allure(json_body,"Тело ответа")
    return response

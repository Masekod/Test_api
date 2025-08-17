import requests
from config.settings import BASE_URL, make_headers
from utils.utils import log_allure_api


@log_allure_api
def get_users_tasks(auth_token):
    headers = make_headers(auth_token)
    return requests.get(f'{BASE_URL}/api/todos', headers=headers)

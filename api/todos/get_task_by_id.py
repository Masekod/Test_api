import requests
from api.todos.get_users_tasks import get_users_tasks
from config.settings import BASE_URL, make_headers
from utils.utils import log_allure_api

get_task_id = None

@log_allure_api
def get_task_by_id(auth_token):
    global get_task_id
    headers = make_headers(auth_token)
    all_tasks = get_users_tasks(auth_token).json()

    last_task = all_tasks[-1]
    task_id = last_task['id']

    return requests.get(f'{BASE_URL}/api/todos/{task_id}', headers=headers)

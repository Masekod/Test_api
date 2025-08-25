import requests
from api.todos.get_users_tasks import get_users_tasks
from config.settings import BASE_URL, make_headers
from utils.utils import add_body_to_allure

get_task_id = None


def get_task_by_id(auth_token):
    global get_task_id
    headers = make_headers(auth_token)
    all_tasks = get_users_tasks(auth_token).json()

    last_task = all_tasks[-1]
    task_id = last_task['id']

    add_body_to_allure(last_task, "Тело запроса")
    response = requests.get(f'{BASE_URL}/api/todos/{task_id}', headers=headers)
    add_body_to_allure(response.json(), "Тело ответа")
    return response

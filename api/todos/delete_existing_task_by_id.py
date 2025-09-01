import requests
from api.todos.get_users_tasks import get_users_tasks
from config.settings import BASE_URL, make_headers
from utils.utils import add_body_to_allure


def delete_existing_task_by_id(auth_token):
    headers = make_headers(auth_token)
    all_tasks = get_users_tasks(auth_token).json()

    if not all_tasks:
        print("У пользователя нет задач.")
        return None

    last_task = all_tasks[-1]
    task_id = last_task['id']

    response = requests.delete(f'{BASE_URL}/api/todos/delete/{task_id}', headers=headers)
    try:
        response_body = response.json()
    except ValueError:  # Если тела нет
        response_body = {"message": "No content"}

    add_body_to_allure(response_body, "Тело ответа")
    return response

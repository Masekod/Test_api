import requests
from api.todos.get_users_tasks import get_users_tasks
from config.settings import BASE_URL, make_headers

get_task_id = None


def get_task_by_id(auth_token):
    global get_task_id
    headers = make_headers(auth_token)
    all_task = get_users_tasks(auth_token).json()
    for task in all_task:
        if task['title'] == 'test task':
            get_task_id = task['id']
            break
    if get_task_id is None:
        print("Задача не найдена")

    return requests.get(f'{BASE_URL}/api/todos/{get_task_id}', headers=headers)

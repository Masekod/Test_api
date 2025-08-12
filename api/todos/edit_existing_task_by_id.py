import requests
from api.todos.get_users_tasks import get_users_tasks
from config.settings import BASE_URL, make_headers

edit_task_id = None


def edit_existing_task_by_id(auth_token):
    global edit_task_id
    headers = make_headers(auth_token)
    all_task = get_users_tasks(auth_token).json()
    for task in all_task:
        if task['title'] == 'test task':
            edit_task_id = task['id']
            old_task = task
            break
    if edit_task_id is None:
        print("Задача не найдена")
    else:
        edit_task_payload = {
            "title": "test task",
            "description": old_task['description'],
            "date": old_task['date'],
            "time": old_task['time'],
            "checked": old_task['checked']
        }

    return requests.patch(f'{BASE_URL}/api/todos/edit/{edit_task_id}', headers=headers, json=edit_task_payload)

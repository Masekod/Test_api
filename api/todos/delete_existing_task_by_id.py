import requests
from api.todos.get_users_tasks import get_users_tasks
from config.settings import BASE_URL, make_headers

delete_task_id = None

def delete_existing_task_by_id(auth_token):
    global delete_task_id
    headers = make_headers(auth_token)
    all_task = get_users_tasks(auth_token).json()
    for task in all_task:
        if task['title'] == 'test task':
            delete_task_id = task['id']
            break
    if delete_task_id is None:
        print("Задача не найдена")

    delete_existing_task_by_id_response = requests.delete(
        f'{BASE_URL}/api/todos/delete/{delete_task_id}',
        headers=headers
    )
    return delete_existing_task_by_id_response.status_code

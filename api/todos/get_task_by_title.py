import requests
from config.settings import BASE_URL, make_headers
from conftest import auth_token


def get_task_by_title(title, auth_token):
    headers = make_headers(auth_token)
    params = {
        'title': title,
    }
    return requests.get(f'{BASE_URL}/api/todos/search', headers=headers, params=params)


print(get_task_by_title('test task', auth_token))

import requests
from config.settings import BASE_URL, make_headers


def create_new_task(auth_token):
    headers = make_headers(auth_token)
    payloads = {
        "title": "test task",
        "description": "Creating it is good",
        "date": "2025-08-02",
        "time": "21:30",
        "checked": True
    }
    return requests.post(
        f'{BASE_URL}/api/todos/create',
        headers=headers,
        json=payloads)

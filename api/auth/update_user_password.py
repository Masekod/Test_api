import requests
from config.settings import BASE_URL, make_headers


def update_user_password(auth_token, data: dict):
    headers = make_headers(auth_token)
    return requests.patch(f'{BASE_URL}/api/auth/update-pass', headers=headers, json=data)
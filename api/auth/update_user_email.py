import requests
from config.settings import BASE_URL, make_headers


def update_user_email(auth_token):
    headers = make_headers(auth_token)
    data = {
        "email": "bingo321@mail.ru",
        "password": '321Ytrewq'
    }

    return requests.patch(f'{BASE_URL}/api/auth/update-email', headers=headers, json=data)

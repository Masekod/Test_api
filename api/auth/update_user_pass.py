import requests
from config.settings import BASE_URL, make_headers
from data.login_data import success_login_data


def update_user_pass(auth_token):
    headers = make_headers(auth_token)

    data = success_login_data()
    return requests.patch(f'{BASE_URL}/api/auth/update-pass', headers=headers, json=data)

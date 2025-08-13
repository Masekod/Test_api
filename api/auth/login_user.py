import requests
from config.settings import BASE_URL


def login_user(login_data):
    return requests.post(f'{BASE_URL}/api/auth/login', json=login_data)

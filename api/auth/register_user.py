import requests
from config.settings import BASE_URL


def register_user(register_data):
    return requests.post(f'{BASE_URL}/api/auth/register', json=register_data)

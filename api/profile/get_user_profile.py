import requests
from config.settings import BASE_URL, make_headers


def get_user_profile(auth_token):
    headers = make_headers(auth_token)
    print("Get profile")
    return requests.get(f'{BASE_URL}/api/profile/get', headers=headers)

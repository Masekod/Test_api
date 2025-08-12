import requests
from config.settings import BASE_URL, make_headers


def save_user_profile(dict_names, auth_token):
    headers = make_headers(auth_token)
    return requests.post(f'{BASE_URL}/api/profile/save', headers=headers, json=dict_names)

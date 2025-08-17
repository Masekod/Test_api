import requests
from config.settings import BASE_URL, make_headers
from utils.generator import generate_profile_data
from utils.utils import log_allure_api


@log_allure_api
def save_user_profile(auth_token):
    headers = make_headers(auth_token)
    body = generate_profile_data()
    return requests.post(f'{BASE_URL}/api/profile/save', headers=headers, json=body)

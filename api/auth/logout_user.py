import requests
from config.settings import BASE_URL, make_headers
from utils.utils import add_body_to_allure


def logout_user(auth_token):
    headers = make_headers(auth_token)
    response = requests.get(f'{BASE_URL}/api/auth/logout', headers=headers)
    try:
        body = response.json()
    except ValueError:
        body = response.text or "Empty response body"
    add_body_to_allure(body, "Тело ответа")
    return response

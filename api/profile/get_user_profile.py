# import requests
# from config.settings import BASE_URL, make_headers
# from utils.utils import add_body_to_allure
#
#
# def get_user_profile(auth_token):
#     headers = make_headers(auth_token)
#     response = requests.get(f'{BASE_URL}/api/profile/get', headers=headers)
#     add_body_to_allure(response.json(), "Тело ответа")
#     return response

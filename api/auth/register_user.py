# import requests
# from config.settings import BASE_URL
# from utils.utils import add_body_to_allure
#
#
# def register_user(register_data):
#     add_body_to_allure(register_data, "Тело запроса")
#     response = requests.post(f'{BASE_URL}/api/auth/register', json=register_data)
#     add_body_to_allure(response.json(), "Тело ответа")
#     return response

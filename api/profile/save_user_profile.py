# import requests
# from config.settings import BASE_URL, make_headers
# from utils.generator import generate_profile_data
# from utils.utils import add_body_to_allure
#
#
# def save_user_profile(auth_token):
#     headers = make_headers(auth_token)
#     body = generate_profile_data()
#     add_body_to_allure(body, "Тело запроса")
#     response = requests.post(f'{BASE_URL}/api/profile/save', headers=headers, json=body)
#     add_body_to_allure(response.json(), "Тело ответа")
#     return response

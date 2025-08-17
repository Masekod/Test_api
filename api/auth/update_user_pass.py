import requests
from config.settings import BASE_URL, make_headers


def update_user_pass(auth_token):
    headers = make_headers(auth_token)

    data = {
        "password": "321Ytrewq",
        "newPassword": "321Ytrewq321"

        # "password": "321Ytrewq321",
        # "newPassword": "321Ytrewq"

    }
    return requests.patch(f'{BASE_URL}/api/auth/update-pass', headers=headers, json=data)

# def update_user_pass(auth_token):
#     login_token = login_user("bingo@mail.ru", "Qwerty123@123qwerty")
#     # login_token = login_user("bingo@mail.ru", "321Ytrewq")
#     data = {
#         "password": "Qwerty123@123qwerty",
#         "newPassword": "321Ytrewq"
#         #
#         # "password": "321Ytrewq",
#         # "newPassword": "Qwerty123@123qwerty"
#
#     }
#     headers = set_auth_header(login_token['accessToken'])
#     update_user_password_response = requests.patch(f'{BASE_URL}/api/auth/update-pass', headers=headers, json=data)
#     print(update_user_password_response.status_code)
#     print(update_user_password_response.json())
#     return update_user_password_response.status_code

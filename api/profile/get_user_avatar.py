import requests
import os

from config.settings import BASE_URL, make_headers


def get_user_avatar(auth_token):
    headers = make_headers(auth_token)
    get_user_avatar_response = requests.get(f'{BASE_URL}/api/profile/image', headers=headers)
    os.makedirs('images', exist_ok=True)
    path = os.path.join(os.getcwd(), 'images/avatar.jpg')
    with open('images/avatar.jpg', 'wb') as f:
        f.write(get_user_avatar_response.content)
        os.startfile(path)
    print("	Avatar received successfully")
    return get_user_avatar_response.status_code

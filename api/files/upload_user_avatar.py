import requests
from requests.models import Response
from config.settings import BASE_URL, make_headers

def fake_response(status):
    r = Response()
    r.status_code = status
    return r

def upload_user_avatar(auth_token, file_path):
    headers = make_headers(auth_token)

    if not file_path:
        return fake_response(400)

    if not file_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        print("Неверный формат файла.")
        return fake_response(400)

    try:
        with open(file_path, 'rb') as file:
            files = {'image': (file_path.split("/")[-1], file)}
            return requests.post(f'{BASE_URL}/api/files/upload', headers=headers, files=files)
    except FileNotFoundError:
        return fake_response(400)

import requests
import allure
from config.settings import BASE_URL, make_headers
from utils.utils import add_body_to_allure


def get_user_avatar(auth_token):
    headers = make_headers(auth_token)
    get_user_avatar_response = requests.get(f'{BASE_URL}/api/profile/image', headers=headers)
    add_body_to_allure(
        {
            "status_code": get_user_avatar_response.status_code,
            "content_type": get_user_avatar_response.headers.get("Content-Type")
        }, "Тело ответа")

    # Прикрепляем изображение напрямую к Allure без сохранения на диск
    allure.attach(
        get_user_avatar_response.content,
        name="Response Image",
        attachment_type=allure.attachment_type.JPG
    )

    print("Avatar received successfully")
    return get_user_avatar_response.status_code

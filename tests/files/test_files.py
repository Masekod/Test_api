import pytest
from http import HTTPStatus
from api.files.upload_user_avatar import  upload_user_avatar
import allure


@allure.feature("Добавление аватара")
@pytest.mark.avatar
@pytest.mark.parametrize(
    "file_path, expected_status",
    [
        ("tests/files/avatar/valid.png", HTTPStatus.CREATED),
        ("tests/files/avatar/invalid.txt", HTTPStatus.BAD_REQUEST),
        (None , HTTPStatus.BAD_REQUEST),
    ]

)
def test_upload_user_avatar(auth_token, file_path, expected_status):
    allure.dynamic.story("Успешное и неуспешное добавление аватара")
    allure.dynamic.title(f"Тест загрузки аватара: {file_path}")

    with allure.step(f"Отправляем файл {file_path} для загрузки"):
        response = upload_user_avatar(auth_token, file_path)

    with allure.step("Проверяем статус ответа"):
        assert response.status_code == expected_status

@allure.feature("Добавление аватара")
@allure.story('Невалидный токен')
@allure.title("Попытка загрузки аватара с невалидным токеном")
def test_upload_user_avatar_with_invalid_token():
    fake_token = '123.invalid.token'

    with allure.step("Отправляем файл с невалидным токеном"):
        response =  upload_user_avatar(fake_token, "tests/files/avatar/valid.png")

    with allure.step("Проверяем, что ответ UNAUTHORIZED"):
        assert response.status_code == HTTPStatus.UNAUTHORIZED

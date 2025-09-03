import pytest
from http import HTTPStatus
import allure


@allure.feature("Добавление аватара")
@allure.story('Валидный токен')
@allure.title("Попытка загрузки аватара с невалидным токеном")
@pytest.mark.parametrize(
    "file_path, expected_status",
    [
        ("tests/files/avatar/valid.png", HTTPStatus.CREATED),
        ("tests/files/avatar/invalid.txt", HTTPStatus.BAD_REQUEST),
        (None, HTTPStatus.BAD_REQUEST),
    ]

)
def test_upload_user_avatar(api_client, file_path, expected_status):
    allure.dynamic.story("Успешное и неуспешное добавление аватара")
    allure.dynamic.title(f"Тест загрузки аватара: {file_path}")

    with allure.step(f"Отправляем файл {file_path} для загрузки"):
        response = api_client.add_avatar(file_path)

    with allure.step("Проверяем статус ответа"):
        assert response.status_code == expected_status

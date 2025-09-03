from http import HTTPStatus
import allure


@allure.feature("Получение аватара пользователя")
def test_get_user_avatar(api_client):
    with allure.step("Отправка запроса"):
        response = api_client.get_user_avatar()
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == HTTPStatus.OK
        # Прикрепляем изображение напрямую к Allure без сохранения на диск
        allure.attach(
            response.content,
            name="Response Image",
            attachment_type=allure.attachment_type.JPG
        )

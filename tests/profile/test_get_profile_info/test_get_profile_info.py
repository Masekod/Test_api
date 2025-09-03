import allure
import json


@allure.feature("Получение данных пользователя")
def test_get_profile_info(api_client):
    with allure.step("Данные пользователя"):
        response = api_client.get_user_profile()
        body = response.json()
        allure.attach(
            json.dumps(body, indent=4, ensure_ascii=False),
            name="User Profile JSON",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка данных пользователя"):
        assert len(body['avatar']) > 0
        assert len(body['dateOfBirth']) > 0
        assert body['id'] > 0 and isinstance(body['id'], int)
        assert len(body['name']) > 0
        assert len(body['patronymic']) > 0
        assert len(body['phone']) > 0
        assert len(body['sex']) == 1
        assert len(body['surname']) > 0
        assert body['userId'] > 0 and isinstance(body['userId'], int)

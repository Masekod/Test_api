import allure
from http import HTTPStatus


@allure.feature("Обновление токена")
@allure.story('Проверка статус кода ответа')
def test_refresh_bearer_token(auth_session):
    response = auth_session.refresh_token()
    assert response.status_code == HTTPStatus.OK


@allure.feature("Обновление токена")
@allure.story('Проверка токена в json')
def test_refresh_bearer_token_is_not_empty(auth_session):
    response = auth_session.refresh_token()
    json = response.json()
    assert 'accessToken' in json

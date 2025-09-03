from http import HTTPStatus
import allure


@allure.feature("Logout")
def test_logout_user(api_client):
    response = api_client.logout()
    assert response.status_code == HTTPStatus.OK

from api.auth.logout_user import logout_user
from http import HTTPStatus

def test_logout_user(auth_token):
    response = logout_user(auth_token)
    assert response.status_code == HTTPStatus.OK

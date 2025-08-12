from api.auth.logout_user import logout_user


def test_logout_user(auth_token):
    response = logout_user(auth_token)
    assert response.status_code == 200

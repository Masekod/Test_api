from api.auth.login_user import login_user
from data.login_data import incorrect_password_login


def test_incorrect_password_login():
    login_data = incorrect_password_login()
    response = login_user(login_data)
    assert response.status_code == 401

from api.auth.login_user import login_user
from utils.generator import generate_invalid_password


def test_incorrect_password_login():
    login_data = generate_invalid_password()
    response = login_user(login_data)
    assert response.status_code == 401

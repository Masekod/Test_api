from api.auth.login_user import login_user
from utils.generator import generate_invalid_email


def test_incorrect_email_data():
    login_data = generate_invalid_email()
    response = login_user(login_data)
    assert response.status_code == 401

from api.auth.login_user import login_user
from data.login_data import incorrect_email_data


def test_incorrect_email_data():
    login_data = incorrect_email_data()
    response = login_user(login_data)
    assert response.status_code == 401

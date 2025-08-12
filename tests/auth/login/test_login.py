from api.auth.login_user import login_user
from data.login_data import success_login_data


def test_success_login():
    login_data = success_login_data()
    response = login_user(login_data)
    assert response.status_code == 200

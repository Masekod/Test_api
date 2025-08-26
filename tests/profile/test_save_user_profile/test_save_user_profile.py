from api.profile.save_user_profile import save_user_profile
from http import HTTPStatus

def test_save_user_profile(auth_token):
    assert save_user_profile(auth_token).status_code == HTTPStatus.OK

from api.profile.get_user_avatar import get_user_avatar
from http import HTTPStatus

def test_get_user_avatar(auth_token):
    assert get_user_avatar(auth_token) == HTTPStatus.OK

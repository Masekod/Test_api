import pytest
from http import HTTPStatus
from api.files.upload_user_avatar import  upload_user_avatar

@pytest.mark.avatar
def test_upload_user_avatar(auth_token):
    assert upload_user_avatar(auth_token).status_code == HTTPStatus.CREATED

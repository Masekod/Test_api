import pytest
from http import HTTPStatus
from api.files.upload_user_avatar import  upload_user_avatar

@pytest.mark.avatar
@pytest.mark.parametrize(
    "file_path, expected_status",
    [
        ("tests/files/avatar/valid.png", HTTPStatus.CREATED),
        ("tests/files/avatar/invalid.txt", HTTPStatus.BAD_REQUEST),
        (None , HTTPStatus.BAD_REQUEST),
    ]

)
def test_upload_user_avatar(auth_token, file_path, expected_status):
    response =  upload_user_avatar(auth_token, file_path)
    assert response.status_code == expected_status


def test_upload_user_avatar_with_invalid_token():
    fake_token = '123.invalid.token'
    response =  upload_user_avatar(fake_token, "tests/files/avatar/valid.png")
    assert response.status_code == HTTPStatus.UNAUTHORIZED

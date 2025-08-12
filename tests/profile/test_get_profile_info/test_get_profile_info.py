from api.profile.get_user_profile import get_user_profile


def test_get_profile_info(auth_token):
    assert get_user_profile(auth_token).status_code == 200

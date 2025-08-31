from api.profile.get_user_profile import get_user_profile


def test_get_profile_info(auth_token):
    response = get_user_profile(auth_token)
    body = response.json()

    avatar = body['avatar']
    date_of_birth = body['dateOfBirth']
    id = body['id']
    name = body['name']
    patronymic = body['patronymic']
    phone = body['phone']
    sex = body['sex']
    surname = body['surname']
    user_id = body['userId']

    assert len(avatar) > 0
    assert len(date_of_birth) > 0
    assert id > 0
    assert isinstance(id, int)
    assert len(name) > 0
    assert len(patronymic) > 0
    assert len(phone) > 0
    assert len(sex) == 1
    assert len(surname) > 0
    assert user_id > 0
    assert isinstance(user_id, int)

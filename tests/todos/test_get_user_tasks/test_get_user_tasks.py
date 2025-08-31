from api.todos.get_users_tasks import get_users_tasks
from http import HTTPStatus

def test_get_users_tasks(auth_token):
    assert get_users_tasks(auth_token).status_code == HTTPStatus.OK
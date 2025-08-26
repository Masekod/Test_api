from api.todos.get_task_by_title import get_task_by_title
from http import HTTPStatus

def test_get_task_by_title(auth_token):
    assert get_task_by_title('title', auth_token).status_code == HTTPStatus.OK

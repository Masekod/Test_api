from api.todos.get_task_by_id import get_task_by_id


def test_get_task_by_id(auth_token):
    assert get_task_by_id(auth_token).status_code == 200
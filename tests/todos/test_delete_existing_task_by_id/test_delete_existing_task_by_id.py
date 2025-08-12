from api.todos.delete_existing_task_by_id import delete_existing_task_by_id


def test_delete_existing_task_by_id(auth_token):
    assert delete_existing_task_by_id(auth_token) == 204
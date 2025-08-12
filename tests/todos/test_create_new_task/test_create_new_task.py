from api.todos.create_new_task import create_new_task


def test_create_new_task(auth_token):
    assert create_new_task(auth_token).status_code == 201
from api.todos.edit_existing_task_by_id import edit_existing_task_by_id



def test_edit_existing_task_by_id(auth_token):
    assert edit_existing_task_by_id(auth_token).status_code == 200
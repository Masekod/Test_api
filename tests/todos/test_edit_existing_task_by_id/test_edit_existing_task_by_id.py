import allure
from http import HTTPStatus
from shcemas.todos.TodosModel import TodosSuccessResponse
from utils.generator import edit_task_payload


@allure.feature("Обновление задачи по id")
@allure.story("Успешное обновление задачи")
def test_edit_existing_task_by_id(api_client):
    with allure.step("Получение списка задач"):
        all_tasks_response = api_client.get_tasks()
        assert all_tasks_response.status_code == HTTPStatus.OK
        all_tasks = all_tasks_response.json()
        assert all_tasks, "Список задач пустой"

        last_task = all_tasks[-1]
        task_id = last_task['id']

    with allure.step(f"Получение задачи по id={task_id}"):
        body = edit_task_payload(last_task)
        response = api_client.update_task_by_id(task_id, body)
        assert response.status_code == HTTPStatus.OK
        task_data = response.json()

    with allure.step("Проверка структуры и содержимого задачи"):
        validated = TodosSuccessResponse(**task_data).model_dump()
        assert task_data == validated, "Структура задачи не соответствует схеме"

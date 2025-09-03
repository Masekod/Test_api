import allure
from http import HTTPStatus
from shcemas.todos.TodosModel import TodosSuccessResponse


@allure.feature("Получение задачи по id")
@allure.story("Успешное получение задачи")
def test_get_task_by_id(api_client):
    with allure.step("Получение списка задач"):
        all_tasks_response = api_client.get_tasks()
        assert all_tasks_response.status_code == HTTPStatus.OK
        all_tasks = all_tasks_response.json()
        assert all_tasks, "Список задач пустой"

        last_task = all_tasks[-1]
        task_id = last_task['id']

    with allure.step(f"Получение задачи по id={task_id}"):
        response = api_client.get_task_by_id(task_id)
        assert response.status_code == HTTPStatus.OK
        task_data = response.json()

    with allure.step("Проверка структуры и содержимого задачи"):
        validated = TodosSuccessResponse(**task_data).model_dump()
        assert task_data == validated, "Структура задачи не соответствует схеме"
        for key in ["id", "title", "description", "date", "time", "checked", "userId"]:
            assert task_data[key] == last_task[key], f"Поле {key} не совпадает"

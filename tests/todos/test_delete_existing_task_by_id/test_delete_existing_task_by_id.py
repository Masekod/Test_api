import allure
from http import HTTPStatus


@allure.feature("Удаление задачи по id")
@allure.story("Успешное удаление")
def test_delete_existing_task_by_id(api_client):
    with allure.step("Получение списка задач"):
        all_tasks_response = api_client.get_tasks()
        assert all_tasks_response.status_code == HTTPStatus.OK
        all_tasks = all_tasks_response.json()
        assert all_tasks, "Список задач пустой"

        last_task = all_tasks[-1]
        task_id = last_task['id']

    with allure.step("Отправка запроса на удаление существующей залачи"):
        response = api_client.delete_task_by_id(task_id)
    with allure.step("Проверка статус кода"):
        assert response.status_code == HTTPStatus.NO_CONTENT
    with allure.step("Проверка отсутствия тела ответа"):
        assert response.text == ""  # тело пустое

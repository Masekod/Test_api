import allure
from shcemas.todos.TodosModel import TodosSuccessResponse


@allure.feature("Получение задачи по title")
@allure.story("Успешное получение задачи")
def test_get_task_by_title(api_client):
    task_title = "Падать ход налоговый мелькнуть возможно."

    with allure.step("Отправка запроса"):
        response = api_client.get_task_by_title(task_title)
        data = response.json()

    with allure.step("Проверка структуры тела ответа"):
        validated = [TodosSuccessResponse(**item).model_dump() for item in data]
        assert data == validated

    with allure.step("Проверка, что результат содержит искомый title"):
        assert any(item['title'] == task_title for item in data), "Задача с указанным title не найдена"

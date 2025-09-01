from api.todos.get_task_by_title import get_task_by_title
import allure

from shcemas.todos.TodosModel import TodosSuccessResponse


@allure.feature("Получение задачи по title")
@allure.story("Успешное получение задачи")
def test_get_task_by_title(auth_token):
    with allure.step("Отправка запроса"):
        response = get_task_by_title('title', auth_token)
        data = response.json()

    with allure.step("Проверка структуры тела ответа"):
        validated = [TodosSuccessResponse(**item).model_dump() for item in data]
        assert data == validated

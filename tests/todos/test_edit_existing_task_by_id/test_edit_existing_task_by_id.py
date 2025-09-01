from api.todos.edit_existing_task_by_id import edit_existing_task_by_id
from shcemas.todos.TodosModel import TodosSuccessResponse
import allure


@allure.feature("Обновление задачи")
@allure.story("Успешное обновление задачи")
def test_edit_existing_task_by_id(auth_token):
    with allure.step("Отправка запроса"):
        response = edit_existing_task_by_id(auth_token)
    with allure.step("Проверка структуры тела ответа"):
        assert response.json() == TodosSuccessResponse(**response.json()).model_dump()

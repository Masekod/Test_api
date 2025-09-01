from api.todos.create_new_task import create_new_task
from shcemas.todos.TodosModel import TodosSuccessResponse
import allure


@allure.feature("Создание задачи")
@allure.story("Успешное создание задачи")
def test_create_new_task(auth_token):
    with allure.step("Отправка запроса"):
        response = create_new_task(auth_token)

    with allure.step("Проверка структуры тела ответа"):
        assert response.json() == TodosSuccessResponse(**response.json()).model_dump()

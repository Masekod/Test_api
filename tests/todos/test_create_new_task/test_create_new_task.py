from shcemas.todos.TodosModel import TodosSuccessResponse
import allure

from utils.generator import generate_new_task


@allure.feature("Создание задачи")
@allure.story("Успешное создание задачи")
def test_create_new_task_body(api_client):
    with allure.step("Отправка запроса"):
        test_task = generate_new_task()
        response = api_client.create_task(test_task)
        allure.attach(
            str(test_task),
            name="Request body",
            attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            str(response.json()),
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )
    with allure.step("Проверка структуры тела ответа"):
        assert response.json() == TodosSuccessResponse(**response.json()).model_dump()

import allure
from http import HTTPStatus
from shcemas.todos.TodosModel import TodosSuccessResponse
import json

@allure.feature("Получение списка задач")
@allure.story('Проверка статус кода ответа')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_users_tasks_status(api_client):
    response = api_client.get_tasks()
    assert response.status_code == HTTPStatus.OK


@allure.feature("Получение списка задач")
@allure.story("Проверка структуры тела ответа")
def test_get_users_tasks(api_client):
    with allure.step("Отправка запроса"):
        response = api_client.get_tasks()
        data = response.json()

        allure.attach(
            json.dumps(data, indent=2, ensure_ascii=False),
            name="Список задач",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверка структуры тела ответа"):
        validated = [TodosSuccessResponse(**item).model_dump() for item in data]
        assert data == validated

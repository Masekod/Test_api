from api.todos.delete_existing_task_by_id import delete_existing_task_by_id
import allure
from http import HTTPStatus


@allure.feature("Удаление задачи")
@allure.story("Успешное удаление")
def test_delete_existing_task_by_id(auth_token):
    with allure.step("Отправка запроса на удаление существующей залачи"):
        response = delete_existing_task_by_id(auth_token)
    with allure.step("Проверка статус кода"):
        assert response.status_code == HTTPStatus.NO_CONTENT
    with allure.step("Проверка отсутствия тела ответа"):
        assert response.text == ""  # тело пустое
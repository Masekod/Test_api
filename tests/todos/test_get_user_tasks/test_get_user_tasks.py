from api.todos.get_users_tasks import get_users_tasks
import allure
from shcemas.todos.TodosModel import TodosSuccessResponse



@allure.feature("Получение списка задач")
@allure.story("Успешное получение списка задач")
def test_get_users_tasks(auth_token):
    with allure.step("Отправка запроса"):
        response = get_users_tasks(auth_token)
        data = response.json()
    with allure.step("Проверка структуры тела ответа"):
        validated = [TodosSuccessResponse(**item).model_dump() for item in data]
        assert data == validated
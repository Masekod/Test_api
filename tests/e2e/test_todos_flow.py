import allure
import pytest
from http import HTTPStatus

from config.settings import CREDENTIALS_PASSWORD, CREDENTIALS_EMAIL
from utils.generator import generate_new_task


@allure.feature("Авторизация")
@allure.story("Выпронение е2е теста на регистрацию и авторизацию")
@pytest.mark.e2e
def test_todos_flow(api_client):
    # 1. Авторизация
    with allure.step("Регистрация пользователя"):
        credentials = {
            "email": CREDENTIALS_EMAIL,
            "password": CREDENTIALS_PASSWORD
        }
        login_resp = api_client.login(credentials)
        assert login_resp.status_code == HTTPStatus.OK

    # 2. Получение списка дел
    with allure.step("Получеие списка задач"):
        tasks_resp = api_client.get_tasks()
        assert tasks_resp.status_code == HTTPStatus.OK
        initial_tasks = tasks_resp.json()
        assert isinstance(initial_tasks, list)

    # 3. Создание новой задачи
    with allure.step("Создание новой задачи"):
        new_task = generate_new_task()
        create_resp = api_client.create_task(new_task)
        assert create_resp.status_code == HTTPStatus.CREATED
        task_id = create_resp.json().get("id")
        assert task_id is not None

    # 4. Обновление задачи
    with allure.step("Обновление созданной задачи"):
        updated_task = generate_new_task()
        update_resp = api_client.update_task_by_id(task_id, updated_task)
        assert update_resp.status_code == HTTPStatus.OK
        assert update_resp.json().get("title") == updated_task["title"]
        assert update_resp.json().get("description") == updated_task["description"]

    # 5. Удаление задачи
    with allure.step("Удаление обновленной задачи"):
        delete_resp = api_client.delete_task_by_id(task_id)
        assert delete_resp.status_code == HTTPStatus.NO_CONTENT

    # 6. Проверка, что задачи нет
    with allure.step("Проверка отсутствия удалённой задачи в списке"):
        final_tasks_resp = api_client.get_tasks()
        assert final_tasks_resp.status_code == HTTPStatus.OK
        final_tasks = final_tasks_resp.json()
        task_ids = [task["id"] for task in final_tasks]
        assert task_id not in task_ids
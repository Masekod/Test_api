import requests
import allure
from typing import Dict, Any
from requests import HTTPError, RequestException, Timeout, Response
from config.settings import BASE_URL


# Паттерн API Client (аналог Page Object Model)
# Инкапсулирует все HTTP-запросы в отдельный класс ApiClient
# Это отделяет логику взаимодейсвтия API от тестов, упрощает смену базового URL или заголовков
# Этот паттерн даёт центролизованное управление запросами, переиспользование кода, легкую интеграци авторизации
# (токен хранится в сеcсии)

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None

    # Внутренний метод для выполнения HTTP-запросов с обработкой ошибок
    def _request(self, method, endpoint, **kwargs) -> Response | None | Any:
        url = f"{self.base_url}{endpoint}"
        allure.attach(
            f"Request: {method} {url}",
            name="Request details",
            attachment_type=allure.attachment_type.TEXT
        )
        if 'json' in kwargs:
            allure.attach(
                str(kwargs['json']),
                name="Request body",
                attachment_type=allure.attachment_type.JSON
            )

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()  # Обработка ошибок при 4хх/5xx статус кодов
            return response
        except (HTTPError, ConnectionError, Timeout, RequestException) as e:
            allure.attach(
                str(e),
                name="Error details",
                attachment_type=allure.attachment_type.TEXT
            )
            print(f"Request error: {e}")
            # Возвращаем объект ответа даже при ошибке, чтобы тест мог его проанализировать
            if isinstance(e, HTTPError):
                return e.response
            # В случае других ошибок возвращаем None или пустой объект ответа
            return None

    # Методы API
    @allure.step("Авторизация пользователя")
    def login(self, credentials: Dict[str, Any]) -> requests.Response:
        response = self.session.post(f"{self.base_url}/api/auth/login", json=credentials)
        if response.status_code == 200:
            self.set_tokens(
                response.json().get("accessToken"),
                response.json().get('refreshToken'),
            )
        return response

    @allure.step("Регистрация пользователя")
    def register(self, user_data: Dict[str, Any]) -> requests.Response:
        response = self.session.post(f"{self.base_url}/api/auth/register", json=user_data)
        if response.status_code == 201 and "accessToken" in response.json():
            self.set_tokens(
                response.json().get("accessToken"),
                response.json().get("refreshToken"),
            )
        return response

    @allure.step("Выход из системы")
    def logout(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/auth/logout")

    @allure.step("Обновление токена")
    def refresh(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/auth/refresh")

    @allure.step("Смена почты")
    def change_email(self, task_data) -> requests.Response:
        return self.session.patch(f"{self.base_url}/api/auth/update-email", json=task_data)

    @allure.step("Смена пароля")
    def change_password(self, task_data) -> requests.Response:
        return self.session.patch(f"{self.base_url}/api/auth/update-pass", json=task_data)

    @allure.step("Сохранение данные пользователя")
    def save_user_profile(self, body) -> requests.Response:
        return self.session.post(f"{self.base_url}/api/profile/save", json=body)

    @allure.step("Получение аватара пользователя")
    def get_user_avatar(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/profile/image")

    @allure.step("Получение данных пользователя")
    def get_user_profile(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/profile/get")

    @allure.step("Создание задачи")
    def create_task(self, task_data) -> requests.Response:
        return self.session.post(f"{self.base_url}/api/todos/create", json=task_data)

    @allure.step("Обновление задачи по id")
    def update_task_by_id(self, task_id: str, task_data) -> requests.Response:
        return self.session.patch(f"{self.base_url}/api/todos/edit/{task_id}", json=task_data)

    @allure.step("Удаление задачи по id")
    def delete_task_by_id(self, task_id: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}/api/todos/delete/{task_id}")

    @allure.step("Получение списка задач")
    def get_tasks(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/todos")

    @allure.step("Получение задачи по title")
    def get_task_by_title(self, task_title: str) -> requests.Response:
        params = {"title": task_title}
        return self.session.get(f"{self.base_url}/api/todos/search", params=params)

    @allure.step("Получение задачи по id")
    def get_task_by_id(self, task_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/api/todos/{task_id}")

    @allure.step("Добавление аватара")
    def add_avatar(self, file_path: str) -> requests.Response:
        if not file_path or not file_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            resp = Response()
            resp.status_code = 400
            return resp

        with open(file_path, 'rb') as file:
            files = {'image': (file_path.split("/")[-1], file)}
            return self.session.post(f'{BASE_URL}/api/files/upload', files=files)

    # Служебные методы
    def set_tokens(self, access_token, refresh_token):
        """При сохранении токенов обновить заголовки"""
        if access_token:
            self.access_token = access_token
            self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})
        if refresh_token:
            self.refresh_token = refresh_token

    def clear_tokens(self):
        """Очистить токены и заголовки при вызове метода logout"""
        self.access_token = None
        self.refresh_token = None
        self.session.headers.pop("Authorization", None)

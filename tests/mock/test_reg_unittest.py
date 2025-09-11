import unittest
from unittest.mock import patch, MagicMock
from api.ApiClient import ApiClient
class TestApiClientRegister(unittest.TestCase):
    # В unittest есть встроенные хуки setUp() и tearDown(), которые выполняются перед/после каждого теста
    def setUp(self):
        """Этот метод выполняется перед КАЖДЫМ тестом"""
        self.client = ApiClient()
    @patch("requests.Session.request")
    def test_register_success(self, mock_request):
        """Успешная регистрация пользователя"""
        # --- Описываем тестовые данные, которые хотим получить в ответ---
        # Этот фрагмент кода используется для создания мок-объекта (макета) HTTP-ответа,
        # который имитирует поведение сервера при выполнении запроса.
        # Мы используем его, чтобы избежать реальных сетевых вызовов и проверить, как система обрабатывает определённые ответы.
        # Создание мок-объекта ответа
        mock_response = MagicMock()
        # Здесь создаётся экземпляр `MagicMock` — инструмента библиотеки `unittest.mock`, который позволяет создавать объекты с любыми атрибутами и методами. В данном случае он будет имитировать HTTP-ответ.
        # Ниже задание статус-кода ответа
        mock_response.status_code = 201
        # Ниже идёт настройка JSON-данных ответа
        mock_response.json.return_value = {
            "accessToken": "fake_access",
            "refreshToken": "fake_refresh",
            "user": {
                "id": 1,
                "email": "vadim_zviagintsev@mail.ru"
            }
        }
        # Здесь настраивается поведение метода `.json()` объекта `fake_response`. Когда этот метод будет вызван, он вернёт указанный словарь с данными, например, токенами доступа и информации о пользователе. Это имитирует успешный ответ API, например, после регистрации или авторизации
        # Ниже привязываем мок-ответа к мок-запросу
        mock_request.return_value = mock_response
        # Здесь объект `mock_request`, который, скорее всего, является моком функции, выполняющей HTTP-запросы (например, `requests.post`), настраивается так, чтобы возвращать ранее созданный `fake_response`. Это позволяет в тестах заменить настоящий вызов API на возвращение заранее заданных данных.
        # --- Отправляем запрос ---
        response = self.client.register({"email": "vadim_zviagintsev@mail.ru", "password": "VadimQA"})
        # --- Делаем проверки ---
        # Этот фрагмент кода представляет собой набор утверждений (asserts), используемых в тесте, с использованием unittest.
        # Целью этого кода является проверка корректности работы функционала регистрации пользователя в системе.
        # Ниже приведено подробное объяснение каждой строки и общего функционала
        # Проверка статус-кода ответа
        # - Эта строка проверяет, что HTTP-статус ответа равен `201`, что означает "Created" — успешное создание ресурса.
        # - Если статус не соответствует ожидаемому, тест завершится с ошибкой.
        self.assertEqual(response.status_code, 201)
        # Проверка ID пользователя в JSON-ответе
        # - Здесь извлекается JSON-тело ответа (`response.json()`), а затем проверяется значение поля `"id"` под ключом `"user"`.
        # - Ожидается, что пользователь будет иметь идентификатор `1`.
        self.assertEqual(response.json()["user"]["id"], 1)
        # Проверка email пользователя в JSON-ответ
        # - Проверяется, что поле `"email"` возвращённого пользователя совпадает с ожидаемым значением `"vadim_zviagintsev@mail.ru"`.
        # - Это гарантирует, что данные пользователя были корректно сохранены и возвращены.
        self.assertEqual(response.json()["user"]["email"], "vadim_zviagintsev@mail.ru")
        # Проверка access_token клиента
        # - Проверяется, что клиент после регистрации получил ожидаемый `access_token` — `"fake_access"`.
        # - Обычно это используется для авторизации в дальнейших запросах.
        self.assertEqual(self.client.access_token, "fake_access")
        # Проверка refresh_token клиента
        # - Аналогично предыдущему шагу, проверяется, что клиент получил ожидаемый `refresh_token` — `"fake_refresh"`.
        # - Такие токены часто используются для обновления `access_token`, когда последний истёк
        self.assertEqual(self.client.refresh_token, "fake_refresh")
        # Проверка вызова метода mock_request
        mock_request.assert_called_once_with(
            "POST",
            f"{self.client.base_url}/api/auth/register",
            json={"email": "vadim_zviagintsev@mail.ru", "password": "VadimQA"}
        )
    @patch("requests.Session.request")
    def test_register_bad_request(self, mock_request):
        """Ошибка при регистрации (400 Bad Request)"""
        # --- Описываем тестовые данные, которые хотим получить в ответ---
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {
          "statusCode": 400,
          "message": "Bad Request"
        }
        mock_request.return_value = mock_response
        # --- Отправляем запрос ---
        response = self.client.register({"email": "vadim_zviagintsev@mail.ru", "password": "VadimQA"})
        # --- Делаем проверки ---
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Bad Request")
        self.assertIsNone(self.client.access_token)  # токены не должны обновиться
        self.assertIsNone(self.client.refresh_token)
    @patch("requests.Session.request")
    def test_register_server_error(self, mock_request):
        """Ошибка 500 от сервера"""
        # --- Описываем тестовые данные, которые хотим получить в ответ---
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {
          "statusCode": 500,
          "message": "Internal server"
        }
        mock_request.return_value = mock_response
        # --- Отправляем запрос ---
        response = self.client.register({"email": "vadim_zviagintsev@mail.ru", "password": "VadimQA"})
        # --- Делаем проверки ---
        self.assertEqual(response.status_code, 500)
        self.assertIsNone(self.client.access_token)
        self.assertIsNone(self.client.refresh_token)
        """
        Также есть другие assert-методы, например:
        assertEqual(a, b) — a == b - проверка равенства по значению
        assertTrue(x) — bool(x) is True
        assertFalse(x) — bool(x) is False
        assertIs(a, b) — a is b проверка равенства по ссылке, т.е. проверка a и b ссылаются на один и тот же объект
        assertIsNot(a, b) — a is not b
        assertIsNone(x) — x is None
        assertIsNotNone(x) — x is not None
        """
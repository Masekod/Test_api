import unittest
from unittest.mock import patch, MagicMock
from api.ApiClient import ApiClient


class TestApiClientLogin(unittest.TestCase):
    def setUp(self):
        """Создаём клиент перед каждым тестом"""
        self.client = ApiClient()

    @patch("requests.Session.request")
    def test_login_success(self, mock_request):
        """Успешная авторизация пользователя"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "accessToken": "fake_access_login",
            "refreshToken": "fake_refresh_login",
            "user": {
                "id": 1,
                "email": "simple_test@mail.ru"
            }
        }
        mock_request.return_value = mock_response
        response = self.client.login({"email": "simple_test@mail.ru", "password": "SimpleQA"})
        # ---Проверки---
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["user"]["id"], 1)
        self.assertEqual(response.json()["user"]["email"], "simple_test@mail.ru")
        self.assertEqual(self.client.access_token, "fake_access_login")
        self.assertEqual(self.client.refresh_token, "fake_refresh_login")
        mock_request.assert_called_once_with(
            "POST",
            f"{self.client.base_url}/api/auth/login",
            json={"email": "simple_test@mail.ru", "password": "SimpleQA"}

        )

    @patch("requests.Session.request")
    def test_login_unauthorized(self, mock_request):
        """Ошибка при неверных данных (401 Unauthorized)"""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {
            "statusCode": 401,
            "message": "Unauthorized"
        }
        mock_request.return_value = mock_response
        response = self.client.login(
            {"email": "simple_test@mail.ru", "password": "wrongpass"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["message"], "Unauthorized")
        self.assertIsNone(self.client.access_token)
        self.assertIsNone(self.client.refresh_token)

    @patch("requests.Session.request")
    def test_login_server_error(self, mock_request):
        """Ошибка сервера (500 Internal Server Error)"""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {
            "statusCode": 500,
            "message": "Internal Server Error"
        }
        mock_request.return_value = mock_response
        response = self.client.login({
            "email": "simple_test@mail.ru",
            "password": "SimpleQA"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json()["message"], "Internal Server Error")
        self.assertIsNone(self.client.access_token)
        self.assertIsNone(self.client.refresh_token)

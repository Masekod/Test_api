import allure
import json
import functools
import requests


# Добавляем тело запроса/ответа в Allure отчет
def add_body_to_allure(body, body_type):
    allure.attach(
        json.dumps(body, ensure_ascii=False, indent=3),
        # json.dumps - превращает словарь в строку, indent=3 - добавляет 3 отступа
        name=body_type,
        attachment_type=allure.attachment_type.JSON
    )


# Дебаг API ответа
def api_debug(response):
    print("=== DEBUG INFO ===")
    print(f"Status Code: {response.status_code}")
    print("Request:")
    print(f"URL: {response.request.url}")
    print(f"Method: {response.request.method}")
    print(f"Headers: {response.request.headers}")
    print(f"Body: {response.request.body}")

    print("Response:")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text}")

    try:
        print(f"JSON: {response.json()}")
    except ValueError:
        print("Response is not JSON")

    print("=== END DEBUG ===")



def log_allure_api(func):
    """
    Декоратор для автоматической отправки запроса и логирования в Allure
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # --- тело запроса ---
        body = kwargs.get('json') or kwargs.get('data')
        if body is not None:
            add_body_to_allure(body, "Тело запроса")
        url = kwargs.get('url') or (args[0] if args else 'Unknown URL')
        method = func.__name__.upper()
        request_info = {
            "method": method,
            "url": url,
            "body": body if body is not None else "No body"
        }
        add_body_to_allure(request_info, "Запрос")

        # --- вызов функции ---
        response = func(*args, **kwargs)

        # --- тело ответа ---
        if isinstance(response, requests.Response):
            try:
                content = response.json()
            except ValueError:
                content = response.text or f"No content, status: {response.status_code}"
            response_info = {
                "status_code": response.status_code,
                "body": content
            }
            add_body_to_allure(response_info, "Ответ")
        else:
            # если функция вернула что-то кроме Response
            add_body_to_allure(str(response), "Ответ")

        return response

    return wrapper

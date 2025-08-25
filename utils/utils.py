import allure
import json


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

    body = response.request.body
    if body:
        if isinstance(body, bytes):
            body = body.decode("utf-8")
        try:
            parsed = json.loads(body)
            print(json.dumps(parsed, ensure_ascii=False, indent=4))
        except:
            print(body)

    print("Response:")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text}")

    try:
        response_json = response.json()
        print("JSON:", json.dumps(response_json, ensure_ascii=False, indent=4))
    except ValueError:
        print("Response is not JSON")

    print("=== END DEBUG ===")

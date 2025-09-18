from utils.generator import generate_random_email, generate_random_password

BASE_URL = 'http://2.59.41.2:7320'

NEW_EMAIL = generate_random_email()
NEW_PASSWORD = generate_random_password()

INVALID_EMAIL = "new_email_test.com"
INVALID_PASSWORD = '1'

CREDENTIALS_EMAIL = 'first_test@mail.ru'
CREDENTIALS_PASSWORD = 'testwork'

# def make_headers(auth_token: str) -> dict:
#     return {"Authorization": f"Bearer {auth_token}"}

from utils.generator import generate_random_email


BASE_URL = 'http://2.59.41.2:7320'

CREDENTIALS_PASSWORD = "321Ytrewq"

NEW_EMAIL = generate_random_email()
INVALID_EMAIL = "new_email_test.com"

def make_headers(auth_token: str) -> dict:
    return {"Authorization": f"Bearer {auth_token}"}

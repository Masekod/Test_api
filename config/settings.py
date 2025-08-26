BASE_URL = 'http://2.59.41.2:7320'
CREDENTIALS_EMAIL = "bingo@mail.ru"
CREDENTIALS_PASSWORD = "321Ytrewq"



def make_headers(auth_token: str) -> dict:
    return {"Authorization": f"Bearer {auth_token}"}

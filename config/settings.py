BASE_URL = 'http://2.59.41.2:7320'


def make_headers(auth_token: str) -> dict:
    return {"Authorization": f"Bearer {auth_token}"}


# def set_auth_header(token):
#     return {
#         'Authorization': f'Bearer {token}',
#         'Content-Type': 'application/json'
#     }

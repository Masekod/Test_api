# import requests
#
# from api.auth.refresh_bearer_token import refresh_bearer_token
# from config.settings import BASE_URL
#
#
# def test_refresh_bearer_token(cookie_token):
#     response = refresh_bearer_token(cookie_token)
#     assert response.status_code == 200
#
#
# def test_refresh_bearer_token_is_not_empty(cookie_token):
#     response = refresh_bearer_token(cookie_token)
#     json = response.json()
#     assert 'accessToken' in json
#
#
# def test_refresh_bearer_token_missing_cookie():
#     session = requests.Session()
#     response = refresh_bearer_token(session)
#     assert response.status_code == 401
#
#
# def test_refresh_bearer_token_invalid_cookie():
#     session = requests.Session()
#     session.cookies.set(
#         "refreshToken",
#         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3QxMjNAbWFpbC5ydSIsImlkIjo4NzgwLCJpYXQiOjE3NTQ3MzY0NDYsImV4cCI6MTc1NDc0MDA0Nn0.KWlIvX5QW_hPIN5FRuxkvliT1X78FsE2SgrPzF93q1k",
#         domain=BASE_URL)
#     response = refresh_bearer_token(session)
#     assert response.status_code == 401
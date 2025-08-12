from config.settings import BASE_URL


def refresh_bearer_token(session):
    return session.get(f'{BASE_URL}/api/auth/refresh')

import time


def generate_test_email_with_password():
    timestamp = int(time.time() * 1000)
    print(timestamp)
    return {
        "email": f"test_user_{timestamp}@mail.com",
        "password": "321Ytrewq"
    }

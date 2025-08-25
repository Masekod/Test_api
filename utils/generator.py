from faker import Faker
import random

fake = Faker("ru_RU")


def generate_random_user():
    return {
        "email": fake.email(),
        "password": fake.password(length=10)
    }


def generate_invalid_email():
    return {
        "email": fake.email(),
        "password": "QWERTY!@#"
    }


def generate_invalid_password():
    return {
        "email": "bingo@mail.ru",
        "password": fake.password(length=10)
    }


def generate_random_gender():
    return random.choice(["m", "f"])


def generate_profile_data():
    return {
        "name": fake.first_name(),
        "patronymic": fake.middle_name(),
        "surname": fake.last_name(),
        "dateOfBirth": fake.date(),
        "sex": generate_random_gender(),
        "phone": fake.numerify("+7 (9##) ###-##-##")
    }


def random_bool():
    return random.choice([True, False])


def generate_next_7_days_data() -> str:
    # Случайная дата в пределах ближайших 7 дней без времени в формате YYYY-MM-DD
    random_date = fake.date_between(start_date="today", end_date="+7d")
    return random_date.strftime("%Y-%m-%d")


def generate_new_task():
    return {
        "title": fake.text(max_nb_chars=50),
        "description": fake.text(max_nb_chars=100),
        "date": generate_next_7_days_data(),
        "time": fake.time(pattern="%H:%M"),
        "checked": random_bool()
    }


def edit_task_payload(last_task):
    return {
        "title": fake.text(max_nb_chars=50),
        "description": last_task['description'],
        "date": last_task['date'],
        "time": last_task['time'],
        "checked": last_task['checked']
    }

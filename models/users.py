from dataclasses import dataclass
import time


@dataclass
class User:
    email: str
    firstname: str
    lastname: str
    password: str


LOGIN_USER = User(
    email = 'qwe@qwe543.com',
    firstname = 'John',
    lastname = 'Doe',
    password = 'qwe123'
)


def generate_user():
    return User(
        email = f'user{int(time.time())}@example.com',
        firstname = 'John',
        lastname = 'Doe',
        password = 'qwe123'
    )

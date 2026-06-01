import uuid

import requests

from urls import DELETE_USER_ENDPOINT, REGISTER_ENDPOINT


def generate_user_credentials() -> dict:
    unique_part = uuid.uuid4().hex[:10]
    return {
        "email": f"autotest_{unique_part}@yandex.ru",
        "password": "123456",
        "name": "Autotest User",
    }


def register_user(credentials: dict) -> dict:
    response = requests.post(
        REGISTER_ENDPOINT,
        json=credentials,
    )
    response.raise_for_status()
    return response.json()


def delete_user(access_token: str) -> None:
    requests.delete(
        DELETE_USER_ENDPOINT,
        headers={"Authorization": access_token},
    )

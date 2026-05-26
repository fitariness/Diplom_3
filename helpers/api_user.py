import uuid

import requests

import config


def generate_user_credentials() -> dict:
    unique_part = uuid.uuid4().hex[:10]
    return {
        "email": f"autotest_{unique_part}@yandex.ru",
        "password": "123456",
        "name": "Autotest User",
    }


def register_user(credentials: dict) -> dict:
    response = requests.post(
        f"{config.API_URL}/auth/register",
        json=credentials,
    )
    response.raise_for_status()
    return response.json()


def delete_user(access_token: str) -> None:
    requests.delete(
        f"{config.API_URL}/auth/user",
        headers={"Authorization": access_token},
    )


def create_order(access_token: str, ingredient_ids: list[str] | None = None) -> dict:
    payload = {
        "ingredients": ingredient_ids or config.ORDER_INGREDIENT_IDS,
    }
    response = requests.post(
        f"{config.API_URL}/orders",
        json=payload,
        headers={"Authorization": access_token},
    )
    response.raise_for_status()
    return response.json()


def authorize_driver(driver, user_data: dict) -> None:
    driver.get(config.BASE_URL)
    driver.execute_script(
        "localStorage.setItem('accessToken', arguments[0]);",
        user_data["accessToken"],
    )
    driver.execute_script(
        "localStorage.setItem('refreshToken', arguments[0]);",
        user_data["refreshToken"],
    )
    driver.refresh()

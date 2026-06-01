import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

import config
from config import IMPLICIT_WAIT
from helpers.api_user import delete_user, generate_user_credentials, register_user
from pages.base_page import BasePage


@pytest.fixture(params=["chrome", "firefox"], ids=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        browser_driver = webdriver.Chrome(options=options)
    else:
        browser_driver = webdriver.Firefox()
        browser_driver.set_window_size(1920, 1080)

    browser_driver.implicitly_wait(IMPLICIT_WAIT)
    yield browser_driver
    browser_driver.quit()


@pytest.fixture
def registered_user():
    credentials = generate_user_credentials()
    user_data = register_user(credentials)
    yield user_data
    delete_user(user_data["accessToken"])


@pytest.fixture
def authorized_driver(driver, registered_user):
    page = BasePage(driver)
    page.authorize_with_tokens(
        config.BASE_URL, registered_user["accessToken"], registered_user["refreshToken"]
    )
    return driver

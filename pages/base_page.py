import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    @allure.step("Дождаться видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента")
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Дождаться исчезновения элемента")
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Перейти на URL")
    def navigate_to(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Обновить страницу")
    def refresh_page(self) -> None:
        self.driver.refresh()

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Найти элементы по локатору")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу через JavaScript")
    def click_js(self, element):
        self.execute_script("arguments[0].click();", element)

    @allure.step("Авторизовать пользователя через токены")
    def authorize_with_tokens(self, base_url: str, access_token: str, refresh_token: str) -> None:
        self.navigate_to(base_url)
        self.execute_script(
            "localStorage.setItem('accessToken', arguments[0]);",
            access_token,
        )
        self.execute_script(
            "localStorage.setItem('refreshToken', arguments[0]);",
            refresh_token,
        )
        self.refresh_page()

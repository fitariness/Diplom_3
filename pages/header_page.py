import allure

from locators.header_locators import HeaderLocators as Loc
from pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step("Кликнуть «Конструктор» в шапке")
    def click_constructor(self):
        self.wait_clickable(Loc.CONSTRUCTOR_LINK).click()

    @allure.step("Кликнуть «Лента заказов» в шапке")
    def click_order_feed(self):
        self.wait_clickable(Loc.FEED_LINK).click()

    @allure.step("Проверить, что активна ссылка «Конструктор»")
    def is_constructor_link_active(self) -> bool:
        return len(self.driver.find_elements(*Loc.CONSTRUCTOR_LINK_ACTIVE)) > 0

    @allure.step("Проверить, что активна ссылка «Лента заказов»")
    def is_feed_link_active(self) -> bool:
        return len(self.driver.find_elements(*Loc.FEED_LINK_ACTIVE)) > 0

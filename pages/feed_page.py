import allure

from locators.feed_locators import FeedLocators as Loc
from pages.header_page import HeaderPage
from urls import FEED_PAGE_URL, MAIN_PAGE_URL


class FeedPage(HeaderPage):
    @allure.step('Открыть страницу ленты заказов')
    def open(self):
        self.driver.get(FEED_PAGE_URL)

    @allure.step('Дождаться загрузки ленты заказов')
    def wait_feed_loaded(self):
        self.wait_visible(Loc.FEED_TITLE)
        self.wait_visible(Loc.ORDERS_LIST)

    @allure.step('Получить заголовок ленты заказов')
    def get_feed_title(self) -> str:
        return self.wait_visible(Loc.FEED_TITLE).text

    @allure.step('Получить счётчик «Выполнено за всё время»')
    def get_total_orders_count(self) -> int:
        return int(self.wait_visible(Loc.TOTAL_ORDERS_COUNTER).text)

    @allure.step('Получить счётчик «Выполнено за сегодня»')
    def get_today_orders_count(self) -> int:
        return int(self.wait_visible(Loc.TODAY_ORDERS_COUNTER).text)

    @allure.step('Обновить ленту после создания заказа')
    def refresh_after_new_order(self):
        self.driver.get(MAIN_PAGE_URL)
        self.open()
        self.wait_feed_loaded()

    @allure.step('Дождаться увеличения счётчика «Выполнено за всё время»')
    def wait_total_orders_count_increased(self, previous_count: int) -> None:
        self.wait.until(lambda _: self.get_total_orders_count() > previous_count)

    @allure.step('Дождаться увеличения счётчика «Выполнено за сегодня»')
    def wait_today_orders_count_increased(self, previous_count: int) -> None:
        self.wait.until(lambda _: self.get_today_orders_count() > previous_count)

    @allure.step('Получить номера заказов в разделе «В работе»')
    def get_in_progress_order_numbers(self) -> list[str]:
        elements = self.driver.find_elements(*Loc.IN_PROGRESS_ORDER_NUMBERS)
        return [element.text.strip() for element in elements]

    @allure.step('Дождаться появления номера заказа в разделе «В работе»')
    def wait_order_in_progress(self, order_number: str) -> None:
        normalized_order = order_number.lstrip('0') or '0'
        self.wait.until(
            lambda driver: normalized_order
            in [
                number.lstrip('0') or '0'
                for number in self.get_in_progress_order_numbers()
            ]
        )

    def is_on_feed_url(self) -> bool:
        return '/feed' in self.get_current_url()

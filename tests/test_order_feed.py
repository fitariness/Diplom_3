import allure

from config import INGREDIENTS
from helpers.api_user import create_order
from helpers.checkers import check_counters_increased, check_order_in_progress, check_value_increased


@allure.feature('Лента заказов')
class TestOrderFeedCounters:
    @allure.title('Счётчик «Выполнено за всё время» увеличивается после нового заказа')
    def test_total_orders_counter_increases(self, feed_page, registered_user):
        """Проверка роста общего счётчика после создания нового заказа"""
        feed_page.open()
        feed_page.wait_feed_loaded()
        total_before = feed_page.get_total_orders_count()
        today_before = feed_page.get_today_orders_count()

        create_order(registered_user['accessToken'])
        feed_page.refresh_after_new_order()
        feed_page.wait_total_orders_count_increased(total_before)
        feed_page.wait_today_orders_count_increased(today_before)
        total_after = feed_page.get_total_orders_count()
        today_after = feed_page.get_today_orders_count()
        check_counters_increased(total_before, total_after, today_before, today_after)

    @allure.title('Счётчик «Выполнено за сегодня» увеличивается после нового заказа')
    def test_today_orders_counter_increases(self, feed_page, registered_user):
        """Проверка роста дневного счётчика после создания нового заказа"""
        feed_page.open()
        feed_page.wait_feed_loaded()
        today_before = feed_page.get_today_orders_count()

        create_order(registered_user['accessToken'])
        feed_page.refresh_after_new_order()
        feed_page.wait_today_orders_count_increased(today_before)
        today_after = feed_page.get_today_orders_count()
        check_value_increased(today_before, today_after)


@allure.feature('Лента заказов')
class TestOrderInProgress:
    @allure.title('Номер заказа появляется в разделе «В работе»')
    def test_order_number_appears_in_progress_section(
        self, authorized_constructor_page, authorized_feed_page
    ):
        """Проверка появления номера созданного заказа в разделе «В работе»"""
        authorized_constructor_page.open()
        authorized_constructor_page.wait_constructor_loaded()
        for ingredient in INGREDIENTS:
            authorized_constructor_page.drag_ingredient_to_order(ingredient['id'])
        authorized_constructor_page.click_place_order()
        authorized_constructor_page.wait_order_success_modal()
        order_number = authorized_constructor_page.get_order_number_from_modal()

        authorized_feed_page.open()
        authorized_feed_page.wait_feed_loaded()
        authorized_feed_page.wait_order_in_progress(order_number)
        check_order_in_progress(authorized_feed_page, order_number)

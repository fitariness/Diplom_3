import allure
import pytest

from config import INGREDIENTS
from helpers.checkers import (
    check_constructor_page_opened,
    check_counter_increased,
    check_feed_page_opened,
    check_ingredient_modal_opened,
    check_modal_closed,
    check_order_modal_opened,
)
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage

INGREDIENT_IDS = [ingredient["slug"] for ingredient in INGREDIENTS]


@allure.feature("Конструктор")
class TestConstructorNavigation:
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_navigates_to_constructor(self, driver):
        """Проверка перехода из ленты заказов в конструктор"""
        feed_page = FeedPage(driver)
        constructor_page = ConstructorPage(driver)
        feed_page.open()
        feed_page.wait_feed_loaded()
        constructor_page.click_constructor()
        constructor_page.wait_constructor_loaded()
        check_constructor_page_opened(constructor_page)

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed_navigates_to_feed(self, driver):
        """Проверка перехода из конструктора в ленту заказов"""
        constructor_page = ConstructorPage(driver)
        feed_page = FeedPage(driver)
        constructor_page.open()
        constructor_page.wait_constructor_loaded()
        constructor_page.click_order_feed()
        feed_page.wait_feed_loaded()
        check_feed_page_opened(feed_page)


@allure.feature("Конструктор")
class TestIngredientModal:
    @allure.title("По клику на ингредиент открывается модальное окно с деталями")
    @pytest.mark.parametrize("ingredient", INGREDIENTS, ids=INGREDIENT_IDS)
    def test_click_ingredient_opens_details_modal(self, driver, ingredient):
        """Проверка открытия модального окна для каждого типа ингредиента"""
        constructor_page = ConstructorPage(driver)
        constructor_page.open()
        constructor_page.wait_constructor_loaded()
        constructor_page.click_ingredient(ingredient["id"])
        constructor_page.wait_ingredient_modal()
        check_ingredient_modal_opened(constructor_page)

    @allure.title("Модальное окно закрывается кликом по крестику")
    @pytest.mark.parametrize("ingredient", INGREDIENTS, ids=INGREDIENT_IDS)
    def test_click_close_button_closes_modal(self, driver, ingredient):
        """Проверка закрытия модального окна ингредиента по крестику"""
        constructor_page = ConstructorPage(driver)
        constructor_page.open()
        constructor_page.wait_constructor_loaded()
        constructor_page.click_ingredient(ingredient["id"])
        constructor_page.wait_ingredient_modal()
        constructor_page.close_modal()
        check_modal_closed(constructor_page)


@allure.feature("Конструктор")
class TestIngredientCounter:
    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    @pytest.mark.parametrize("ingredient", INGREDIENTS, ids=INGREDIENT_IDS)
    def test_drag_ingredient_increases_counter(self, driver, ingredient):
        """Проверка роста счётчика после добавления ингредиента в заказ"""
        constructor_page = ConstructorPage(driver)
        constructor_page.open()
        constructor_page.wait_constructor_loaded()
        counter_before = constructor_page.get_ingredient_counter_value(ingredient["id"])
        constructor_page.drag_ingredient_to_order(ingredient["id"])
        counter_after = constructor_page.get_ingredient_counter_value(ingredient["id"])
        check_counter_increased(counter_before, counter_after)


@allure.feature("Конструктор")
class TestPlaceOrder:
    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, authorized_driver):
        """Проверка оформления заказа авторизованным пользователем"""
        constructor_page = ConstructorPage(authorized_driver)
        constructor_page.open()
        constructor_page.wait_constructor_loaded()
        for ingredient in INGREDIENTS:
            constructor_page.drag_ingredient_to_order(ingredient["id"])
        constructor_page.click_place_order()
        constructor_page.wait_order_success_modal()
        check_order_modal_opened(constructor_page)

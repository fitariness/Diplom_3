import allure

from config import BASE_URL
from locators.constructor_locators import ConstructorLocators as Loc
from locators.modal_locators import ModalLocators as ModalLoc
from pages.header_page import HeaderPage
from urls import MAIN_PAGE_URL


class ConstructorPage(HeaderPage):
    @allure.step("Открыть главную страницу — конструктор")
    def open(self):
        self.navigate_to(MAIN_PAGE_URL)

    @allure.step("Дождаться загрузки конструктора")
    def wait_constructor_loaded(self):
        self.wait_visible(Loc.CONSTRUCTOR_TITLE)
        self.wait_visible(Loc.ORDER_SECTION)

    @allure.step("Получить заголовок конструктора")
    def get_constructor_title(self) -> str:
        return self.wait_visible(Loc.CONSTRUCTOR_TITLE).text

    @allure.step("Кликнуть по ингредиенту")
    def click_ingredient(self, ingredient_id: str):
        self.wait_clickable(Loc.ingredient_card(ingredient_id)).click()

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter_value(self, ingredient_id: str) -> int:
        counter_text = self.wait_visible(Loc.ingredient_counter(ingredient_id)).text
        return int(counter_text)

    @allure.step("Перетащить ингредиент в конструктор заказа")
    def drag_ingredient_to_order(self, ingredient_id: str):
        ingredient = self.wait_visible(Loc.ingredient_card(ingredient_id))
        drop_zone = self.wait_visible(Loc.ORDER_DROP_ZONE_TOP)
        self.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', ingredient
        )
        self.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, dataTransfer}));
            target.dispatchEvent(new DragEvent('dragover', {bubbles: true, dataTransfer}));
            target.dispatchEvent(new DragEvent('drop', {bubbles: true, dataTransfer}));
            source.dispatchEvent(new DragEvent('dragend', {bubbles: true, dataTransfer}));
            """,
            ingredient,
            drop_zone,
        )

    @allure.step("Кликнуть «Оформить заказ»")
    def click_place_order(self):
        order_button = self.wait_clickable(Loc.ORDER_BUTTON)
        self.click_js(order_button)

    @allure.step("Дождаться модального окна ингредиента")
    def wait_ingredient_modal(self):
        self.wait_visible(ModalLoc.INGREDIENT_MODAL_TITLE)

    @allure.step("Получить заголовок модального окна ингредиента")
    def get_ingredient_modal_title(self) -> str:
        return self.wait_visible(ModalLoc.INGREDIENT_MODAL_TITLE).text

    @allure.step("Закрыть модальное окно по крестику")
    def close_modal(self):
        self.wait_clickable(ModalLoc.MODAL_CLOSE_BUTTON).click()

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self) -> bool:
        return len(self.find_elements(ModalLoc.OPENED_MODAL)) == 0

    @allure.step("Дождаться модального окна успешного заказа")
    def wait_order_success_modal(self):
        self.wait_visible(ModalLoc.ORDER_MODAL_SUBTITLE)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self) -> str:
        order_number_element = self.wait_visible(ModalLoc.ORDER_MODAL_NUMBER)
        self.wait.until(lambda _: order_number_element.text.strip() != "9999")
        return order_number_element.text.strip()

    @allure.step("Получить подзаголовок модального окна заказа")
    def get_order_modal_subtitle(self) -> str:
        return self.wait_visible(ModalLoc.ORDER_MODAL_SUBTITLE).text

    @allure.step("Проверить, что текущий URL соответствует странице конструктора")
    def is_on_constructor_url(self) -> bool:
        return self.get_current_url().rstrip("/") == BASE_URL.rstrip("/")

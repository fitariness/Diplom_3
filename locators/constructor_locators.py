from selenium.webdriver.common.by import By


class ConstructorLocators:
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'BurgerIngredients_ingredients')]"
        "//h1[contains(@class, 'text_type_main-large')]",
    )
    ORDER_SECTION = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    ORDER_DROP_ZONE_TOP = (
        By.XPATH,
        "//div[contains(@class, 'constructor-element_pos_top')]",
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'button') and text()='Оформить заказ']",
    )

    @staticmethod
    def ingredient_card(ingredient_id: str) -> tuple:
        return (
            By.XPATH,
            f"//a[contains(@href, '/ingredient/{ingredient_id}')]",
        )

    @staticmethod
    def ingredient_counter(ingredient_id: str) -> tuple:
        return (
            By.XPATH,
            f"//a[contains(@href, '/ingredient/{ingredient_id}')]"
            "//div[contains(@class, 'counter_counter')]"
            "//p[contains(@class, 'counter_counter__num')]",
        )

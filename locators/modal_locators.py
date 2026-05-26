from selenium.webdriver.common.by import By


class ModalLocators:
    OPENED_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal') and contains(@class, 'Modal_modal_opened')]",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//button[contains(@class, 'Modal_modal__close')]",
    )
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//h2[contains(@class, 'Modal_modal__title')]",
    )
    ORDER_MODAL_SUBTITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//h2/following-sibling::p[contains(@class, 'text_type_main-medium')]",
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//h2[contains(@class, 'text_type_digits-large')]",
    )
    ORDER_MODAL_LOADING = (
        By.XPATH,
        "//img[@alt='loading animation']",
    )

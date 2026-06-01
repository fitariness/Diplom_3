from selenium.webdriver.common.by import By


class FeedLocators:
    FEED_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_orderFeed')]//h1",
    )
    ORDERS_LIST = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_list')]",
    )
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    IN_PROGRESS_ORDERS_LIST = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]",
    )
    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]"
        "//li[contains(@class, 'text_type_digits-default')]",
    )

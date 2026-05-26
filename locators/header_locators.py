from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[contains(@class, 'AppHeader_header__link') and @href='/']",
    )
    CONSTRUCTOR_LINK_ACTIVE = (
        By.XPATH,
        "//a[contains(@class, 'AppHeader_header__link_active') and @href='/']",
    )
    FEED_LINK = (
        By.XPATH,
        "//a[contains(@class, 'AppHeader_header__link') and @href='/feed']",
    )
    FEED_LINK_ACTIVE = (
        By.XPATH,
        "//a[contains(@class, 'AppHeader_header__link_active') and @href='/feed']",
    )

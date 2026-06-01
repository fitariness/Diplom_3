def check_constructor_page_opened(constructor_page) -> None:
    """Проверка, что открыта страница конструктора"""
    assert constructor_page.is_on_constructor_url()
    assert "Соберите бургер" in constructor_page.get_constructor_title()
    assert constructor_page.is_constructor_link_active()


def check_feed_page_opened(feed_page) -> None:
    """Проверка, что открыта страница ленты заказов"""
    assert feed_page.is_on_feed_url()
    assert "Лента заказов" in feed_page.get_feed_title()
    assert feed_page.is_feed_link_active()


def check_ingredient_modal_opened(constructor_page) -> None:
    """Проверка открытия модального окна с деталями ингредиента"""
    assert "Детали ингредиента" in constructor_page.get_ingredient_modal_title()


def check_modal_closed(constructor_page) -> None:
    """Проверка закрытия модального окна"""
    assert constructor_page.is_modal_closed()


def check_counter_increased(before: int, after: int) -> None:
    """Проверка увеличения счётчика ингредиента"""
    assert after > before


def check_value_increased(before: int, after: int) -> None:
    """Проверка увеличения числового значения"""
    assert after > before


def check_order_modal_opened(constructor_page) -> None:
    """Проверка открытия модального окна успешного заказа"""
    assert "идентификатор заказа" in constructor_page.get_order_modal_subtitle()


def _normalize_order_number(order_number: str) -> str:
    return order_number.lstrip("0") or "0"


def check_order_in_progress(feed_page, order_number: str) -> None:
    """Проверка, что номер заказа появился в разделе «В работе»"""
    normalized_order = _normalize_order_number(order_number)
    feed_numbers = [
        _normalize_order_number(number)
        for number in feed_page.get_in_progress_order_numbers()
    ]
    assert normalized_order in feed_numbers


def check_counters_increased(
    total_before: int, total_after: int, today_before: int, today_after: int
) -> None:
    """Проверка роста общего и дневного счётчиков заказов"""
    assert total_after > total_before
    assert today_after > today_before

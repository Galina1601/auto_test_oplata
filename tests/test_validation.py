import time
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

#  Пустые поля (5 тестов)
def test_empty_card_number(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Пустой номер карты: нет ошибки"

def test_empty_month(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Пустой месяц: нет ошибки"

def test_empty_year(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Пустой год: нет ошибки"

def test_empty_owner(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Пустой владелец: нет ошибки"

def test_empty_cvc(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Пустой CVC: нет ошибки"

# ----- Невалидные значения (10 тестов) -----
def test_month_13(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("13")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Месяц 13: нет ошибки"

def test_year_expired(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("20")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Истёкший год (20): нет ошибки"

def test_owner_cyrillic(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("Иван Петров")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Кириллица: нет ошибки"

def test_owner_digits(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("12345")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Цифры в имени: нет ошибки"

def test_owner_special_chars(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("@#$%")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Спецсимволы в имени: нет ошибки"

def test_year_future(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()
    payment_page.wait_for_form()

    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("30")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Год 30: ожидалась ошибка"
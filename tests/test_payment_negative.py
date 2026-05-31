import time
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

def test_declined_card(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()

    payment_page.wait_for_form()
    payment_page.fill_card_number("5555 6666 7777 8888")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Отклонённая карта: нет ошибки"

def test_card_not_in_set(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()

    payment_page.wait_for_form()
    payment_page.fill_card_number("1234 5678 9012 3456")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("123")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ Карта не из набора: нет ошибки"

def test_invalid_cvc(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)

    main_page.open()
    main_page.click_buy_button()

    payment_page.wait_for_form()
    payment_page.fill_card_number("1111 2222 3333 4444")
    payment_page.fill_month("12")
    payment_page.fill_year("26")
    payment_page.fill_owner("Ivan Petrov")
    payment_page.fill_cvc("023")
    payment_page.click_submit()

    time.sleep(3)
    assert payment_page.is_error_message_displayed(), "❌ CVC 023: нет ошибки"


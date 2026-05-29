import allure
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

# Тест №1: Отклонённая карта 5555...
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

    assert not payment_page.is_success_message_displayed(), "❌ Баг: отклонённая карта дала успех!"

# Тест №2: Карта не из набора
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

    assert not payment_page.is_success_message_displayed(), "❌ Баг: карта не из набора дала успех!"

# Тест №3: Невалидный CVC 023
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

    assert not payment_page.is_success_message_displayed(), "❌ Баг: CVC 023 дал успех!"
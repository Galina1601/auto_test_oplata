from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']"))
        )

    def _get_all_inputs(self):
        """Внутренний метод: ждёт появления и возвращает список всех полей ввода"""
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(By.TAG_NAME, "input")) >= 5
        )
        return self.driver.find_elements(By.TAG_NAME, "input")

    def fill_card_number(self, card_number):
        inputs = self._get_all_inputs()
        inputs[0].send_keys(card_number)

    def fill_month(self, month):
        inputs = self._get_all_inputs()
        inputs[1].send_keys(month)

    def fill_year(self, year):
        inputs = self._get_all_inputs()
        inputs[2].send_keys(year)

    def fill_owner(self, owner):
        inputs = self._get_all_inputs()
        inputs[3].send_keys(owner)

    def fill_cvc(self, cvc):
        inputs = self._get_all_inputs()
        inputs[4].send_keys(cvc)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.button.button_view_extra").click()

    def is_success_message_displayed(self):
        try:
            WebDriverWait(self.driver, 15).until(
                lambda d: "Успешно" in d.page_source
            )
            return True
        except:
            return False
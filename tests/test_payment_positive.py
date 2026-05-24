import time
import psycopg2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_payment_positive(driver):
    driver.get("http://localhost:8080")
    driver.find_element(By.CSS_SELECTOR, "button[role='button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']"))
    )

    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "input")) >= 5
    )

    all_inputs = driver.find_elements(By.TAG_NAME, "input")

    all_inputs[0].send_keys("1111 2222 3333 4444")
    all_inputs[1].send_keys("12")
    all_inputs[2].send_keys("26")
    all_inputs[3].send_keys("Ivan Petrov")
    all_inputs[4].send_keys("123")

    driver.find_element(By.CSS_SELECTOR, "button.button.button_view_extra").click()

    # Ждём, пока на странице не появится слово "Успешно"
    WebDriverWait(driver, 20).until(
        lambda d: "Успешно" in d.page_source
    )

    time.sleep(2)

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="app",
        user="app",
        password="pass"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM payment_entity ORDER BY created DESC LIMIT 1;")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    assert row is not None, "В таблице payment_entity нет записей"
    status = row[0]
    assert status == "APPROVED"
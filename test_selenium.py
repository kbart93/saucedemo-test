import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://www.saucedemo.com/"
driver.get(url)

logging.basicConfig(level=logging.INFO)



def test_sel():

    login_form = driver.find_element(By.ID, 'login_credentials')

    splitted_lg = login_form.text.split()
    username = splitted_lg[3]

    password_form = driver.find_element(By.CLASS_NAME, "login_password")

    splitted_password = password_form.text.split()
    password = splitted_password[4]

    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    time.sleep(5)
    field = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    field.click()
    time.sleep(3)

    a_z = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]')
    a_z.click()
    time.sleep(5)

    backpack_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    backpack_button.click()

    jacket_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    jacket_button.click()

    tshirt = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    tshirt.click()

    cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()
    time.sleep(3)

    conti_nue = driver.find_element(By.ID, 'continue-shopping')
    conti_nue.click()

    time.sleep(3)

    cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()

    check_button = driver.find_element(By.ID, 'checkout')
    check_button.click()

    name = driver.find_element(By.ID, 'first-name')
    name.send_keys('John')

    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('XXX')

    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.send_keys('12345')

    conti_nue2 = driver.find_element(By.ID, 'continue')
    conti_nue2.click()

    summm = driver.find_element(By.CLASS_NAME, 'summary_info_label')
    info1 = driver.find_element(By.CLASS_NAME, 'summary_value_label')
    info2 = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    time.sleep(5)


    logging.info(summm.text)
    logging.info(info1.text)
    logging.info(info2.text)

    finish_button = driver.find_element(By.ID, 'finish')
    finish_button.click()
    time.sleep(3)

    back_button = driver.find_element(By.ID, 'back-to-products')
    back_button.click()

    driver.quit()

test_sel()
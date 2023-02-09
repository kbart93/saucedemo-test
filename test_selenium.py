from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/jakub/Downloads/chromedriver_win322/chromedriver')
driver = webdriver.Chrome(service = s)
url = "https://www.saucedemo.com/"
driver.get(url)


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
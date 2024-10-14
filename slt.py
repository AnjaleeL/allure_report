import time

import pytest
from selenium import webdriver

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

# Test data for login
test_data = [
    {'user_id': 'qatestslt001@gmail.com', 'password': 'TestQA@1234', 'reason': 'Valid credentials'}
]


# Fixture for the driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(5)
    driver.quit()


# Test function for checking promotion button clickability after login
def test_promotion_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Check clickability of promotion button
    xpath = "//*[@id='root']/div/div/div[1]/button[5]"
    try:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"Button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")


# Test function for checking new services button clickability after login
def test_new_services_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    xpath = "//*[@id='root']/div/div/div[2]/div[1]/button"
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"Button with XPath {xpath} is clickable")

        # Wait for 10 seconds
        time.sleep(10)

        # Check clickability of request button
        xpath = "//*[@id='root']/div/div/div/div[2]/div[2]/div[2]/button"
        try:
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            button.click()
            print(f"Button with XPath {xpath} is clickable")
        except TimeoutException:
            print(f"Button with XPath {xpath} is not clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")


def test_megaline_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click on the button with XPath "//*[@id='root']/div/div/div[2]/div[1]/button"
    xpath = "//*[@id='root']/div/div/div[2]/div[1]/button"
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"Button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")

    # Click on the radio button with CSS selector "#Megaline"
    radio_button_css_selector = "#Megaline"
    try:
        radio_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, radio_button_css_selector)))
        radio_button.click()
        print(f"Radio button with CSS selector {radio_button_css_selector} is clickable")
    except TimeoutException:
        print(f"Radio button with CSS selector {radio_button_css_selector} is not clickable")
    #
    # Send two data sets separately
    data_sets = [
        {"first_name": "kavishni", "last_name": "chanika", "nic": "200150104593", "mobile": "0704906203"},
        # {"first_name": "kashintha", "last_name": "chamani", "nic": "98123456V", "mobile": "0703008423"}
    ]

    for data_set in data_sets:
        # Enter first name
        first_name_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(1) > input[type=text]"
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, first_name_input_css_selector)))
        first_name_input.send_keys(data_set["first_name"])

        # Enter last name
        last_name_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(2) > input[type=text]"
        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, last_name_input_css_selector)))
        last_name_input.send_keys(data_set["last_name"])

        # Enter NIC
        nic_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(3) > input[type=text]"
        nic_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, nic_input_css_selector)))
        nic_input.send_keys(data_set["nic"])

        # Enter mobile
        mobile_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(4) > input[type=number]"
        mobile_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, mobile_input_css_selector)))
        mobile_input.send_keys(data_set["mobile"])

        # Select all 3 items from radio boxes
        radio_box_css_selectors = ["#isVoice", "#isPeo", "#isBB"]
        for radio_box_css_selector in radio_box_css_selectors:
            radio_box = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, radio_box_css_selector)))
            radio_box.click()

            # Click on submit button
            submit_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#root > div > div > div > div.formViews > div.submit > button")))
            time.sleep(10)
            submit_button.click()
            print("Submit button clicked")

            # Click on "No" button in the popup message
            no_button_css_selector = "#root > div > div > div > div.alertView > div > div.actionButton > button.blue.p-1.pl-3.pr-3.mr-2"
            no_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, no_button_css_selector)))
            no_button.click()
            print("No button clicked")

        print("All data sets sent successfully")


# Test function for checking 4G LTE button clickability after login
def test_4glte_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click on the button with XPath "//*[@id='root']/div/div/div[2]/div[1]/button"
    xpath = "//*[@id='root']/div/div/div[2]/div[1]/button"
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"Button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")

    # Click on the radio button with CSS selector "#4G LTE"
    radio_button_xpath = "//*[@id='4g']"
    try:
        radio_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
        radio_button.click()
        print(f"Radio button with XPath {radio_button_xpath} is clickable")
    except TimeoutException:
        print(f"Radio button with XPath {radio_button_xpath} is not clickable")
    # Send two data sets separately
    data_sets = [
        {"first_name": "Gayani", "last_name": "Herath", "nic": "200018729736", "mobile": "0765142309"},
    ]

    for data_set in data_sets:
        # Enter first name
        first_name_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(1) > input[type=text]"
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, first_name_input_css_selector)))
        first_name_input.send_keys(data_set["first_name"])

        # Enter last name
        last_name_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(2) > input[type=text]"
        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, last_name_input_css_selector)))
        last_name_input.send_keys(data_set["last_name"])

        # Enter NIC
        nic_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(3) > input[type=text]"
        nic_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, nic_input_css_selector)))
        nic_input.send_keys(data_set["nic"])

        # Enter mobile
        mobile_input_css_selector = "#root > div > div > div > div.formViews > div.fields.clearfix > div:nth-child(4) > input[type=number]"
        mobile_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, mobile_input_css_selector)))
        mobile_input.send_keys(data_set["mobile"])

        # Select all 3 items from radio boxes
        radio_box_css_selectors = ["#isVoice", "#isPeo", "#isBB"]
        for radio_box_css_selector in radio_box_css_selectors:
            radio_box = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, radio_box_css_selector)))
            radio_box.click()

            # Click on submit button
            submit_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#root > div > div > div > div.formViews > div.submit > button")))
            time.sleep(10)
            submit_button.click()
            print("Submit button clicked")

            # Click on "No" button in the popup message
            no_button_css_selector = "#root > div > div > div > div.alertView > div > div.actionButton > button.blue.p-1.pl-3.pr-3.mr-2"
            no_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, no_button_css_selector)))
            no_button.click()
            print("No button clicked")

        print("All data sets sent successfully")


def test_digital_life_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Check clickability of digital life button
    xpath = "//*[@id='root']/div/div/div[2]/div[2]/button"
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        time.sleep(10)
        print(f"Button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")

    # Check clickability of additional 8 buttons
    buttons_css_selectors = [
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(1)",  # Duthaya
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(2)",  # eSport
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(3)",  # Kaspersky
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(4)",  # SLT Storage
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(5)",  # CCTV
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(6)",  # Smart home
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(7)",  # eSiphala
        "#root > div > div > div.mainBody > div > div.bodyView > div.item-set > div:nth-child(8)"  # SLT Lynked
    ]

    for css_selector in buttons_css_selectors:
        try:
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
            button.click()
            print(f"Button with CSS selector {css_selector} is clickable")
            # Wait for some time
            time.sleep(15)
        except TimeoutException:
            print(f"Button with CSS selector {css_selector} is not clickable")


# Test function for checking hot device button clickability after login
def test_hot_device_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    time.sleep(20)

    # Check clickability of hot device button
    xpath = "//*[@id='root']/div/div/div[2]/div[3]/button"
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"Button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")


# Test function for checking mobile button clickability after login
def test_mobile_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Check clickability of mobile button
    xpath = '//*[@id="root"]/div/div/div[1]/button[4]/div[1]'
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"Button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"Button with XPath {xpath} is not clickable")


# Test function for checking mobile 'Go' button clickability
def test_mobile_go_button_clickability(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait until the mobile 'Go' button is clickable and click it
    xpath_go_button = "//*[@id='root']/div/div/div[6]/div/button"
    try:
        go_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_go_button)))
        go_button.click()
        print(f"'Go' button with XPath {xpath_go_button} is clickable and clicked")

        # Wait for the page to navigate (if the button leads to a website)
        WebDriverWait(driver, 20).until(EC.url_changes(driver.current_url))
        print(f"Navigation successful. New URL: {driver.current_url}")

    except TimeoutException:
        print(f"'Go' button with XPath {xpath_go_button} is not clickable or page did not navigate")


# Test function for checking if the voice button is clickable
def test_voice_button_clickability(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait until the voice button is clickable and click it
    xpath_voice_button = "//*[@id='root']/div/div/div[1]/button[3]"
    try:
        voice_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_voice_button)))
        voice_button.click()
        print(f"'Voice' button with XPath {xpath_voice_button} is clickable and clicked")

        # Optional: Add more checks if needed (e.g., check for changes after clicking the button)

    except TimeoutException:
        print(f"'Voice' button with XPath {xpath_voice_button} is not clickable")


# Test function for checking if the voice button and call forwarding button are clickable and error handling

# Test function for checking if the voice button and call forwarding button are clickable and error handling
def test_voice_and_call_forwarding(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait until the voice button is clickable and click it
    xpath_voice_button = "//*[@id='root']/div/div/div[1]/button[3]"
    try:
        voice_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_voice_button)))
        voice_button.click()
        print(f"'Voice' button with XPath {xpath_voice_button} is clickable and clicked")

    except TimeoutException:
        print(f"'Voice' button with XPath {xpath_voice_button} is not clickable")
        return  # Exit the function since the voice button was not clicked

    # Wait until the Call Forwarding button is clickable and click it
    xpath_call_forwarding_button = "//*[@id='root']/div/div/div[6]/div/div[1]/div[2]"
    try:
        call_forwarding_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath_call_forwarding_button)))
        call_forwarding_button.click()
        print(f"'Call Forwarding' button with XPath {xpath_call_forwarding_button} is clickable and clicked")

    except TimeoutException:
        print(f"'Call Forwarding' button with XPath {xpath_call_forwarding_button} is not clickable")
        return  # Exit the function since the call forwarding button was not clicked

    # Check for the error message after clicking the Call Forwarding button
    xpath_error_message = "//*[@id='root']/div/div/div[6]/div/div[2]/div/div"
    try:
        error_message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_error_message)))
        error_message = error_message_element.text

        # Check if the specific error message is displayed
        if "Sorry, the service is temporarily unavailable. Please try again later." in error_message:
            print("Error message appeared: 'Sorry, the service is temporarily unavailable. Please try again later.'")
            # Fail the test case
            assert False, "Test failed due to service unavailability error"

    except TimeoutException:
        print("No error message appeared, proceeding with the test")

# Test function for checking PeoTV button clickability after login
def test_peotv_button_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Check clickability of PeoTV button
    xpath = "//*[@id='root']/div/div/div[1]/button[2]"
    try:
        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
        print(f"PeoTV button with XPath {xpath} is clickable")
    except TimeoutException:
        print(f"PeoTV button with XPath {xpath} is not clickable")
# Test function for checking Peo TV button and My Package button clickability after login
def test_peotv_mypackage_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the PeoTV button to be clickable and click on it
    peotv_button_xpath = "//*[@id='root']/div/div/div[1]/button[2]"
    try:
        peotv_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, peotv_button_xpath)))
        peotv_button.click()
        print(f"Peo TV button with XPath {peotv_button_xpath} is clickable")
    except TimeoutException:
        print(f"Peo TV button with XPath {peotv_button_xpath} is not clickable")
        return

    # Wait for the "My Package" button to be clickable and click on it
    my_package_button_xpath = "//*[@id='root']/div/div/div[6]/div/div[1]/div[1]"
    try:
        my_package_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, my_package_button_xpath)))
        my_package_button.click()
        print(f"My Package button with XPath {my_package_button_xpath} is clickable")
    except TimeoutException:
        print(f"My Package button with XPath {my_package_button_xpath} is not clickable")
# Test function for checking Peo TV's "VOD" button clickability after login
def test_peotv_vod_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the PeoTV button to be clickable and click on it
    peotv_button_xpath = "//*[@id='root']/div/div/div[1]/button[2]"
    try:
        peotv_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, peotv_button_xpath)))
        peotv_button.click()
        print(f"Peo TV button with XPath {peotv_button_xpath} is clickable")
    except TimeoutException:
        print(f"Peo TV button with XPath {peotv_button_xpath} is not clickable")
        return

    # Wait for the "VOD" button to be clickable and click on it
    vod_button_xpath = "//*[@id='root']/div/div/div[6]/div/div[1]/div[2]"
    try:
        vod_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, vod_button_xpath)))
        vod_button.click()
        print(f"VOD button with XPath {vod_button_xpath} is clickable")
    except TimeoutException:
        print(f"VOD button with XPath {vod_button_xpath} is not clickable")
# Test function for checking Peo TV's "PeoTVGo" button clickability after login
def test_peotv_peotvgo_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the PeoTV button to be clickable and click on it
    peotv_button_xpath = "//*[@id='root']/div/div/div[1]/button[2]"
    try:
        peotv_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, peotv_button_xpath)))
        peotv_button.click()
        print(f"Peo TV button with XPath {peotv_button_xpath} is clickable")
    except TimeoutException:
        print(f"Peo TV button with XPath {peotv_button_xpath} is not clickable")
        return

    # Wait for the "PeoTVGo" button to be clickable and click on it
    peotvgo_button_xpath = "//*[@id='root']/div/div/div[6]/div/div[1]/div[3]"
    try:
        peotvgo_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, peotvgo_button_xpath)))
        peotvgo_button.click()
        print(f"PeoTVGo button with XPath {peotvgo_button_xpath} is clickable")
    except TimeoutException:
        print(f"PeoTVGo button with XPath {peotvgo_button_xpath} is not clickable")
# Test function for checking Peo TV's "Package" button clickability after login
def test_peotv_package_clickability_after_login(driver):
    # Navigate to the login page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the PeoTV button to be clickable and click on it
    peotv_button_xpath = "//*[@id='root']/div/div/div[1]/button[2]"
    try:
        peotv_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, peotv_button_xpath)))
        peotv_button.click()
        print(f"Peo TV button with XPath {peotv_button_xpath} is clickable")
    except TimeoutException:
        print(f"Peo TV button with XPath {peotv_button_xpath} is not clickable")
        return

    # Wait for the "Package" button to be clickable and click on it
    package_button_xpath = "//*[@id='root']/div/div/div[6]/div/div[1]/div[4]"
    try:
        package_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, package_button_xpath)))
        package_button.click()
        print(f"Package button with XPath {package_button_xpath} is clickable")
    except TimeoutException:
        print(f"Package button with XPath {package_button_xpath} is not clickable")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Test function for checking if "See Bill" button is clickable
def test_see_bill_button_clickability(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the "See Bill" button to be clickable
    see_bill_button_xpath = '//*[@id="root"]/div/div/div[2]/div[4]/button'
    try:
        see_bill_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, see_bill_button_xpath)))
        see_bill_button.click()
        print(f"'See Bill' button with XPath {see_bill_button_xpath} is clickable and clicked.")
    except TimeoutException:
        print(f"'See Bill' button with XPath {see_bill_button_xpath} is not clickable.")



import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

# Test data for login
test_data = [
    {'user_id': 'qatestslt001@gmail.com', 'password': 'TestQA@1234', 'reason': 'Valid credentials'}
]


# Fixture for the driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(5)
    driver.quit()

# Test function to click on Broadband button and fetch details
def test_broadband_button_clickability_and_fetch_details(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the Broadband button to be clickable
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print(f"'Broadband' button with XPath {broadband_button_xpath} is clickable and clicked.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Now, fetch broadband details after clicking the button
    try:
        # Wait for the broadband details to load, for example, some element containing the details
        broadband_details = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#broadband-details-container')))  # Replace with actual CSS/XPath of details element
        print("Broadband details fetched:")
        print(broadband_details.text)  # Or scrape specific elements within this container
    except TimeoutException:
        print("Failed to fetch broadband details.")



# Test function to click on Broadband Summary and verify details
def test_broadband_summary_details(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the Broadband button to be clickable and click it
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print(f"'Broadband' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Now, click on the Broadband Summary button
    summary_button_xpath = '//*[@id="root"]/div/div/div[6]/div[1]/div[1]/a/div'
    try:
        summary_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, summary_button_xpath)))
        summary_button.click()
        print(f"'Broadband Summary' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband Summary' button with XPath {summary_button_xpath} is not clickable.")
        return

    # Verify the broadband details on the summary page
    try:
        # Locate the package, status, and username elements (adjust selectors as needed)
        package_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Package')]/following-sibling::div")))
        status_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Status')]/following-sibling::div")))
        username_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Username')]/following-sibling::div")))

        # Verify the details match the expected values
        expected_package = "ANY TRIO SHINE"
        expected_status = "Active"
        expected_username = "94112421536"

        if package_element.text == expected_package and status_element.text == expected_status and username_element.text == expected_username:
            print("Broadband summary details are correct:")
            print(f"Package: {package_element.text}")
            print(f"Status: {status_element.text}")
            print(f"Username: {username_element.text}")
        else:
            print("Broadband summary details do not match expected values.")
            print(f"Package: {package_element.text}, Status: {status_element.text}, Username: {username_element.text}")

    except TimeoutException:
        print("Failed to fetch broadband summary details.")



# Test function to click on My Package in Broadband Summary and verify details
def test_broadband_my_package(driver):

    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # After logging in and clicking the broadband summary (same steps as before)
    # Assuming broadband summary click is already implemented

    # XPath for the My Package button in Broadband Summary
    my_package_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/a[1]/div'
    try:
        my_package_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, my_package_xpath)))
        my_package_button.click()
        print(f"'My Package' button clicked successfully.")
    except TimeoutException:
        print(f"'My Package' button with XPath {my_package_xpath} is not clickable.")
        return

    # Verify if the correct package details are displayed
    try:
        # Locate the text elements (adjust selectors as needed)
        speed_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Your speed is')]/following-sibling::div")))
        usage_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Any Time Usage')]")))

        # Expected values
        expected_speed = "Your speed is NORMAL right now"
        expected_usage = "Any Time Usage"

        # Check if the text matches expected values
        if expected_speed in speed_element.text and expected_usage in usage_element.text:
            print("My Package details are correct:")
            print(f"Speed: {speed_element.text}")
            print(f"Usage: {usage_element.text}")
        else:
            print("My Package details do not match expected values.")
            print(f"Speed: {speed_element.text}, Usage: {usage_element.text}")

    except TimeoutException:
        print("Failed to fetch My Package details.")


# Test function to click on Extra GB in Broadband Summary and verify details
def test_broadband_extra_gb(driver):
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # XPath for the Extra GB button in Broadband Summary
    extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/a[2]/div'
    try:
        extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, extra_gb_xpath)))
        extra_gb_button.click()
        print(f"'Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Extra GB' button with XPath {extra_gb_xpath} is not clickable.")
        return

    # Verify if the correct Extra GB details are displayed
    try:
        # Locate the text element containing Remaining Volume
        remaining_volume_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Remaining Volume as of')]")))

        # Expected value
        expected_remaining_volume = "Remaining Volume as of : 2024-10-10 07:23:00"

        # Check if the text matches the expected value
        if expected_remaining_volume in remaining_volume_element.text:
            print(f"Extra GB details are correct: {remaining_volume_element.text}")
        else:
            print(f"Extra GB details do not match expected values. Found: {remaining_volume_element.text}")

    except TimeoutException:
        print("Failed to fetch Extra GB details.")



# Test function to click on Bonus Data in Broadband Summary and verify details
def test_broadband_bonus_data(driver):
    # Navigate to the PeoTV or SLT login page
    driver.get("https://myslt.slt.lk/")  # Replace with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # After logging in and clicking the broadband summary (same steps as before)
    # Assuming broadband summary click is already implemented

    # Wait for the Broadband button to be clickable and click it
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print("'Broadband' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Click on the Broadband Summary button
    summary_button_xpath = '//*[@id="root"]/div/div/div[6]/div[1]/div[1]/a/div'
    try:
        summary_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, summary_button_xpath)))
        summary_button.click()
        print("'Broadband Summary' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband Summary' button with XPath {summary_button_xpath} is not clickable.")
        return

    # Now, click on the Bonus Data button in Broadband Summary
    bonus_data_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/a[3]/div'
    try:
        bonus_data_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, bonus_data_xpath)))
        bonus_data_button.click()
        print("'Bonus Data' button clicked successfully.")
    except TimeoutException:
        print(f"'Bonus Data' button with XPath {bonus_data_xpath} is not clickable.")
        return

    # Verify if the correct bonus data details are displayed
    try:
        remaining_volume_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Remaining Volume as of')]/following-sibling::div"))
        )
        loyalty_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Loyalty')]"))
        )

        # Expected values
        expected_remaining_volume = "Remaining Volume as of : 2024-10-10 08:09:00"
        expected_loyalty = "Loyalty"

        # Check if the text matches expected values
        if expected_remaining_volume in remaining_volume_element.text and expected_loyalty in loyalty_element.text:
            print("Bonus Data details are correct:")
            print(f"Remaining Volume: {remaining_volume_element.text}")
            print(f"Loyalty: {loyalty_element.text}")
        else:
            print("Bonus Data details do not match expected values.")
            print(f"Remaining Volume: {remaining_volume_element.text}, Loyalty: {loyalty_element.text}")

    except TimeoutException:
        print("Failed to fetch Bonus Data details.")
def test_broadband_add_ons_data(driver):
    # Navigate to the PeoTV or SLT login page
    driver.get("https://myslt.slt.lk/")  # Replace with the correct URL if needed
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # After logging in and clicking the broadband summary (same steps as before)
    # Assuming broadband summary click is already implemented


    # Wait for the Broadband button to be clickable and click it
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print("'Broadband' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Click on the Broadband Summary button
    summary_button_xpath = '//*[@id="root"]/div/div/div[6]/div[1]/div[1]/a/div'
    try:
        summary_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, summary_button_xpath)))
        summary_button.click()
        print("'Broadband Summary' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband Summary' button with XPath {summary_button_xpath} is not clickable.")
        return

    # Now, click on the Add-Ons Data button in Broadband Summary
    add_ons_data_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/a[4]/div'
    try:
        add_ons_data_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, add_ons_data_xpath)))
        add_ons_data_button.click()
        print("'Add-Ons Data' button clicked successfully.")
    except TimeoutException:
        print(f"'Add-Ons Data' button with XPath {add_ons_data_xpath} is not clickable.")
        return

    # Verify if the correct add-ons data details are displayed
    try:
        usage_volume_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Usage Volume as of')]"))
        )

        # Expected value
        expected_usage_volume = "Usage Volume as of"

        # Check if the text matches expected values
        if expected_usage_volume in usage_volume_element.text:
            print("Add-Ons Data details are correct:")
            print(f"Usage Volume: {usage_volume_element.text}")
        else:
            print("Add-Ons Data details do not match expected values.")
            print(f"Usage Volume: {usage_volume_element.text}")

    except TimeoutException:
        print("Failed to fetch Add-Ons Data details.")




# Test function to click on Free Data in Broadband Summary and verify details
def test_broadband_free_data(driver):
    # Navigate to the PeoTV or SLT login page
    driver.get("https://myslt.slt.lk/")  # Replace with the correct URL if needed
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the Broadband button to be clickable and click it
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print("'Broadband' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Click on the Broadband Summary button
    summary_button_xpath = '//*[@id="root"]/div/div/div[6]/div[1]/div[1]/a/div'
    try:
        summary_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, summary_button_xpath)))
        summary_button.click()
        print("'Broadband Summary' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband Summary' button with XPath {summary_button_xpath} is not clickable.")
        return

    # Now, click on the Free Data button in Broadband Summary
    free_data_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/a[5]/div/div/p[1]'
    try:
        free_data_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, free_data_xpath)))
        free_data_button.click()
        print("'Free Data' button clicked successfully.")
    except TimeoutException:
        print(f"'Free Data' button with XPath {free_data_xpath} is not clickable.")
        return

    # Verify if the correct free data details are displayed
    try:
        free_data_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'free data')]"))
        )

        # Expected value
        expected_free_data = "free data"

        # Check if the text matches expected values
        if expected_free_data in free_data_element.text.lower():
            print("Free Data details are correct:")
            print(f"Free Data: {free_data_element.text}")
        else:
            print("Free Data details do not match expected values.")
            print(f"Free Data: {free_data_element.text}")

    except TimeoutException:
        print("Failed to fetch Free Data details.")



# Test function to click on Package Upgrade in Broadband Summary
def test_broadband_package_upgrade(driver):
    # Navigate to the PeoTV or SLT login page
    driver.get("https://myslt.slt.lk/")  # Replace with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the Broadband button to be clickable and click it
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print("'Broadband' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Click on the Broadband Summary button
    summary_button_xpath = '//*[@id="root"]/div/div/div[6]/div[1]/div[1]/a/div'
    try:
        summary_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, summary_button_xpath)))
        summary_button.click()
        print("'Broadband Summary' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband Summary' button with XPath {summary_button_xpath} is not clickable.")
        return

    # Now, click on the Package Upgrade button in Broadband Summary
    package_upgrade_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[1]/div/div[2]/button'
    try:
        package_upgrade_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, package_upgrade_xpath)))
        package_upgrade_button.click()
        print("'Package Upgrade' button clicked successfully.")
    except TimeoutException:
        print(f"'Package Upgrade' button with XPath {package_upgrade_xpath} is not clickable.")
        return

    # Optionally, verify if the correct page or message is displayed after clicking "Package Upgrade"
    try:
        confirmation_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Upgrade Confirmation')]"))  # Adjust as needed
        )
        print(f"Package Upgrade page displayed: {confirmation_element.text}")

    except TimeoutException:
        print("Package Upgrade confirmation page not found.")


# Test function to click on Get Extra GB in Broadband Summary
def test_broadband_get_extra_gb(driver):
    # Navigate to the PeoTV or SLT login page
    driver.get("https://sltweb.lakmobile.com/")  # Replace with the correct URL if needed
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()



    # Wait for the Broadband button to be clickable and click it
    broadband_button_xpath = '//*[@id="root"]/div/div/div[1]/button[1]'
    try:
        broadband_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, broadband_button_xpath)))
        broadband_button.click()
        print("'Broadband' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband' button with XPath {broadband_button_xpath} is not clickable.")
        return

    # Click on the Broadband Summary button
    summary_button_xpath = '//*[@id="root"]/div/div/div[6]/div[1]/div[1]/a/div'
    try:
        summary_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, summary_button_xpath)))
        summary_button.click()
        print("'Broadband Summary' button clicked successfully.")
    except TimeoutException:
        print(f"'Broadband Summary' button with XPath {summary_button_xpath} is not clickable.")
        return

    # Now, click on the Get Extra GB button in Broadband Summary
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Optionally, verify if the correct page or message is displayed after clicking "Get Extra GB"
    try:
        confirmation_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Extra GB details')]"))  # Adjust as needed
        )
        print(f"Extra GB page displayed: {confirmation_element.text}")

    except TimeoutException:
        print("Extra GB confirmation page not found.")




# Test function to click each GB amount and verify if the same amount is displayed
def test_click_each_gb_amount(driver):
    # Navigate to the PeoTV or SLT login page
    driver.get("https://myslt.slt.lk/")  # Replace with the correct URL if needed
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Now, click on the "Get Extra GB" section (adjust XPath if needed)
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Function to click a specific GB button and verify the display
    def click_and_verify_gb(gb_xpath, expected_gb):
        try:
            # Click the specific GB button
            gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_xpath)))
            gb_button.click()
            print(f"{expected_gb} GB button clicked successfully.")
        except TimeoutException:
            print(f"{expected_gb} GB button with XPath {gb_xpath} is not clickable.")
            return

        # Verify if the same GB amount is displayed in the specified location
        try:
            displayed_gb_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[1]/div[1]'))
            )
            if expected_gb in displayed_gb_element.text:
                print(f"Displayed GB amount is correct: {displayed_gb_element.text}")
            else:
                print(f"Displayed GB amount is incorrect. Expected: {expected_gb}, but got: {displayed_gb_element.text}")
        except TimeoutException:
            print(f"Failed to verify displayed GB amount for {expected_gb} GB.")

    # Test for each GB button and verify display
    click_and_verify_gb('//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]', "1GB")  # Click 1GB
    click_and_verify_gb('//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[2]', "2GB")  # Click 2GB
    click_and_verify_gb('//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[3]', "3GB")  # Click 3GB
    click_and_verify_gb('//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[4]', "4GB")  # Click 4GB
    click_and_verify_gb('//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[5]', "5GB")  # Click 5GB





# Test function to click the "Get Extra GB" button and navigate through the "More" button
def test_get_extra_gb(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Click the 'More' button to navigate to the next page
    more_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/div'
    try:
        more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, more_button_xpath)))
        more_button.click()
        print("'More' button clicked successfully.")
    except TimeoutException:
        print(f"'More' button with XPath {more_button_xpath} is not clickable.")
        return

    # Verify if 10GB is displayed on the next page
    try:
        gb_amount_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[1]/div[1]'
        gb_amount_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, gb_amount_xpath)))

        # Verify if it displays 10GB as expected
        expected_gb = "10GB"
        if expected_gb in gb_amount_element.text:
            print(f"'More' page displays correct GB amount: {gb_amount_element.text}")
        else:
            print(f"'More' page displays incorrect GB amount: {gb_amount_element.text}")

    except TimeoutException:
        print("Failed to fetch the GB amount on the 'More' page.")

def test_gb_selection_next_and_back(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Verify the payment page has 'Add to Bill'
    try:
        add_to_bill_xpath = "//*[contains(text(), 'Add to Bill')]"
        add_to_bill_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_to_bill_xpath)))
        if 'Add to Bill' in add_to_bill_element.text:
            print("'Add to Bill' is displayed on the payment page.")
        else:
            print(f"'Add to Bill' is not displayed correctly. Displayed value: {add_to_bill_element.text}")
    except TimeoutException:
        print("Failed to verify 'Add to Bill' on the payment page.")
        return

    # Click 'Back' button to go back to GB selection page
    back_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[1]'
    try:
        back_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
        back_button.click()
        print("'Back' button clicked successfully.")
    except TimeoutException:
        print(f"'Back' button with XPath {back_button_xpath} is not clickable.")
        return

    # Verify you are back on the GB selection page and that "1GB to 4GB" is displayed
    try:
        gb_plan_xpath = "//*[contains(text(), '1GB to 4GB')]"
        gb_plan_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, gb_plan_xpath)))
        if '1GB to 4GB' in gb_plan_element.text:
            print("'1GB to 4GB' plan is displayed correctly.")
        else:
            print(f"'1GB to 4GB' is not displayed correctly. Displayed value: {gb_plan_element.text}")
    except TimeoutException:
        print("Failed to verify '1GB to 4GB' on the GB selection page.")

 #Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Add to Bill' option on the payment page
    add_to_bill_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
    try:
        add_to_bill_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, add_to_bill_xpath)))
        add_to_bill_button.click()
        print("'Add to Bill' option selected successfully.")
    except TimeoutException:
        print(f"Failed to select 'Add to Bill' option with XPath {add_to_bill_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Verify the confirmation page displays "I agree to the general terms and conditions"
    try:
        agree_terms_xpath = "//*[contains(text(), 'I agree to the general terms and conditions')]"
        agree_terms_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, agree_terms_xpath)))
        if 'I agree to the general terms and conditions' in agree_terms_element.text:
            print("'I agree to the general terms and conditions' is displayed on the confirmation page.")
        else:
            print(f"Text mismatch: '{agree_terms_element.text}' instead of 'I agree to the general terms and conditions'")

    except TimeoutException:
        print("Failed to verify 'I agree to the general terms and conditions' on the confirmation page.")




# Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Add to Bill' option on the payment page
    add_to_bill_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
    try:
        add_to_bill_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, add_to_bill_xpath)))
        add_to_bill_button.click()
        print("'Add to Bill' option selected successfully.")
    except TimeoutException:
        print(f"Failed to select 'Add to Bill' option with XPath {add_to_bill_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Agree to the terms and conditions
    agree_terms_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[3]/input'
    try:
        agree_terms_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_terms_xpath)))
        agree_terms_checkbox.click()
        print("'I agree to the general terms and conditions' checkbox clicked successfully.")
    except TimeoutException:
        print(f"Failed to click 'I agree to the general terms and conditions' checkbox with XPath {agree_terms_xpath}.")
        return

    # Click 'Submit' button to complete the payment process
    submit_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[2]'
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()
        print("'Submit' button clicked successfully.")
    except TimeoutException:
        print(f"'Submit' button with XPath {submit_button_xpath} is not clickable.")
        return

    # Verify success message is displayed
    try:
        success_message_xpath = "//*[contains(text(), 'Your payment was successful')]"
        success_message_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, success_message_xpath)))
        if 'Your payment was successful' in success_message_element.text:
            print("Payment was successful.")
        else:
            print(f"Text mismatch: '{success_message_element.text}' instead of 'Your payment was successful'")
    except TimeoutException:
        print("Failed to verify payment success message.")



# Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Add to Bill' option on the payment page
    add_to_bill_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
    try:
        add_to_bill_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, add_to_bill_xpath)))
        add_to_bill_button.click()
        print("'Add to Bill' option selected successfully.")
    except TimeoutException:
        print(f"Failed to select 'Add to Bill' option with XPath {add_to_bill_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Agree to the terms and conditions
    agree_terms_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[3]/input'
    try:
        agree_terms_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_terms_xpath)))
        agree_terms_checkbox.click()
        print("'I agree to the general terms and conditions' checkbox clicked successfully.")
    except TimeoutException:
        print(f"Failed to click 'I agree to the general terms and conditions' checkbox with XPath {agree_terms_xpath}.")
        return

    # Click 'Submit' button to complete the payment process
    submit_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[2]'
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()
        print("'Submit' button clicked successfully.")
    except TimeoutException:
        print(f"'Submit' button with XPath {submit_button_xpath} is not clickable.")
        return

    # Verify success message is displayed
    try:
        success_message_xpath = "//*[contains(text(), 'Your payment was successful')]"
        success_message_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, success_message_xpath)))
        if 'Your payment was successful' in success_message_element.text:
            print("Payment was successful.")
        else:
            print(f"Text mismatch: '{success_message_element.text}' instead of 'Your payment was successful'")
    except TimeoutException:
        print("Failed to verify payment success message.")

    # Click the 'Back' button to return to the payment selection page
    back_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[1]'
    try:
        back_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
        back_button.click()
        print("'Back' button clicked successfully.")
    except TimeoutException:
        print(f"'Back' button with XPath {back_button_xpath} is not clickable.")
        return

    # Verify that we are back on the payment selection page and check for 'Add to Bill' button
    try:
        add_to_bill_display_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
        add_to_bill_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_to_bill_display_xpath)))
        if add_to_bill_display.is_displayed():
            print("'Add to Bill' button is displayed successfully.")
        else:
            print("'Add to Bill' button is NOT displayed.")
    except TimeoutException:
        print(f"Failed to verify display of 'Add to Bill' button with XPath {add_to_bill_display_xpath}.")


# Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Add to Bill' option on the payment page
    add_to_bill_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
    try:
        add_to_bill_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, add_to_bill_xpath)))
        add_to_bill_button.click()
        print("'Add to Bill' option selected successfully.")
    except TimeoutException:
        print(f"Failed to select 'Add to Bill' option with XPath {add_to_bill_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Agree to the terms and conditions
    agree_terms_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[3]/input'
    try:
        agree_terms_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_terms_xpath)))
        agree_terms_checkbox.click()
        print("'I agree to the general terms and conditions' checkbox clicked successfully.")
    except TimeoutException:
        print(f"Failed to click 'I agree to the general terms and conditions' checkbox with XPath {agree_terms_xpath}.")
        return

    # Click 'Submit' button to complete the payment process
    submit_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[2]'
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()
        print("'Submit' button clicked successfully.")
    except TimeoutException:
        print(f"'Submit' button with XPath {submit_button_xpath} is not clickable.")
        return

    # Verify success message is displayed
    try:
        success_message_xpath = "//*[contains(text(), 'Your payment was successful')]"
        success_message_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, success_message_xpath)))
        if 'Your payment was successful' in success_message_element.text:
            print("Payment was successful.")
        else:
            print(f"Text mismatch: '{success_message_element.text}' instead of 'Your payment was successful'")
    except TimeoutException:
        print("Failed to verify payment success message.")

    # Click the 'Back' button to return to the payment selection page
    back_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[1]'
    try:
        back_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
        back_button.click()
        print("'Back' button clicked successfully.")
    except TimeoutException:
        print(f"'Back' button with XPath {back_button_xpath} is not clickable.")
        return

    # Verify that we are back on the payment selection page and check for 'Add to Bill' button
    try:
        add_to_bill_display_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
        add_to_bill_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_to_bill_display_xpath)))
        if add_to_bill_display.is_displayed():
            print("'Add to Bill' button is displayed successfully.")
        else:
            print("'Add to Bill' button is NOT displayed.")
    except TimeoutException:
        print(f"Failed to verify display of 'Add to Bill' button with XPath {add_to_bill_display_xpath}.")

# Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Now Pay' option on the payment method page
    now_pay_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[2]/svg'
    try:
        now_pay_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, now_pay_xpath)))
        now_pay_button.click()
        print("'Now Pay' button clicked successfully.")
    except TimeoutException:
        print(f"Failed to select 'Now Pay' option with XPath {now_pay_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Agree to the terms and conditions
    agree_terms_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[3]/input'
    try:
        agree_terms_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_terms_xpath)))
        agree_terms_checkbox.click()
        print("'I agree to the general terms and conditions' checkbox clicked successfully.")
    except TimeoutException:
        print(f"Failed to click 'I agree to the general terms and conditions' checkbox with XPath {agree_terms_xpath}.")
        return

    # Click 'Submit' button to complete the payment process
    submit_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[2]'
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()
        print("'Submit' button clicked successfully.")
    except TimeoutException:
        print(f"'Submit' button with XPath {submit_button_xpath} is not clickable.")
        return

    # Verify success message is displayed
    try:
        success_message_xpath = "//*[contains(text(), 'Your payment was successful')]"
        success_message_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, success_message_xpath)))
        if 'Your payment was successful' in success_message_element.text:
            print("Payment was successful.")
        else:
            print(f"Text mismatch: '{success_message_element.text}' instead of 'Your payment was successful'")
    except TimeoutException:
        print("Failed to verify payment success message.")

    # Click the 'Back' button to return to the payment selection page
    back_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[1]'
    try:
        back_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
        back_button.click()
        print("'Back' button clicked successfully.")
    except TimeoutException:
        print(f"'Back' button with XPath {back_button_xpath} is not clickable.")
        return

    # Verify that we are back on the payment selection page and check for 'Add to Bill' button
    try:
        add_to_bill_display_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
        add_to_bill_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_to_bill_display_xpath)))
        if add_to_bill_display.is_displayed():
            print("'Add to Bill' button is displayed successfully.")
        else:
            print("'Add to Bill' button is NOT displayed.")
    except TimeoutException:
        print(f"Failed to verify display of 'Add to Bill' button with XPath {add_to_bill_display_xpath}.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Now Pay' option on the payment method page
    now_pay_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[2]/svg'
    try:
        now_pay_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, now_pay_xpath)))
        now_pay_button.click()
        print("'Now Pay' button clicked successfully.")
    except TimeoutException:
        print(f"Failed to select 'Now Pay' option with XPath {now_pay_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Agree to the terms and conditions
    agree_terms_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[3]/input'
    try:
        agree_terms_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_terms_xpath)))
        agree_terms_checkbox.click()
        print("'I agree to the general terms and conditions' checkbox clicked successfully.")
    except TimeoutException:
        print(f"Failed to click 'I agree to the general terms and conditions' checkbox with XPath {agree_terms_xpath}.")
        return

    # Click 'Submit' button to complete the payment process
    submit_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/form/button'
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()
        print("'Submit' button clicked successfully.")
    except TimeoutException:
        print(f"'Submit' button with XPath {submit_button_xpath} is not clickable.")
        return

    # Verify success message is displayed
    try:
        success_message_xpath = "//*[contains(text(), 'Your payment was successful')]"
        success_message_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, success_message_xpath)))
        if 'Your payment was successful' in success_message_element.text:
            print("Payment was successful.")
        else:
            print(f"Text mismatch: '{success_message_element.text}' instead of 'Your payment was successful'")
    except TimeoutException:
        print("Failed to verify payment success message.")

    # Click the 'Back' button to return to the payment selection page
    back_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[1]'
    try:
        back_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
        back_button.click()
        print("'Back' button clicked successfully.")
    except TimeoutException:
        print(f"'Back' button with XPath {back_button_xpath} is not clickable.")
        return

    # Verify that we are back on the payment selection page and check for 'Add to Bill' button
    try:
        add_to_bill_display_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
        add_to_bill_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_to_bill_display_xpath)))
        if add_to_bill_display.is_displayed():
            print("'Add to Bill' button is displayed successfully.")
        else:
            print("'Add to Bill' button is NOT displayed.")
    except TimeoutException:
        print(f"Failed to verify display of 'Add to Bill' button with XPath {add_to_bill_display_xpath}.")



# Test function to navigate through the GB selection, payment, and confirmation process
def test_payment_method_and_confirmation(driver):
    # Navigate to the PeoTV page (or the appropriate page)
    driver.get("https://myslt.slt.lk/")  # Replace this with the correct URL if needed

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Click the 'Get Extra GB' button
    get_extra_gb_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[1]/button'
    try:
        get_extra_gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_extra_gb_xpath)))
        get_extra_gb_button.click()
        print("'Get Extra GB' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Extra GB' button with XPath {get_extra_gb_xpath} is not clickable.")
        return

    # Select a GB option, for example 1GB
    try:
        gb_1gb_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/div[1]/button[1]'
        gb_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, gb_1gb_xpath)))
        gb_button.click()
        print("'1GB' button clicked successfully.")
    except TimeoutException:
        print("Failed to click '1GB' button.")
        return

    # Click 'Next' button to go to the payment page
    next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div/div[3]/div[2]/button'
    try:
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        print("'Next' button clicked successfully.")
    except TimeoutException:
        print(f"'Next' button with XPath {next_button_xpath} is not clickable.")
        return

    # Click the 'Now Pay' option on the payment method page
    now_pay_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[2]/svg'
    try:
        now_pay_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, now_pay_xpath)))
        now_pay_button.click()
        print("'Now Pay' button clicked successfully.")
    except TimeoutException:
        print(f"Failed to select 'Now Pay' option with XPath {now_pay_xpath}.")
        return

    # Click 'Next' button to go to the confirmation page
    payment_next_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/button[2]'
    try:
        payment_next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, payment_next_button_xpath)))
        payment_next_button.click()
        print("'Next' button clicked successfully on the payment page.")
    except TimeoutException:
        print(f"'Next' button with XPath {payment_next_button_xpath} is not clickable.")
        return

    # Agree to the terms and conditions
    agree_terms_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[3]/input'
    try:
        agree_terms_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_terms_xpath)))
        agree_terms_checkbox.click()
        print("'I agree to the general terms and conditions' checkbox clicked successfully.")
    except TimeoutException:
        print(f"Failed to click 'I agree to the general terms and conditions' checkbox with XPath {agree_terms_xpath}.")
        return

    # Click 'Submit' button to complete the payment process
    submit_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/form/button'
    try:
        submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submit_button.click()
        print("'Submit' button clicked successfully.")
    except TimeoutException:
        print(f"'Submit' button with XPath {submit_button_xpath} is not clickable.")
        return

    # Verify success message is displayed
    try:
        success_message_xpath = "//*[contains(text(), 'Your payment was successful')]"
        success_message_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, success_message_xpath)))
        if 'Your payment was successful' in success_message_element.text:
            print("Payment was successful.")
        else:
            print(f"Text mismatch: '{success_message_element.text}' instead of 'Your payment was successful'")
    except TimeoutException:
        print("Failed to verify payment success message.")

    # Click the 'Back' button to return to the payment selection page
    back_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[4]/button[1]'
    try:
        back_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, back_button_xpath)))
        back_button.click()
        print("'Back' button clicked successfully.")
    except TimeoutException:
        print(f"'Back' button with XPath {back_button_xpath} is not clickable.")
        return

    # Verify that we are back on the payment selection page and check for 'Add to Bill' button
    try:
        add_to_bill_display_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]/svg'
        add_to_bill_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_to_bill_display_xpath)))
        if add_to_bill_display.is_displayed():
            print("'Add to Bill' button is displayed successfully.")
        else:
            print("'Add to Bill' button is NOT displayed.")
    except TimeoutException:
        print(f"Failed to verify display of 'Add to Bill' button with XPath {add_to_bill_display_xpath}.")





def test_get_data_add_ons(driver):
    # Navigate to the broadband summary page
    driver.get("https://myslt.slt.lk/")
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the "Get Data Add-ons" button to be clickable
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'

    try:
        get_data_add_ons_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, get_data_add_ons_xpath))
        )
        get_data_add_ons_button.click()
        print("'Get Data Add-ons' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Data Add-ons' button with XPath {get_data_add_ons_xpath} is not clickable.")

# Example usage
# test_get_data_add_ons(driver)
def test_home_schooling_whf(driver):
    # Assuming you are already on the Get Data Add-ons page

    # XPath for Home Schooling and WHF options
    home_schooling_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[1]/div[1]/div'
    whf_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[1]/div[2]/div'  # Adjust if needed

    # Click Home Schooling
    try:
        home_schooling_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, home_schooling_xpath))
        )
        home_schooling_button.click()
        print("'Home Schooling' option clicked successfully.")
    except TimeoutException:
        print(f"'Home Schooling' option with XPath {home_schooling_xpath} is not clickable.")

    # Click WHF
    try:
        whf_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, whf_xpath))
        )
        whf_button.click()
        print("'WHF' option clicked successfully.")
    except TimeoutException:
        print(f"'WHF' option with XPath {whf_xpath} is not clickable.")

    # Verify if "Meet Lite" is displayed
    try:
        meet_lite_xpath = "//*[contains(text(), 'Meet Lite')]"  # Adjust selector as needed
        meet_lite_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, meet_lite_xpath))
        )
        if meet_lite_element.is_displayed():
            print("'Meet Lite' is displayed successfully.")
        else:
            print("'Meet Lite' is not displayed.")
    except TimeoutException:
        print("Failed to find 'Meet Lite'.")



def test_meet_lite_purchase(driver):
    # Navigate to the broadband summary page
    driver.get("https://myslt.slt.lk/")
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # Wait for the "Get Data Add-ons" button to be clickable
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'

    # XPath for the Meet Lite button
    meet_lite_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div/div[2]'

    # Click the Meet Lite button
    try:
        meet_lite_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, meet_lite_xpath))
        )
        meet_lite_button.click()
        print("'Meet Lite' button clicked successfully.")
    except TimeoutException:
        print(f"'Meet Lite' button with XPath {meet_lite_xpath} is not clickable.")
        return

    # Verify the purchase confirmation message
    try:
        confirmation_message_xpath = "//*[contains(text(), 'Do you want to purchase and activate Meet Lite?')]"
        confirmation_message_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, confirmation_message_xpath))
        )
        if confirmation_message_element.is_displayed():
            print("Confirmation message displayed: 'Do you want to purchase and activate Meet Lite?'")
        else:
            print("Confirmation message is not displayed.")
    except TimeoutException:
        print("Failed to find the confirmation message.")




def test_meet_lite_purchase(driver):
    # Assuming you are already on the Home Schooling and WHF page

    # XPath for the Meet Lite button
    meet_lite_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[1]/div/div[2]'

    # Click the Meet Lite button
    try:
        meet_lite_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, meet_lite_xpath))
        )
        meet_lite_button.click()
        print("'Meet Lite' button clicked successfully.")
    except TimeoutException:
        print(f"'Meet Lite' button with XPath {meet_lite_xpath} is not clickable.")
        return

    # Verify the purchase confirmation message
    try:
        confirmation_message_xpath = "//*[contains(text(), 'Do you want to purchase and activate Meet Lite?')]"
        confirmation_message_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, confirmation_message_xpath))
        )
        if confirmation_message_element.is_displayed():
            print("Confirmation message displayed: 'Do you want to purchase and activate Meet Lite?'")
        else:
            print("Confirmation message is not displayed.")
    except TimeoutException:
        print("Failed to find the confirmation message.")





def test_meet_lite_recurrent_purchase(driver):
    # Assuming you are already on the Home Schooling and WHF page and have clicked on "Meet Lite"

    # XPath for the Recurrent option
    recurrent_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/div/div[3]/input'

    # Click the Recurrent option
    try:
        recurrent_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, recurrent_xpath))
        )
        recurrent_option.click()
        print("'Recurrent' option clicked successfully.")
    except TimeoutException:
        print(f"'Recurrent' option with XPath {recurrent_xpath} is not clickable.")
        return

    # XPath for the Yes button
    yes_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/div/div[4]/button[2]'

    # Click the Yes button to confirm purchase
    try:
        yes_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, yes_button_xpath))
        )
        yes_button.click()
        print("'Yes' button clicked successfully.")
    except TimeoutException:
        print(f"'Yes' button with XPath {yes_button_xpath} is not clickable.")
        return

    # Verify the success message
    try:
        success_message_xpath = "//*[contains(text(), 'You have purchased the data Add-on successfully.')]"
        success_message_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, success_message_xpath))
        )
        if success_message_element.is_displayed():
            print("Success message displayed: 'You have purchased the data Add-on successfully.'")
        else:
            print("Success message is not displayed.")
    except TimeoutException:
        print("Failed to find the success message.")





def test_meet_max_purchase(driver):
    # Navigate to the broadband summary page
    driver.get("https://myslt.slt.lk/")
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # Wait for the "Get Data Add-ons" button to be clickable
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'
    # Click the "Get Data Add-Ons" button
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'
    try:
        get_data_add_ons_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, get_data_add_ons_xpath))
        )
        get_data_add_ons_button.click()
        print("'Get Data Add-Ons' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Data Add-Ons' button with XPath {get_data_add_ons_xpath} is not clickable.")
        return

    # Click the "Home Schooling & WHF" button
    home_schooling_whf_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[1]/div[1]/div/div/p'
    try:
        home_schooling_whf_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, home_schooling_whf_xpath))
        )
        home_schooling_whf_button.click()
        print("'Home Schooling & WHF' button clicked successfully.")
    except TimeoutException:
        print(f"'Home Schooling & WHF' button with XPath {home_schooling_whf_xpath} is not clickable.")
        return

    # Click the "Meet Max" button
    meet_max_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/div/div[2]'
    try:
        meet_max_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, meet_max_xpath))
        )
        meet_max_button.click()
        print("'Meet Max' button clicked successfully.")
    except TimeoutException:
        print(f"'Meet Max' button with XPath {meet_max_xpath} is not clickable.")
        return

    # Verify the confirmation message is displayed
    try:
        confirm_message_xpath = "//*[contains(text(), 'Do you want to purchase and activate Meet Max ?')]"
        confirm_message_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, confirm_message_xpath))
        )
        if confirm_message_element.is_displayed():
            print("Confirmation message displayed: 'Do you want to purchase and activate Meet Max ?'")
        else:
            print("Confirmation message is not displayed.")
    except TimeoutException:
        print("Failed to find the confirmation message.")
        return
import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Test data for login
test_data = [
    {'user_id': 'qatestslt001@gmail.com', 'password': 'TestQA@1234', 'reason': 'Valid credentials'}
]


# Fixture for the driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(5)
    driver.quit()


def test_meet_max_purchase1(driver):
    # Navigate to the broadband summary page
    driver.get("https://myslt.slt.lk/")
    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()
    # Wait for the "Get Data Add-ons" button to be clickable
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'
    # Click the "Get Data Add-Ons" button
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'
    try:
        get_data_add_ons_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, get_data_add_ons_xpath))
        )
        get_data_add_ons_button.click()
        print("'Get Data Add-Ons' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Data Add-Ons' button with XPath {get_data_add_ons_xpath} is not clickable.")
        return

    # Click the "Home Schooling & WHF" button
    home_schooling_whf_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[1]/div[1]/div/div/p'
    try:
        home_schooling_whf_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, home_schooling_whf_xpath))
        )
        home_schooling_whf_button.click()
        print("'Home Schooling & WHF' button clicked successfully.")
    except TimeoutException:
        print(f"'Home Schooling & WHF' button with XPath {home_schooling_whf_xpath} is not clickable.")
        return

    meet_max_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/div/div[2]'
    try:
        meet_max_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, meet_max_xpath))
        )
        meet_max_button.click()
        print("'Meet Max' button clicked successfully.")
    except TimeoutException:
        print(f"'Meet Max' button with XPath {meet_max_xpath} is not clickable.")
        return



    # Click the "Yes" button to confirm the purchase
    yes_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/div/div[4]/button[2]'
    try:
        yes_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, yes_button_xpath))
        )
        yes_button.click()
        print("'Yes' button clicked successfully.")
    except TimeoutException:
        print(f"'Yes' button with XPath {yes_button_xpath} is not clickable.")
        return


def test_meet_max_purchase1(driver):
    # Navigate to the broadband summary page
    driver.get("https://myslt.slt.lk/")

    # Enter user_id
    user_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(1) > input[type="text"]')))
    user_id_input.send_keys(test_data[0]["user_id"])

    # Enter password
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-group > div:nth-child(2) > input[type="password"]')))
    password_input.send_keys(test_data[0]["password"])

    # Click Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     '#root > div > div.formView > div.form.d-block.m-auto.login-form > div.input-container-footer > button')))
    sign_in_button.click()

    # Wait for the "Get Data Add-ons" button to be clickable
    get_data_add_ons_xpath = '//*[@id="root"]/div/div/div[6]/div[2]/div/div[2]/div/div[2]/button'
    try:
        get_data_add_ons_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, get_data_add_ons_xpath))
        )
        get_data_add_ons_button.click()
        print("'Get Data Add-Ons' button clicked successfully.")
    except TimeoutException:
        print(f"'Get Data Add-Ons' button with XPath {get_data_add_ons_xpath} is not clickable.")
        return

    # Click the "Home Schooling & WHF" button
    home_schooling_whf_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[1]/div[1]/div/div/p'
    try:
        home_schooling_whf_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, home_schooling_whf_xpath))
        )
        home_schooling_whf_button.click()
        print("'Home Schooling & WHF' button clicked successfully.")
    except TimeoutException:
        print(f"'Home Schooling & WHF' button with XPath {home_schooling_whf_xpath} is not clickable.")
        return

    # Click the "Meet Max" button
    meet_max_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div/div[2]/div/div[2]/div/div[2]'
    try:
        meet_max_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, meet_max_xpath))
        )
        meet_max_button.click()
        print("'Meet Max' button clicked successfully.")
    except TimeoutException:
        print(f"'Meet Max' button with XPath {meet_max_xpath} is not clickable.")
        return

    # Click the "Yes" button to confirm the purchase
    yes_button_xpath = '//*[@id="root"]/div/div/div[6]/div[3]/div[1]/div/div[4]/button[2]'
    try:
        yes_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, yes_button_xpath))
        )
        yes_button.click()
        print("'Yes' button clicked successfully.")
    except TimeoutException:
        print(f"'Yes' button with XPath {yes_button_xpath} is not clickable.")
        return

    # Check if "Internal Server Error" is displayed
    error_message_xpath = "//*[contains(text(), 'Internal Server Error')]"
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, error_message_xpath))
        )
        # Fail the test if the error message is found
        if error_message:
            print("Test failed: 'Internal Server Error' message is displayed.")
            assert False, "'Internal Server Error' appeared after clicking the 'Yes' button."
    except TimeoutException:
        print("No 'Internal Server Error' message. Test passed.")

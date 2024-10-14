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
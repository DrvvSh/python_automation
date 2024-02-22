from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    sleep(3)

''' Searching By.ID '''
def test_by_id(driver):
    page1 = 'https://www.qa-practice.com/elements/input/simple'
    input_data = 'Text'
    driver.get(page1)
    text_string = driver.find_element(By.ID,'id_text_string')
    text_string.send_keys(input_data)
    # Submit using the 'Enter' key on the keyboard
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert input_data == result_text.text

''' Searching By.CLASS_NAME '''
def test_by_class_name(driver):
    page1 = 'https://www.qa-practice.com/elements/input/simple'
    input_data = 'Text'
    driver.get(page1)
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    assert input_data == result_text.text

''' Searching By.TAG_NAME '''
def test_by_tag_name(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'

''' Searching By.LINK_TEXT '''
def test_by_link_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    # contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'act')
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'

''' Searching By.CSS_SELECTOR '''
def test_by_css_selector(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    # text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
    text_string = driver.find_element(By.CSS_SELECTOR, '.form-control')
    text_string.send_keys('Text')
    # text_string.send_keys(Keys.ENTER)
    print(text_string.value_of_css_property('border-color'))
    assert text_string.get_attribute('placeholder') == 'Submit me'

''' Searching By.XPATH '''
def test_by_xpath(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    text_string.send_keys('Text')
    text_string.submit()

from selenium import webdriver
import pytest
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    sleep(3)
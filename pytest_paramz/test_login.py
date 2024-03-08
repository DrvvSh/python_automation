from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

users = ['user1@gmail.com', 'user2@gmail.com', 'user3@gmail.com']
passws = ['password1', 'password2', 'password3']


def generate_pairs():
    pairs = list()
    for user in users:
        for passw in passws:
            pairs.append(pytest.param((user, passw), id=f'{user}, {passw}'))
    return pairs


# @pytest.mark.parametrize('creds',
#                          [pytest.param(('user1@gmail.com', 'password1'), id='user1@gmail.com, password1'),
#                           pytest.param(('user2@gmail.com', 'password2'), id='user2@gmail.com, password2'),
#                           pytest.param(('user3@gmail.com', 'password3'), id='user3@gmail.com, password3')]
#                           )

@pytest.mark.skip
@pytest.mark.parametrize('creds', generate_pairs())
def test_login(creds):
    login, passw = creds
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.ID, 'send2').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert ('The account sign-in was incorrect or your account is disabled temporarily. '
    'Please wait and try again later.' == error_text)

# Indirect parameterization
@pytest.fixture()
def page(request):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    params = request.param
    if params == 'what_is_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif params == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale.html')
    return driver

@pytest.mark.parametrize('page', ['what_is_new'], indirect=True)
def test_what_is_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'What\'s New'

@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Sale'

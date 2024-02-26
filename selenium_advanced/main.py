from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep


# New tab open
def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])


# Iframe testing
def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()


# Dropdown menu testing
def test_drop_menu(driver):
    driver.implicitly_wait(3)
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    ActionChains(driver).move_to_element(women).move_to_element(tops).click(jackets).perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'


# Drag and drop testing
def test_d_n_d(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    first = driver.find_element(By.ID, 'rect-draggable')
    second = driver.find_element(By.ID, 'rect-droppable')
    ActionChains(driver).drag_and_drop(first, second).perform()


# Open new tab with Ctrl key
def test_open_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()


# Alert testing
def test_alerts(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    alert.accept()


# Scroll down to the bottom
def test_scroll(driver):
    driver.get('https://rateyourmusic.com')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


# Scroll to the element
def test_scroll_to_element(driver):
    driver.get('https://rateyourmusic.com/genres/')
    element = driver.find_element(By.LINK_TEXT, 'Experimental')
    driver.execute_script('arguments[0].scrollIntoView()', element)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


options = Options()
# options.add_argument('start-maximized')
# options.add_argument('--window-size=600,800')
# options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

page = 'https://www.startpage.com'
driver.get(page)
# print(driver.title)

# Search for Darkthrone band on Startpage.com
search = driver.find_element(By.NAME, 'query')
search.send_keys('Darkthrone')
search_button = driver.find_element(By.CLASS_NAME, 'search-btn')
search_button.click()


sleep(3)

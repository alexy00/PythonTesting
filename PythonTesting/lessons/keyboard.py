import time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://google.com')


element = driver.find_element_by_link_text('About')
#element.click()


ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .perform()

time.sleep(2) # Pause to allow you to inspect the browser.

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

time.sleep(5)

time.sleep(5)
#driver.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.walmart.com/")
driver.find_element_by_link_text("My Account").click()
driver.implicitly_wait(10)
#driver.find_element_by_id("Create an Account").click()

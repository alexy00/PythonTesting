from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class AirIndia():

    def test(self):

        driver = webdriver.Chrome()
        
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://www.airindia.in/")

        driver.find_element_by_id('from').send_keys('mos')
        driver.find_element_by_partial_link_text('Moscow - Domodedovo').click()
        driver.find_element_by_id('to').send_keys('del')
        driver.find_element_by_partial_link_text('Indira Gandhi International Airport').click()

        #Sort_by = driver.find_element_by_id("_classType1")
        DropDown = Select(driver.find_element_by_id("_classType1"))
        DropDown.select_by_visible_text('First/Executive')
        time.sleep(3)
        DropDownOption = driver.find_element_by_xpath("//option[@value='PremiumBusiness']")

        print("Sort By option: " + DropDownOption.text)


        time.sleep(3)
        driver.quit()

ff = AirIndia()
ff.test()













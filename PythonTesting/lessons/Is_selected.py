from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class IsSelected():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://www.airindia.in/")

        OneWay = driver.find_element_by_id('oneway')
        RoundTrip = driver.find_element_by_id('roundtrip')
        FixedDates = driver.find_element_by_id('fixedDate')
        FlexibleDates = driver.find_element_by_id('flexibleDate')
        print("'One Way' Radio Button is selected?-> " + str(OneWay.is_selected()))
        print("'Round Trip' Radio Button is selected?-> " + str(RoundTrip.is_selected()))
        print("'Fixed Dates' Radio Button is selected?-> " + str(FixedDates.is_selected()))
        print("'Flexible Dates' Radio Button is selected?-> " + str(FlexibleDates.is_selected()))
        driver.find_element_by_xpath("//label[@for='rdrules1']").click()
        radio2 = driver.find_element_by_id('rdrules2')
        if radio2.is_selected():
            print("Would you like to avail of domestic Concession? 'No' is selected: -> TRUE")
        else:
            print("Would you like to avail of domestic Concession? 'Yes' is selected: -> FALSE")

        time.sleep(3)
        driver.quit()

ff = IsSelected()
ff.test()

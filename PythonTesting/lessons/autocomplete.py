from selenium import webdriver
import time

class Autocomplete():

    def test(self):
        url = "https://www.southwest.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
            # One-way
        driver.find_element_by_xpath(".//*[@id='trip-type-one-way']").click()
            #Depart
        driver.find_element_by_id('air-city-departure').send_keys('new')
        driver.find_element_by_id('air-city-departure-menu-item2').click()
        time.sleep(2)
            # Arrive
        driver.find_element_by_id('air-city-arrival').send_keys('mia')
        driver.find_element_by_id('air-city-arrival-menu-item1').click()
        driver.find_element_by_id('air-date-departure').clear()
        driver.find_element_by_id('air-date-departure').send_keys('12/21')
        #driver.find_element_by_id('calendar-december-21').click()
        driver.find_element_by_id('jb-booking-form-submit-button').click()


        time.sleep(3)
        driver.quit()

ff = Autocomplete()
ff.test()
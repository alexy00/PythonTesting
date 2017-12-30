# Xpath writing Standarts

# .//*[@ attribute='value']

# example: <input value="Log In" tabindex="4" id="u_0_n" type="submit">
            # id='u_0_n'
            # value='Log In'
            # tabindex='4'
            # type='submit'



from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://facebook.com")
driver.find_element_by_xpath(".//*[@id='u_0_1']").send_keys("Vasssa")
driver.find_element_by_xpath(".//*[@id='u_0_3']").send_keys("Pukin")
driver.find_element_by_xpath(".//*[@id='u_0_i']").click()

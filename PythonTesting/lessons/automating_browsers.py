
from selenium import webdriver
import time

class AutomatingBrowsers():


    def test(self):

        driver = webdriver.Ie()

        driver.implicitly_wait(5)

        driver.get("http://google.com")

        print(driver.current_url)

        print(driver.title)

        driver.get("http://gmail.com")

        print(driver.title)

        driver.back()

        print(driver.title)

        driver.forward()

        print(driver.title)

        driver.refresh()

        driver.maximize_window()

        driver.close()

        driver.quit()

        print("Start : %s" % (time.ctime()))
        time.sleep(5)
        print("End : %s" % (time.ctime()))

ff = AutomatingBrowsers()
ff.test()
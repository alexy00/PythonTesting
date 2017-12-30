from selenium import webdriver
import time

class abs():

    def test(self):
        url = ""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)

        time.sleep(3)
        driver.quit()


ff = abs()
ff.test()

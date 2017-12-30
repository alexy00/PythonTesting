from selenium import webdriver
import time


class SwitchToAlert():
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "https://letskodeit.teachable.com/pages/practice"
        driver.get(url)
        driver.find_element_by_id("name").send_keys("Alex")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(3)
# Switching to java script pop up
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Alex")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        #alert2.accept()
        alert2.dismiss()

        driver.quit()

ff = SwitchToAlert()
ff.test()



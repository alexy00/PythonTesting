from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
import time



class UsingWrappers():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "https://letskodeit.teachable.com/pages/practice"
        driver.get(url)
        hw = HandyWrappers(driver)
        print("The title of this page is: " + driver.title)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()



        print("Start : %s" % (time.ctime()))
        time.sleep(5)
        print("End : %s" % (time.ctime()))
        driver.quit()

ff = UsingWrappers()
ff.test()

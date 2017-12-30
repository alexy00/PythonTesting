from selenium import webdriver
import time

class Frames():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "http://jqueryui.com/tooltip/"
        driver.get(url)

        print("The title of this page is: " + driver.title)

        fr = driver.find_element_by_class_name("demo-frame")
#switch to frame
        driver.switch_to.frame(fr)
        driver.find_element_by_css_selector("#age").send_keys("22")
        time.sleep(3)
#swich back to window
        driver.switch_to.default_content()
        driver.find_element_by_xpath(".//*[@id='sidebar']//a[contains(text(),'Draggable')]").click()
        time.sleep(3)
        driver.quit()


ff = Frames()
ff.test()
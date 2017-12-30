from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class SliderAction():

    def test(self):
        driver = webdriver.Chrome()
        url = "http://jqueryui.com/slider/"
        driver.get(url)
        driver.implicitly_wait(5)
        driver.maximize_window()
        # driver.switch_to.frame(0) Switch to frame by number  OR by class name:
        fr = driver.find_element_by_class_name("demo-frame")
        driver.switch_to.frame(fr)
        element = driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
        except:
            print("Sliding Failed On Element")


ff = SliderAction()
ff.test()



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class DragAndDrop():

    def test(self):
        driver = webdriver.Chrome()
        url = "http://jqueryui.com/droppable/"
        driver.get(url)
        driver.implicitly_wait(5)
        driver.maximize_window()
        # driver.switch_to.frame(0) Switch to frame by number  OR by class name:
        fr = driver.find_element_by_class_name("demo-frame")
        driver.switch_to.frame(fr)

        FromElement = driver.find_element_by_id("draggable")
        ToElement = driver.find_element_by_id("droppable")
        time.sleep(3)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(FromElement, ToElement).perform()
            #actions.click_and_hold(FromElement).move_to_element(ToElement).release().perform()
            print("Drag And Drop Element Successful")
        except:
            print("Drag And Drop Failed On Element")

ff = DragAndDrop()
ff.test()


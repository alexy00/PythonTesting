from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class RightClick():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        url = "http://google.com"
        driver.get(url)



        added_box = driver.find_element_by_css_selector("#lst-ib")
        added_box.send_keys("aaaaaaa")
        time.sleep(3)
        ActionChains(driver).move_to_element(added_box).context_click().perform()
        added_box.clear()


        time.sleep(3)
        driver.quit()


ff = RightClick()
ff.test()
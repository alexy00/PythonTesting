from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class MouseHoover():

    def test(self):
        driver = webdriver.Chrome()
        url = "http://spicejet.com/"
        driver.get(url)
        driver.implicitly_wait(5)
        driver.maximize_window()

        Investors = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/a")
        ActionChains(driver).move_to_element(Investors).perform()
        time.sleep(5)


        Financial_info = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/a")
        ActionChains(driver).move_to_element(Financial_info).perform()
        time.sleep(5)

        Anual_report = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/ul/li[1]/a")
        ActionChains(driver).move_to_element(Anual_report).perform()
        time.sleep(5)

        Anual_report_14_15 = driver.find_element_by_xpath(".//*[@id='smoothmenu1']/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[1]/a")
        ActionChains(driver).move_to_element(Anual_report_14_15).click().perform()

        print("New page opened. URL-> ", driver.current_url)
        title = driver.title
        print(title)
        
        time.sleep(5)
        print("Start : %s" % (time.ctime()))
        time.sleep(5)
        print("End : %s" % (time.ctime()))
        driver.quit()

ff = MouseHoover()
ff.test()

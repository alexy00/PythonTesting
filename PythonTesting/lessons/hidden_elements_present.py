from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Utilities.handy_wrappers import HandyWrappers
import time



class HiddenElementsPresent():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        url = "https://www.expedia.com/"
        driver.get(url)
        print("The title of this page is: " + driver.title)

        driver.find_element_by_id("tab-flight-tab").click()

        Children = driver.find_element_by_id("flight-children")
        NumOfChildren = Select(Children)
        NumOfChildren.select_by_visible_text('1')

        time.sleep(3)

        NumOfChildren =driver.find_element_by_xpath(
            ".//*[@id='flight-children']/option[@value='1']")
        if NumOfChildren.is_selected():
            print("Number Of Children is selected? --> " + str(NumOfChildren.is_selected()))
        else:
            print("Number Of Children is Not selected")

        print("Number of children selected is: " + NumOfChildren.text)

        ChildAge = hw.isElementPresent("flight-age-select-1", By.ID)
        print(str(ChildAge))

        ChildAge = driver.find_element_by_id("flight-age-select-1")
        print("Is 'Child Age' element displayed?:--> " + str(ChildAge.is_displayed()))
        time.sleep(3)
        driver.close()
        print("---------------------TEST 2---------------TEST 2---------------------")

    def test2(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        url = "https://www.expedia.com/"
        driver.get(url)
        print("The title of this page is: " + driver.title)

        driver.find_element_by_id("tab-flight-tab").click()

        Children = driver.find_element_by_id("flight-children")


        if Children.is_selected():
            print("Number Of Children is selected? --> " + str(Children.is_selected()))
        else:
            print("Number Of Children is Not selected")
        time.sleep(3)

        ChildAge = hw.isElementPresent("flight-age-select-1", By.ID)
        print(str(ChildAge))

        print("Start : %s" % (time.ctime()))
        time.sleep(5)
        print("End : %s" % (time.ctime()))
        driver.quit()

ff = HiddenElementsPresent()
ff.test()
ff.test2()
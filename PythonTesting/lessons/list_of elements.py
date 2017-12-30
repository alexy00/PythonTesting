from selenium import webdriver
import time

class ListOfElements():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "http://www.titleboxing.com/gloves"
        driver.get(url)
        print("The title of this page is: " + driver.title)

        PageNumbersList = driver.find_elements_by_xpath(".//*[@id='productGrid']/div[1]/div[2]/div[2]/ol/li")
        size = len(PageNumbersList)
        print("Visible number of pages is: " + str(size - 1)) # minus 'Next' from the PageNumbersList

        for PageNumber in PageNumbersList:
            isSelected = PageNumber.is_selected()




        time.sleep(3)
        driver.quit()

    print("Start : %s" % (time.ctime()))
    time.sleep(5)
    print("End : %s" % (time.ctime()))
ff = ListOfElements()
ff.test()
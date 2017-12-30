from selenium import webdriver

import time

class IsEnable():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "https://www.google.com/"
        driver.get(url)

        print("The title of this page is: " + driver.title)

        SearchBox = driver.find_element_by_id("lst-ib")
        SearchBoxState = SearchBox.is_enabled() # True for enebled and False for disabled
        print("SearchBox is Enabled? -> " + str(SearchBoxState))

        SearchBox.send_keys("Toyota")
        time.sleep(3)

        driver.quit()

    print("Start : %s" % (time.ctime()))
    time.sleep(5)
    print("End : %s" % (time.ctime()))

ff = IsEnable()
ff.test()
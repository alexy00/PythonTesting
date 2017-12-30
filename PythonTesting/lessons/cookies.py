from selenium import webdriver

class Cookies():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "http://google.com/"
        driver.get(url)

        cook = driver.get_cookies()
        print(len(cook))
        driver.delete_all_cookies()
        cook1 = driver.get_cookies()
        print(len(cook1))
        driver.quit()

ff = Cookies()
ff.test()

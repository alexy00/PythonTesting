from selenium import webdriver

class BrowserInteractions():

    def test(self):
        base_url = "https://www.google.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        title = driver.title
        print("Title of the page is: " + title)
        current_url = driver.current_url
        print("Current URL of the page is: " + current_url)
        driver.refresh()
        url = "https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/#identifier"
        driver.get(url)
        title = driver.title
        print("Title of the page is: " + title)
        current_url = driver.current_url
        print("Current URL of the page is: " + current_url)
        driver.back()
        print("Current URL of the page is: " + current_url)
        driver.forward()

        driver.quit()

ff = BrowserInteractions()
ff.test()

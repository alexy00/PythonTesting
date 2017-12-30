from selenium import webdriver

class screenshot():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "http://google.com/"
        driver.get(url)

        destinationFileName = 'C:\\Users\\alba\\Desktop\\scr.png'

        try:
            driver.save_screenshot(destinationFileName)
            print('Screenshot saved to directiry--> ' + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue" )

        #driver.get_screenshot_as_file("screenshot.jpg")
# will save in a same file where script is saved(desktop/Testfiles)

        driver.quit()

ff = screenshot()
ff.test()
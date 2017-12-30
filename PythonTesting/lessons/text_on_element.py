from selenium import webdriver




class Text_onElement():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)


        element = driver.find_element_by_id("opentab")
        output = element.text
        print(output)

        element2 = driver.find_element_by_id("openwindow")
        output2 = element2.get_attribute("innerText")
        print(output2)

        driver.quit()


ff = Text_onElement()
ff.test()
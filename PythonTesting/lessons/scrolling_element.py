from selenium import webdriver
import time

class ScrollingElement():


    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        url = "http://www.titleboxing.com/"
        driver.get(url)
        driver.implicitly_wait(10)

        try:
            driver.find_element_by_css_selector(".fancybox-item.fancybox-close").click()
        except:
                pass

        # Scroll Down
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(3)

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(3)

        # Scroll Element Into View
        element = driver.find_element_by_xpath("//a[@class='product-image'][@tabindex='0']/img[@alt='TITLE COMMAND FULL TRAINING HEADGEAR']")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)

        # Native Way To Scroll Element Into View
        driver.execute_script("window.scrollBy(0, -1500);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))
        time.sleep(3)

        driver.quit()




ff = ScrollingElement()
ff.test()


from selenium import webdriver
import time

class SwitchToWindow():


    def test(self):
        driver = webdriver.Chrome()
        url = "https://accounts.google.com/SignUp?hl=en"
        driver.get(url)
        driver.implicitly_wait(5)
# Find parent handle -> Main Window
        parentWindow = driver.current_window_handle
        print("Parent Window Title: " + driver.title)
# Find LearnMore link and click on it
        driver.find_element_by_css_selector(".why-information>a").click()


# Find all handles(there should be two) and print them - OPTIONAL-
        handles = driver.window_handles

        for handle in handles:
            print("Handle: " + handle)
# Switch to child window
        driver.switch_to.window(driver.window_handles[-1])
        childWindow = driver.current_window_handle
        print("Switched to window: " + driver.title)
        driver.find_element_by_xpath("//a[@name='name']").click()
        time.sleep(3)

 # Swithc back to the parent window
        driver.switch_to.window(parentWindow)
        print("Switched to window: " + driver.title)
        driver.find_element_by_id('FirstName').send_keys("Vasya")
        time.sleep(3)
# Swith back to child window
        driver.switch_to.window(childWindow)
        print("Switched to window: " + driver.title)
        driver.find_element_by_xpath("//a[@name='username']").click()
        time.sleep(3)
        driver.close()

# Swithc back to the parent window
        driver.switch_to.window(parentWindow)
        print("Switched to window: " + driver.title)
        driver.find_element_by_id('LastName').send_keys("Super")

        time.sleep(3)
        driver.quit()



ff = SwitchToWindow()
ff.test()



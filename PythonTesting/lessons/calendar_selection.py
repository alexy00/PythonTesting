from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("primary-header-flight").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH,
                                           "(//div[@class='datepicker-cal-month'])[1]//button[text()='30']")
        print("Date selected is: " + dateToSelect.text)
        # Click the date
        dateToSelect.click()
        print("--------------------------TEST 2------------------TEST 2--------------")

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab").click()
        # Click departing field
        driver.find_element_by_id("flight-departing").click()
        # Pick the month between two [1] or [2]
        calMonth = driver.find_element(By.XPATH, "(//div[@class='datepicker-cal-month'])[1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

        time.sleep(2)

        for date in allValidDates:
            if date.text == "30":
                date.click()
                break

        time.sleep(3)
        driver.quit()

ff = CalendarSelection()
ff.test1()
ff.test2()

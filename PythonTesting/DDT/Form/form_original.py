from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest


class Canada_Shipping(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = "http://www.lifecellskin.com/ExclusiveOffer/index.php"
        cls.driver.get(page_url)

    # All fields are filled and  "GET 30 DAY TRIAL" button clicked - for USA(Fedex Only)

    def test_1_AllFields_Canada(self):

        first_name = self.driver.find_element(By.CSS_SELECTOR, "#fields_fname")
        first_name.send_keys("TEST")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "#fields_lname")
        last_name.send_keys("TEST")
        address1 = self.driver.find_element(By.CSS_SELECTOR, "#fields_address1")
        address1.send_keys("1909 Tyler st.")

        country_drop = self.driver.find_element(By.CSS_SELECTOR, "#country")
        Select(country_drop).select_by_visible_text("Canada")

        state_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_state")
        Select(state_drop).select_by_visible_text("Alberta")

        city = self.driver.find_element(By.CSS_SELECTOR, "#fields_city")
        city.send_keys("FAKE CITY")

        zip = self.driver.find_element(By.CSS_SELECTOR, "#fields_zip")
        zip.send_keys("33020")

        phone = self.driver.find_element(By.CSS_SELECTOR, "#fields_phone")
        phone.send_keys("11111111111")

        email = self.driver.find_element(By.CSS_SELECTOR, "#fields_email")
        email.send_keys("fake@fake.com")

        order_btn = self.driver.find_element(By.CSS_SELECTOR, ".rush_order_btn")
        order_btn.click()
        time.sleep(3)



        print("\nNew page opened. URL-> ", self.driver.current_url)
        url = self.driver.current_url

        if "order" in url:
            print("\n""ORDER page for Canada is loaded")
        else:
            print("ORDER page for Canada is NOT loaded")

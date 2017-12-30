from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import unittest


class MASTER_VISA_AMEX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = "https://www.lifecellskin.com/ExclusiveOffer/order.php?tempOrderId=1BEFAC3A1E994B3E0ECA342A8CB4803B"
        cls.driver.get(page_url)


    def test_1__Master(self):

        cc_number_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_number")
        cc_number_field.send_keys("5105105105105100")
        month_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expmonth")
        Select(month_drop).select_by_value("12")
        year_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expyear")
        Select(year_drop).select_by_value("25")
        sec_code_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_cvv")
        sec_code_field.send_keys("333")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
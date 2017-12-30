from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest
import datetime    # <--- import datetime!!    ----SEE CSREENSHOTS-----


class DynamicDates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = "https://www.lifecellskin.com/ExclusiveOffer/order.php?tempOrderId=1BEFAC3A1E994B3E0ECA342A8CB4803B"
        cls.driver.get(page_url)


    def test(self):

        now = datetime.datetime.now()

        now_month = now.month
        input_month = now_month + 1  # input month will be 1 month ahead
        print(input_month)
        if now_month == 12:
            input_month = 1

        # by visible text
        input_year = str(now.year)  # <--- convert to string
        print(input_year)


         #by index
        '''
        input_year = (now.year)
        print(input_year)
        input_year = 0
        '''


        cc_number_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_number")
        cc_number_field.send_keys("5105105105105100")
        month_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expmonth")
        Select(month_drop).select_by_index(input_month)      #<---------

        year_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expyear")
        Select(year_drop).select_by_visible_text(input_year)  #<---------

        sec_code_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_cvv")
        sec_code_field.send_keys("333")
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
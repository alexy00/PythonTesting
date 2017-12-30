from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import unittest


class Shipping_Billing_Yes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = "https://www.lifecellskin.com/ExclusiveOffer/order.php?tempOrderId=1BEFAC3A1E994B3E0ECA342A8CB4803B"
        cls.driver.get(page_url)


    def test_1_ShippingAddress_Yes(self):  # Test if Shipping/Billing address is selected Yes by default
        time.sleep(3)
        radio_yes = self.driver.find_element(By.XPATH, ".//input[@id='sameAsShippingYes']")
        result = radio_yes.is_selected()
        assert result == True
        print("\nRadio button 'YES' is selected by default")


    def test_2_CC_number_popup(self):  # Test the popups
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rushmy_trial_button)
        rushmy_trial_button.click()
        alert_cc_number = self.driver.switch_to.alert
        alert_cc_number.accept()
        print("\nPlease Enter Your Credit Card Number popup is displayed")


    def test_3_exp_date_popup(self):
        cc_number_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_number")
        cc_number_field.send_keys("5105105105105100")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rushmy_trial_button)
        rushmy_trial_button.click()
        alert_exp_date = self.driver.switch_to.alert
        alert_exp_date.accept()
        print("\nPlease Enter Your Exp. Date popup is displayed")


    def test_4_sec_code_popup(self):
        month_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expmonth")
        Select(month_drop).select_by_value("12")
        year_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expyear")
        Select(year_drop).select_by_value("25")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your Security Code popup is displayed")


    def test_5_succes(self):
        sec_code_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_cvv")
        sec_code_field.send_keys("333")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()

        try:
            wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                                ignored_exceptions=[NoSuchElementException,
                                                    ElementNotVisibleException,
                                                    ElementNotSelectableException,
                                                    ElementNotInteractableException])
            next = wait.until(EC.element_to_be_clickable((By.ID, "wistia_smallPlayButton_65")))
            url = self.driver.current_url
            self.assertIn("success", url)
            print("\n""Success page is loaded")
            time.sleep(2)
            stop = self.driver.find_element(By.CSS_SELECTOR, "#wistia_smallPlayButton_151")
            stop.click()
        except:
            pass


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(verbosity=2)
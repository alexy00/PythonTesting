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



    def test_01_shipping_No(self):
        radio_no = self.driver.find_element(By.XPATH, ".//*[@id='final-step-table']//label[@for='sameAsShippingNo']")
        radio_no.click()
        result = radio_no.is_enabled()
        assert result == True
        print("\nRadio button 'NO' is selected")


    def test_02_CCNumber_popup(self):
        # Test the popups
        self.driver.execute_script("window.scrollBy(0,1500);")
        time.sleep(3)
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert_cc_number = self.driver.switch_to.alert
        alert_cc_number.accept()
        print("\nPlease Enter Your Credit Card Number --> is displayed")


    def test_03_ExpDate_popup(self):
        cc_number_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_number")
        cc_number_field.send_keys("5105105105105100")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert_exp_date = self.driver.switch_to.alert
        alert_exp_date.accept()
        print("\nPlease Enter Your Exp. Date --> is displayed")


    def test_04_SecCode_popup(self):
        month_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expmonth")
        Select(month_drop).select_by_value("12")
        year_drop = self.driver.find_element(By.CSS_SELECTOR, "#fields_expyear")
        Select(year_drop).select_by_value("25")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your Security Code --> is displayed")


    def test_05_billingAddr_popup(self):
        sec_code_field = self.driver.find_element(By.CSS_SELECTOR, "#cc_cvv")
        sec_code_field.send_keys("333")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your  Billing Address --> is displayed")


    def test_06_billingFname_popup(self):
        self.driver.execute_script("window.scrollBy(0,-300);")
        bill_addr_field = self.driver.find_element(By.CSS_SELECTOR, "#billing_street_address")
        bill_addr_field.send_keys("FAKE STREET")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your  Billing First Name --> is displayed")


    def test_07_billingLname_popup(self):
        self.driver.execute_script("window.scrollBy(0,-200);")
        bill_fname_field = self.driver.find_element(By.CSS_SELECTOR, "#billing_fname")
        bill_fname_field.send_keys("FAKE")
        self.driver.execute_script("window.scrollBy(0,200);")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your  Billing Last Name --> is displayed")


    def test_08_billingCity_popup(self):

        bill_lname_field = self.driver.find_element(By.CSS_SELECTOR, "#billing_lname")
        bill_lname_field.send_keys("FAKE")
        self.driver.execute_script("window.scrollBy(0,450);")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your  Billing City --> is displayed")


    def test_09_billingState_popup(self):

        bill_city_field = self.driver.find_element(By.CSS_SELECTOR, "#billing_city")
        bill_city_field.send_keys("FAKE-CITY")
        self.driver.execute_script("window.scrollBy(0,150);")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease enter your Billing State --> is displayed")


    def test_10_billingZip_popup(self):
        state = self.driver.find_element(By.CSS_SELECTOR, "#billing_state")
        state.send_keys("Florida")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rushmy_trial_button)
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your  Billing Zip --> is displayed")


    def test_11_billingCountry_popup(self):
        bill_zip_field = self.driver.find_element(By.CSS_SELECTOR, "#billing_postcode")
        bill_zip_field.send_keys("010101000")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rushmy_trial_button)
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease choose your Billing Country --> is displayed")


    def test_12_BillingState2_popup(self):
        country_drop = self.driver.find_element(By.CSS_SELECTOR, "#billing_country")
        Select(country_drop).select_by_value("223")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rushmy_trial_button)
        rushmy_trial_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        print("\nPlease Enter Your  Billing State --> is displayed-2")


    def test_13(self):
        state_drop = self.driver.find_element(By.CSS_SELECTOR, "#billing_state")
        Select(state_drop).select_by_value("Florida")
        rushmy_trial_button = self.driver.find_element(By.CSS_SELECTOR, ".trial-submit-button")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rushmy_trial_button)
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
            print("The success page for good Mastercard is loaded")
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

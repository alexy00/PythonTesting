from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class CCPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    _cc_number = "#cc_number"
    _exp_month = "#fields_expmonth"
    _exp_year = "#fields_expyear"
    _security_code = "#cc_cvv"
    _rush_my_trial = ".trial-submit-button"
    _month_drop = "#fields_expmonth"
    _year_drop = "#fields_expyear"




    def getCCNumber(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._cc_number)

    def getSecCode(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._security_code)

    def getRushMyTrial(self):
        return self.driver.find_element(By.CSS_SELECTOR,self._rush_my_trial)


    # actions

    def enterCCNumber(self,CCnumber):
        self.getCCNumber().send_keys(CCnumber)

    def selectExpMonth(self,month):
        month_drop = self.driver.find_element(By.CSS_SELECTOR,self._exp_month)
        Select(month_drop).select_by_value(month)

    def selectExpYear(self,year):
        year_drop = self.driver.find_element(By.CSS_SELECTOR, self._exp_year)
        Select(year_drop).select_by_value(year)


    def enterSecCode(self,code):
        self.getSecCode().send_keys(code)

    def clickRushMyTrial(self):
        self.getRushMyTrial().click()



    def CCformFillup(self,CCnumber,code):
        self.enterCCNumber(CCnumber)
        self.selectExpMonth(month="12")
        self.selectExpYear(year="25")
        self.enterSecCode(code)
        self.clickRushMyTrial()

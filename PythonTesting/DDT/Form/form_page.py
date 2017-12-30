from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class FormPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators

    _first_name = "#fields_fname"
    _last_name = "#fields_lname"
    _address1 = "#fields_address1"
    _country_drop = "#country"
    _state_drop = "#fields_state"
    _city = "#fields_city"
    _zip = "#fields_zip"
    _phone = "#fields_phone"
    _email = "#fields_email"
    _order_btn = ".rush_order_btn"


    def getFname(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._first_name)

    def getLname(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._last_name)

    def getAddress(self):
        return self.driver.find_element(By.CSS_SELECTOR,self._address1)


    def getCity(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._city)

    def getZip(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._zip)

    def getPhone(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._phone)

    def getEmail(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._email)

    def getOrderBtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._order_btn)


    # actions

    def enterFname(self):
        self.getFname().send_keys("TEST")

    def enterLname(self):
        self.getLname().send_keys("TEST")

    def enterAddress(self):
        self.getAddress().send_keys("1909 Tyler st.")

    def selectCountry(self,country):
        country_drop = self.driver.find_element(By.CSS_SELECTOR,self._country_drop)
        Select(country_drop).select_by_visible_text(country)

    def selectState(self,state):
        state_drop = self.driver.find_element(By.CSS_SELECTOR, self._state_drop)
        Select(state_drop).select_by_visible_text(state)

    def enterCity(self):
        self.getCity().send_keys("FAKE CITY")

    def enterZip(self):
        self.getZip().send_keys("33020")

    def enterPhone(self):
        self.getPhone().send_keys("11111111111")

    def enterEmail(self):
        self.getEmail().send_keys("fake@fake.com")

    def clickOrderBtn(self):
        self.getOrderBtn().click()



    def formFillup(self,country,state):
        self.enterFname()
        self.enterLname()
        self.enterAddress()
        self.selectCountry(country)
        self.selectState(state)
        self.enterCity()
        self.enterZip()
        self.enterPhone()
        self.enterEmail()
        self.clickOrderBtn()


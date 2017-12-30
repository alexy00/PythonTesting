from selenium import webdriver
from utilities.login_page import LoginPage
import unittest



class Test(LoginPage, unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://letskodeit.teachable.com/")

    def tearDown(self):
        self.driver.quit()

    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True



if __name__ == '__main__':
    unittest.main(verbosity=2)
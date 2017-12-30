from selenium import webdriver
import time
import unittest
from  DDT.Form.cc_page import CCPage
from ddt import ddt, data, unpack       #<======   import ddt



@ddt                                         #<======  @ddt
class MASTER_VISA_AMEX(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = "https://www.lifecellskin.com/ExclusiveOffer/order.php?tempOrderId=1BEFAC3A1E994B3E0ECA342A8CB4803B"

        cls.driver.get(page_url)



    @data(("5105105105105100","333"),("4012888888881881", "333"),("371449635398431", "3333"))   #<======= @data(provide data set)
    @unpack                      #<=======@unpack
    def test_1__Master(self, ccnumber, sec):

        form = CCPage(driver=self.driver)
        form.CCformFillup(CCnumber=ccnumber,code=sec)
        self.driver.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
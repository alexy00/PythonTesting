from selenium import webdriver
import time
import unittest
from  DDT.Form.cc_page import CCPage
from ddt import ddt, data, unpack       #<======   import ddt
from utilities.read_data import getCSVData  #<======== import read_data file


@ddt                                         #<======  @ddt
class MASTER_VISA_AMEX(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        page_url = "https://www.lifecellskin.com/ExclusiveOffer/order.php?tempOrderId=1BEFAC3A1E994B3E0ECA342A8CB4803B"
        cls.driver.get(page_url)


    @data(*getCSVData("E:\\Python\\Test files\\testdata.csv"))   #<======= @data(provide full path if file is outside of a project)
    @unpack                      #<=======@unpack
    def test(self, ccnumber, sec):

        form = CCPage(driver=self.driver)
        form.CCformFillup(CCnumber=ccnumber,code=sec)
        self.driver.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
import unittest
from selenium import webdriver

class TitleBoxing(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.driver.get("https://titleboxing.com/")

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()



    def test_assertEqual(self):
        a = "Title Boxing Equipment: Boxing Gloves, Punching Bags, MMA Gear & Training Supplies - TITLE Boxing"
        b = self.driver.title
        self.assertEqual(a,b,msg="'a' is not Equal to 'b'")
        print("Title of the homepage is: ", self.driver.title)

    def test_is_element_present(self,):
        element = self.driver.find_element_by_xpath("//img[@alt='TITLE Boxing']")
        if element is not None:
            print("TITLE BOXING-> Element is found")

        else:
            print("TITLE BOXING-> Element is NOT found")



if __name__ == '__main__':
    unittest.main(verbosity=2)
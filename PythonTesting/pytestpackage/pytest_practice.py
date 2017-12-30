import pytest
from selenium import webdriver

class TitleBoxing():

    @pytest.yield_fixture()
    def setUp():
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.implicitly_wait(3)
            driver.get("https://titleboxing.com/")
            yield
            driver.quit()

    def test_assertEqual_1(setUp):
            a = "Title Boxing Equipment: Boxing Gloves, Punching Bags, MMA Gear & Training Supplies - TITLE Boxing"
            b = sef.driver.title
            assertEqual(a,b,msg="'a' is not Equal to 'b'")

    def test_is_element_present(setUp):
        element = driver.find_element_by_xpath("//img[@alt='TITLE Boxing']")
        if element is not None:
            print("TITLE BOXING-> Element is found")

        else:
            print("TITLE BOXING-> Element is NOT found")




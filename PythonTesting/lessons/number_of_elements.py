'''
from selenium import webdriver
import time

class NumberOfElements():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "http://www.ebay.com/"
        driver.get(url)
        print("The title of this page is: " + driver.title)

        totallinks=driver.find_elements_by_tag_name("a")
        print(len(totallinks))

        footer = driver.find_element_by_xpath(".//*[@id='glbfooter']")
        links_footer = footer.find_elements_by_tag_name("a")
        print(len(links_footer))  # number of links in footer

        for obj in links_footer:  # toprint names of links in footer
            print(obj.text)

        print("Start : %s" % (time.ctime()))
        time.sleep(5)
        print("End : %s" % (time.ctime()))
        driver.quit()

ff = NumberOfElements()
ff.test()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Akita():


    def test_Akita(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        page_url = ("https://www.puppyspot.com/breed/akita/?breed_id=209")
        driver.get(page_url)



        Sort = driver.find_element(By.XPATH, ".//div[@id='main']//h4[@class='sort-list closed']")
        Sort.click()
        time.sleep(2)
        LowToHigh = driver.find_element(By.XPATH, ".//form[@id='frmSearch04']//label[@for='price-low-to-high']")
        LowToHigh.click()
        time.sleep(2)

        page1 = driver.find_element_by_xpath(".//*[@id='main']//div[@class='puppy-page no-border page1']")
        links_imgs = page1.find_elements(By.CSS_SELECTOR, ".list-image")
        print(len(links_imgs))  # number of images on page1

        for obj in links_imgs:  # toprint names of images
            print(obj.text)

ff = Akita()
ff.test_Akita()
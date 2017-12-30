from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class Title():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        url = "http://www.titleboxing.com/"
        driver.get(url)
        print("The title of this page is: " + driver.title)


#this is to close the popup
        try:
            driver.find_element_by_css_selector(".fancybox-item.fancybox-close").click()
        except:
                pass

        Glove_menu = driver.find_element_by_css_selector(".level-top>span")
#Glove_menu = driver.find_element_by_xpath("//a[@class='level-top']/span[text()='Gloves']")
        drop_down = driver.find_element_by_css_selector(".level1.nav-1-1.first>a>span")
#drop_down = driver.find_element_by_xpath("//li[@class='level1 nav-1-1 first']//span")

        action = ActionChains(driver)
        action.move_to_element(Glove_menu).perform()
        action.move_to_element(drop_down).click().perform()
        time.sleep(3)


        DropDown = Select(driver.find_element_by_css_selector(".sort-by>select"))
        DropDown.select_by_visible_text("Name (A-Z)")
        time.sleep(3)
        DropDownOption = driver.find_element_by_css_selector(".sort-by>select>[selected='selected']")

        print("Sort By option: " + DropDownOption.text)

        print(driver.find_element_by_css_selector(".product-name>a[title='BOON SPORT LEATHER LACE TRAINING']").text)
        Brand = driver.find_elements_by_xpath(".//*[@id='narrow-by-list']/dd[1]/ol/li")

        for obj in Brand:  # to print names of links in footer
            print(obj.text)

        time.sleep(3)
        driver.quit()

    print("Start : %s" % (time.ctime()))
    time.sleep(5)
    print("End : %s" % (time.ctime()))
ff = Title()
ff.test()

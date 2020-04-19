import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Mfscrm_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/customer_list")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[3]/div/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Bill Davis")
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("this is a test")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("omaha")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("100")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[7]/td[8]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Barbara York")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(5)

        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[4]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[3]/div/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Sobie Testing")
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("this is a test")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("6")
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("500")
        time.sleep(5)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(5)
        driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

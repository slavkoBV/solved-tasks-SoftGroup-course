import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

        cls.driver.get("http://meblilem.com.ua/")

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        self.search_field.send_keys('спальні')
        self.search_field.submit()
        try:
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "item")))
            self.assertEqual(20, len(products))
        except Exception as err:
            print(err)

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        self.search_field.send_keys('Соня')
        self.search_field.submit()
        try:
            WebDriverWait(self.driver, 20)
            product = self.driver.find_element_by_xpath("//div[@class='item']/a[2]")
            self.assertEqual('Соня', product.text.split()[0])
        except Exception as err:
            print(err)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

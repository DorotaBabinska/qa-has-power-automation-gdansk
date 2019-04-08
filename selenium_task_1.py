import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DuckDuckGoSearch(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--lang=pl')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_search_in_duck_duck_go(self):
        driver = self.driver
        driver.get("http://www.duckduckgo.com")
        field = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
        field.send_keys('he biggest python software house')
        element = driver.find_element_by_xpath('//*[@id="search_button_homepage"]')
        element.click()
        element2 = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
        element2.click()
        assert 'STX Next' in driver.page_source

if __name__ == "__main__":
    unittest.main()

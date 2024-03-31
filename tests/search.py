import time
import unittest
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearchBar(unittest.TestCase):
    SEARCH_BAR = (By.CSS_SELECTOR, 'input[class="searchBarInput form-control"]')
    TYPE_CONFIRM = (By.XPATH, '//div[@data-cy="phone-title')
    SEARCH_CONFIRM = (By.CSS_SELECTOR, 'rect[width="34"]')
    COOKIE_ACCEPT_BUTTON = (By.XPATH, '//span[contains(text(), "Da, sunt de acord")]')
    PRODUCT_ITEM_TITLE = (By.XPATH, '//div[@data-cy="phone-title"]')


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://flip.ro/magazin/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def testSearch(self):
        self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*self.SEARCH_BAR).send_keys('iphone 15')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()
        time.sleep(2)
        actualResult = self.driver.find_elements(*self.PRODUCT_ITEM_TITLE)
        print(actualResult[0].text)
        expectedMessage = 'Apple, iPhone 15, 128 GB, Black'
        time.sleep(2)
        self.assertIn(expectedMessage, actualResult[0].text, 'nu e ceea ce trebuie cautat')
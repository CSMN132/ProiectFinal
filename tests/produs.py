import time
import unittest
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProdus(unittest.TestCase):
    PRIMUL_PRODUS = (By.CSS_SELECTOR, '[class="card-phone-new position-relative d-flex flex-md-column"]')
    COLOR_SELECT = (By.CSS_SELECTOR, '[class="btn btn-device-parameter color btn-link"]')
    STORAGE_SELECT = (By.CSS_SELECTOR, '[class="btn btn-device-parameter btn-secondary"]')
    CONDITION_SELECT = (By.CSS_SELECTOR, '[class="btn btn-device-parameter btn-condition relative btn-secondary"]')
    

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://flip.ro/magazin/apple/iphone-15/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON).click()

    def tearDown(self):
        self.driver.quit()















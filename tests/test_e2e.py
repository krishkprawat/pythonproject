
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        # driver = webdriver.Chrome()
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
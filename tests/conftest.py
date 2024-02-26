import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action ="Store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getOption("browser_name")
    if browser_name=="chrome":

        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browser_name=="firefox":
        #firefox invocation
    request.cls.driver = driver
    yield
    driver.close()
    return driver




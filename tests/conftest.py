import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.pages.register_page import RegisterPage

MAIN_URL = "https://demo.assessment.playershealth.com/register"

@pytest.fixture
def driver():
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    yield wd
    wd.quit()

@pytest.fixture
def register_page(driver, request):
    driver.get(MAIN_URL)
    return RegisterPage(driver)

import pytest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.locator import RegisterPageLocators

valid_names = ["Иван1", "Sergey1", "Куауе1"]
invalid_names = [" ", "7888", "__", "Иван1880", ";№№@#$;;&%^", "\/",
                       "ыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы",
                       "Ъыпыпр", "Ьроро", "", "Нрнhjjjj"]

valid_last_names = ["Иван", "Sergey", "Куауе"]
invalid_last_names = [" ", "7888", "__", "Иван1880", ";№№@#$;;&%^", "\/",
                       "ыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы",
                       "Ъыпыпр", "Ьроро", "", "Нрнhjjjj"]

valid_email = ["rt@mo.com", "rt@mo.ru"]
invalid_email = ["rtmo.com", "rt@moru", "hjhjhj", ""]

valid_phone = ["1111111111"]
invalid_phone = ["[899", "", "   ", "444444444", "44444444444", "adsjls", "%;:;%;*"]

valid_title = ["athleticDirector", "athleticTrainer", "sportsClubAdministrator", "other"]

valid_password = ["Q1qq11qq", "R4T5tttt", "Th7y7yygcfmnkl"]
invalid_password = ["Q1qq1", "t", "", "dddddddddddddddddddddddddddddddddddddddddddddd", "11111111", "qqqqqqqq", "QQQQQQQQ"]

valid_org_name = ["123"]
valid_org_type = ["club"]
valid_org_zip = ["45408"]
valid_org_state = ["AL"]


@pytest.mark.parametrize("first_name", valid_names)
@pytest.mark.parametrize("last_name", valid_names)
@pytest.mark.parametrize("email", valid_email)
@pytest.mark.parametrize("phone", valid_phone)
@pytest.mark.parametrize("title", valid_title)
@pytest.mark.parametrize("password", valid_password)
@pytest.mark.parametrize("org_name", valid_org_name)
@pytest.mark.parametrize("org_type", valid_org_type)
@pytest.mark.parametrize("org_zip", valid_org_zip)
@pytest.mark.parametrize("org_state", valid_org_state)
def test_1(driver, register_page, first_name, last_name, email, phone, title, password, org_name, org_state, org_type, org_zip):
    register_page.first_name().send_keys(first_name)
    register_page.last_name().send_keys(last_name)
    register_page.email().send_keys(email)
    register_page.phone_number().send_keys(phone)
    register_page.password().send_keys(password)
    register_page.password_repeat().send_keys(password)
    register_page.org_zip().send_keys(org_zip)

    select = Select(register_page.title())
    select.select_by_value(title)

    register_page.org_state().send_keys(org_state)
    register_page.org_type().send_keys(org_type)
    register_page.org_name().send_keys(org_name)
    register_page.submit().click()
    #WebDriverWait(driver, 30).until(
        #EC.presence_of_element_located(RegisterPageLocators.START))
    time.sleep(15)
    assert driver.current_url == "https://demo.assessment.playershealth.com/customer/form"
    #"Player's Health Safety Needs Assessment"

    time.sleep(30)
    pass



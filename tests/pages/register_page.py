from tests.pages.base_page import BasePage
from tests.pages.locator import RegisterPageLocators


class RegisterPage(BasePage):
    def first_name(self):
        return self.driver.find_element(*RegisterPageLocators.FIRST_NAME)

    def last_name(self):
        return self.driver.find_element(*RegisterPageLocators.LAST_NAME)

    def email(self):
        return self.driver.find_element(*RegisterPageLocators.EMAIL)

    def phone_number(self):
        return self.driver.find_element(*RegisterPageLocators.PHONE_NUMBER)

    def title(self):
        return self.driver.find_element(*RegisterPageLocators.TITLE)

    def password(self):
        return self.driver.find_element(*RegisterPageLocators.PASSWORD)

    def password_repeat(self):
        return self.driver.find_element(*RegisterPageLocators.PASSWORD_REPEAT)

    def org_name(self):
        return self.driver.find_element(*RegisterPageLocators.ORG_NAME)

    def org_type(self):
        return self.driver.find_element(*RegisterPageLocators.ORG_TYPE)

    def org_zip(self):
        return self.driver.find_element(*RegisterPageLocators.ORG_ZIP)

    def org_state(self):
        return self.driver.find_element(*RegisterPageLocators.ORG_STATE)

    def submit(self):
        return self.driver.find_element(*RegisterPageLocators.SUBMIT)
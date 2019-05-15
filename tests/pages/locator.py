from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.NAME, "email")
    PHONE_NUMBER = (By.NAME, "phoneNumber")
    TITLE = (By.NAME, "title")
    PASSWORD = (By.NAME, "password")
    PASSWORD_REPEAT = (By.NAME, "passwordRepeat")
    ORG_NAME = (By.NAME, "orgName")
    ORG_STATE = (By.NAME, "orgState")
    ORG_TYPE = (By.NAME, "orgType")
    ORG_ZIP = (By.NAME, "orgZip")
    SUBMIT = (By.CSS_SELECTOR, "[class=\"btn btn--orange\"]")
    START = (By.CSS_SELECTOR, "[class=\"ButtonWrapper-sc-1g3rldj-0 dKNLk\"]")


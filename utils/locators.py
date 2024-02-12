from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.XPATH, "//a[@class='header_logo']")
    SIGNUP = (By.XPATH, "//button[text()='Sign up']")
    SIGNIN = (By.XPATH, "//button[contains(@class, 'header_signin')]")


class LoginPageLocators(object):
    EMAIL = (By.ID, "signinEmail")
    PASSWORD = (By.ID, "signinPassword")
    LOGIN = (By.CSS_SELECTOR, "button.btn.btn-primary")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class SignupPageLocators(object):
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER = (By.XPATH, "//button[text()='Register']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")
    
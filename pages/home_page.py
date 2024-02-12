from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.locators import *


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver=driver)

    def check_if_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def click_sign_in_button(self):
        self.find_element(*self.locator.SIGNIN).click()
        return LoginPage(self.driver)

    def click_sign_up_button(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignupPage(self.driver)


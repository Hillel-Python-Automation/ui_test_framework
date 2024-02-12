from pages.base_page import BasePage
from pages.garage_page import GaragePage
from utils.locators import SignupPageLocators
from utils import users


class SignupPage(BasePage):
    def __init__(self, driver):
        self.locator = SignupPageLocators
        super().__init__(driver)

    def enter_name(self, name):
        self.find_element(*self.locator.NAME).send_keys(name)

    def enter_lastname(self, lastname):
        self.find_element(*self.locator.LAST_NAME).send_keys(lastname)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def repeat_password(self, password):
        self.find_element(*self.locator.REPEAT_PASSWORD).send_keys(password)

    def click_register_button(self):
        self.find_element(*self.locator.REGISTER).click()

    def register(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_name(user["name"])
        self.enter_lastname(user["name"])
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.repeat_password(user["password"])
        self.click_register_button()

    def register_with_valid_user(self, user):
        self.register(user)
        return GaragePage(self.driver)

    def register_with_in_valid_user(self, user):
        self.register(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text




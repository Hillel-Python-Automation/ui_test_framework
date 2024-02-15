from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage


class TestSignInPage:
    def test_page_load(self, driver):
        page = HomePage(driver)
        assert page.check_if_loaded() is True

    def test_register_user(self, driver):
        page = HomePage(driver)
        page = page.click_sign_up_button()
        page = page.register_with_valid_user("validuser")
        assert page.garage_menu.is_displayed()

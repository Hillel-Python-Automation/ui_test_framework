from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chromium.service import ChromiumService

from pages.home_page import HomePage


class TestSignInPage:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def teardown_method(self, method):
        self.driver.quit()

    def test_page_load(self):
        page = HomePage(self.driver)
        assert page.check_if_loaded() is True

    def test_register_user(self):
        page = HomePage(self.driver)
        page = page.click_sign_up_button()
        page = page.register_with_valid_user("validuser")
        assert (page.find_element(By.XPATH, "//a[@href='/panel/garage' and contains(@class, 'btn-sidebar')]")
                .is_displayed())




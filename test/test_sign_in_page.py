from selenium import webdriver
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

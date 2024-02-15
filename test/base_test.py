from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def teardown_method(self):
        self.driver.quit()

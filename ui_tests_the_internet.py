import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

URL = "https://the-internet.herokuapp.com/"


class TestTheInternetWebsite:
    def setup_method(self, method):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_open_url(self):
        self.driver.get(URL)
        assert self.driver.title == 'The Internet'

    def test_check_checkboxes(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/checkboxes']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Checkboxes'
        checkbox_1 = self.driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
        checkbox_2 = self.driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")
        assert not checkbox_1.is_selected()
        assert checkbox_2.is_selected()
        checkbox_1.click()
        checkbox_2.click()
        assert checkbox_1.is_selected()
        assert not checkbox_2.is_selected()
        checkbox_1.click()
        checkbox_2.click()
        assert not checkbox_1.is_selected()
        assert checkbox_2.is_selected()

    def test_drag_and_drop(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/drag_and_drop']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Drag and Drop'
        element_a = (WebDriverWait(self.driver, 20)
                     .until(EC.element_to_be_clickable((By.XPATH, "//div[@id='column-a']"))))
        element_b = (WebDriverWait(self.driver, 20)
                     .until(EC.element_to_be_clickable((By.XPATH, "//div[@id='column-b']"))))
        action = ActionChains(self.driver)
        sleep(2)
        action.drag_and_drop(element_a, element_b).perform()
        sleep(2)






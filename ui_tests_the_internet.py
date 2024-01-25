import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

URL = "https://the-internet.herokuapp.com/"


class TestTheInternetWebsite:
    def setup_method(self, method):
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
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

    def test_base_auth(self):
        # Sending base auth "https://<username>:<password>@www.example.com/index.html"

        # self.driver.get(URL)
        self.driver.get('https://admin:admin@the-internet.herokuapp.com')
        self.driver.find_element(By.XPATH, "//a[@href='/basic_auth']").click()
        # sleep(2)
        # self.driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
        sleep(2)
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Basic Auth'

    def test_add_remove_elements(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/add_remove_elements/']").click()
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h3").text == 'Add/Remove Elements'
        add_element = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        assert add_element.is_displayed()
        sleep(1)
        add_element.click()
        sleep(1)
        delete_elements = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        assert delete_elements.__len__() == 1
        sleep(1)
        add_element.click()
        sleep(1)
        add_element.click()
        sleep(1)
        add_element.click()
        sleep(1)
        delete_elements = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        assert delete_elements.__len__() == 4
        for i, del_el in enumerate(delete_elements):
            if i % 2 != 0:
                del_el.click()
                sleep(1)

        delete_elements = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        assert delete_elements.__len__() == 2

    def test_dropdown(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/dropdown']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Dropdown List'
        dropdown = self.driver.find_element(By.XPATH, '//select[@id="dropdown"]')
        select = Select(dropdown)
        sleep(1)
        select.select_by_visible_text('Option 1')
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").is_selected()
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").get_attribute('value') == '1'
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").text == 'Option 1'
        select.select_by_index(2)
        sleep(1)
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").is_selected()
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").get_attribute('value') == '2'
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").text == 'Option 2'
        select.select_by_value('1')
        sleep(1)
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").is_selected()
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").get_attribute('value') == '1'
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").text == 'Option 1'

    def test_inputs(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/inputs']").click()
        assert self.driver.find_element(By.XPATH, "//div[@id='content']//h3").text == 'Inputs'
        input_element = self.driver.find_element(By.XPATH, '//input')
        assert input_element.get_attribute('value') == ''
        sleep(1)
        input_element.send_keys('45')
        sleep(1)
        assert input_element.get_attribute('value') == '45'
        self.driver.refresh()
        input_element = self.driver.find_element(By.XPATH, '//input')
        input_element.send_keys(Keys.ARROW_UP)
        assert input_element.get_attribute('value') == '1'

    def test_iframe(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/frames']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Frames'
        self.driver.find_element(By.XPATH, "//a[@href='/iframe']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == ('An iFrame containing the '
                                                                                         'TinyMCE WYSIWYG Editor')
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        element = self.driver.find_element(By.XPATH, '/html/body/p')
        assert element.text == 'Your content goes here.'
        self.driver.switch_to.default_content()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == ('An iFrame containing the '
                                                                                         'TinyMCE WYSIWYG Editor')

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage(object):
    def __init__(self, driver, base_url="https://qauto.forstudy.space/"):
        time.sleep(1)
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, 5)

    def find_elem(self, locator):
        # return self.driver.find_element(*locator)
        self.wait_for_page_loading()
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_for_page_loading(self):
        self.wait.until(lambda x: x.execute_script('return document.readyState;') == 'complete')

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)




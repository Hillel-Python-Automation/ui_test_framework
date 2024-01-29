import time


class BasePage(object):
    def __init__(self, driver, base_url="https://qauto.forstudy.space/"):
        time.sleep(2)
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

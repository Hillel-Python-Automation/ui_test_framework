import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")
    yield driver
    driver.quit()
    print('driver quit')

# @pytest.fixture(scope='function')
# def driver(request):
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")
#
#     def teardown():
#         driver.quit()
#         print('driver quit')
#     request.addfinalizer(teardown)
#     return driver

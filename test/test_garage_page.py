import pytest

from pages.home_page import HomePage


class TestGaragePage:
    @pytest.fixture
    def open_garage_page(self, driver):
        page = HomePage(driver)
        page = page.click_sign_in_button()
        page = page.login_with_valid_user("test_user")
        return page

    def test_page_load(self, open_garage_page):
        page = open_garage_page
        assert page.check_if_loaded()

    def test_add_new_car(self, open_garage_page):
        test_car = {"brand": "Ford", "model": "Focus", "mileage": 100}

        page = open_garage_page
        page = page.click_add_button()
        page = page.add_a_car(**test_car)
        assert page.the_car_is_added(**test_car)

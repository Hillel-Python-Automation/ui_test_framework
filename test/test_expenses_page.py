import pytest

from pages.expenses_page import ExpensesPage
from pages.home_page import HomePage


class TestExpensePage:

    @pytest.fixture(scope='function')
    def open_fuel_expenses_page(self, driver):
        page = HomePage(driver)
        page = page.click_sign_in_button()
        page = page.login_with_valid_user("test_user")
        page.fuel_expenses_menu.click()
        return ExpensesPage(driver)

    def test_page_load(self, open_fuel_expenses_page):
        page = open_fuel_expenses_page
        assert page.check_if_loaded()

    def test_add_an_expense(self, open_fuel_expenses_page):
        test_expense = {"vehicle": 1,
                        "report_date": "15.02.2024",
                        "mileage": 1,
                        "number_of_litters": 10,
                        "total_cost": 10}

        page = open_fuel_expenses_page
        page = page.click_add_expense_button()
        page = page.add_an_expense(**test_expense)
        assert page.the_expense_is_added(**test_expense)

import time

from pages.base_page import BasePage
from utils.locators import ExpensesPageLocators

from selenium.webdriver.support.ui import Select


class ExpensesPage(BasePage):
    def __init__(self, driver):
        self.locator = ExpensesPageLocators
        super().__init__(driver=driver)

    def check_if_loaded(self):
        return True if self.find_elem(self.locator.HEADER).text == 'Fuel expenses' else False

    def click_add_expense_button(self):
        self.find_elem(self.locator.ADD_NEW_EXPENSE).click()
        return ExpensesPage(self.driver)

    def add_an_expense(self, **kwargs):
        vehicle = Select(self.find_elem(self.locator.VEHICLE))
        vehicle.select_by_index(kwargs['vehicle'])
        time.sleep(1)

        report_date = self.find_elem(self.locator.REPORT_DATE)
        report_date.clear()
        report_date.send_keys(kwargs['report_date'])

        mileage = self.find_elem(self.locator.MILEAGE)
        new_value = int(mileage.get_attribute('value')) + kwargs['mileage']
        mileage.clear()
        mileage.send_keys(new_value)

        number_of_litters = self.find_elem(self.locator.NUMBER_OF_LITTERS)
        number_of_litters.clear()
        number_of_litters.send_keys(kwargs['number_of_litters'])

        total_cost = self.find_elem(self.locator.TOTAL_COST)
        total_cost.clear()
        total_cost.send_keys(kwargs['total_cost'])

        self.find_elem(self.locator.ADD_BUTTON).click()
        return ExpensesPage(self.driver)

    def the_expense_is_added(self, **kwargs):
        expense_table = self.find_elem(self.locator.EXPENSE_TABLE)
        first_row = expense_table.find_element(*self.locator.FIRST_ROW)
        report_date = first_row.find_element(*self.locator.DATE_COLUMN)
        mileage = first_row.find_element(*self.locator.MILEAGE_COLUMN)
        number_of_litters = first_row.find_element(*self.locator.LITERS_COLUMN)
        total_cost = first_row.find_element(*self.locator.TOTAL_COST_COLUMN)

        return (report_date.text == kwargs['report_date'] and
                # mileage.text == kwargs['mileage'] and
                str(kwargs['number_of_litters']) in number_of_litters.text and
                str(kwargs['total_cost']) in total_cost.text)

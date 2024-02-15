import time

from pages.base_page import BasePage
from utils.locators import GaragePageLocators
from selenium.webdriver.support.ui import Select


class GaragePage(BasePage):
    def __init__(self, driver):
        self.locator = GaragePageLocators
        super().__init__(driver=driver)

    def check_if_loaded(self):
        return True if self.find_elem(self.locator.HEADER).text == 'Garage' else False

    def click_add_button(self):
        self.find_elem(self.locator.ADD_CAR_BUTTON).click()
        return GaragePage(self.driver)

    def add_a_car(self, **kwargs):
        brand = Select(self.find_elem(self.locator.BRAND_SELECT))
        brand.select_by_visible_text(kwargs['brand'])
        time.sleep(1)

        model = Select(self.find_elem(self.locator.MODEL_SELECT))
        model.select_by_visible_text(kwargs['model'])

        self.find_elem(self.locator.MILEAGE_TEXTBOX).send_keys(kwargs['mileage'])
        self.find_elem(self.locator.ADD_BUTTON).click()
        return GaragePage(self.driver)

    def the_car_is_added(self, **kwargs):
        added_car = self.find_elem(self.locator.CAR_ADDED)
        brand = added_car.find_element(*self.locator.BRAND_ADDED)
        model = added_car.find_element(*self.locator.MODEL_ADDED)
        mileage = added_car.find_element(*self.locator.MILEAGE_ADDED)

        return (brand.get_attribute('alt') == kwargs['model'] and
                model.text == f"{kwargs['brand']} {kwargs['model']}" and
                mileage.get_attribute('value') == str(kwargs['mileage']))

    @property
    def garage_menu(self):
        return self.find_elem(self.locator.GARAGE_MENU)

    @property
    def fuel_expenses_menu(self):
        return self.find_elem(self.locator.FUEL_EXPENSE_MENU)


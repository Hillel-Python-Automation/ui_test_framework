from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.XPATH, "//a[@class='header_logo']")
    SIGNUP = (By.XPATH, "//button[text()='Sign up']")
    SIGNIN = (By.XPATH, "//button[contains(@class, 'header_signin')]")


class LoginPageLocators(object):
    EMAIL = (By.ID, "signinEmail")
    PASSWORD = (By.ID, "signinPassword")
    LOGIN = (By.XPATH, "//button[@class='btn btn-primary']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class SignupPageLocators(object):
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER = (By.XPATH, "//button[text()='Register']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class GaragePageLocators(object):
    HEADER = (By.XPATH, '//h1')
    ADD_CAR_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    BRAND_SELECT = (By.ID, "addCarBrand")
    MODEL_SELECT = (By.ID, "addCarModel")
    MILEAGE_TEXTBOX = (By.ID, "addCarMileage")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")

    CAR_ADDED = (By.XPATH, "(//div[@class='car jumbotron'])[1]")
    BRAND_ADDED = (By.XPATH, "//img[@class='car-logo_img']")
    MODEL_ADDED = (By.XPATH, "//p[@class='car_name h2']")
    MILEAGE_ADDED = (By.XPATH, "//input[contains(@class,'update-mileage-form_input')]")

    GARAGE_MENU = (By.XPATH, "//a[@href='/panel/garage' and contains(@class, 'btn-sidebar')]")
    FUEL_EXPENSE_MENU = (By.XPATH, "//a[@href='/panel/expenses' and contains(@class, 'btn-sidebar')]")


class ExpensesPageLocators(object):
    HEADER = (By.XPATH, '//h1')
    CAR_SELECTION = (By.ID, "carSelectDropdown")
    ADD_NEW_EXPENSE = (By.XPATH, "//button[text()='Add an expense']")
    VEHICLE = (By.ID, "addExpenseCar")
    REPORT_DATE = (By.ID, "addExpenseDate")
    MILEAGE = (By.ID, "addExpenseMileage")
    NUMBER_OF_LITTERS = (By.ID, "addExpenseLiters")
    TOTAL_COST = (By.ID, "addExpenseTotalCost")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    EXPENSE_TABLE = (By.XPATH, "//table[@class='table expenses_table']")
    FIRST_ROW = (By.XPATH, '(//tbody/tr)[1]')
    DATE_COLUMN = (By.XPATH, '(//td)[1]')
    MILEAGE_COLUMN = (By.XPATH, '(//td)[2]')
    LITERS_COLUMN = (By.XPATH, '(//td)[3]')
    TOTAL_COST_COLUMN = (By.XPATH, '(//td)[4]')

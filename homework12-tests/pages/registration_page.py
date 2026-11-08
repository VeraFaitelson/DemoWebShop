from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class RegistrationPage:
    REGISTER_LINK = (By.XPATH, "//a[text()='Register']")
    NAME_INPUT = (By.CSS_SELECTOR, "#FirstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#LastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#ConfirmPassword")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register-button")
    LOG_OUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    EMAIL_VALIDATION_ERROR = (By.CSS_SELECTOR, "span.field-validation-error, span[for='Email'], span[for='Password']")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTER_LINK).click()

    def fill_name_field(self, name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def fill_lastname_field(self, lastname):
        self.driver.find_element(*self.LASTNAME_INPUT).clear()
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(lastname)

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def fill_confirm_password_field(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)

    def click_on_registration_button(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION).click()

    def is_log_out_displayed(self):
        try:
            WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_element_located(self.LOG_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    def get_email_error_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_VALIDATION_ERROR)
        )
        return element.text

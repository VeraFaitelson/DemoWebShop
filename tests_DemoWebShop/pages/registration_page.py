from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    REGISTER_LINK = (By.XPATH, "//a[text()='Register']")
    NAME_INPUT = (By.CSS_SELECTOR, "#FirstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#LastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#ConfirmPassword")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register-button")
    LOG_OUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    EMAIL_VALIDATION_ERROR = (By.CSS_SELECTOR, "span.field-validation-error, span[for='Email'], span[for='Password']")
    ALREADY_EXIST_ERROR = (By.XPATH, "//div[@class='validation-summary-errors']//li")

    def open_registration_page(self):
        self.click(self.REGISTER_LINK)

    def fill_name_field(self, name):
        self.fill(self.NAME_INPUT, name)

    def fill_lastname_field(self, lastname):
        self.fill(self.LASTNAME_INPUT, lastname)

    def fill_email_field(self, email):
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def fill_confirm_password_field(self, confirm_password):
        self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def fill_registration_form(self, user):
        self.fill(self.NAME_INPUT, user.name)
        self.fill(self.LASTNAME_INPUT, user.lastname)
        self.fill(self.EMAIL_INPUT, user.email)
        self.fill(self.PASSWORD_INPUT, user.password)
        self.fill(self.CONFIRM_PASSWORD_INPUT, user.password)

    def click_on_registration_button(self):
        self.click(self.BUTTON_REGISTRATION)

    def is_log_out_displayed(self):
        return self.is_visible(self.LOG_OUT_BUTTON)

    def get_email_error_text(self):
        return self.get_text(self.EMAIL_VALIDATION_ERROR)

    def get_already_exist_error_text(self):
        return self.get_text(self.ALREADY_EXIST_ERROR)
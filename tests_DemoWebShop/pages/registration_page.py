"""Page Object for the Demo Web Shop Registration page"""

from selenium.webdriver.common.by import By

from models.user import User
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Encapsulates locators and actions for registering a new customer account"""

    # Locators
    REGISTER_LINK = (By.XPATH, "//a[text()='Register']")
    NAME_INPUT = (By.CSS_SELECTOR, "#FirstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#LastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#ConfirmPassword")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register-button")
    FIELD_VALIDATION_ERROR = (By.CSS_SELECTOR, "span.field-validation-error")
    ALREADY_EXIST_ERROR = (By.XPATH, "//div[@class='validation-summary-errors']//li")

    def open_registration_page(self):
        """Navigates to the Registration page"""
        self.click(self.REGISTER_LINK)
        self.find(self.NAME_INPUT)

    def fill_name_field(self, name: str):
        """Enters first name into the First Name field"""
        self.fill(self.NAME_INPUT, name)

    def fill_lastname_field(self, lastname: str):
        """Enters last name into the Last Name field"""
        self.fill(self.LASTNAME_INPUT, lastname)

    def fill_email_field(self, email: str):
        """Enters email into the Email field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password: str):
        """Enters password into the Password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def fill_confirm_password_field(self, confirm_password: str):
        """Enters password confirmation into the Confirm Password field"""
        self.fill(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def fill_registration_form(self, user: User):
        """Fills all required fields of the registration form using a User model"""
        self.fill_name_field(user.name)
        self.fill_lastname_field(user.lastname)
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)
        self.fill_confirm_password_field(user.password)

    def click_on_registration_button(self):
        """Clicks the 'Register' submit button"""
        self.click(self.BUTTON_REGISTRATION)

    def get_field_error_text(self) -> str:
        """Returns the inline validation error displayed under an invalid input field"""
        return self.get_text(self.FIELD_VALIDATION_ERROR)

    def get_already_exist_error_text(self) -> str:
        """Returns the error message when attempting to register with an existing email"""
        return self.get_text(self.ALREADY_EXIST_ERROR)

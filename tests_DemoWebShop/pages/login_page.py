"""Page Object for the Demo Web Shop Login page"""

from selenium.webdriver.common.by import By

from models.user import User
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates locators and actions for user authentication"""

    # Locators
    LOGIN_LINK = (By.XPATH, "//a[text()='Log in']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "input.button-1.login-button")
    ERROR_MAIN_MSG = (By.XPATH, "//span[contains(text(), 'Login was unsuccessful')]")
    EMAIL_VALIDATION_ERROR = (By.XPATH, "//span[@for='Email']")
    ERROR_DETAIL_MSG = (By.XPATH, "//div[@class='validation-summary-errors']//li")

    def open_login_page(self):
        """Navigates to the Login page"""
        self.click(self.LOGIN_LINK)
        self.find(self.EMAIL_INPUT)

    def fill_email_field(self, email: str):
        """Enters email into the Email field"""
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password: str):
        """Enters password into the Password field"""
        self.fill(self.PASSWORD_INPUT, password)

    def fill_login_form(self, user: User):
        """Fills both email and password fields using a User model"""
        self.fill_email_field(user.email)
        self.fill_password_field(user.password)

    def click_on_login_button(self):
        """Clicks the 'Log in' submit button"""
        self.click(self.BUTTON_LOGIN)

    def get_main_error_text(self) -> str:
        """Returns the summary error header when login fails"""
        return self.get_text(self.ERROR_MAIN_MSG)

    def get_credentials_error_text(self) -> str:
        """Returns the detailed validation summary error message"""
        return self.get_text(self.ERROR_DETAIL_MSG)

    def get_email_error_text(self) -> str:
        """Returns the inline validation error displayed under the Email field"""
        return self.get_text(self.EMAIL_VALIDATION_ERROR)

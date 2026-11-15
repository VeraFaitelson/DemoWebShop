from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[text()='Log in']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "input.button-1.login-button")
    LOG_OUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    ERROR_MAIN_MSG = (By.XPATH, "//span[contains(text(), 'Login was unsuccessful')]")
    EMAIL_VALIDATION_ERROR = (By.XPATH, "//span[@for='Email']")
    ERROR_DETAIL_MSG = (By.XPATH, "//div[@class='validation-summary-errors']//li")

    def open_login_page(self):
        self.click(self.LOGIN_LINK)

    def fill_email_field(self,email):
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self,password):
        self.fill(self.PASSWORD_INPUT, password)

    def fill_login_form(self, user):
        self.fill(self.EMAIL_INPUT, user.email)
        self.fill(self.PASSWORD_INPUT, user.password)

    def click_on_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def is_log_out_displayed(self):
        return self.is_visible(self.LOG_OUT_BUTTON)

    def get_main_error_text(self):
        return self.get_text(self.ERROR_MAIN_MSG)

    def get_credentials_error_text(self):
        return self.get_text(self.ERROR_DETAIL_MSG)

    def get_email_error_text(self):
        return self.get_text(self.EMAIL_VALIDATION_ERROR)
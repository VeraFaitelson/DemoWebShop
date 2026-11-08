from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    LOGIN_LINK = (By.XPATH, "//a[text()='Log in']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "input.button-1.login-button")
    LOG_OUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    ERROR_MAIN_MSG = (By.XPATH, "//span[contains(text(), 'Login was unsuccessful')]")
    EMAIL_VALIDATION_ERROR = (By.XPATH, "//span[@for='Email']")
    ERROR_DETAIL_MSG = (By.XPATH, "//div[@class='validation-summary-errors']//li")

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def fill_email_field(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()

    def is_log_out_displayed(self):
        try:
            WebDriverWait(self.driver, timeout=10).until(
                expected_conditions.visibility_of_element_located(self.LOG_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    def get_main_error_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MAIN_MSG)
        )
        return element.text

    def get_credentials_error_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_DETAIL_MSG)
        )
        return element.text

    def get_email_error_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_VALIDATION_ERROR)
        )
        return element.text
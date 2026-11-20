"""Base Page Object containing shared Selenium helper methods"""

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class for all Page Objects. Wraps common WebDriver interactions"""

    # Common header locator shared across pages
    LOG_OUT_BUTTON = (By.XPATH, "//a[text()='Log out']")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """Stores WebDriver instance and initializes a reusable explicit wait"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Waits until the element is visible on the page and returns it"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Waits until the element is clickable and performs a click"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value: str):
        """Clears an input field and enters the given text"""
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator) -> str:
        """Waits until the element is visible and returns its text"""
        return self.find(locator).text

    def is_visible(self, locator, timeout: int = 5) -> bool:
        """Safely checks if an element becomes visible within timeout without raising an exception"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_log_out_displayed(self) -> bool:
        """Checks if the 'Log out' link is visible in the top navigation bar"""
        return self.is_visible(self.LOG_OUT_BUTTON)

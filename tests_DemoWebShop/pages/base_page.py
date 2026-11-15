from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element(*locator)

    def click(self,locator):
        self.find(locator).click()

    def fill(self,locator,value):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

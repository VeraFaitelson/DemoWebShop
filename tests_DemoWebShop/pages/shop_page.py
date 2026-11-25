"""Page Object for the Demo Web Shop catalog and shopping cart"""
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ShopPage(BasePage):
    """Encapsulates actions for selecting a product, adding to cart, and proceeding to checkout"""

    # Locators
    LAPTOP_ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//a[text()='14.1-inch Laptop']/ancestor::div[@class='details']//input[@value='Add to cart']",
    )
    NOTIFICATION_BAR = (By.ID, "bar-notification")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "li#topcartlink a.ico-cart")
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    NOTIFICATION_CART_LINK = (By.CSS_SELECTOR, "#bar-notification a[href='/cart']")

    def add_laptop_to_cart(self):
        """Adds '14.1-inch Laptop' to the shopping cart and waits for confirmation"""
        logger.info("Adding '14.1-inch Laptop' to shopping cart")
        self.click(self.LAPTOP_ADD_TO_CART_BUTTON)
        notification_text = self.find(self.NOTIFICATION_BAR).text
        logger.debug("Notification bar displayed: '%s'", notification_text)

    def open_shopping_cart(self):
        """Clicks the 'shopping cart' link inside the notification bar to open the cart"""
        logger.info("Opening shopping cart from notification bar")
        self.click(self.NOTIFICATION_CART_LINK)
        self.wait.until(EC.url_contains("/cart"))

    def proceed_to_checkout(self):
        """Agrees to the terms of service and clicks the Checkout button"""
        logger.info("Accepting terms of service and proceeding to checkout")
        self.click(self.TERMS_OF_SERVICE_CHECKBOX)
        self.click(self.CHECKOUT_BUTTON)
        self.wait.until(EC.url_contains("/onepagecheckout"))

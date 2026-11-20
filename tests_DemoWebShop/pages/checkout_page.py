"""Page Object for the Demo Web Shop One-Page Checkout process"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Encapsulates locators and step-by-step actions for completing an order"""

    # Billing Address Form Fields (shown only on the first order if no address is saved)
    COUNTRY_SELECT = (By.ID, "BillingNewAddress_CountryId")
    CITY_INPUT = (By.ID, "BillingNewAddress_City")
    ADDRESS1_INPUT = (By.ID, "BillingNewAddress_Address1")
    ZIP_INPUT = (By.ID, "BillingNewAddress_ZipPostalCode")
    PHONE_INPUT = (By.ID, "BillingNewAddress_PhoneNumber")

    # Step-by-step 'Continue' & 'Confirm' Buttons
    BILLING_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#billing-buttons-container input.new-address-next-step-button")
    SHIPPING_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#shipping-buttons-container input.new-address-next-step-button")
    SHIPPING_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#shipping-method-buttons-container input.shipping-method-next-step-button")
    PAYMENT_METHOD_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#payment-method-buttons-container input.payment-method-next-step-button")
    PAYMENT_INFO_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#payment-info-buttons-container input.payment-info-next-step-button")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "#confirm-order-buttons-container input.confirm-order-next-step-button")

    # Order Completion Message
    ORDER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.section.order-completed div.title strong")

    def complete_billing_address(self):
        """Fills billing address if required (first order) and proceeds to the next step"""
        if self.is_visible(self.COUNTRY_SELECT, timeout=2):
            Select(self.find(self.COUNTRY_SELECT)).select_by_visible_text("Israel")
            self.fill(self.CITY_INPUT, "Haifa")
            self.fill(self.ADDRESS1_INPUT, "Herzl Street 10")
            self.fill(self.ZIP_INPUT, "3300000")
            self.fill(self.PHONE_INPUT, "0501234567")
        self.click(self.BILLING_CONTINUE_BUTTON)

    def complete_shipping_address(self):
        """Confirms the default shipping address and proceeds"""
        self.click(self.SHIPPING_CONTINUE_BUTTON)

    def complete_shipping_method(self):
        """Confirms the default shipping method and proceeds"""
        self.click(self.SHIPPING_METHOD_CONTINUE_BUTTON)

    def complete_payment_method(self):
        """Confirms the default payment method (Cash On Delivery) and proceeds"""
        self.click(self.PAYMENT_METHOD_CONTINUE_BUTTON)

    def complete_payment_info(self):
        """Confirms the payment information step and proceeds"""
        self.click(self.PAYMENT_INFO_CONTINUE_BUTTON)

    def confirm_order(self):
        """Clicks the final 'Confirm' button to place the order"""
        self.click(self.CONFIRM_ORDER_BUTTON)

    def complete_checkout_steps(self):
        """Executes all checkout steps sequentially from billing address to order confirmation"""
        self.complete_billing_address()
        self.complete_shipping_address()
        self.complete_shipping_method()
        self.complete_payment_method()
        self.complete_payment_info()
        self.confirm_order()

    def get_order_success_message(self) -> str:
        """Returns the confirmation text displayed after a successful order"""
        return self.get_text(self.ORDER_SUCCESS_MESSAGE)

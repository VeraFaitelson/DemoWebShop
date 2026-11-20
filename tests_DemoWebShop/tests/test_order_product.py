"""End-to-end test for purchasing a product in Demo Web Shop"""

from pages.checkout_page import CheckoutPage
from pages.shop_page import ShopPage


def test_order_single_product_success(authenticated):
    """Verify full purchase flow: add a laptop to cart, complete checkout, and verify order confirmation"""
    shop_page = ShopPage(authenticated)
    checkout_page = CheckoutPage(authenticated)

    shop_page.add_laptop_to_cart()
    shop_page.open_shopping_cart()
    shop_page.proceed_to_checkout()

    checkout_page.complete_checkout_steps()

    assert checkout_page.get_order_success_message() == "Your order has been successfully processed!"

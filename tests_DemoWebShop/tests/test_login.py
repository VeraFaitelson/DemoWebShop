"""Tests for Demo Web Shop user login functionality (positive and negative scenarios)"""

from conftest import DEFAULT_USER
from models.user import User
from pages.login_page import LoginPage
from utils.data_generator import generate_unique_email

# Test data constants for negative scenarios
INVALID_EMAIL = "testQAgmailcom"
INVALID_PASSWORD = "test"


def test_valid_login_success(driver):
    """Verify successful login with valid credentials"""
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    assert login_page.is_log_out_displayed()


def test_login_with_invalid_email_and_valid_password(driver):
    """Verify inline validation error when email format is invalid"""
    login_page = LoginPage(driver)
    user = User(email=INVALID_EMAIL, password=DEFAULT_USER.password)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    assert login_page.get_email_error_text() == "Please enter a valid email address."


def test_login_with_valid_email_and_invalid_password(driver):
    """Verify error summary appears when password is incorrect"""
    login_page = LoginPage(driver)
    user = User(email=DEFAULT_USER.email, password=INVALID_PASSWORD)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    assert "Login was unsuccessful" in login_page.get_main_error_text()
    assert login_page.get_credentials_error_text() == "The credentials provided are incorrect"


def test_login_with_unregistered_email(driver):
    """Verify error summary appears when attempting to log in with a non-existent email"""
    login_page = LoginPage(driver)
    user = User(email=generate_unique_email(), password=DEFAULT_USER.password)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    assert "Login was unsuccessful" in login_page.get_main_error_text()
    assert login_page.get_credentials_error_text() == "No customer account found"

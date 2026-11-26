"""Tests for Demo Web Shop user login functionality (positive and negative scenarios)"""
import pytest

from conftest import DEFAULT_USER
from models.user import User
from pages.login_page import LoginPage
from utils.data_generator import generate_unique_email

def test_valid_login_success(driver):
    """Verify successful login with valid credentials"""
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    assert login_page.is_log_out_displayed()


@pytest.mark.parametrize(
    "invalid_email",
    [
        "testQAgmailcom",      # without @
        "testQA@",             # without domain
        "@gmail.com",          # No username
        "test QA@gmail.com",   # With a space inside
    ],
)
def test_login_with_invalid_email_and_valid_password(driver, invalid_email):
    """Verify inline validation error when email format is invalid"""
    login_page = LoginPage(driver)
    user = User(email=invalid_email, password=DEFAULT_USER.password)

    login_page.open_login_page()
    login_page.fill_login_form(user)
    login_page.click_on_login_button()

    assert login_page.get_email_error_text() == "Please enter a valid email address."

@pytest.mark.parametrize(
    "invalid_password",
    [
        "test",              # short password
        "testpass!12345",    # Incorrect case (no capital letters)
        "TestPass!123456",   # Extra character at the end
    ],
)
def test_login_with_valid_email_and_invalid_password(driver, invalid_password):
    """Verify error summary appears when password is incorrect"""
    login_page = LoginPage(driver)
    user = User(email=DEFAULT_USER.email, password=invalid_password)

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

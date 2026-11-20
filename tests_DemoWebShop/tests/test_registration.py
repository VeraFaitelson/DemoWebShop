"""Tests for Demo Web Shop user registration functionality (positive and negative scenarios)"""

from conftest import DEFAULT_USER
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_user

# Test data constants for negative scenarios
INVALID_EMAIL = "testQAgmailcom"
INVALID_PASSWORD = "test"


def test_valid_registration_success(driver):
    """Verify successful registration with valid user data"""
    registration_page = RegistrationPage(driver)
    user = generate_user()

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_registration_button()

    assert registration_page.is_log_out_displayed()


def test_registration_with_invalid_email_and_valid_password(driver):
    """Verify inline validation error when email format is invalid"""
    registration_page = RegistrationPage(driver)
    user = generate_user()
    user.email = INVALID_EMAIL

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_registration_button()

    assert registration_page.get_field_error_text() == "Wrong email"


def test_registration_with_valid_email_and_invalid_password(driver):
    """Verify inline validation error when password is shorter than 6 characters"""
    registration_page = RegistrationPage(driver)
    user = generate_user()
    user.password = INVALID_PASSWORD

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    registration_page.click_on_registration_button()

    assert "The password should have at least 6 characters" in registration_page.get_field_error_text()


def test_registration_with_already_exist_email(driver):
    """Verify error message appears when registering with an already registered email"""
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(DEFAULT_USER)
    registration_page.click_on_registration_button()

    assert registration_page.get_already_exist_error_text() == "The specified email already exists"

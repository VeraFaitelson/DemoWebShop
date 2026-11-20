"""Pytest fixtures for Demo Web Shop browser setup and user authentication"""

import pytest
from selenium import webdriver

from models.user import User
from pages.login_page import LoginPage

BASE_URL = "https://demowebshop.tricentis.com/"

DEFAULT_USER = User(
    name="Test",
    lastname="User",
    email="qa_shop_user@gmail.com",
    password="TestPass!12345",
)


@pytest.fixture
def driver():
    """Initializes Chrome WebDriver before a test and closes it afterward"""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def authenticated(driver):
    """Logs in as the default customer and returns the authenticated driver"""
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    assert login_page.is_log_out_displayed(), "Failed to log in inside 'authenticated' fixture"

    return driver

"""Pytest fixtures for Demo Web Shop browser setup and user authentication"""

import logging
import pytest
from selenium import webdriver

from models.user import User
from pages.login_page import LoginPage
from utils.logger_config import configure_logger

BASE_URL = "https://demowebshop.tricentis.com/"

DEFAULT_USER = User(
    name="Test",
    lastname="User",
    email="qa_shop_user@gmail.com",
    password="TestPass!12345",
)

configure_logger()
logger = logging.getLogger(__name__)


@pytest.fixture
def driver(request):
    """Initializes Chrome WebDriver before a test and closes it afterward"""
    logger.info("=== Start test: %s ===", request.node.name)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(BASE_URL)

    yield browser

    logger.info("=== End test: %s ===\n", request.node.name)
    browser.quit()


@pytest.fixture
def authenticated(driver):
    """Logs in as the default customer and returns the authenticated driver"""
    logger.debug("Running 'authenticated' fixture setup")
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_login_form(DEFAULT_USER)
    login_page.click_on_login_button()

    assert login_page.is_log_out_displayed(), "Failed to log in inside 'authenticated' fixture"

    return driver

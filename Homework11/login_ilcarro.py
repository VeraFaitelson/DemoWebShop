import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://icarro-v1.netlify.app/login"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()


def test_login_success(driver):
    driver.implicitly_wait(5)  # Ждём загрузки элементов

    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("testVeraf12345@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Test123456789!")

    driver.find_element(By.XPATH, "//button[contains(text(), 'Y') and contains(text(), 'alla')]").click()

    import time
    time.sleep(2)

    login_success = driver.find_elements(By.XPATH,
                                                "//*[contains(text(), 'success') or contains(text(), 'Success') or contains(text(), 'logged')]")

    if len( login_success) > 0:
        print("\nLogin successful")
        assert True
    else:
        print("\nError Login")
        print("Text:", driver.find_element(By.TAG_NAME, "body").text[:200])
        assert False
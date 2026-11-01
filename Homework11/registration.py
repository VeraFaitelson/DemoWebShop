import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demowebshop.tricentis.com/register"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()

def test_login_success(driver):
   driver.find_element(By.XPATH,"//input[@id='gender-female']").click()
   driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Vera")
   driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("F")

   driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("testVeraf@gmail.com")
   driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("VX8jku@4wxTNSv")
   driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("VX8jku@4wxTNSv")
   driver.find_element(By.XPATH, "//input[@id='register-button']").click()

   registration_success = driver.find_elements(By.XPATH, "//div[contains(text(), 'Your registration completed')]")
   if len(registration_success) > 0 and registration_success[0].text.strip() == "Your registration completed":
       print("Registration successful")
   print("Error Registration")


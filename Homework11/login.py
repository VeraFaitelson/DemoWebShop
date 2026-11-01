import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demowebshop.tricentis.com/login"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()

def test_login_success(driver):
   driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("testVeraf@gmail.com")
   driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("VX8jku@4wxTNSv")
   driver.find_element(By.XPATH, "//input[@value='Log in']").click()

   login_success = driver.find_elements(By.XPATH, "//a[text()='Log out']")
   if len(login_success) > 0 and login_success[0].text.strip() == "Log out":
       print("login successful")
   print("Error login")


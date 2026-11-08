import time
from pages.registration_page import RegistrationPage

VALID_EMAIL = f"testveraf{int(time.time())}@gmail.com"
VALID_PASSWORD = "Vera!123456789@"
VALID_NAME = "Vera"
VALID_LAST_NAME = "V"
INVALID_EMAIL1 = "testvera@gmail"
INVALID_EMAIL2 = "testveragmail.com"
INVALID_EMAIL3 = ""
INVALID_PASSWORD1 = "123"
INVALID_PASSWORD2 = "1@$!"
INVALID_PASSWORD3 = ""

# #Сценарий 1: Успешная регистрация с корректными данными
# Создание новой учетной записи пользователя при вводе валидных параметров.
# • Тест 1: test_valid_registration_success
# • Шаги: Ввести корректное Имя (First Name), ввести корректную Фамилию (Last Name),
#   Ввести корректный Email (Email), ввести корректный Пароль (Password),
#   подтвердить пароль идентичным значением в поле Подтверждение пароля (Confirm Password)
#   и нажать кнопку Регистрация (Register).
# • Ожидаемый результат: Пользователь успешно зарегистрирован в системе,
#   на странице отображается кнопка Выйти (Log out).
def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.fill_confirm_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()
    assert registration_page.is_log_out_displayed()


# Сценарий 2: Неудачная регистрация из-за некорректного формата Email
# Проверка клиентской валидации текстовых полей ввода на этапе заполнения формы.
# • Тесты:
# 	• Тест 2.1 - test_registration_with_wrong_email1 — ввод email без доменной части (testvera@gmail).
# 	• Тест 2.2 - test_registration_with_wrong_email2 — ввод email без знака @ (testveragmail.com).
# • Шаги: Ввести Имя (First Name), Фамилию (Last Name), Пароль (Password) и Подтверждение пароля (Confirm Password).
#   Ввести текст с нарушением формата в поле Email (Email) и нажать кнопку Регистрация (Register).
# • Ожидаемый результат: Форма не отправляется на сервер.
#   Прямо под полем ввода Email (Email) мгновенно появляется сообщение об ошибке формата: «Wrong email»
def test_registration_with_wrong_email1(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(INVALID_EMAIL1)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.fill_confirm_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()
    email_error = registration_page.get_email_error_text()
    expected_error = "Wrong email"
    assert email_error == expected_error

def test_registration_with_wrong_email2(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(INVALID_EMAIL2)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.fill_confirm_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()
    email_error = registration_page.get_email_error_text()
    expected_error = "Wrong email"
    assert email_error == expected_error


# Сценарий 3: Неудачная регистрация из-за пустого поля EMAIL
# Проверка обязательности заполнения полей формы на стороне клиента.
# • Тест 3: test_registration_with_wrong_email3
# 	• Шаги: Ввести валидные Имя (First Name), Фамилию (Last Name), Пароль (Password)
# 	и Подтверждение пароля (Confirm Password).
#     Оставить поле ввода Email (Email) абсолютно пустым (INVALID_EMAIL3 = "")
#     и нажать кнопку Регистрация (Register).
# 	• Ожидаемый результат: Форма блокируется. Под незаполненным полем Email (Email)
#     появляется точечное сообщение об ошибке: «Email is required.»
def test_registration_with_wrong_email3(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(INVALID_EMAIL3)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.fill_confirm_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()
    email_error = registration_page.get_email_error_text()
    assert email_error == "Email is required."


# Сценарий 4: Неудачная регистрация из-за неверных данных поля PASSWORD
# Проверка вывода сообщений об ошибках при отправке некорректных параметров пароля.
# • Тест 4.1: test_registration_with_wrong_password1 — ввод цифрового пароля, не соответствующего
# правилам безопасности сложности.
# • Тест 4.2: test_registration_with_wrong_password2 — ввод слишком короткого пароля из спецсимволов.
# • Шаги: Ввести валидные Имя (First Name), Фамилию (Last Name) и Email (Email).
#   В поля Пароль (Password) и Подтверждение пароля (Confirm Password) ввести
#   некорректное значение и нажать кнопку Регистрация (Register).
# • Ожидаемый результат: Под полем ввода Пароль (Password) отображается сообщение
# об ошибке валидации формата: «The password should have at least 6 characters.»
def test_registration_with_wrong_password1(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(f"test{int(time.time())}@gmail.com")
    registration_page.fill_password_field(INVALID_PASSWORD1)
    registration_page.fill_confirm_password_field(INVALID_PASSWORD1)
    registration_page.click_on_registration_button()
    password_error = registration_page.get_email_error_text()
    assert password_error == "The password should have at least 6 characters."


def test_registration_with_wrong_password2(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(f"test{int(time.time())}@gmail.com")
    registration_page.fill_password_field(INVALID_PASSWORD2)
    registration_page.fill_confirm_password_field(INVALID_PASSWORD2)
    registration_page.click_on_registration_button()
    password_error = registration_page.get_email_error_text()
    assert password_error == "The password should have at least 6 characters."


# Сценарий 5: Неудачная регистрация из-за пустого поля PASSWORD
# Проверка обязательности заполнения поля секретного ключа.
# • Тест 5: test_registration_with_wrong_password3
# • Шаги: Ввести валидные Имя (First Name), Фамилию (Last Name) и Email (Email).
#   Оставить поля Пароль (Password) и Подтверждение пароля (Confirm Password)
#   пустыми (INVALID_PASSWORD3 = "") и нажать кнопку Регистрация (Register).
# • Ожидаемый результат: Форма не отправляется. Под незаполненными полями
# появляется сообщение «Password is required.».
def test_registration_with_wrong_password3(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_name_field(VALID_NAME)
    registration_page.fill_lastname_field(VALID_LAST_NAME)
    registration_page.fill_email_field(f"test{int(time.time())}@gmail.com")
    registration_page.fill_password_field(INVALID_PASSWORD3)
    registration_page.fill_confirm_password_field(INVALID_PASSWORD3)
    registration_page.click_on_registration_button()
    password_error = registration_page.get_email_error_text()
    assert "Password is required." in password_error

from pages.login_page import LoginPage

VALID_EMAIL = "testvera@gmail.com"
VALID_PASSWORD = "123456789@$!"
INVALID_EMAIL1 = "testvera@gmail"
INVALID_EMAIL2 = "testveragmail.com"
INVALID_EMAIL3 = ""
INVALID_PASSWORD1 = "123456789"
INVALID_PASSWORD2 = "1@$!"
INVALID_PASSWORD3 = ""


# #Сценарий 1: Успешная авторизация с корректными данными
# Вход в систему с валидными учетными данными пользователя.
# • Тест 1: test_valid_login_success
# • Шаги: Ввести корректный Email (VALID_EMAIL),
#   корректный пароль (VALID_PASSWORD) и нажать кнопку входа.
# • Ожидаемый результат: Пользователь успешно авторизован,
#   на странице отображается кнопка «Log out».
def test_valid_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    assert login_page.is_log_out_displayed()


# Сценарий 2: Неудачная авторизация из-за некорректного формата Email
# Проверка валидации полей ввода на этапе заполнения формы.
# • Тесты:
# 	• Тест 2.1 - test_with_wrong_email1 — ввод email без доменной части
# 	(testvera@gmail).
# 	• Тест 2.2 - test_with_wrong_email2 — ввод email без знака @
# 	(testveragmail.com).
# • Шаги: Ввести текст с нарушением формата в поле Email
# и нажать кнопку входа.
# • Ожидаемый результат: Форма не отправляется.
# Прямо под полем ввода Email мгновенно появляется
# сообщение об оишбке: «Please enter a valid email address.»

def test_with_wrong_email1(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(INVALID_EMAIL1)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    email_error = login_page.get_email_error_text()
    expected_error = "Please enter a valid email address."
    assert email_error == expected_error

def test_with_wrong_email2(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(INVALID_EMAIL2)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    email_error = login_page.get_email_error_text()
    expected_error = "Please enter a valid email address."
    assert email_error == expected_error



# Сценарий 3: Неудачная авторизация из-за пустого поля EMAIL
# Проверка серверных ошибок при отправке незаполненных данных.
# • Тест 3: Пустое поле Email (test_with_wrong_email3)
# 	• Шаги: Оставить поле ввода Email абсолютно пустым
# 	(INVALID_EMAIL3 = ""), ввести валидный пароль и нажать кнопку входа.
# 	• Ожидаемый результат: На странице появляется общая ошибка
# 	авторизации: «Login was unsuccessful.
# 	Please correct the errors and try again.»,
# 	а ниже отображается текст «No customer account found».

def test_with_wrong_email3(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(INVALID_EMAIL3)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()
    main_error = login_page.get_main_error_text()
    expected_main_error = "Login was unsuccessful. Please correct the errors and try again."
    assert main_error == expected_main_error
    credentials_error = login_page.get_credentials_error_text()
    expected_cred_error = "No customer account found"
    assert credentials_error == expected_cred_error

# Сценарий 4:
# Неудачная авторизация из-за неверных данных поля PASSWORD
# Проверка серверных ошибок при отправке некорректных
# или незаполненных данных
# # Проверка серверных ошибок при отправке незаполненных данных.
# • Тест 4.1: Первый вариант неверного пароля (test_with_wrong_password1)
# 	• Шаги: Ввести валидный Email, ввести некорректную комбинацию цифр
# 	в поле пароля (INVALID_PASSWORD1 = "123456789") и
# 	нажать кнопку входа.
# 	• Ожидаемый результат: Вход не выполняется,
# 	выводятся сообщения: «Login was unsuccessful...» и
# 	«The credentials provided are incorrect».
# • Тест 4.2: Второй вариант неверного пароля (test_with_wrong_password2)
# 	• Шаги: Ввести валидный Email, ввести некорректную комбинацию
# 	спецсимволов в поле пароля (INVALID_PASSWORD2 = "1@$!")
# 	и нажать кнопку входа.
# 	• Ожидаемый результат: Вход не выполняется,
# 	система выводит аналогичные ошибки: «Login was unsuccessful...»
# 	и «The credentials provided are incorrect».
#

def test_with_wrong_password1(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(INVALID_PASSWORD1)
    login_page.click_on_login_button()
    main_error = login_page.get_main_error_text()
    expected_main_error = "Login was unsuccessful. Please correct the errors and try again."
    assert main_error == expected_main_error
    credentials_error = login_page.get_credentials_error_text()
    expected_cred_error = "The credentials provided are incorrect"
    assert credentials_error == expected_cred_error

def test_with_wrong_password2(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(INVALID_PASSWORD2)
    login_page.click_on_login_button()
    main_error = login_page.get_main_error_text()
    expected_main_error = "Login was unsuccessful. Please correct the errors and try again."
    assert main_error == expected_main_error
    credentials_error = login_page.get_credentials_error_text()
    expected_cred_error = "The credentials provided are incorrect"
    assert credentials_error == expected_cred_error

# Сценарий 5: Неудачная авторизация из-за пустого поля PASSWORD
# Проверка серверных ошибок при отправке незаполненных данных.
# •Тест 5: пустое поле Пароль (test_with_wrong_password3)
# • Шаги: Ввести валидный Email,
# оставить поле ввода пароля абсолютно пустым
# (INVALID_PASSWORD3 = "") и нажать кнопку входа.
# • Ожидаемый результат: На странице появляется общая ошибка
# авторизации: «Login was unsuccessful.
# Please correct the errors and try again.»,
# а ниже отображается текст «The credentials provided are incorrect».

def test_with_wrong_password3(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(INVALID_PASSWORD3)
    login_page.click_on_login_button()
    main_error = login_page.get_main_error_text()
    expected_main_error = "Login was unsuccessful. Please correct the errors and try again."
    assert main_error == expected_main_error
    credentials_error = login_page.get_credentials_error_text()
    expected_cred_error = "The credentials provided are incorrect"
    assert credentials_error == expected_cred_error
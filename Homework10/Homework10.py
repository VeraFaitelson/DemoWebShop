from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://demowebshop.tricentis.com/")

    # Поиск облоков DIV
    # Находит все элементы <div> на странице (возвращает список)
    div1 = driver.find_elements(By.TAG_NAME, "div")
    # Находит самый первый <div> на странице через CSS-селектор тега
    div2 = driver.find_element(By.CSS_SELECTOR, "div")
    # Находит самый первый <div> на странице через XPath (двойной слэш ищет в любом месте документа)
    div3 = driver.find_element(By.XPATH, "//div")

    # Поиск полей ввода INPUT
    input1 = driver.find_element(By.TAG_NAME, "input")
    input2 = driver.find_element(By.CSS_SELECTOR, "input")
    input3 = driver.find_element(By.XPATH, "//input")

    # Поиск всех ссылок (тег "a")
    a_list1 = driver.find_elements(By.TAG_NAME, "a")
    a_list2 = driver.find_elements(By.CSS_SELECTOR, "a")
    a_list3 = driver.find_elements(By.XPATH, "//a")

    # Поиск по одному классу "inactive")
    # Находит элементы, у которых в атрибуте class написано "inactive"
    inactive1 = driver.find_elements(By.CLASS_NAME, "inactive")
    # В CSS перед именем класса ОБЯЗАТЕЛЬНО ставится точка (".")
    inactive2 = driver.find_elements(By.CSS_SELECTOR, ".inactive")
    # В XPath класс проверяется как обычный атрибут через знак "@"
    inactive3 = driver.find_elements(By.XPATH, "//*[@class='inactive']")

    # Поиск по составным классам (через пробел в HTML)
    # Кнопка поиска - input class="button-1 search-box-button"
    # В CSS-селекторах несколько классов одного элемента соединяются точками без пробелов:
    button1 = driver.find_elements(By.CSS_SELECTOR, ".button-1.search-box-button")
    button2 = driver.find_elements(By.CSS_SELECTOR, ".button-1.search-box-button")
    # В XPath для поиска элемента с несколькими классами используем функцию contains():
    button3 = driver.find_elements(By.XPATH,"//*[contains(@class, 'button-1') and contains(@class, 'search-box-button')]")

    # Поиск по ID элемента
    # Прямой поиск по названию ID
    id_1 = driver.find_elements(By.ID, "goog-gt-tt")
    # В CSS-селекторах поиск по ID со знака "#"
    id_2 = driver.find_elements(By.CSS_SELECTOR, "#goog-gt-tt")
    # В XPath ID проверяется как стандартный атрибут [@id='значение']
    id_3 = driver.find_elements(By.XPATH, "//*[@id='goog-gt-tt']")

    # Поиск по конкретному атрибуту (Поле ввода Email для рассылки)
    # input id="newsletter-email" name="NewsletterEmail"
    # Ищем тег input, у которого атрибут name равен "NewsletterEmail" (в CSS квадратные скобки)
    news_letter1 = driver.find_element(By.CSS_SELECTOR, "input[name='NewsletterEmail']")
    # В XPath перед именем атрибута "name" обязательно ставится "@"
    news_letter2 = driver.find_element(By.XPATH, "//input[@name='NewsletterEmail']")

    # Поиск кнопки по тексту или значению (кнопка голосования "Vote")
    # input type="button" value="Vote" class="button-1 vote-poll-button"
    # Тег input, "Vote" лежит в атрибуте value, ищем совпадение по @value через XPath
    vote_button = driver.find_elements(By.XPATH, "//input[@value='Vote']")
    # Находит элементы, у которых в атрибуте value содержится подстрока 'Vote'
    vote_button1 = driver.find_elements(By.XPATH, "//*[contains(@value, 'Vote')]")

    # Поиск по частичному совпадению атрибута
    # "^=" в CSS: атрибут начинается на
    css_input1 = driver.find_element(By.CSS_SELECTOR, "input[name^='News']")
    # В XPath для этого используется функция starts-with()
    xpath_input1 = driver.find_element(By.XPATH, "//input[starts-with(@name, 'News')]")

    # "$=" в CSS: атрибут заканчивается на
    css_input2 = driver.find_element(By.CSS_SELECTOR, "input[name$='Email']")
    # В XPath нет ends-with, используем универсальный contains() (проверяет, есть ли эта строка внутри)
    xpath_input2 = driver.find_element(By.XPATH, "//input[contains(@name, 'Email')]")

    # "*=" в CSS: подстрока содержится внутри значения (ищем 'letter' внутри name)
    css_input3 = driver.find_element(By.CSS_SELECTOR, "input[name*='letter']")
    # В XPath для поиска подстроки - contains()
    xpath_input3 = driver.find_element(By.XPATH, "//input[contains(@name, 'letter')]")

finally:

    driver.quit()
    # закрывает все окна и полностью завершает работу сессии WebDriver
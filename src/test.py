import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://accounts.google.com")   #Открытие браузера нужной страницы


def check_email(email):   # Создаем фенкции
    email_field = driver.find_element_by_name("identifier") # Выбераем поле в которое будим вводить текст
    email_field.clear()
    email_field.send_keys(email) #Вводим текст

    next_button = driver.find_element_by_id("identifierNext")  # Выбираем кнопку (По id) по которой должны кликнуть
    next_button.click() # команда нажатия кнопки

    time.sleep(1) # устанавливаем задержку

    assert "Введіть дійсні електронну адресу або номер телефону" or "Не вдалося знайти ваш обліковий запис Google" in driver.page_source # Проверка что на тестируемой странице есть текст "Введите адрес электронной почты или номер телефона"

check_email("!@#$%^&&*+")
check_email("ajddg@@dkg,")
check_email("bgmgdf@46784834")
check_email("email#domain")
check_email("ksghkjgh@dgf..com")

driver.quit() # Закрытие тестируемой страницы
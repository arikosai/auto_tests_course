from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'sample.txt')           # добавляем к этому пути имя файла 

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys('Alex')
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys('Nazarov')
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys('alnaz@ya.ru')

    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
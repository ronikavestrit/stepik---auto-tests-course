from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = (browser.find_element_by_id("num1")).text
    y = (browser.find_element_by_id("num2")).text
    sum = str(int(x)+int(y))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(sum)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
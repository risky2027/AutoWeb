import os.path
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login, check_element_present
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def test_about_me():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/about'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        name = browser.find_element(By.NAME, "name")
        name.send_keys("Андрей")
        surname = browser.find_element(By.NAME, "surname")
        surname.send_keys("Павлов")
        specialist = browser.find_element(By.ID, "age1").get_attribute("checked")
        assert specialist, "По умолчанию выбрано значние Не ручной тестировщик"
        browser.find_element(By.ID, "age2").click()
        browser.find_element(By.ID, "lang1").click()
        browser.find_element(By.ID, "lang3").click()
        element = browser.find_element(By.ID, "lvl")
        select = Select(element)
        select.select_by_visible_text("Senior")
        surname.send_keys(Keys.ENTER)
        by, value = By.CLASS_NAME, "is-success"
        assert browser.find_element(by, value).text == "Успех.", \
            "Сообщение об отправке формы не успешно"


def test_upload_file():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/upload_file'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        element_for_upload = browser.find_element(By.NAME, "file")
        element_for_upload.send_keys(os.path.join(os.getcwd(), 'resources', 'cat.png'))
        browser.find_element(By.CLASS_NAME, "button").click()
        by, value = By.CLASS_NAME, "is-success"
        assert browser.find_element(by, value).text == "Успех", \
            "Сообщение о загрузке файла не успешно"
        browser.refresh()
        time.sleep(1)
        assert not check_element_present(browser, by, value), "Появилось сообщение об успехе"

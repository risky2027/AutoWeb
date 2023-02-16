import os.path
import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from functions import login, element_is_present, wait_until_clickable, \
    wait_until_visible, check_alert_is_present, wait_until_present, check_until_url, check_until_title, \
    wait_until_text


def test_inputs_page():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/inputs'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, "test")).send_keys("Сообщение")
        wait_until_clickable(browser, (By.CLASS_NAME, "button:nth-child(2)")).click()
        by, value = By.CLASS_NAME, "is-success"
        assert element_is_present(browser, (by, value)), "Не появилось сообщение об успехе"
        assert browser.find_element(by, value).text == "Верно", "Сообщение неверное"


def test_my_pet_positive():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/my_pet'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, "pet")).send_keys("Мой вид")
        wait_until_clickable(browser, (By.NAME, "name")).send_keys("Мое имя")
        wait_until_clickable(browser, (By.NAME, "age")).send_keys("2")
        wait_until_clickable(browser, (By.NAME, "sex")).send_keys("Мужской")
        wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()
        by, value = By.CLASS_NAME, "is-success"
        assert element_is_present(browser, (by, value)), "Не появилось сообщение об успехе"
        assert browser.find_element(by, value).text == "Успех.", "Сообщение неверное"


def test_my_pet_negative():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/my_pet'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, "pet")).send_keys("Мой вид")
        wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()
        by, value = By.CLASS_NAME, "is-danger"
        assert element_is_present(browser, (by, value)), "Не появилось сообщение об ошибке"
        assert browser.find_element(by, value).text == "Заполнены не все поля.", "Сообщение неверное"
        by, value = By.CLASS_NAME, "is-success"
        assert not element_is_present(browser, (by, value)), "Появилось сообщение об успехе"


def test_about_me():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/about'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.NAME, "name")).send_keys("Андрей")
        wait_until_clickable(browser, (By.NAME, "surname")).send_keys("Павлов")
        specialist = wait_until_clickable(browser, (By.ID, "age1")).get_attribute("checked")
        assert specialist, "По умолчанию выбрано значние Не ручной тестировщик"

        wait_until_clickable(browser, (By.ID, "age2")).click()
        wait_until_clickable(browser, (By.ID, "lang1")).click()
        wait_until_clickable(browser, (By.ID, "lang3")).click()
        element = wait_until_clickable(browser, (By.ID, "lvl"))
        select = Select(element)
        select.select_by_visible_text("Senior")

        wait_until_clickable(browser, (By.NAME, "surname")).send_keys(Keys.ENTER)
        by, value = By.CLASS_NAME, "is-success"
        assert wait_until_visible(browser, (by, value)).text == "Успех.", \
            "Сообщение об отправке формы не успешно"


def test_upload_file():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/upload_file'
        browser.get(url)
        browser.maximize_window()
        login(browser)

        element_for_upload = browser.find_element(By.NAME, "file")
        element_for_upload.send_keys(os.path.join(os.getcwd(), 'resources', 'cat.png'))

        # wait_until_clickable(browser, (By.CLASS_NAME, "file-input")).\
        #    send_keys(os.path.join(os.getcwd(), 'resources', 'cat.png'))
        wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()

        by, value = By.CLASS_NAME, "is-success"
        assert wait_until_visible(browser, (by, value)).text == "Успех", \
            "Сообщение о загрузке файла не успешно"
        browser.refresh()
        time.sleep(1)
        assert not element_is_present(browser, (by, value)), "Появилось сообщение об успехе"


def test_names_left_menu():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/login'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        by, value = By.CSS_SELECTOR, ".menu-list .navbar-item"
        items = wait_until_visible(browser, (by, value))
        names = ["Поля ввода и кнопки", "Мой питомец", "О себе", "Загрузка файла",
                 "Ожидание", "Медленная загрузка", "Модальные окна", "Новая вкладка",
                 "iframe", "Drag-and-drop"]
        for i, item in enumerate(names):
            assert item == names[i], "Название не соответствует полю"


def test_page_with_timer():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/wait'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_text(browser, (By.ID, "demo"), "100")
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[onclick="check_value()"]')).click()
        check_alert_is_present(browser)


def test_low_load():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/slow_load'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.ID, 'text_input')).send_keys("Текст для поля")
        wait_until_clickable(browser, (By.ID, 'button')).click()
        assert wait_until_visible(browser, (By.CLASS_NAME, 'is-success')).text == "Успех.",\
            "Сообщение неверное"
        browser.refresh()
        assert not element_is_present(browser, (By.CLASS_NAME, 'is-success')), \
            "Сообщение об успехе осталось"


def test_profile():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/profile'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[href="/my_pet"]')).click()
        assert check_until_url(browser, "https://qastand.valhalla.pw/my_pet"), \
            "URL неверный"
        browser.refresh()
        assert check_until_title(browser, "Course Test Stand"), "Заголовок страницы неверный"

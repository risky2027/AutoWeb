from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login, check_element_present


def test_inputs_page():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/inputs'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        input_test = browser.find_element(By.NAME, "test")
        input_test.send_keys("Сообщение")
        browser.find_element(By.CLASS_NAME, "button:nth-child(2)").click()
        by, value = By.CLASS_NAME, "is-success"
        assert check_element_present(browser, by, value), "Не появилось сообщение об успехе"
        assert browser.find_element(by, value).text == "Верно", "Сообщение неверное"


def test_my_pet_positive():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/my_pet'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        input_pet = browser.find_element(By.NAME, "pet")
        input_pet.send_keys("Мой вид")
        input_name = browser.find_element(By.NAME, "name")
        input_name.send_keys("Мое имя")
        input_age = browser.find_element(By.NAME, "age")
        input_age.send_keys("2")
        input_sex = browser.find_element(By.NAME, "sex")
        input_sex.send_keys("Мужской")
        browser.find_element(By.CLASS_NAME, "button").click()
        by, value = By.CLASS_NAME, "is-success"
        assert check_element_present(browser, by, value), "Не появилось сообщение об успехе"
        assert browser.find_element(by, value).text == "Успех.", "Сообщение неверное"


def test_my_pet_negative():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/my_pet'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        input_pet = browser.find_element(By.NAME, "pet")
        input_pet.send_keys("Мой вид")
        browser.find_element(By.CLASS_NAME, "button").click()
        by, value = By.CLASS_NAME, "is-danger"
        assert check_element_present(browser, by, value), "Не появилось сообщение об ошибке"
        assert browser.find_element(by, value).text == "Заполнены не все поля.", "Сообщение неверное"
        by, value = By.CLASS_NAME, "is-success"
        assert not check_element_present(browser, by, value), "Появилось сообщение об успехе"


def test_names_left_menu():
    with Chrome() as browser:
        url = 'https://qastand.valhalla.pw/login'
        browser.get(url)
        browser.maximize_window()
        login(browser)
        by, value = By.CSS_SELECTOR, "ul li"
        items = browser.find_elements(by, value)
        names = ["Поля ввода и кнопки", "Мой питомец", "О себе", "Загрузка файла",
                 "Ожидание", "Медленная загрузка", "Модальные окна", "Новая вкладка",
                 "iframe", "Drag-and-drop"]
        for i, item in enumerate(names):
            assert item == names[i], "Название не соответствует полю"

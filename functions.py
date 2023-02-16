from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def login(browser):
    wait_until_clickable(browser, (By.NAME, "email")).send_keys("qa_test@test.ru")
    wait_until_clickable(browser, (By.NAME, "password")).send_keys("!QAZ2wsx")
    wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()


def wait_until_clickable(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_present(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))


def wait_until_visible(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))


def element_is_present(browser: Chrome, locator: Tuple, timeout: int = 5) -> bool:
    try:
        wait_until_visible(browser, locator, timeout)
        return True
    except TimeoutException:
        return False


def check_alert_is_present(driver: Chrome, timeout=5):
    alert = WebDriverWait(driver, timeout).until(ec.alert_is_present())
    assert "Успех!" in alert.text, "Уведомление неверное, нажатие кнопки не своевременно"


def wait_until_text(driver: Chrome, locator: Tuple, text, timeout: int = 10) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.text_to_be_present_in_element(locator, text))


def check_until_url(driver: Chrome, url, timeout: int = 5) -> bool:
    try:
        WebDriverWait(driver, timeout).until(ec.url_to_be(url))
        return True
    except TimeoutException:
        return False


def check_until_title(driver: Chrome, title, timeout: int = 5) -> bool:
    try:
        WebDriverWait(driver, timeout).until(ec.title_is(title))
        return True
    except TimeoutException:
        return False

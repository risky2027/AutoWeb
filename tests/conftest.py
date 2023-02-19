import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def browser():
    browser = Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

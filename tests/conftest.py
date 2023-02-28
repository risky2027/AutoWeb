import random

import pytest
from selenium.webdriver import Chrome

from tests.constants import Links


@pytest.fixture()
def browser():
    browser = Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def url(request):
    """Фикстура для получения заданного из командной строки окружения"""
    env = request.config.getoption("--env")
    url = Links.base_url.get(env)
    if not url:
        raise Exception("Передано неверное окружение")
    return url


def pytest_addoption(parser):
    parser.addoption(
        "--env", default="prod"
    )


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return random.randint(0, 9999)

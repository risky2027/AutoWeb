import random

import pytest

from api.api_client import Client
from constants import Links, VALID_BROWSERS
from selenium.webdriver import Remote


@pytest.fixture()
def browser(request):
    launch = request.config.getoption("--launch")
    browser = VALID_BROWSERS[launch]()
    #browser = Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities={
    #                    "browserName": "chrome", "version": "110.0"
    #                })
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


@pytest.fixture()
def login(browser, url):
    cookie = Client(url).auth()
    browser.get(url)
    browser.add_cookie({"name": "session", "value": cookie["session"]})


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "auth: tests for auth testing"
    )
    config.addinivalue_line(
        "markers", "smoke: tests for smoke testing"
    )


def pytest_addoption(parser):
    parser.addoption(
        "--env", default="prod"
    )
    parser.addoption(
        "--launch", default="chrome", choices=["chrome", "opera"]
    )


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return random.randint(0, 9999)

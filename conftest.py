import random

import pytest

from constants import Links, VALID_BROWSERS


@pytest.fixture()
def browser(request):
    launch = request.config.getoption("--launch")
    browser = VALID_BROWSERS[launch]()
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

import pytest

from tests.constants import Links, SESSION_COOKIE


@pytest.fixture(autouse=True)
def login(browser):
    browser.get(Links.login)
    browser.add_cookie(SESSION_COOKIE)

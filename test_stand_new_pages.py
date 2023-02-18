import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from constants import NEGATIVE_LOGIN_CREDENTIALS, POSITIVE_LOGIN_CREDENTIALS, LINKS
from functions import wait_until_clickable, wait_until_url, check_until_url, login, login_with_params


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self):
        with Chrome() as browser:
            url = LINKS["login"]
            browser.get(url)
            browser.maximize_window()
            login_with_params(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
            wait_until_url(browser, LINKS["profile"], 5)
            assert browser.get_cookie("session") is not None, "В cookie нет записи о сессии"

    @pytest.mark.parametrize("email, password",
                             NEGATIVE_LOGIN_CREDENTIALS,
                             ids=["empty email", "empty password", "wrong email", "unregister email and login"])
    def test_login_negative(self, email, password):
        with Chrome() as browser:
            url = LINKS["login"]
            browser.get(url)
            browser.maximize_window()
            login_with_params(browser, email, password)
            assert check_until_url(browser, LINKS["login"], 5)

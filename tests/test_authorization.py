import pytest

from constants import POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS, Links
from functions import wait_for_url_to_be, login_ui


@pytest.mark.auth
class TestAuthorization:
    @pytest.mark.smoke
    def test_login_positive(self, browser, url):
        browser.get(url + Links.login)
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        wait_for_url_to_be(browser, url + Links.profile)
        assert browser.get_cookie("session")

    @pytest.mark.parametrize("email, password",
                             NEGATIVE_LOGIN_CREDENTIALS, ids=["empty email", "empty password", "invalid email",
                                                              "unregistered user"])
    def test_login_negative(self, browser, url, email, password):
        browser.get(url + Links.login)
        login_ui(browser, email, password)
        wait_for_url_to_be(browser, url + Links.login)

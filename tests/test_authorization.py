import pytest

from constants import POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS, Links
from pages.auth_page import AuthPage
from pages.blog_pages.main_page import MainPage


@pytest.mark.auth
class TestAuthorization:

    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self. auth_page = AuthPage(browser, url + Links.login)
        self.auth_page.open_page()
        self.blog_page = MainPage(browser, url + Links.blog)

    @pytest.mark.smoke
    def test_login_positive(self, url):
        self.auth_page.login_ui(POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        self.auth_page.check_page_is_open(url + Links.profile)
        self.auth_page.check_user_is_authorized()

    @pytest.mark.parametrize("email, password",
                             NEGATIVE_LOGIN_CREDENTIALS, ids=["empty email", "empty password", "invalid email",
                                                              "unregistered user"])
    def test_login_negative(self, url, email, password):

        self.auth_page.login_ui(email, password)
        self.auth_page.check_page_is_open(url + Links.login)

    @pytest.mark.usefixtures("login")
    def test_logout(self):
        self.blog_page.open_page()
        self.auth_page.logout()
        self.blog_page.open_page()
        self.blog_page.check_unauthorized_user_cannot_create_post()

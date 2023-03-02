from webbrowser import Chrome

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей авторизации (/login)
class AuthPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    AUTH_BUTTON = (By.CLASS_NAME, "button")

    def login_ui(self: Chrome, email: str, password: str) -> None:
        """Функция логина на стенде через UI"""
        self.wait_until_clickable(self.EMAIL).send_keys(email)
        self.wait_until_clickable(self.PASSWORD).send_keys(password)
        self.wait_until_clickable(self.AUTH_BUTTON).click()

    def check_user_is_authorized(self):
        assert self.browser.get_cookie("session")

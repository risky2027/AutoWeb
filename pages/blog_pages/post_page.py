from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей отображения поста (пример URL — /blog/page/1/test-post/ или /blog/page/1)
class PostPage(BasePage):
    TITLE_FIELD = (By.ID, "title")
    POST_TEXT = (By.CSS_SELECTOR, ".container p+p")
    DELETE_BUTTON = (By.ID, "delete")
    SUBMIT_BUTTON = (By.ID, "submit")
    SUBMIT_DELETE_BUTTON = (By.ID, "confirmedDelete")
    EDIT_BUTTON = (By.ID, "edit")

    def check_post_text(self, text):
        post_text = self.wait_until_visible(self.POST_TEXT)
        assert post_text.text == text, "Неверный текст"

    def click_edit_button(self):
        self.wait_until_clickable(self.EDIT_BUTTON).click()

    def click_submit_button(self):
        self.wait_until_clickable(self.SUBMIT_BUTTON).click()

    def remove_last_symbol_title(self):
        self.wait_until_clickable(self.TITLE_FIELD).send_keys(Keys.BACKSPACE)

    def click_delete_button(self):
        self.wait_until_clickable(self.DELETE_BUTTON).click()

    def click_submit_delete_button(self):
        self.wait_until_clickable(self.SUBMIT_DELETE_BUTTON).click()

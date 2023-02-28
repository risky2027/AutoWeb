from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы с главной страницей блога (/blog)
class MainPage(BasePage):
    POST_TITLE = '//h1[text()="{}"]'
    POST_TITLE_EDITED = (By.CSS_SELECTOR, "h1")
    CREATE_POST_BUTTON = (By.ID, "new")
    CREATE_POST_SUCCESS_MESSAGE = (By.ID, "alert_div")
    DELETE_POST_SUCCESS_MESSAGE = (By.ID, "alert_div")
    FIRST_POST_TITLE = (By.TAG_NAME, "h1")
    EDIT_BUTTON = (By.ID, "edit")

    def click_on_post_title(self, title):
        self.wait_until_clickable((By.XPATH, self.POST_TITLE.format(title))).click()

    def click_create_post_button(self):
        self.wait_until_clickable(self.CREATE_POST_BUTTON).click()

    def check_post_created_successfully_message(self):
        assert "Blog posted successfully!" in self.wait_until_visible(
            self.CREATE_POST_SUCCESS_MESSAGE).text, \
            "Не отобразилось сообщение об успехе"

    def check_post_exists(self, title):
        assert self.element_is_present((By.XPATH, self.POST_TITLE.format(title))), "Пост не опубликовался"

    def click_created_blog(self, title):
        self.wait_until_clickable((By.XPATH, self.POST_TITLE.format(title))).click()

    def click_edit_button(self):
        self.wait_until_clickable(self.EDIT_BUTTON).click()

    def check_edited_title(self, title):
        assert self.wait_until_visible(self.POST_TITLE_EDITED).text == title[:-1], \
            "Заголовок не отредактирован"

    def check_post_deleted_successfully_message(self):
        assert "Your post was successfully deleted" in self.wait_until_visible(
            self.DELETE_POST_SUCCESS_MESSAGE).text, \
            "Не отобразилось сообщение об успехе"

    def check_post_not_exists(self, title):
        assert not self.element_is_present((By.XPATH, self.POST_TITLE.format(title))), "Пост не удален"

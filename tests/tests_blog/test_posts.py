import pytest
from selenium.webdriver.common.by import By

from api.api_helpers import delete_all_posts
from tests.constants import Links
from tests.functions import wait_until_clickable, wait_until_visible


@pytest.fixture()
def delete_user_posts(url):
    yield
    delete_all_posts(url)


@pytest.mark.blog
class TestsBlogOpen:
    def test_open_post(self, browser, url):
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.CSS_SELECTOR, "[href='/blog/page/1/test-post/']")).click()
        assert wait_until_visible(browser, (By.CSS_SELECTOR, ".container p+p")).text ==\
               "Hello world!", "Неверный приветственный текст"


@pytest.mark.usefixtures("delete_user_posts")
class TestsBlogModify:
    def test_create_post(self, browser, url, faker):
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.ID, 'new')).click()
        title = faker.text(10)
        wait_until_clickable(browser, (By.ID, "title")).send_keys(title)
        text = faker.text(20)
        wait_until_clickable(browser, (By.ID, "text")).send_keys(text)
        tag = faker.text(6)
        wait_until_clickable(browser, (By.ID, "tags")).send_keys(tag)
        wait_until_clickable(browser, (By.ID, "submit")).click()

        assert "Blog posted successfully!" in wait_until_visible(browser, (By.ID, "alert_div")).text, \
            "Нет сообщения об успехе"
        assert wait_until_visible(browser, (By.TAG_NAME, "h1")).text == title, "Пост не опубликовался"

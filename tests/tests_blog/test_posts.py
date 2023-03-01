import pytest

from api.api_helpers import delete_all_posts
from api.blog_api import BlogApi
from constants import Links
from pages.blog_pages.main_page import MainPage
from pages.blog_pages.post_modify_page import PostModifyPage
from pages.blog_pages.post_page import PostPage


@pytest.fixture()
def delete_user_posts(url):
    yield
    delete_all_posts(url)


@pytest.fixture()
def create_post_for_test(url, faker):
    api = BlogApi(url)
    title = faker.text(10)
    text = faker.text(100)
    api.create_post(title=title, text=text, tags=[faker.text(5)])
    return title, text


@pytest.mark.usefixtures("delete_user_posts", "login")
class TestsBlogOpen:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.blog_page = MainPage(browser, url + Links.blog)
        self.post_page = PostPage(browser, url + Links.blog)

    def test_open_post(self, create_post_for_test):
        title, text = create_post_for_test

        self.blog_page.open_page()
        self.blog_page.click_on_post_title(title)
        self.post_page.check_post_text(text)


@pytest.mark.usefixtures("delete_user_posts", "login")
class TestsBlogModify:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.blog_page = MainPage(browser, url + Links.blog)
        self.post_modify_page = PostModifyPage(browser, url + Links.blog)
        self.post_page = PostPage(browser, url + Links.blog)

    def test_create_post(self, browser, url, faker):
        title = faker.text(10)

        self.blog_page.open_page()
        self.blog_page.click_create_post_button()

        self.post_modify_page.add_title(title)
        self.post_modify_page.add_text(faker.text(100))
        self.post_modify_page.add_tags(faker.text(5))
        self.post_modify_page.click_submit_button()

        self.blog_page.check_post_created_successfully_message()
        self.blog_page.check_post_exists(title)

    def test_change_title(self, browser, url, create_post_for_test):
        title, _ = create_post_for_test
        self.blog_page.open_page()
        self.blog_page.click_created_blog(title)

        self.blog_page.click_edit_button()
        self.post_page.remove_last_symbol_title()
        self.post_page.click_submit_button()

        self.blog_page.check_edited_title(title)

    def test_delete_post(self, browser, url, create_post_for_test):
        title, _ = create_post_for_test
        self.blog_page.open_page()
        self.blog_page.click_created_blog(title)

        self.post_page.click_delete_button()
        self.post_page.click_submit_delete_button()

        self.blog_page.check_post_deleted_successfully_message()
        self.blog_page.check_post_not_exists(title)

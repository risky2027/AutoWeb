import pytest
from selenium.webdriver.common.by import By

from tests.constants import Links
from tests.functions import wait_until_clickable, wait_until_visible


@pytest.mark.blog
class TestBlogClass:

    def test_blog(self, browser):
        browser.get(Links.blog)
        wait_until_clickable(browser, (By.CSS_SELECTOR, "[href='/blog/page/1/test-post/']")).click()
        assert wait_until_visible(browser, (By.CSS_SELECTOR, ".container p:nth-child(3)")).text ==\
               "Hello world!", "Текст неверный"

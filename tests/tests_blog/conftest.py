import pytest

from api.blog_api import BlogApi


@pytest.fixture(autouse=True)
def login(browser, url):
    browser.get(url)
    cookie = BlogApi(url).auth()
    browser.add_cookie({"name": "session", "value": cookie["session"]})

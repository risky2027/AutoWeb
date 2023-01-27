from selenium.webdriver import Chrome

url = 'https://qastand.valhalla.pw/login'

class TestOpen:
    def test_open_browser(self):
        browser = Chrome()
        browser.get(url)
        print(url.get)
        browser.quit()
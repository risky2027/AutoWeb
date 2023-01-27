from selenium.webdriver import Chrome

url = 'https://qastand.valhalla.pw/login'

class TestOpen:
    def test_open_browser(self):
        with Chrome() as browser:
            browser.get(url)
            print(f"{browser.current_url}")
            browser.quit()

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from selene import browser
from lesson_9_Page_object.utils import attach
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")
browser.config.window_width = 1920
browser.config.window_height = 1080
browser.config.driver_options = chrome_options
browser.config.driver_manager = ChromeDriverManager()

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser1 = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser1)
    attach.add_logs(browser1)
    attach.add_html(browser1)
    attach.add_video(browser1)

    browser1.quit()
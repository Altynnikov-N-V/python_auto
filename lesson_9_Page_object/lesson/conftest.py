import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from lesson_9_Page_object.utils import attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()

    # Настройки для Selenoid
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser_instance = Browser(Config(driver))
    browser_instance.config.window_width = 1920
    browser_instance.config.window_height = 1080

    yield browser_instance

    attach.add_screenshot(browser_instance)
    attach.add_logs(browser_instance)
    attach.add_html(browser_instance)
    attach.add_video(browser_instance)

    browser_instance.quit()

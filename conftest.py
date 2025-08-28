import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    login = os.getenv('SELENOID_LOGIN', 'user1')
    password = os.getenv('SELENOID_PASS', '1234')
    host = os.getenv('SELENOID_URL', 'selenoid.autotests.cloud')

    options = Options()
    options.set_capability('browserName', 'chrome')
    options.set_capability('browserVersion', '128.0')
    options.set_capability('selenoid:options', {
        'enableVNC': True,
        'enableVideo': True  # Включить запись видео
    })

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{host}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = 10

    yield

    # Добавление вложений
    from lesson_jenkins.utils import attach
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)  # Теперь видео будет работать

    browser.quit()
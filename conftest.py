import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    host = os.getenv('SELENOID_URL')

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
    attach.add_video(browser)

    browser.quit()
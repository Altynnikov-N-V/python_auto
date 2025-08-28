import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def remote_browser_setup():
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    host = os.getenv('SELENOID_URL', '')

    assert all([login, password, host]), f'ENV missing: login={bool(login)}, pass={bool(password)}, url={bool(host)}'

    host = host.replace('http://', '').replace('https://', '').rstrip('/')

    options = Options()
    options.set_capability('browserName', 'chrome')
    options.set_capability('browserVersion', '128.0')
    options.set_capability('selenoid:options', {'enableVNC': True, 'enableVideo': True})
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{host}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()
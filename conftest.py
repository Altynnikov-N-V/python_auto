
import os
import pytest
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv(override=True)

@pytest.fixture(scope='function', autouse=True)
def remote_browser_setup():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selene.support.shared import browser

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    host = os.getenv('SELENOID_URL', '')

    assert all([login, password, host]), f'ENV missing: login={bool(login)}, pass={bool(password)}, url={bool(host)}'

    host = host.replace('http://','').replace('https://','').rstrip('/')

    options = Options()
    options.set_capability('browserName', 'chrome')
    options.set_capability('browserVersion', '128.0')
    options.set_capability('selenoid:options', {'enableVNC': True, 'enableVideo': True})
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@{host}/wd/hub',
        options=options
    )
    browser.config.driver = driver
    yield
    browser.quit()

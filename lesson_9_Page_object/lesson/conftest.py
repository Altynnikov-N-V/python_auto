import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import uuid
import tempfile
import shutil
from selene import Browser, Config

from ..utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    chrome_options = Options()

    # Базовые опции
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--no-default-browser-check')

    # Решение проблемы user-data-dir
    temp_user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f'--user-data-dir={temp_user_data_dir}')

    # Дополнительные опции для стабильности
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.add_argument('--disable-popup-blocking')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    # Завершение и очистка
    driver.quit()
    shutil.rmtree(temp_user_data_dir, ignore_errors=True)

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
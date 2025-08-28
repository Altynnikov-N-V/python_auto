import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selene import browser
import tempfile
import shutil
import os


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    # Настройка Chrome options для локального запуска
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--no-default-browser-check')

    # Уникальная user-data директория чтобы избежать конфликтов
    temp_user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f'--user-data-dir={temp_user_data_dir}')

    # Используем установленный ChromeDriver
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')

    # Установка и настройка драйвера
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Конфигурация Selene
    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    # Завершение
    browser.quit()
    shutil.rmtree(temp_user_data_dir, ignore_errors=True)
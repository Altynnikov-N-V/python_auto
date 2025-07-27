import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selene import have
from selene import browser

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search_selenium(driver):
    driver.get('https://www.google.com/')

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('selene github')
    search_box.send_keys(Keys.ENTER)

    expected_text = 'yashaka/selene: User-oriented Web UI browser tests in ...'

    h3_element = WebDriverWait(driver,40).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert h3_element.text == expected_text

def test_google_search_selene():
    browser.open('https://ya.ru/')
    browser.element('[name=text]').type('selene github').press_enter()
    browser.element('h2').should(have.text('GitHub - yashaka/selene'))
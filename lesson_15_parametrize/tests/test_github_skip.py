import pytest
from selene import browser, by

def test_mobile_skip(setup_browser):
    if setup_browser =='mobile':
        pytest.skip("Мобильная версия браузера")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()

def test_desktop_skip(setup_browser):
    if setup_browser == 'desktop':
        pytest.skip("Десктопная версия браузера")
    browser.open("https://github.com/")
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()
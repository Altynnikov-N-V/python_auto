import pytest
from selene import browser, by

@pytest.mark.parametrize('desktop_browser_setup', [(1366, 768)], indirect=True, ids=['desktop_size'])
def test_desktop_parametrize(desktop_browser_setup):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()

@pytest.mark.parametrize('mobile_browser_setup', [(800, 600)], indirect=True, ids=['mobile_size'])
def test_mobile_parametrize(mobile_browser_setup):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-button').click()

from selene import browser, by

def test_desktop_fixtures(desktop_browser_setup):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()

def test_mobile_fixtures(mobile_browser_setup):
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element(by.text("Sign up")).click()
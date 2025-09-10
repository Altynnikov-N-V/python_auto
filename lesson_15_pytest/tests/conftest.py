import pytest
from selene import browser

@pytest.fixture(params=[
    (1920, 1080),
    (1440, 900),
    (1366, 768),
    (1280, 768),
    (800, 600),
    (800, 480)])

def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width > 800:
        yield 'desktop'
    else:
        yield 'mobile'
    browser.quit()

@pytest.fixture(params=[
    (1920, 1080),
    (1440, 900),
    (1366, 768),
    (1280, 768)])

def desktop_browser_setup(request):
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width
    yield
    browser.quit()

@pytest.fixture(params=[
    (800, 600),
    (800, 480)])
def mobile_browser_setup(request):
    widht, height = request.param
    browser.config.window_height = height
    browser.config.window_width = widht
    yield
    browser.quit()
import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23",
        "app": "bs://sample.app",
        "bstack:options": {
            "userName": "bsuser_oH0Eba",
            "accessKey": "gvxzoGEYMxuigMaqnWxY",
            "projectName": "First Python project",
            "buildName": "browserstack-build-2",
            "sessionName": "BStack home_work"
        }
    })

    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    driver.implicitly_wait(10)
    yield driver

    try:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot_final", attachment_type=allure.attachment_type.PNG)
        page_source = driver.page_source
        allure.attach(page_source, name="page_source_final", attachment_type=allure.attachment_type.XML)
        logs = driver.get_log('logcat')
        allure.attach(str(logs), name="logcat_final", attachment_type=allure.attachment_type.TEXT)

    except Exception:
        pass
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot_on_failure", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass
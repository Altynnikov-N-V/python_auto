import pytest
import requests
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options

BROWSERSTACK_USERNAME = "bsuser_oH0Eba"
BROWSERSTACK_ACCESS_KEY = "gvxzoGEYMxuigMaqnWxY"

def get_browserstack_video_url(session_id):
    url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
    response = requests.get(url, auth=(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY))
    if response.status_code == 200:
        data = response.json()
        return data.get("automation_session", {}).get("video_url")
    return None

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23",
        "app": "bs://sample.app",
        "bstack:options": {
            "userName": BROWSERSTACK_USERNAME,
            "accessKey": BROWSERSTACK_ACCESS_KEY,
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

        session_id = driver.session_id
        video_url = get_browserstack_video_url(session_id)
        if video_url:
            video_response = requests.get(video_url)
            if video_response.status_code == 200:
                allure.attach(video_response.content, name="test_execution_video", attachment_type=allure.attachment_type.MP4)

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

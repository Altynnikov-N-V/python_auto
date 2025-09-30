import pytest
import requests
import time
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options

BROWSERSTACK_USERNAME = "bsuser_oH0Eba"
BROWSERSTACK_ACCESS_KEY = "gvxzoGEYMxuigMaqnWxY"

def get_browserstack_video_url(session_id):
    url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"
    resp = requests.get(url, auth=(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY))
    if resp.status_code == 200:
        data = resp.json()
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
            "sessionName": "BStack home_work",
            "video": True
        }
    })

    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    driver.implicitly_wait(10)

    yield driver

    try:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_final", attachment_type=allure.attachment_type.PNG)
        allure.attach(driver.page_source, name="page_source_final", attachment_type=allure.attachment_type.XML)
        logs = driver.get_log('logcat')
        allure.attach(str(logs), name="logcat_final", attachment_type=allure.attachment_type.TEXT)

        session_id = driver.session_id
        time.sleep(35)

        video_url = get_browserstack_video_url(session_id)
        if video_url:
            print(f"BrowserStack video URL: {video_url}")
            video_resp = requests.get(video_url)
            if video_resp.status_code == 200:
                allure.attach(video_resp.content, name="test_execution_video.mp4", attachment_type="video/mp4")
            else:
                print(f"Failed to download video, status code {video_resp.status_code}")
        else:
            print("Video URL not found")

    except Exception as e:
        print(f"Error attaching video: {e}")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            try:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot_on_failure", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass

import pytest
import allure
import time
from lesson_19_ui_1.tests.test_home_work import config
from appium import webdriver
from appium.options.android import UiAutomator2Options

def attach_bstack_video(session_id):
    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.bstack_userName, config.bstack_accessKey),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session'].get('video_url')
    if video_url:
        allure.attach(
            '<html><body>'
            '<video width="100%" height="100%" controls autoplay>'
            f'<source src="{video_url}" type="video/mp4">'
            '</video>'
            '</body></html>',
            name='video recording',
            attachment_type=allure.attachment_type.HTML,
        )
    else:
        print("Видео из BrowserStack не найдено в ответе API")

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23",
        "app": "bs://sample.app",
        "bstack:options": {
            "userName": config.bstack_userName,
            "accessKey": config.bstack_accessKey,
            "projectName": "First Python project",
            "buildName": "browserstack-build-2",
            "sessionName": "BStack home_work",
            "video": True,
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
        time.sleep(5)
        attach_bstack_video(driver.session_id)

    except Exception as e:
        print(f"Ошибка при добавлении аттачей: {e}")

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

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from allure_commons._allure import step


options = UiAutomator2Options()
options.load_capabilities({
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "Samsung Galaxy S23",
    "app": "bs://sample.app",
    "bstack:options": {
        "userName": "bsuser_oH0Eba",    # Правильное название ключа в bstack:options - userName
        "accessKey": "gvxzoGEYMxuigMaqnWxY",
        "projectName": "First Python project",
        "buildName": "browserstack-build-2",
        "sessionName": "BStack home_work"
    }
})

@step('Открытие любой статьи и клик на нее')
def test_search_wikipedia_str():
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    try:
        search_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        )
        search_element.click()
        search_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
        )
        search_input.send_keys("Home")
        time.sleep(5)
        search_results = driver.find_elements(AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        assert len(search_results) > 0

        search_results[0].click()

        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot_after_click", attachment_type=allure.attachment_type.PNG)

        page_source = driver.page_source
        allure.attach(page_source, name="page_source", attachment_type=allure.attachment_type.XML)

        logs = driver.get_log('logcat')
        allure.attach(str(logs), name="logcat", attachment_type=allure.attachment_type.TEXT)

    finally:
        driver.quit()

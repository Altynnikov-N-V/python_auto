import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy

@step('Открытие любой статьи и клик на нее')
def test_search_wikipedia_str(driver):
    search_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
    search_element.click()
    search_input = driver.find_element(AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    search_input.send_keys("Home")
    search_results = driver.find_elements(AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
    assert len(search_results) > 0
    search_results[0].click()

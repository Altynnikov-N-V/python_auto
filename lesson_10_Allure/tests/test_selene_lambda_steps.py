import allure
import selene
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s
from selene.support.conditions import be

def test_dynamic_find():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com/home")
    browser.driver.maximize_window()

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("input.QueryBuilder-Input").type("eroshenkoam/allure-github-example").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-github-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issues"):
        s(by.partial_text("Apr")).should(be.visible)
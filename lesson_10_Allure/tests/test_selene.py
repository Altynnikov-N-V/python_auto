import selene
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s
from selene.support.conditions import be


def test_issues_find():
    browser.open("https://github.com/home")
    browser.driver.maximize_window()
    s(".header-search-button").click()
    s("input.QueryBuilder-Input").type("eroshenkoam/allure-example").press_enter()
    s(by.link_text("eroshenkoam/allure-github-example")).click()
    s("#issues-tab").click()
    s(by.partial_text("Apr")).should(be.visible)


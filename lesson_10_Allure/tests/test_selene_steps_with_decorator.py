import allure
import selene
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s
from selene.support.conditions import be

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-github-example")
    open_issue_tab()
    should_see_issue_with_text("Apr")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com/home")

@allure.step("Ищем репозиторий")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("input.QueryBuilder-Input").type(repo).press_enter()

@allure.step("Переходим по ссылке репозитория")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()

@allure.step("Проверяем наличие Issues{text}")
def should_see_issue_with_text(text):
    s(by.partial_text(text)).should(be.visible)

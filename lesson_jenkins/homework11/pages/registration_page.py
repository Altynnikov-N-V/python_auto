import os

from selene import browser, have, be
from lesson_jenkins.homework11.models import User
from pathlib import Path
import allure

class RegistrationPage:

    def open_form(self):
        with allure.step("Переход на страницу"):
            browser.open('https://demoqa.com/automation-practice-form')
        return self

    def register(self, user: User):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', user.file_name))
        with allure.step("Заполнение имени"):
            browser.element('#firstName').type(user.first_name)
        with allure.step("Заполнение фамилии"):
            browser.element('#lastName').type(user.last_name)
        with allure.step("Заполнение емеила"):
            browser.element('#userEmail').type(user.email)
        with allure.step("Выбор пола"):
            browser.element(f'//label[text()="{user.gender}"]').click()
        with allure.step("Заполнение номера телефона"):
            browser.element('#userNumber').type(user.phone)

        # birthday
        with allure.step("Заполнение даты рождения"):
            browser.element('#dateOfBirthInput').click()
            browser.element('.react-datepicker__month-select').send_keys(user.month)
            browser.element('.react-datepicker__year-select').send_keys(str(user.year))
            browser.element(f'.react-datepicker__day--0{user.day:02}').click()
        with allure.step("Выбор предмета"):
            browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        with allure.step("Выбор хобби"):
            element = browser.element(f'//label[text()="{user.hobby}"]')
            browser.driver.execute_script("arguments[0].click();", element.locate())
        with allure.step("Загрузка изображения"):
            browser.element('#uploadPicture').send_keys(file_path)
        with allure.step("Выбор адреса"):
            browser.element('#currentAddress').type(user.address)
            state_element = browser.element('#state')
            browser.execute_script("arguments[0].click();", state_element)
            state_option = browser.element(f'//div[text()="{user.state}"]')
            browser.execute_script("arguments[0].click();", state_option)
            browser.element('#city').click().element(f'//div[text()="{user.city}"]').click()
        with allure.step("Отправка формы"):
            browser.element('#submit').press_enter()
        return self

    def should_have_registered(self, user: User):
        with allure.step("Проверка формы"):
            modal = browser.element('.modal-content')
            modal.should(have.text(f'{user.first_name} {user.last_name}'))
            modal.should(have.text(user.email))
            modal.should(have.text(user.gender))
            modal.should(have.text(user.phone))
            modal.should(have.text(f'{user.day} {user.month},{user.year}'))
            modal.should(have.text(user.subject))
            modal.should(have.text(user.hobby))
            modal.should(have.text(user.file_name))
            modal.should(have.text(user.address))
            modal.should(have.text(f'{user.state} {user.city}'))
import os
import time
import allure
from selene import browser, have, be
from lesson_jenkins.homework11.models import User


class RegistrationPage:

    def open_form(self):
        with allure.step("Переход на страницу"):
            browser.open('https://demoqa.com/automation-practice-form')
            browser.driver.maximize_window()
            # Ждем загрузки страницы
            time.sleep(3)

            # Отладочная информация
            self.debug_page_elements()

        return self

    def debug_page_elements(self):
        """Отладочная информация о элементах страницы"""
        print("=== DEBUG: Page Elements ===")

        # Проверяем наличие основных элементов
        elements_to_check = [
            '#firstName', '#lastName', '#userEmail', '#userNumber',
            '#dateOfBirthInput', '#subjectsInput', '#uploadPicture',
            '#currentAddress', '#state', '#city', '#submit'
        ]

        for selector in elements_to_check:
            try:
                element = browser.element(selector)
                print(f"✓ Found: {selector}")
            except:
                print(f"✗ Missing: {selector}")

        # Проверяем элементы пола
        print("\nGender elements:")
        gender_inputs = browser.all('input[name="gender"]')
        for i, inp in enumerate(gender_inputs):
            try:
                value = inp.locate().get_attribute('value')
                id_attr = inp.locate().get_attribute('id')
                print(f"Gender {i}: value={value}, id={id_attr}")
            except:
                print(f"Gender {i}: cannot get attributes")

        # Проверяем элементы хобби
        print("\nHobby elements:")
        hobby_inputs = browser.all('input[type="checkbox"]')
        for i, inp in enumerate(hobby_inputs):
            try:
                value = inp.locate().get_attribute('value')
                id_attr = inp.locate().get_attribute('id')
                print(f"Hobby {i}: value={value}, id={id_attr}")
            except:
                print(f"Hobby {i}: cannot get attributes")

    def register(self, user: User):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', user.file_name))

        with allure.step("Заполнение имени"):
            browser.element('#firstName').type(user.first_name)

        with allure.step("Заполнение фамилии"):
            browser.element('#lastName').type(user.last_name)

        with allure.step("Заполнение email"):
            browser.element('#userEmail').type(user.email)

        with allure.step("Выбор пола"):
            # Пробуем разные варианты селекторов
            try:
                # Вариант 1: по value
                browser.element('input[value="Female"]').click()
            except:
                try:
                    # Вариант 2: по name и значению
                    browser.element('input[name="gender"][value="Female"]').click()
                except:
                    try:
                        # Вариант 3: через label
                        browser.element('label[for="gender-radio-2"]').click()
                    except:
                        # Вариант 4: просто кликнем на второй radio
                        gender_inputs = browser.all('input[name="gender"]')
                        if len(gender_inputs) > 1:
                            gender_inputs[1].click()

        with allure.step("Заполнение номера телефона"):
            browser.element('#userNumber').type(user.phone)

        with allure.step("Заполнение даты рождения"):
            browser.element('#dateOfBirthInput').click()
            browser.element('.react-datepicker__month-select').send_keys(user.month)
            browser.element('.react-datepicker__year-select').send_keys(str(user.year))
            # Селектор для дня
            browser.element(f'.react-datepicker__day--0{user.day}').click()

        with allure.step("Выбор предмета"):
            browser.element('#subjectsInput').type(user.subject)
            browser.element('#subjectsInput').press_enter()

        with allure.step("Выбор хобби"):
            # Пробуем разные варианты селекторов для хобби
            try:
                browser.element('input[value="1"]').click()
            except:
                try:
                    browser.element('input[id="hobbies-checkbox-1"]').click()
                except:
                    try:
                        browser.element('label[for="hobbies-checkbox-1"]').click()
                    except:
                        # Кликнем на первый чекбокс
                        hobby_inputs = browser.all('input[type="checkbox"]')
                        if len(hobby_inputs) > 0:
                            hobby_inputs[0].click()

        with allure.step("Загрузка изображения"):
            browser.element('#uploadPicture').send_keys(file_path)

        with allure.step("Выбор адреса"):
            browser.execute_script("window.scrollBy(0, 300);")
            browser.element('#currentAddress').type(user.address)

        with allure.step("Выбор штата и города"):
            # Простой способ через клики
            browser.element('#state').click()
            browser.element(f'//div[text()="{user.state}"]').click()

            browser.element('#city').click()
            browser.element(f'//div[text()="{user.city}"]').click()

        with allure.step("Отправка формы"):
            browser.execute_script("document.querySelector('#submit').scrollIntoView(true);")
            browser.element('#submit').click()

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
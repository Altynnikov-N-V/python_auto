import os
import time
import allure
from selene import browser, have, be
from lesson_jenkins.homework11.models import User


class RegistrationPage:

    def open_form(self):
        with allure.step("Переход на страницу"):
            browser.open('https://demoqa.com/automation-practice-form')
            # Удаляем мешающие элементы при открытии формы
            self.remove_obstructing_elements()
        return self

    def register(self, user: User):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', user.file_name))

        # Прокручиваем в начало для начала заполнения
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)

        with allure.step("Заполнение имени"):
            browser.element('#firstName').type(user.first_name)

        with allure.step("Заполнение фамилии"):
            browser.element('#lastName').type(user.last_name)

        with allure.step("Заполнение email"):
            browser.element('#userEmail').type(user.email)

        with allure.step("Выбор пола"):
            browser.element(f'//label[text()="{user.gender}"]').click()

        with allure.step("Заполнение номера телефона"):
            browser.element('#userNumber').type(user.phone)

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
            browser.execute_script("document.querySelector('#uploadPicture').scrollIntoView(true);")
            browser.element('#currentAddress').type(user.address)

        with allure.step("Выбор штата и города"):
            browser.execute_script("document.querySelector('#currentAddress').scrollIntoView(true);")
            self.select_dropdown_option('#state', user.state)
            self.select_dropdown_option('#city', user.city)

        with allure.step("Отправка формы"):
            # Прокручиваем к кнопке и кликаем через JavaScript
            browser.execute_script("document.querySelector('#city').scrollIntoView(true);")
            time.sleep(0.5)
            browser.execute_script("window.scrollBy(0, 100);")
            time.sleep(0.5)
            browser.execute_script("document.querySelector('#submit').click();")

        return self

    def select_dropdown_option(self, dropdown_selector, option_text):
        """Выбор опции в выпадающем списке через JavaScript"""
        try:
            browser.execute_script(f"""
                var dropdown = document.querySelector('{dropdown_selector}');
                if (dropdown) {{
                    // Прокручиваем к элементу
                    dropdown.scrollIntoView({{behavior: 'smooth', block: 'center'}});

                    // Кликаем чтобы открыть список
                    dropdown.click();

                    // Ждем и ищем нужную опцию
                    setTimeout(function() {{
                        var options = document.querySelectorAll('div[class*="option"]');
                        for (var i = 0; i < options.length; i++) {{
                            if (options[i].textContent.trim() === '{option_text}') {{
                                // Кликаем на опцию
                                options[i].click();
                                break;
                            }}
                        }}
                    }}, 1000);
                }}
            """)
            time.sleep(1.5)  # Ждем завершения выбора
        except Exception as e:
            print(f"Error selecting dropdown option {option_text}: {e}")
            # Альтернативный способ через ввод текста
            try:
                browser.execute_script(f"""
                    var dropdown = document.querySelector('{dropdown_selector}');
                    if (dropdown) {{
                        var input = dropdown.querySelector('input');
                        if (input) {{
                            input.value = '{option_text}';
                            var event = new Event('input', {{ bubbles: true }});
                            input.dispatchEvent(event);
                            var changeEvent = new Event('change', {{ bubbles: true }});
                            input.dispatchEvent(changeEvent);
                        }}
                    }}
                """)
            except Exception as e2:
                print(f"Alternative method also failed: {e2}")

    def remove_obstructing_elements(self):
        """Удаление элементов, которые могут мешать взаимодействию"""
        try:
            browser.execute_script("""
                // Удаляем рекламные баннеры и мешающие элементы
                var elementsToRemove = [
                    'footer', 
                    'header',
                    'div[class*="ad"]',
                    'div[class*="banner"]',
                    'div[style*="fixed"]',
                    'div[style*="absolute"]',
                    'iframe',
                    'span[style*="position"]',
                    'div[class*="popup"]',
                    'div[class*="modal"]'
                ];

                elementsToRemove.forEach(function(selector) {
                    var elements = document.querySelectorAll(selector);
                    elements.forEach(function(el) {
                        if (el && el.parentNode) {
                            el.parentNode.removeChild(el);
                        }
                    });
                });
            """)
        except Exception as e:
            print(f"Error removing elements: {e}")

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
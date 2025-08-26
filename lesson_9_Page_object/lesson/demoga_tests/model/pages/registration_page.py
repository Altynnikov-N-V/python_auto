from selene import have, command, by, be
from selene.support.shared import browser
from lesson_9_Page_object import resource


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_email(self, email):
        browser.element('[id="userEmail"]').type(email)
        return self

    def set_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()
        return self

    def fill_phone_number(self, value):
        browser.element('[id="userNumber"]').type(value)
        return self

    def set_subject_by_click(self, type_letter, value):
        browser.element('#subjectsInput').type(type_letter)
        browser.all('.subjects-auto-complete__menu div').element_by(have.exact_text(value)).click()
        return self

    def set_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    def download_file(self, value):
        browser.element('[id = "uploadPicture"]').should(be.visible).send_keys(resource.image_path(value))
        return self

    def fill_current_address(self, value):
        browser.element('[id="currentAddress"]').set_value(value)
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def choose_location(self, state, city):
        browser.element('#state input').type(state).press_enter()
        browser.element('#city input').type(city).press_enter()
        return self

    def submit_form(self):
        browser.element('[id="submit"]').click()
        return self

    def should_registered_user_with(self, full_name, email, *tbd):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                'Female',
                '1234567891',
                '11 May,1999',
                'Computer Science',
                'Reading',
                'textfile.txt',
                'Moscowskaya Street 18',
                'NCR Delhi',
            )
        )
        return self

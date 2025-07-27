import os
import time
from selene import browser, be, have


def test_form():
    file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
    browser.open('/automation-practice-form')
    time.sleep(5)
    browser.element('#firstName').should(be.visible).type('Василий')
    browser.element('#lastName').should(be.blank).type('Васильев')
    browser.element('#userEmail').should(be.blank).type('VVasilii@mail.ru')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('0987654321')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1989')
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('ул. Пушкина, 123')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').press_enter()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Василий Васильев',
        'VVasilii@mail.ru',
        'Male',
        '0987654321',
        '2 October,1989',
        'Maths',
        'Music',
        'file.txt',
        'ул. Пушкина, 123',
        'NCR Delhi'
    ))
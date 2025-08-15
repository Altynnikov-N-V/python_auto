import os
import sys
import pytest
from selene import browser, be, have
from pages.registration_page import RegistrationPage
from users import User


def test_form_submission():
    registration_page = RegistrationPage()
    ivan = User(first_name='Olga',
                 last_name='YA',
                 email='name@example.com',
                 gender="Female",
                 phone_number='1234567891',
                 birthday=('August', '1995', '5'),
                 first_subject='Maths',
                 second_subject=('p', 'Computer Science'),
                 hobby="Reading",
                 file_name='textfile.txt',
                 address='Moscowskaya Street 18',
                 user_location=('NCR', 'Delhi')
                 )

    registration_page.open()
    registration_page.register(ivan)
    registration_page.should_have_registered(ivan)
    print('test finished')
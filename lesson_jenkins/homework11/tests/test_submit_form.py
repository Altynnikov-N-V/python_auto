import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from lesson_jenkins.homework11.pages.registration_page import RegistrationPage
from lesson_jenkins.homework11.models.user import User


def test_fill_form():
    sofi = User(
        first_name="Маргарита",
        last_name="Иванова",
        email="sofia@example.com",
        gender="Female",
        phone="1234567890",
        day=15,
        month="June",
        year=1990,
        subject="Maths",
        hobby="Sports",
        file_name="test.png",
        address="Moscow, ул. Советская, д. 4",
        state="NCR",
        city="Delhi"
    )

    registration_page = RegistrationPage()
    registration_page.open_form()
    registration_page.register(sofi)
    registration_page.should_have_registered(sofi)
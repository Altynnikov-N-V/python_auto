from demoga_tests.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    (registration_page
    .fill_first_name('Olga')
    .fill_last_name('YA')
    .fill_email('name@example.com')
    .set_gender("Female")
    .fill_phone_number('1234567891')
    .fill_date_of_birth('1999', 'May', '11')
    .set_subject_by_click('p', 'Computer Science')
    .set_hobby("Reading")
    .download_file('textfile.txt')
    .fill_current_address('Moscowskaya Street 18')
    .choose_location('NCR', 'Delhi')
    .submit_form()
     )

    # THEN
    registration_page.should_registered_user_with(
        'Olga YA',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'textfile.txt',
        'Moscowskaya Street 18',
        'NCR Delhi',
    )
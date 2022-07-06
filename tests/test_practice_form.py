from selene.support.shared import browser
from selene import have, command


def test_practice_form():

    browser.open('/automation-practice-form')
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(4))
        .perform(command.js.remove)
    )
    # remove ads

    browser.element('#firstName').type('elena')

    browser.element('#lastName').type('truniak')

    browser.element('#userEmail').type('elena.truniak@gmail.com')

    browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text('Female')).click()

    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1990"]').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element('.react-datepicker__day--014').click()

    browser.element('#subjectsInput').type('Math').press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    from demoqa_tests.utils import resource
    browser.element('#uploadPicture').send_keys(resource('test_QA.png'))

    browser.element('#currentAddress').type('My current address')
    browser.element('#state').element('input').type('Haryana').press_enter()
    browser.element('#city').element('input').type('Karnal').press_enter()

    browser.element('#submit').press_enter()

    # checks
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-dialog').all('table tr')[1].all('td').should(have.exact_texts('Student Name', 'elena truniak'))
    browser.all('.modal-dialog').all('table tr')[2].all('td').should(have.exact_texts('Student Email', 'elena.truniak@gmail.com'))
    browser.all('.modal-dialog').all('table tr')[3].all('td').should(have.exact_texts('Gender', 'Female'))
    browser.all('.modal-dialog').all('table tr')[4].all('td').should(have.exact_texts('Mobile', '1234567890'))
    browser.all('.modal-dialog').all('table tr')[5].all('td').should(have.exact_texts('Date of Birth', '14 January,1990'))
    browser.all('.modal-dialog').all('table tr')[6].all('td').should(have.exact_texts('Subjects', 'Maths'))
    browser.all('.modal-dialog').all('table tr')[7].all('td').should(have.exact_texts('Hobbies', 'Sports, Reading, Music'))
    browser.all('.modal-dialog').all('table tr')[8].all('td').should(have.exact_texts('Picture', 'test_QA.png'))
    browser.all('.modal-dialog').all('table tr')[9].all('td').should(have.exact_texts('Address', 'My current address'))
    browser.all('.modal-dialog').all('table tr')[10].all('td').should(have.exact_texts('State and City', 'Haryana Karnal'))
    browser.element('#closeLargeModal').click()

    print("Form is tested")

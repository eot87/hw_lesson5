from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1980
    browser.config.window_height = 1980
    yield
    print("Browser is open")
    browser.quit()

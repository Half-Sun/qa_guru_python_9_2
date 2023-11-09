import pytest

from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def window():
    browser.config.window_width = 320
    browser.config.window_width = 569
    browser.open('https://google.com')

def test_check_text(window):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_no_result(window):
    browser.element('[name="q"]').should(be.blank).type('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy432424').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено. '))
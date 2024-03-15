import pytest
from selene import browser, be, have


@pytest.fixture()
def open_browser():
    browser.driver.set_window_size(1900, 1000)
    browser.open('https://google.com/')


def test_should_find(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_not_found(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fdvjnhkfdeverufiofj4565262654738%^^&').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))

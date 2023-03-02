import os
import time
import pytest

PASSWORD = os.environ['PASSWORD']
EMAIL = os.environ['EMAIL']
BASE_URL = os.environ['BASE_URL']


@pytest.fixture(scope="session")
def set_up(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(3000)

    page.goto(BASE_URL)

    yield page
    page.close()


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=300)
    context = browser.new_context()

    page = context.new_page()
    page.goto(BASE_URL)
    page.set_default_timeout(3000)

    page.locator("#header").get_by_text("Войти").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").fill(EMAIL)
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").press("Tab")
    page.locator("#loginForm").get_by_placeholder("Пароль").fill(PASSWORD)
    page.locator("#loginForm").get_by_text("Войти").click()
    page.wait_for_load_state(timeout=10000)
    time.sleep(2)
    context.storage_state(path='state.json')

    yield context

@pytest.fixture()
def login_set_up(context_creation, browser):
    context = browser.new_context(storage_state='state.json')

    page = context.new_page()
    page.goto(BASE_URL)
    page.set_default_timeout(3000)

    yield page
    context.close()

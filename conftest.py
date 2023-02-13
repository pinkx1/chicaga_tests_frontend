import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    #
    page = context.new_page()
    page.goto("https://platform.chicaga.ru/")

    yield page
    page.close()

@pytest.fixture(scope="session")
def login_set_up(set_up):

    page = set_up
    page.set_default_timeout(3000)

    page.locator("#header").get_by_text("Войти").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").fill("s@s.s1")
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").press("Tab")
    page.locator("#loginForm").get_by_placeholder("Пароль").fill("11111111")
    page.locator("#loginForm").get_by_text("Войти").click()

    yield page
    page.close()
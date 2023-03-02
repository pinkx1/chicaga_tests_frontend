import os
from playwright.sync_api import expect

PASSWORD = os.environ['PASSWORD']
EMAIL = os.environ['EMAIL']
BASE_URL = os.environ['BASE_URL']


def test_login_to_acc(page) -> None:
    page.goto(BASE_URL)
    page.set_default_timeout(3000)

    page.locator("#header").get_by_text("Войти").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").fill(EMAIL)
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").press("Tab")
    page.locator("#loginForm").get_by_placeholder("Пароль").fill(PASSWORD)
    page.locator("#loginForm").get_by_text("Войти").click()
    page.get_by_text("Закрыть").click()

    expect(page).to_have_url(BASE_URL + '/app/#/lk/start')

import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.parametrize("email, password", [("s@s.s1", "11111111"),
                         pytest.param("fakeemail", "facepassword", marks=pytest.mark.xfail),
                         pytest.param("s@s", "11111111", marks=pytest.mark.xfail)])
def test_login_to_acc(page, email,password) -> None:
    page.goto("https://platform.chicaga.ru/")
    page.set_default_timeout(3000)

    page.locator("#header").get_by_text("Войти").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").fill(email)
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").press("Tab")
    page.locator("#loginForm").get_by_placeholder("Пароль").fill(password)
    page.locator("#loginForm").get_by_text("Войти").click()
    page.get_by_text("Закрыть").click()

    expect(page).to_have_url('https://platform.chicaga.ru/app/#/lk/start')

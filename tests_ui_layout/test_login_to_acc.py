import os
import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_to_acc(page) -> None:
    page.goto("https://platform.chicaga.ru/")
    page.set_default_timeout(3000)

    page.locator("#header").get_by_text("Войти").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").click()
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").fill(os.environ['EMAIL'])
    page.locator("#loginForm").get_by_placeholder("Электронный адрес").press("Tab")
    page.locator("#loginForm").get_by_placeholder("Пароль").fill(os.environ['PASSWORD'])
    page.locator("#loginForm").get_by_text("Войти").click()
    page.get_by_text("Закрыть").click()

    expect(page).to_have_url('https://platform.chicaga.ru/app/#/lk/start')

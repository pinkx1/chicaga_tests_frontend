import os
from playwright.sync_api import expect
from pom.Home_page_elements import TestHomePage

BASE_URL = os.environ['BASE_URL']


def test_login_and_pay(login_set_up) -> None:
    page = login_set_up
    home_page = TestHomePage(page)

    page.locator(":nth-match(:text('Купить'), 2)").click()
    buy_button = page.get_by_role("button", name="Оплатить")

    expect(buy_button).to_be_disabled()
    expect(home_page.demo_lesson_header).to_be_visible()
    expect(home_page.demo_lesson_description).to_be_visible()

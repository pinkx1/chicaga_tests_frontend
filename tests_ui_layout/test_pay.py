from playwright.sync_api import Playwright, sync_playwright, expect
from pom.Home_page_elements import TestHomePage


def test_login_and_pay(login_set_up) -> None:
    page = login_set_up
    home_page = TestHomePage(page)

    page.get_by_text("Закрыть").click()

    expect(page).to_have_url('https://platform.chicaga.ru/app/#/lk/start')
    page.locator(":nth-match(:text('Купить'), 2)").click()
    expect(page).to_have_url('https://platform.chicaga.ru/app/#/lk/start')
    buy_button = page.get_by_role("button", name="Оплатить")
    expect(buy_button).to_be_disabled()
    expect(home_page.demo_lesson_header).to_be_visible()
    expect(home_page.demo_lesson_description).to_be_visible()

    # ---------------------
    # context.close()
    # browser.close()


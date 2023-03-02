import datetime
import time
import os
from playwright.sync_api import expect

BASE_URL = os.environ['BASE_URL']


def test_clock_is_updated_every_minute(login_set_up) -> None:
    page = login_set_up
    current_time = page.get_by_text(datetime.datetime.now().strftime("%H:%M")).inner_text()
    time.sleep(60)
    new_current_time = page.get_by_text(datetime.datetime.now().strftime("%H:%M")).inner_text()

    assert current_time != new_current_time


def test_display_todays_date_in_the_calendar(login_set_up) -> None:
    page = login_set_up
    current_date = page.get_by_text(datetime.datetime.now().strftime("%m/%d/%Y"))

    expect(current_date).to_be_visible()


def test_opening_the_settings_page_by_clicking_on_the_profile_picture(login_set_up) -> None:
    page = login_set_up
    page.get_by_alt_text("Ваше фото").click()
    expect(page).to_have_url(BASE_URL+'/app/#/lk/settings')


def test_navigation_links(login_set_up) -> None:
    page = login_set_up
    page.get_by_text("Личный кабинет").click()
    expect(page).to_have_url(BASE_URL+'/app/#/lk/start')


def test_option_menu_curator(login_set_up) -> None:
    page = login_set_up
    page.get_by_role("button", name="Вызвать меню профиля").click()
    with page.expect_popup(timeout=5000) as page1_info:
        page.get_by_role("link", name="Связаться с куратором").click()
    page1 = page1_info.value
    expect(page1).to_have_url("https://t.me/CHICAGA_Platform")


def test_option_menu_tutor(login_set_up) -> None:
    page = login_set_up
    page.get_by_role("button", name="Вызвать меню профиля").click()
    with page.expect_popup(timeout=5000) as page1_info:
        page.get_by_role("link", name="Связаться с тьютором").click()
    page1 = page1_info.value
    expect(page1).to_have_url("https://t.me/CHICAGA_Platform_tutor")


def test_option_menu_settings(login_set_up) -> None:
    page = login_set_up
    page.get_by_role("button", name="Вызвать меню профиля").click()
    page.get_by_role("button", name="Настройки").click()

    expect(page).to_have_url(BASE_URL+'/app/#/lk/settings')


def test_option_menu_logout(login_set_up) -> None:
    page = login_set_up
    page.get_by_role("button", name="Вызвать меню профиля").click()
    page.get_by_role("button", name="Выход").click()

    expect(page).to_have_url(BASE_URL+'/?modal=modalPlatformLogin')

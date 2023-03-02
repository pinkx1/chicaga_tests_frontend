from playwright.sync_api import expect
import os

BASE_URL = os.environ['BASE_URL']


def test_buy_course(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("link", name="Купить курс").click()
    expect(page).to_have_url(BASE_URL + '/app/#/lk/catalog-courses')


def test_click_need_another_level(login_set_up) -> None:
    page = login_set_up
    page.get_by_role("button", name="А мне нужен другой уровень").click()
    modal_locator = page.locator('.demo-note__inner')
    expect(modal_locator).to_be_visible(timeout=5000)


def test_click_request_call(login_set_up) -> None:
    page = login_set_up
    page.set_default_timeout(5000)

    page.get_by_role("button", name="А мне нужен другой уровень").click()
    page.get_by_role("button", name="Заказать звонок").click()
    modal_locator = page.locator('.demo-notice__inner')

    expect(modal_locator).to_be_visible(timeout=5000)


def test_click_on_the_test_button(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("button", name="Пройти тест").click()

    expect(page).to_have_url(BASE_URL + '/app/#/level-test/')


def test_opening_lesson_beginner(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("button", name="Beginner").click()
    expect(page).to_have_url(BASE_URL + '/app/#/lesson/99871807ef5f180315520d094fc2ccb9/63?course_id=65')


def test_opening_lesson_elementary(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("button", name="Elementary").click()
    expect(page).to_have_url(BASE_URL + '/app/#/lesson/356094a6a1e5a7d1b15dea2e1394a004/63?course_id=58')


def test_opening_lesson_pre_intermediate(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("button", name="Pre-Intermediate").click()
    expect(page).to_have_url(BASE_URL + '/app/#/lesson/9f71609a47e3f86a2f4c442bcec89b61/63?course_id=61')


def test_opening_lesson_intermediate(login_set_up) -> None:
    page = login_set_up

    page.get_by_role("button", name="Intermediate", exact=True).click()
    expect(page).to_have_url(BASE_URL + '/app/#/lesson/714809ed52a3a595119736d0b9cbd30a/63?course_id=64')

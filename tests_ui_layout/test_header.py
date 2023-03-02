import datetime
import time


def test_clock_is_updated_every_minute(login_set_up) -> None:
    page = login_set_up
    current_time = page.get_by_text(datetime.datetime.now().strftime("%H:%M")).inner_text()
    time.sleep(60)
    new_current_time = page.get_by_text(datetime.datetime.now().strftime("%H:%M")).inner_text()

    assert current_time != new_current_time

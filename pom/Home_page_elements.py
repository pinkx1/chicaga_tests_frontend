

class TestHomePage:
    __test__ = False

    def __init__(self, page):
        self.demo_lesson_header = page.get_by_text("Пройдите бесплатный вводный урок")
        self.demo_lesson_description = page.get_by_text("и получите подарок: 10 разговорных карточек c выражениями, которыми вы поразите носителей английского")
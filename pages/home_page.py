from pages.base_page import BasePage
from locators.home_locators import HomeLocators


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate(self, url):
        self.page.goto(url)

    def is_home_loaded(self):
        return self.page.get_by_text(
            HomeLocators.HERO_TEXT
        ).is_visible()

    def is_start_now_visible(self):
        return (
            self.page
            .get_by_role(
                "button",
                name=HomeLocators.START_NOW_BUTTON
            )
            .first
            .is_visible()
        )
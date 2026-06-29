from pages.base_page import BasePage
from locators.main_menu_locators import MainMenuLocators


class MainMenuPage(BasePage):

    def is_dashboard_loaded(self):
        return self.is_visible(MainMenuLocators.STOCK_AND_INVENTORY)
from pages.base_page import BasePage
from config.settings import BASE_URL
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def open_login_page(self):
        self.open(f"{BASE_URL}/login/")

    def enter_email(self, email):
        self.fill(LoginLocators.EMAIL, email)

    def enter_password(self, password):
        self.fill(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
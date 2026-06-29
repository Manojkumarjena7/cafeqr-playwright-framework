from playwright.sync_api import Page

class LoginLocators:
    EMAIL = "input[type='email']"
    PASSWORD = "input[type='password']"
    LOGIN_BUTTON= "button[type='submit']"
    FORGOT_PASSWORD = "text=Forgot Password?"
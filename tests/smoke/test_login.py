from pages.login_page import LoginPage
from config.settings import EMAIL, PASSWORD


def test_valid_login(page):
    login = LoginPage(page)

    login.open_login_page()
    login.login(EMAIL, PASSWORD)

    page.wait_for_url("**/owner/**", timeout=10000)
    assert "/owner/" in page.url
from pages.home_page import HomePage
from config.settings import BASE_URL


def test_start_now_button_visible(page):

    home = HomePage(page)

    home.navigate(BASE_URL)

    assert home.is_start_now_visible()
from pages.home_page import HomePage
from config.settings import BASE_URL


def test_homepage_load(page):

    home = HomePage(page)

    home.navigate(BASE_URL)

    assert home.is_home_loaded()
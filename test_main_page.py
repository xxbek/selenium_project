from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


class TestLoginFromMainPage:
    LINK = "http://selenium1py.pythonanywhere.com/"

    def test_guest_can_go_to_login_page(self, browser, link=LINK):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser, link=LINK):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link='http://selenium1py.pythonanywhere.com/'):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.there_is_no_product_in_basket()
    page.your_basket_is_empty_message()




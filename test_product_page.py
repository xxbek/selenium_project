from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


class TestUserAddToBasketFromProductPage:
    LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    REGISTRATION_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link=REGISTRATION_LINK):
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + '@mail.ru', str(time.time()))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_to_basket()
        page.product_name_in_basket_is_correct()
        page.product_price_in_basket_is_correct()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
class TestSearchAssertionWithPromoUrl:

    urls = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer{no}" if no != 7
            else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]

    @pytest.mark.parametrize('link', urls)
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_to_basket()
        page.product_name_in_basket_is_correct()
        page.product_price_in_basket_is_correct()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.there_is_no_product_in_basket()
    page.your_basket_is_empty_message()


class TestWaitForSuccessInfo:
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_disappeared_success_message()



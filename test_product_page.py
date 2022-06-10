from .pages.product_page import ProductPage
import pytest


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
#
#
# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#     page.add_product_to_basket()
#     page.product_name_in_basket_is_correct()
#     page.product_price_in_basket_is_correct()
#     # page.should_disappeared_success_message() - assertion

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_disappeared_success_message()


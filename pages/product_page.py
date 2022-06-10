from .base_page import BasePage
from .locators import ProductPageLocators
from time import sleep


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.is_element_present(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def product_price_in_basket_is_correct(self):
        product_price = self._get_product_price()
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert product_price == product_price_in_basket.text, 'Not correct price in the basket'

    def product_name_in_basket_is_correct(self):
        product_name = self._get_product_name()
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        assert product_name == product_name_in_basket.text, 'Not correct name in basket'

    def _get_product_name(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_on_page.text

    def _get_product_price(self):
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_on_page.text





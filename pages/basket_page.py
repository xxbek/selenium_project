from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def there_is_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            'There is some products in the basket'

    def your_basket_is_empty_message(self):
        message = self.browser.find_element(*BasketPageLocators.NO_PRODUCT_MESSAGE)
        assert message.text == 'Your basket is empty. Continue shopping', \
            f'There is no message about empty basket. Heir is {message.text}'

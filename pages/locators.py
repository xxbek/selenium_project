from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.ID, 'messages')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')  #
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')

    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success .alertinner strong')

from selenium.webdriver.common.by import By


class MainPageLocators:
    ...


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_LOGIN_FORM = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_FORM = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_FORM_CONFIRM = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert.alert-safe')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')  #
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')

    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alertinner p strong')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success .alertinner strong')


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.ID, 'basket_formset')
    NO_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')


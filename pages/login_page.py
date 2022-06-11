from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'There is not login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not available'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not available'

    def register_new_user(self, email, password):
        login_form = self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN_FORM)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM)
        password_confirm_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM_CONFIRM)

        login_form.send_keys(email)
        password_form.send_keys(password)
        password_confirm_form.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


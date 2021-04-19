from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_login(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT), "No login input form"

    def login_user(self, login, password):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_input.send_keys(login)
        login_btn.click()
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        # Кнопка после заполнения логина меняет свое положение но локатор у нее тот же
        login_btn2 = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn2.click()


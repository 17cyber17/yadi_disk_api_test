from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def login_user(self, login, password):
        login_input = self.is_element_present(*LoginPageLocators.LOGIN_INPUT)
        login_btn = self.is_element_present(*LoginPageLocators.LOGIN_BTN)
        login_input.send_keys(login)
        login_btn.click()
        password_input = self.is_element_present(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)


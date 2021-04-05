from selenium.webdriver.common.by import By

class BasePageLocators():
    def search_for_file_or_folder(self, name):
        FOLDER_OR_FILE = (By.XPATH, f"//span[text()='{name}']")
        return FOLDER_OR_FILE

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.passp-auth-content')
    LOGIN_INPUT = (By.CSS_SELECTOR, '#passp-field-login')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#passp-field-passwd')
    LOGIN_BTN = (By.CSS_SELECTOR, '[class = "passp-button passp-sign-in-button"] > .Button2')


from selenium.webdriver.common.by import By

class BasePageLocators():
    RECENT_LINK = (By.CSS_SELECTOR, '[href="/client/recent"]')
    DISK_LINK = (By.CSS_SELECTOR, '#/disk')
    PHOTO_LINK = (By.CSS_SELECTOR, '[href="/client/photo"]')
    ALBUMS_LINK = (By.CSS_SELECTOR, '[href="/client/albums"]')
    SHARED_LINK = (By.CSS_SELECTOR, '[href="/client/shared"]')
    JOURNAL_LINK = (By.CSS_SELECTOR, '[href="/client/journal"]')
    ATTACH_LINK = (By.CSS_SELECTOR, '[href="/client/attach"]')
    TRASH_LINK = (By.CSS_SELECTOR, '[href="/client/trash"]')
    def search_for_file_or_folder(self, name):
        FOLDER_OR_FILE = (By.XPATH, f"//span[text()='{name}']")
        return FOLDER_OR_FILE

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.passp-auth-content')
    LOGIN_INPUT = (By.CSS_SELECTOR, '#passp-field-login')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#passp-field-passwd')
    LOGIN_BTN = (By.CSS_SELECTOR, '[class = "passp-button passp-sign-in-button"] > .Button2')


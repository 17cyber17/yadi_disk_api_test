from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_be_resent_link(self):
        assert self.is_element_present(*BasePageLocators.RECENT_LINK), "Resent link is not present"

    def should_be_disk_link(self):
        assert self.is_element_present(*BasePageLocators.DISK_LINK), "Disk link is not present"

    def should_be_shared_link(self):
        assert self.is_element_present(*BasePageLocators.SHARED_LINK), "Shared link is not present"

    def should_be_journal_link(self):
        assert self.is_element_present(*BasePageLocators.JOURNAL_LINK), "Journal link is not present"

    def go_to_resent_page(self):
        link = self.is_element_present(*BasePageLocators.RECENT_LINK)
        link.click()

    def go_to_disk_page(self):
        link = self.is_element_present(*BasePageLocators.DISK_LINK)
        link.click()

    def go_to_shared_page(self):
        link = self.is_element_present(*BasePageLocators.SHARED_LINK)
        link.click()

    def go_to_journal_page(self):
        link = self.is_element_present(*BasePageLocators.JOURNAL_LINK)
        link.click()


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .locators import BasePageLocators
import urllib.parse


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_folder_or_file(self, path):
        def check(beginning_name, end_name, true_path, locator_folder_or_file):
            assert self.is_element_present(*locator_folder_or_file), \
                f'There is no folder or file named "{true_path[beginning_name:end_name]}"'

        self.walk_the_path(path, check)

    def should_not_be_folder_or_file(self, path):
        def check(beginning_name, end_name, true_path, locator_folder_or_file):
            assert self.is_disappeared(*locator_folder_or_file), \
                f'The file or folder named "{true_path[beginning_name:end_name]}"exists, although it shouldnt'

        self.walk_the_path(path, check)

    def should_be_root(self, path):
        root = self.root_directory(path)
        print(root)
        self.should_be_folder_or_file(root)

    def should_not_be_root(self, path):
        root = self.root_directory(path)
        print(root)
        self.should_not_be_folder_or_file(root)

    def root_directory(self, path):
        end_name = 0
        beginning_name = 0
        true_path = urllib.parse.unquote(path)
        for i in true_path:
            end_name += 1
            if i == "/":
                beginning_name = end_name
                return path[0:end_name - 1]

        if beginning_name == 0 and end_name != 0:
            return path

    def walk_the_path(self, path, check_function):
        true_path = urllib.parse.unquote(path)
        end_name = 0
        beginning_name = 0
        locator = BasePageLocators()

        for i in true_path:
            end_name += 1
            if i == "/":
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[beginning_name:end_name - 1])
                assert self.is_element_present(*locator_folder_or_file), \
                    f'There is no folder or file named "{true_path[beginning_name:end_name - 1]}"'
                folder = self.browser.find_element(*locator_folder_or_file)
                driver = self.browser
                actionChains = ActionChains(driver)
                actionChains.double_click(folder).perform()
                beginning_name = end_name

        if beginning_name == 0 and end_name != 0:
            locator_folder_or_file = locator.search_for_file_or_folder(true_path)
            check_function(beginning_name, end_name, true_path, locator_folder_or_file)
        else:
            if beginning_name != 0:
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[beginning_name:end_name])
                check_function(beginning_name, end_name, true_path, locator_folder_or_file)


